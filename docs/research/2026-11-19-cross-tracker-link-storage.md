# Cross-tracker link storage: where an item can hold a link to a ticket in another tracker, and whether items can be found by it

Date: 2026-11-19

## Question

For each tracker product that has a tracker doc template in the playbook plugin (GitHub Issues, OpenProject, Todoist) and for plain Markdown ticket files: where can an item hold a link (a URL) to a ticket in a different tracker, which of those places can the product's search, filters, or API match on, is a full URL or only a fragment matchable, what limits apply, does the link survive an edit made through the product's own interface, and how can every item that carries a link to one given outside ticket be listed (several items may link the same one)? The template `blank.md` is a product-neutral skeleton and is not researched.

The templates describe the tool each product is driven through: GitHub Issues through the `gh` command line, OpenProject through a connected tool that is a client of OpenProject's REST API v3, Todoist through Doist's Todoist MCP server, and Markdown tickets through plain file tools. This document covers the products' own documentation and, where noted, the source code of the open-source product. It does not cover what any particular connector tool exposes beyond the product's own API.

Claims are cited to their source. A claim marked "unverified" has no primary source that states it, or the source could not be read.

## Summary table

| Product | Places a link can be stored (outside tracker URL) | How items are found by it | Limits |
|---|---|---|---|
| GitHub Issues | Issue body; issue comment; text-type issue field (organization level); a label name is possible but not designed for it | Issue search `q` with a text term, restricted with `in:body` or `in:comments`; `field.<name>:<value>` for issue fields. The docs do not say whether a URL or a URL fragment matches, and say exact matching is not supported | Search query: 256 characters excluding operators and qualifiers, at most 5 `AND`/`OR`/`NOT`, 1,000 results per search, 30 search requests per minute authenticated. Body length: no limit stated in the docs |
| OpenProject | Description; comment; custom field of format Text, Long text, or Link (URL); native relations only join two OpenProject work packages | Filters `description`, `comment`, `search` (all operator `~`, contains); custom field filter `customField<id>` where the field is marked as filter; global search is a separate feature | Text custom field: administrator-set min and max length (0 means none). Long text and Link: no limit stated. Page size not stated in the pages read |
| Todoist | Task name (URLs become links); task description; task comment; label name (not designed for it) | Filter query `search: <words>`; the help article lists `search: http` as the way to see tasks that contain web links. Comments cannot be searched by filters. Whether `search:` covers descriptions is not stated | Task name 500 characters; description 16,383; comment 15,000; label name 60; filter query 1,024; labels per task 100 |
| Markdown ticket files | The body of the ticket file, or a new header-style line the project chooses (the template defines no link header line) | Text search over `docs/tickets/`: fixed-string search such as `grep -rlF "<url>" docs/tickets/` or PowerShell `Select-String -SimpleMatch -List` | No product limit. The file format defines no maximum |

## GitHub Issues

Template basis: the template drives GitHub through `gh`. It edits a body by replacing it whole (`gh issue edit <n> --body-file <file>`) and finds issues with `gh issue list --search`.

### Places a link can go

- Issue body and issue comments. Both are free text. The create-an-issue and update-an-issue endpoints take a `body` string; the docs state no maximum length. Source: https://docs.github.com/en/rest/issues/issues
- Issue fields. Issue fields are typed values on an issue. The documented types are text, number, date, and single-select. "Text fields detect URLs and display them as links." They are available on issues only, not pull requests. The page states no limit on the number of fields or on text length. Fields are defined at the organization level (visibility Restricted or Public). Source: https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-and-managing-issue-fields . Values are set through `issue_field_values` (array of objects with `field_id` and `value`) on the create and update endpoints. Source: https://docs.github.com/en/rest/issues/issues
- Labels. A label is a name plus an optional description. The documentation pages read give no length limit for names or descriptions (unverified). Source: https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels
- Native references. Issue URLs and `owner/repo#n` references in a body or comment are converted to links, but only for GitHub issues and pull requests. Custom autolink references can be configured on a repository so that references to an external resource, "such as a JIRA issue or Zendesk ticket", become shortened links; configuring them needs repository admin permission. Autolinks are not created in wikis or repository files. Source: https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/autolinked-references-and-urls
- Native relation types (sub-issues, blocked-by, parent) join GitHub issues only. The REST docs for create and update show `parent_issue_id` as an issue id. Source: https://docs.github.com/en/rest/issues/issues

