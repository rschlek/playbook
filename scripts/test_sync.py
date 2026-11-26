"""Tests for sync.py. Standard library only; run from the plugin root with
`python -m unittest discover -s scripts`."""
import contextlib
import io
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sync  # noqa: E402

TEMPLATE = os.path.join(sync.PLUGIN_ROOT, "template")


class AddFromTemplate(unittest.TestCase):
    """The new skill copies the template, then runs `sync.py --repo <path> --add`."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="playbook-test-")
        self.repo = os.path.join(self.tmp, "demo")
        shutil.copytree(TEMPLATE, self.repo)
        self.agents = os.path.join(self.repo, "AGENTS.md")
        with open(self.agents, "r+b") as f:  # a checkout may have converted line endings
            data = f.read().replace(b"\r\n", b"\n")
            f.seek(0)
            f.write(data)
            f.truncate()

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def add(self, worktrees_dir):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            rc = sync.main(["--repo", self.repo, "--add", "--worktrees-dir", worktrees_dir])
        self.assertEqual(rc, 0, out.getvalue())
        return out.getvalue()

    def read(self):
        with open(self.agents, "rb") as f:
            return f.read()

    def rewrite(self, old, new):
        data = self.read()
        self.assertIn(old, data)
        with open(self.agents, "wb") as f:
            f.write(data.replace(old, new))

    def test_fills_the_placeholder_in_one_run(self):
        self.add(".worktrees")
        text = self.read().decode("utf-8")
        self.assertNotIn("<worktrees_dir>", text)
        self.assertIn("a worktree under `.worktrees/`", text)
        self.assertEqual(text, sync.Standard(".worktrees").agents_new)
        self.assertTrue(os.path.isfile(os.path.join(self.repo, *sync.COPY.split("/"))))

    def test_fills_the_placeholder_with_crlf(self):
        self.rewrite(b"\n", b"\r\n")
        self.add(".worktrees")
        data = self.read()
        self.assertNotIn(b"<worktrees_dir>", data)
        self.assertEqual(data, sync.Standard(".worktrees").agents_new.replace("\n", "\r\n").encode("utf-8"))

    def test_leaves_an_edited_block(self):
        self.rewrite(b"Make one change for one purpose", b"Make one small change for one purpose")
        before = self.read()
        out = self.add(".worktrees")
        self.assertEqual(self.read(), before)
        self.assertIn("differs from the standard", out)

    def test_leaves_a_block_placed_with_another_worktrees_folder(self):
        self.add(".worktrees")
        before = self.read()
        out = self.add("other/worktrees")
        self.assertEqual(self.read(), before)
        self.assertIn("differs from the standard", out)


if __name__ == "__main__":
    unittest.main()
