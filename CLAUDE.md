# CLAUDE.md — environment rules for this repo (Windows 10, Git Bash + PowerShell 5.1)

Repo conventions live in `README.md`; cross-task notes in `knowledge/`.
This file records only the machine facts that sessions keep rediscovering.

## Python on this machine

- The system interpreter is `C:\Chel\Programs\Python\python.exe` (3.9). In Git Bash `python3`
  resolves to the Windows Store stub and does nothing — never call `python3`.
- Prefer the repo venv when it exists: `venv/Scripts/python.exe`. It is gitignored; create it
  with `C:/Chel/Programs/Python/python.exe -m venv venv`.
- The console codepage is cp1251. Anything that prints Cyrillic, Greek or `λ` either dies with
  `UnicodeEncodeError: 'charmap' codec` or prints `����`. Run every Python command with UTF-8
  mode on — Bash: `PYTHONUTF8=1 python …`; PowerShell: `$env:PYTHONUTF8=1; python …` — and open
  files with `encoding="utf-8"`.
- Do not put multi-line Python inside `python -c "…"`, a Bash heredoc with backslashes, or a
  PowerShell here-string: quoting and backslashes break with `SyntaxError`. Write the script to
  the session scratchpad (or `code/`) and run the file.
- The network intercepts TLS. `pip install` needs
  `--trusted-host pypi.org --trusted-host files.pythonhosted.org`; `git clone` over HTTPS needs
  `-c http.sslBackend=schannel`.

## Moving, renaming or syncing the user's files (F:, C:\Chel, any data drive) — ALWAYS

F: is the backup drive (`F:\Дані\Memory` mirrors `C:\Chel\Dima\Memory`; saves live in
`…\Memory\Games\Saves`). On 2026-11-23 a script meant to rearrange 637 save files on F: moved them
all into this repo folder instead, because PowerShell variable names are case-insensitive: the
loop variable `$f` overwrote the target root `$F`. Nothing was lost, only because moves were
checked by hash, but the user waited through a broken operation. Never again:

- **PowerShell variables ignore case.** `$f` and `$F`, `$path` and `$Path` are the same variable.
  Give the root and the loop variable clearly different names (`$destRoot`, `$file`).
- **Assert every destination before touching anything.** Build the full list of
  source → destination paths first; abort if any destination is not under the intended root
  (`$dst.StartsWith($destRoot + '\')`), and print a sample of absolute destinations in a dry run.
  A dry run that only prints counts proves nothing.
- **Copy, verify, then remove** — never a bare `Move-Item` across a layout change. Verify with
  `code`/scratchpad Python (`hashlib`, `os.walk`), which is fast; `Get-FileHash` loops over
  hundreds of files are slow and have given false mismatches here. Report one summary line.
- **No Cyrillic literals in `.ps1` files**: PowerShell 5.1 reads them as ANSI and mangles the
  path. Build such names from char codes or pass them as arguments.
- **Renames fail with "access denied" when something has the folder open**: an Explorer window
  inside it (check `(New-Object -ComObject Shell.Application).Windows()`) or the Windows Search /
  Music-library watcher. Find the holder instead of retrying.
- `C:\Chel` needs explicit write rights for `Dmitriy` (granted 2026-11-23 with `icacls`); this
  session is never elevated, so admin-only paths are the user's to change.
- **Keep the user informed.** Long checks run in the foreground with a time estimate, or say up
  front how long they take; never leave the user waiting without a status line.

## Deliverables

- Word is the only target renderer for `.docx`; never install or render with LibreOffice.
- Ukrainian prose passes `/style-check` before it is shown; a `.docx` is verified structurally
  after `build_docx.py`, not by eye (`/build-docx`).
- `pandoc` is not on PATH. It ships inside the venv via `pypandoc_binary`, so run
  `build_docx.py` with `venv/Scripts/python.exe`.
- `openpyxl`, `requests` and `pytest` are not installed in the venv — add them to
  `requirements.txt` if a task needs them; run tests with `python -m unittest`.