### What can be matched, and the syntax

- Text in title, body, and comments. "When you omit this qualifier, the title, body, and comments are all searched." Restrict with `in:title`, `in:body`, `in:comments`, combined with commas (`error in:title,body`). Matching is case-insensitive. Multi-word terms need quotation marks. Source: https://docs.github.com/en/search-github/searching-on-github/searching-issues-and-pull-requests
- Issue fields. `field.<name>:<value>`, with quotes around names that contain spaces, for example `field.priority:high`, `field."target date":>=2026-03-01`, `field.priority:high,medium`; combinable with `is:open`. The pages show examples for single-select, date, and number fields only; how a text field value is matched (exact, contains, or fragment) is not stated (unverified). Source: https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests
- Labels. `label:LABEL`; separate qualifiers are ANDed (`label:bug label:resolved`); comma-separated values are ORed. Source: https://docs.github.com/en/search-github/searching-on-github/searching-issues-and-pull-requests
- The repository issue list endpoint (`GET /repos/{owner}/{repo}/issues`) filters on `state`, `milestone`, `assignee`, `type`, `creator`, `mentioned`, `issue_field_values` (comma-separated `field_slug:value`), `labels`, `since`. It has no text or body filter. The repository comments endpoint (`GET /repos/{owner}/{repo}/issues/comments`) filters on `sort`, `direction`, `since` only. Text matching on a body or comment is therefore available through the search endpoint. Sources: https://docs.github.com/en/rest/issues/issues and https://docs.github.com/en/rest/issues/comments
- Full URL versus fragment. The search documentation pages read do not address URLs, punctuation, or how a term containing `/`, `:`, `#` is tokenized, and one page states "Currently our search doesn't support exact matching." Whether a full issue URL or a fragment of it matches a body is not stated by the documentation (unverified). Sources: https://docs.github.com/en/search-github/searching-on-github/searching-issues-and-pull-requests and https://docs.github.com/en/search-github/getting-started-with-searching-on-github/about-searching-on-github
- Indexing: "Issues and pull requests are indexed when they are created or modified." No delay figure is given. Source: https://docs.github.com/en/search-github/getting-started-with-searching-on-github/about-searching-on-github

### Limits

