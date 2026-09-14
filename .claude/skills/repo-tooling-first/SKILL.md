---
name: repo-tooling-first
description: Use the scripts this repo already has, and run them the way this machine requires, before searching the web or writing a new one. Use before any WebSearch or WebFetch, before writing a scratch script, before fetching a YouTube transcript or a frame, before pricing anything in a Ukrainian shop, and whenever a task sounds like "fetch", "download", "scrape", "check the price", "read that video" or "count the sources".
---

# Check `code/` before you reach for the web

Dmytro's reaction on 2026-09-12, after a web search for something a repo script does:
*"are you retarded? we have fucking scripts in this repo fucking hell"*. That is the whole
reason this file exists.

## 1. The inventory, and what each one removes the need for

| Script | Run it for | Never do instead |
|---|---|---|
| `code/yt_transcript.py` | a YouTube video's captions, chapters, metadata | search the web for a summary of the video |
| `code/yt_frames.py` | on-screen numbers, charts, spec tables in a video | conclude "the figure is not stated" from the transcript |
| `code/ua_prices.py` | any Ukrainian retail price, with a stock check | quote a price from a search-result snippet |
| `code/build/build_docx.py` | rebuilding a `.docx` from its template | edit the `.docx` by hand |
| `code/build/style_check.py` | Ukrainian prose against `knowledge/WRITING_STYLE.md` | judge the prose by eye |
| `tasks/hardware/pc_build/audit_tools/` | what is filed, measured, covered | count by grepping and hope |

**Before writing a scratch script, `ls code/` and `ls code/build/`.** One of them usually
already does it, and its header says what it will and will not touch.

## 2. How to run anything on this machine

These are `CLAUDE.md`'s rules. They were broken in four of nine sampled sessions.

- `PYTHONUTF8=1 venv/Scripts/python.exe <file>` — never bare `python3` (Windows Store stub),
  never without UTF-8 mode on a cp1251 console.
- **Write the script to the scratchpad and run the file.** Never `python - <<'PY'` and never
  `python -c` for anything multi-line: on 2026-09-11 thirteen heredoc edits went into one
  session and a backslash inside one silently mangled a regex.
- `pip install` needs `--trusted-host pypi.org --trusted-host files.pythonhosted.org`;
  `git push`/`clone` over HTTPS needs `-c http.sslBackend=schannel`.
- Never `ssl.CERT_NONE` or `check_hostname=False`. It tripped the antivirus on 2026-09-11.

## 3. When the web is genuinely the answer

Search only for what no local script can produce — a lab measurement, a manufacturer spec, a
review verdict. Then:

- **WebFetch returns 403 forever on hwbusters.com, techpowerup.com, tomshardware.com,
  rtings.com, kitguru.net, pcpartpicker.com, bequiet.com, cclonline.com.** Use
  `mcp__Claude_Browser__navigate` + `get_page_text` for those instead of retrying.
- Fetch the sub-page that holds the number, not the landing page.
- Read the manufacturer's own specification page before reporting that a figure does not exist.
