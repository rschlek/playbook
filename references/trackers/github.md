# Tracker: GitHub Issues

## Mechanics

- Tool: the `gh` command line, run from inside the repository's checkout so it infers the repository from the git remote (add `--repo <owner>/<repo>` elsewhere). A ticket is an issue. Pass any body longer than one line through a file (`--body-file`), never inline.
- Find by name: `gh issue list --state all --limit 200 --search "<words> in:title"`; check each match's number and state before using it.
- Fetch: `gh issue view <n> --comments` for the body, labels, assignees, and comments, plus any linked pull request. Children: `gh api --paginate repos/{owner}/{repo}/issues/<n>/sub_issues`.
- Comment: `gh issue comment <n> --body-file <file>`.
- Change status: an issue is open or closed. `gh issue close <n> --reason completed` or `--reason "not planned"`, with `--comment` for the closing note; `gh issue reopen <n>`. Any finer state is a label: `gh issue edit <n> --add-label <label> --remove-label <label>`.
- Assign: `gh issue edit <n> --add-assignee @me`.
- Create: `gh issue create --title "<title>" --body-file <file>`, with `--label` and `--assignee` as Layout's New ticket says. It prints the new issue's URL; its number is the last part.
- Edit: `gh issue edit <n> --title "<title>"` or `--body-file <file>`. The body is replaced whole: to add a line, read it, add the line in the file, and write it all back.
- Link parent and child: make the child a sub-issue: `gh api -X POST repos/{owner}/{repo}/issues/<parent>/sub_issues -F sub_issue_id=<child id>`, where the id is the child's numeric id (`gh api repos/{owner}/{repo}/issues/<child> --jq .id`), not its number.
- Link blocking: the native dependency, where the repository has it: `gh api -X POST repos/{owner}/{repo}/issues/<blocked>/dependencies/blocked_by -F issue_id=<blocker id>`, the blocker's numeric id as above. Where the call is refused, write a `Blocked by #<n>` line in the blocked issue's body.
- Quirks:
  - A placeholder such as `#<n>` in a body links to whatever issue has that number. Create issues first and write cross-references with their real numbers afterwards.
  - A label must exist before it is used: `gh label create <name>` once.
  - Closing an issue does not close its sub-issues.
  - The sub-issue and dependency calls need a recent `gh` and a repository where those features are on; tracker setup tries each once and records any fallback under House rules.
  - Lists stop at 30 items unless told otherwise: give `gh issue list` a `--limit` above the number of issues, and `gh api` `--paginate`.
  - `gh` must already be signed in; when it is not, stop and ask the user to sign in.

## Layout

- Where: this repository's issues
- Pickable work: <a search, such as open issues assigned to me with the label ready; then any fallback source, saying whether it is a fallback or merged>
- Ranking: <how to order candidates, such as a priority label, then oldest first>
- Excluded: <labels that are never offered, such as ideas or questions; the map and question labels, or with the fallback markers, titles starting with a wayfinding prefix>
- New ticket: <the labels, assignee, and milestone a captured issue needs>
- Start: assign the issue to the user<, and add the label in-progress if the repository uses one>
- Note: comment on the issue
- Done: close the issue as completed, with a comment saying what was done or linking the merged pull request
- Stopped partway: leave the issue open with a comment saying where it stands
- Cannot proceed: <add the label blocked> with a comment naming the blocker
- Not worth doing: propose closing it as not planned; the user decides
- Parent and children: sub-issues
- Blocking: the native blocked-by link, else a `Blocked by #<n>` line in the body
- Close the parent: close the parent as completed once its last open sub-issue closes

## House rules

<!-- Example: A code issue is not done until its pull request is merged. -->

## Wayfinding operations

- Map: an issue titled with the destination, with the label `wayfinder-map`, its body holding the map body. Find maps with `gh issue list --label wayfinder-map --state open --limit 200`. Fallback that creates nothing, where the user does not want the labels made: the title starts with `[map]`, and maps are found with `gh issue list --state open --search "[map] in:title" --limit 200 --json number,title --jq '.[] | select(.title | startswith("[map]")) | .number'`. Tracker setup records which form is in use. To change the body, fetch it fresh (`gh issue view <map> --json body --jq .body > <file>`; other sessions edit it too), edit the file, and write it back with `gh issue edit <map> --body-file <file>`.
- Child ticket: an issue titled with the question, its body holding the question and any options, made a sub-issue of the map as Mechanics' Link parent and child says. Questions are never sub-issues of each other. Blocking between questions uses the native blocked-by link, wired in a second pass once both issues have numbers. Fallbacks where the repository refuses those calls: a `Part of #<map>` line at the top of the question's body for the parent, and a `Blocked by #<n>` line for each blocker.
- Type marker: exactly one label per question: `wayfinder-research`, `wayfinder-prototype`, `wayfinder-grilling`, or `wayfinder-task` (create each once with `gh label create`). Fallback that creates nothing: the title starts with `[research]`, `[prototype]`, `[grilling]`, or `[task]`. The map and its questions carry no other labels.
- Claim: check the issue (`gh issue view <n> --json assignees,labels,title`) and skip it if it carries the label `wayfinder-claimed` or the `[claimed]` title prefix, or is assigned to someone else. Then, before any work, `gh issue edit <n> --add-assignee @me --add-label wayfinder-claimed`, or in the fallback that creates nothing, assign it and put `[claimed]` at the front of its title. To release a claim when a session stops without resolving the question, remove the label or prefix, and the assignee if the claim set it.
- Frontier query: with `<me>` the user's login (`gh api user --jq .login`), `gh api --paginate repos/{owner}/{repo}/issues/<map>/sub_issues --jq '.[] | select(.state=="open" and ([.labels[].name] | index("wayfinder-claimed") | not) and (.title | startswith("[claimed]") | not) and ([.assignees[].login] - ["<me>"] | length) == 0) | .number'`, in that order; then drop any issue whose `gh api repos/{owner}/{repo}/issues/<n>/dependencies/blocked_by --jq '.[] | select(.state=="open") | .number'` prints anything. With the fallbacks: `gh issue list --state open --limit 1000 --json number,title,body,assignees --jq '.[] | select(([.assignees[].login] - ["<me>"] | length) == 0 and (.title | startswith("[claimed]") | not) and (.body | test("Part of #<map>\\b"))) | .number'`, dropping any whose `Blocked by #<n>` lines name an open issue.
- Resolve: comment the answer's gist with a link to its decision file (or research document) (`gh issue comment <n> --body-file <file>`), close it (`gh issue close <n> --reason completed`), remove `wayfinder-claimed` or the `[claimed]` prefix, then add the one-line pointer under `## Answers so far` in the map's body. A question ruled out of scope is closed with `--reason "not planned"` and a comment starting `Out of scope:`, and its line goes under `## Out of scope` instead.