- Search API: a query cannot be "longer than 256 characters (not including operators or qualifiers)" and cannot "have more than five `AND`, `OR`, or `NOT` operators"; a violation returns a "Validation failed" error. Up to 1,000 results per search; 100 results per page maximum (default 30). Authenticated rate limit 30 requests per minute for search endpoints other than code search; unauthenticated 10. Source: https://docs.github.com/en/rest/search/search
- Search bar nesting: parentheses up to five levels; up to 16 `user` and `org` qualifiers. Source: https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests
- Body length: the reference docs state none. Error messages from the API in third-party reports quote "maximum is 65536 characters", but no GitHub documentation page was found that states it (unverified; secondary sources only, for example https://github.com/orgs/community/discussions/27190).

### Survives an edit through the product's interface

- The body is replaced whole on update (`body` string on `PATCH /repos/{owner}/{repo}/issues/{issue_number}`), so a link in the body survives only if the edit sends it back. The template says the same. Labels and `issue_field_values` are separate parameters; the docs describe `labels` as "Replaces the label set" on update, so an update that sends labels without the link-bearing label removes it. Source: https://docs.github.com/en/rest/issues/issues
- What the web editor does to a link in a body or comment is not described in the pages read (unverified).

### Listing every item that carries a link to one given outside ticket

- Search the body and comments for the URL: `<url> in:body,comments` (the term form and fragment matching are unverified as above). For an issue field, `field.<name>:<value>` if the field is text type and matching of text values behaves as an equality or contains test (unverified). For a label, `label:<name>` returns every issue carrying it; this is exact and documented, but a label per outside ticket must exist first (the template notes a label must exist before use).
- Results are capped at 1,000 per search and search is rate limited; paginate with `per_page` up to 100.

## OpenProject

Template basis: the template drives OpenProject through a connected client of API v3 and treats a ticket as a work package.

### Places a link can go

- Description and comments (journal notes): free text. A description is a formattable object (`format`, `raw`, `html`). Source: https://www.openproject.org/docs/api/endpoints/work-packages/
- Custom fields. Formats include Text (administrator-set minimum and maximum length, 0 for none), Long text (no length limit stated), and Link (URL). Each field also has a regular expression option, a "Used as a filter" option, and a "Searchable" option ("searchable via the global search"). A work package field must be added to the work package type and activated for the project to appear. Custom field definitions are created in the web administration, not through the API. Source: https://www.openproject.org/docs/system-admin-guide/custom-fields/
- In the API the value appears under `customField<N>`; the schema gives each field's type. The one link-type example in the API page shows a link object in `_links` pointing to a user resource, so how a Link (URL) field value is serialised is not shown in the pages read (unverified). Source: https://www.openproject.org/docs/api/endpoints/work-packages/
- Relations. Relation types are related to, predecessor and successor, duplicates and duplicated by, blocks and blocked by, includes and part of, requires and required by, plus parent and child hierarchy. The page describes only work-package-to-work-package relations and does not mention an external target. A native relation cannot point outside OpenProject. Source: https://www.openproject.org/docs/user-guide/work-packages/work-package-relations-hierarchies/
- Categories and labels as link carriers are not applicable: OpenProject categories are project-level values, and no documentation read suggests holding a URL in one (not researched further).

### What can be matched, and the syntax

- Filter syntax. The `filters` query parameter is a URL-encoded JSON array of objects: `[ { "<filter name>": { "operator": "<operator>", "values": [<value>, ...] } } ]`. Several filters combine with AND; "OR filters are not yet possible in a single query." Operators include `=` (equals one of the values), `&=` (contains all values), `!` (is not), `*` and `!*` (not null, null), `**` (searches a string across all string-based attributes) and `~` / `!~` ("Contains / does not contain the words (SQL LIKE), in order"). The same page says availability of filters depends on the endpoint and does not list the work package filter keys. Source: https://www.openproject.org/docs/api/filters/
- Filter keys for text. The documentation pages read do not list the keys. In the open-source code, a filter's key is derived from its class name by removing the `Filter` suffix and underscoring it (`def self.key ... gsub(/_filter$/, "")`), and the source defines `DescriptionFilter` (type text), `CommentFilter` (matches journal notes with the contains operator, honouring internal-comment visibility), `SubjectFilter`, and a `SearchFilter` whose operator is always contains (`~`) and whose columns are subject, description, comments, searchable text or string custom fields, and, where the database supports it, attachment content and file names. The keys `description`, `comment`, and `search` follow from the naming rule but were not confirmed from a documentation page or a captured request (unverified). Sources: https://raw.githubusercontent.com/opf/openproject/dev/app/models/queries/filters/base.rb , https://raw.githubusercontent.com/opf/openproject/dev/app/models/queries/work_packages/filter/search_filter.rb , https://raw.githubusercontent.com/opf/openproject/dev/app/models/queries/work_packages/filter/description_filter.rb , https://raw.githubusercontent.com/opf/openproject/dev/app/models/queries/work_packages/filter/comment_filter.rb
- Web interface filter "Filter by text" "searches subject, description, and comments"; the page does not say whether matching is case-sensitive or partial. Source: https://www.openproject.org/docs/user-guide/work-packages/work-package-table-configuration/
- Custom field filter. A work package custom field produces a filter keyed by its column name (the API form is `customField<id>`; the filter factory resolves names through `CustomField::COLUMN_NAME_PATTERN`). Field formats user, list, version, hierarchy, weighted item list, and bool map to dedicated filter classes; every other format, including string, text, and link, falls to a base class whose operators this research did not read (unverified). The administration page says "Used as a filter" is the setting that lets users filter by the field. Sources: https://raw.githubusercontent.com/opf/openproject/dev/app/models/queries/filters/shared/custom_field_filter.rb and https://www.openproject.org/docs/system-admin-guide/custom-fields/
- Full URL versus fragment. `~` is documented as an SQL LIKE "contains the words", which suggests a fragment can be matched, but the page does not state wildcard escaping, case sensitivity, or how a value with `/` and `:` is treated (unverified). Source: https://www.openproject.org/docs/api/filters/
- Global search (the search bar) is a different feature: it suggests work packages by subject and also matches type, status, ID, and project; the page says full-text search covers wiki pages, work package descriptions, and attachments, and does not mention comments or custom fields. Partial text matching works ("roto" returns "prototyping"). Archived projects are not searched. Source: https://www.openproject.org/docs/user-guide/search/

### Limits

- Text custom field: minimum and maximum characters set by the administrator, 0 for no restriction. Link and Long text: none stated. Source: https://www.openproject.org/docs/system-admin-guide/custom-fields/
- Page size and maximum for list endpoints: the page reads show `pageSize` and `offset` but no default or maximum (unverified). Source: https://www.openproject.org/docs/api/endpoints/work-packages/
- Community Edition: Hierarchy and Weighted item list custom field formats need an Enterprise plan; Text, Long text, and Link do not. Source: https://www.openproject.org/docs/system-admin-guide/custom-fields/

### Survives an edit through the product's interface

- The template says the description is replaced whole on update. For custom fields, the pages read do not state whether a PATCH that omits `customField<N>` leaves it unchanged (unverified); the page shows `lockVersion` as the optimistic-locking integer and does not document the conflict response in the part read. Source: https://www.openproject.org/docs/api/endpoints/work-packages/
- A custom field is a separate attribute from the description, so editing the description does not alter it by the definition of the field, but this was not demonstrated against the documentation (unverified).

### Listing every item that carries a link to one given outside ticket

- By contains match: `[{"description":{"operator":"~","values":["<url or fragment>"]}}]`, or the same with `customField<id>` for a field marked as filter, or `search` to cover several places at once (key names unverified as above). Several outside tickets: values in one filter are matched by the contains operator class named `ContainsAllValues` in the source, which suggests several values must all match (unverified; the file read shows only the include).
- Because OR filters are not available in one query, finding items for several different outside tickets needs one query per ticket.

## Todoist

Template basis: the template drives Todoist through Doist's Todoist MCP server; this section uses Todoist's own documentation.

### Places a link can go

- Task name (content): URLs in task names "are turned into links by default"; a link can also be written in Markdown form `[text](url)`. The page does not say whether URLs auto-link in descriptions or comments. Source: https://www.todoist.com/help/articles/format-text-in-a-todoist-task-e5dHw9
- Task description: free text; the help article says it can be used to "share links that are relevant to the task". Source: https://www.todoist.com/help/articles/add-a-task-description-rOryWIHn
- Task comment: the API describes the content as one that "may contain markdown-formatted text and hyperlinks". Comments are available "dependent on the current user plan". Source: https://developer.todoist.com/api/v1/ (Comments section)
- Labels: tasks carry up to 100 labels, with a label name limit of 60 characters. A URL as a label name is possible in principle only when it fits; the documentation does not address it (unverified). Source: https://www.todoist.com/help/account-and-billing/plans/usage-limits-in-todoist-e5rcSY
- Native relations: subtasks only, within Todoist. There is no native link to a ticket in another tracker. The template itself records that Todoist has no native dependency.

### What can be matched, and the syntax

- Filter `search:`. "To create filters based on keywords, you can use `search:` followed by a keyword." Several words: "the filter finds tasks containing all the keywords, but they may not necessarily be in that exact order" (`search: send email`). The article lists `search: http` for "See all tasks that contain web links". Source: https://www.todoist.com/help/articles/introduction-to-filters-V98wIH
- Comments: "Todoist filters can't access comment content." Source: same article.
- Descriptions: the article never says `search:` matches task description text (unverified whether it does). Source: same article.
- Exact phrase and quoting: not described. An asterisk wildcard is documented for projects, sections, and labels; the article shows no wildcard with `search:`. The article lists no special-character handling for search terms. A URL contains `/`, `:`, `?`, and `&`, and `&` is the filter AND operator, so how a URL with a query string is parsed in a `search:` term is not stated (unverified). Source: same article.
- API: `GET /api/v1/tasks/filter` takes a required `query` (a Todoist filter string, 1 to 1,024 characters), optional `lang`, `cursor`, and `limit` (default 50, maximum 200). "Multiple filters (using the comma `,` operator) are not supported." The task fetch parameter `label` filters by label name. Source: https://developer.todoist.com/api/v1/tasks.md
- Full URL versus fragment: `search: http` shows a fragment matches. Whether a full URL matches reliably is not stated (unverified).

### Limits

- Task name 500 characters; task description 16,383; task comment 15,000; label name 60; labels per task 100; labels per account 500; filter query 1,024; one file attachment per comment. Source: https://www.todoist.com/help/account-and-billing/plans/usage-limits-in-todoist-e5rcSY . An older help article says descriptions hold up to 16,384 characters (https://www.todoist.com/help/articles/add-a-task-description-rOryWIHn); the usage-limits page is the more recent one.
- Request limits: 1 MiB on POST bodies. Source: https://developer.todoist.com/api/v1/request-limits.md
- Saved filters are plan dependent (Beginner 3, Pro 150); the API's filter query endpoint does not require a saved filter. Source: https://www.todoist.com/help/account-and-billing/plans/usage-limits-in-todoist-e5rcSY

### Survives an edit through the product's interface

- API: update is described as an update where most fields say to omit them to leave them unchanged. `labels` on update is "Updated list of label names. Omit this field to keep it unchanged." The template adds that a description is replaced whole when sent. Source: https://developer.todoist.com/api/v1/tasks.md
- Web or app editing of a task name or description that holds a link is not described in the pages read (unverified).

### Listing every item that carries a link to one given outside ticket

- `search: <fragment of the URL>` through the filter endpoint, which returns tasks, not comments. If the link is in a comment, no filter can find it. If the link is in the description, whether `search:` finds it is unverified. Pagination is cursor based, 200 per page maximum.

## Markdown ticket files

Template basis: the template defines a ticket as one file, `docs/tickets/<id>-<short-name>.md`, with this shape: the title line, then header lines (`Status`, `Type`, `Assignee`, `Parent`, `Blocked by`, `Due`, `Created`) one per line in a fixed order and omitted when empty, then the body, then a `## Log` of dated notes. The template says there is no query language: "Read the header lines of every file in `docs/tickets/` and filter on them."

### Places a link can go

- The body (free text) and any dated bullet under `## Log`. The template defines no header line for an outside link; adding one would be a project convention, not part of the template as shipped.
- Native relations: `Parent` and `Blocked by` hold ticket ids of the same folder. They cannot name an outside ticket by their definition (ids are whole numbers of files in the folder).

### What can be matched, and the syntax

- Plain text search over the folder. Fixed-string search treats the pattern as literal text, so a whole URL or any fragment of it matches without escaping:
  - GNU grep: `grep -rlF "<text>" docs/tickets/`. `-F`: "Interpret patterns as fixed strings, not regular expressions." `-l`: "print the name of each input file from which output would normally have been printed." `-r`: "read and process all files in that directory, recursively." Source: https://www.gnu.org/software/grep/manual/grep.html
  - PowerShell: `Select-String -Path docs/tickets/*.md -Pattern "<text>" -SimpleMatch -List`. `-SimpleMatch` means the pattern is not interpreted as a regular expression; `-List` returns only the first match per file. Matching is case-insensitive unless `-CaseSensitive` is given. Source: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/select-string
- Exact match of the header line is possible if the project chooses a header line, since each header is one line.

### Limits

- None defined by the file format.

### Survives an edit through the product's interface

- The template says edits change "the title line or the body text in the file" and that header lines are left to the operations that own them. A link in the body persists unless the edit rewrites that text. A link in a header line the template does not define would be outside any operation that owns it (inference from the template, not a statement in it).

### Listing every item that carries a link to one given outside ticket

- One fixed-string search for the URL over `docs/tickets/` returns every file containing it, regardless of how many files carry the same link.

## Not verified

- GitHub: whether a full issue URL or a fragment matches a body or comment in issue search (the docs do not address URLs or punctuation, and say exact matching is not supported).
- GitHub: how `field.<name>:<value>` matches a text-type issue field (equality, contains, or fragment); examples cover only single-select, date, and number.
- GitHub: any documented maximum body, comment, label name, or issue field text length. The 65,536 figure seen in error reports is from third-party sources only.
- GitHub: what the web editor does to a link in a body on edit.
- OpenProject: the filter keys `description`, `comment`, and `search`, which were derived from the open-source naming rule and class definitions and not from a documentation page or a captured request.
- OpenProject: the operators and behaviour (wildcards, case, escaping) of the filter for string, text, and Link custom fields, and the serialisation of a Link (URL) field value in the API.
- OpenProject: whether a PATCH that omits a custom field keeps its value; the conflict response for a stale `lockVersion`; default and maximum `pageSize`.
- OpenProject: how several values in one `~` filter combine (the source shows `ContainsAllValues` is included but not its body).
- Todoist: whether `search:` matches task descriptions; how a URL containing `&`, `?`, or `:` is handled in a `search:` term; whether URLs auto-link in descriptions and comments; what the apps do to a link on edit.
- Todoist: the Todoist MCP server's own search behaviour ("phrase matching" in the template) is not covered by Doist's filter documentation and was not checked.
