# personal_tasks — repository

A working repo for Dmytro's assorted personal tasks: one-off analyses, documents,
automation scripts and anything else that does not belong to a dedicated project repo.

## Organising principle

> **Code is organised by layer; content is organised by task.**

Each task is self-contained under `tasks/` — its inputs, notes and outputs in one place. Anything
reusable across tasks (a docx builder, a shared loader) moves out to `code/`.

One markdown per matter, and no folder gets a README of its own: the table below is the only place
the layout is described.

**Personal data stays out of git.** A filled-in document — anything carrying a РНОКПП, an address
or a date of birth — is gitignored, not committed. `*_conf.docx` is ignored by convention; keep the
blank template tracked and the filled copy local.

## Folder layout

| Folder | Contents | Rule for new files |
|---|---|---|
| `tasks/` | One folder per area of life (`tcr_tasks/`, …). Inside it, **one markdown per matter** — `<matter>.md` — holding what it is, where it stands and what was established; beside it a `<matter>/` folder for the artefacts: `source/` (documents received as-is, never edited), scripts, outputs. | A new matter gets one markdown and, if it has artefacts, one folder of the same name. Do not spread a matter across several notes. |
| `code/` | Scripts. `build/` = the markdown→docx builder and the prose style checker; `yt_transcript.py` = YouTube captions and chapters as plain text, `yt_frames.py` = stills from a video at given timestamps, for the numbers reviewers put in on-screen graphs rather than speech; a task-specific script starts inside its task folder and moves to `code/` once a second task needs it. | Keep the top level flat until there is a reason to add a subfolder. |
| `knowledge/` | Cross-cutting notes that belong to no single task: `WRITING_STYLE.md` (the Ukrainian register rules), conventions, reference material. | Only put a file here if it genuinely spans tasks. |
| `.claude/skills/` | Repeatable procedures for Claude Code, versioned with the repo: `build-docx`, `style-check`, `component-research`. | One skill per procedure that has been done twice and will be done again. |

## Conventions

- **Run every script from the repo root** (e.g. `python code/foo.py`) — scripts use paths
  relative to the current directory.
- **One fact, one home.** Don't restate a task's details in two files; link instead.
- **Raw inputs are never edited.** Derived files are regenerable; note how to regenerate them.
- `venv/`, `.idea/`, `__pycache__/` and `.env` are local and gitignored.

## Writing and building documents

Ukrainian prose goes through `/style-check` before it is shown; a `.docx` is built and verified
with `/build-docx`. Both are ports from the `articles` repo — the rules and machinery are the
accumulated record of corrections, so a rule is added to `knowledge/WRITING_STYLE.md` **and**
`code/build/style_rules.json` in the same turn it is learnt.

```bash
PYTHONUTF8=1 venv/Scripts/python.exe code/build/style_check.py <draft>.md --fragment
PYTHONUTF8=1 venv/Scripts/python.exe code/build/build_docx.py <template>.md <out>.docx
```

Equations are authored as inline LaTeX in the `.md` and rendered to native Word equations via
pandoc. Word is the only target renderer — never LibreOffice.

## Local environment

Machine facts (interpreter path, encoding, network quirks) are in `CLAUDE.md`.

Create the local virtual environment once:

```bash
C:/Chel/Programs/Python/python.exe -m venv venv
```

Then install the dependencies:

```bash
venv/Scripts/python.exe -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
```

The `--trusted-host` flags are required on this network (see `CLAUDE.md`).
