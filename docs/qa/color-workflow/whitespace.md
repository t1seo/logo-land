# Staged whitespace check

The complete staged diff includes newly added evidence that earlier unstaged `git diff --check` runs did not include. Its whitespace check reports trailing spaces in five captured files: the three native delivery `brand-guide.md` files, `t5-export-evidence/brand-guide.md`, and `t4-red.txt`.

These are generated export payloads and a captured intermediate test log. Empty historical brief values leave a space after the field label; pytest's failure formatting also includes trailing spaces. They are retained to preserve the exported guide/ZIP byte comparisons and the recorded diagnostic text. No source code or authored documentation has this finding.

The check over all remaining staged files passes:

```sh
git diff --cached --check -- . \
  ':(exclude)docs/colors/deliveries/*/brand-guide.md' \
  ':(exclude)docs/qa/color-workflow/t5-export-evidence/brand-guide.md' \
  ':(exclude)docs/qa/color-workflow/t4-red.txt'
```

No repository whitespace rule was disabled, no original export payload was rewritten, and no ZIP hash was changed. This is a documented evidence-format exception, not a claim that the unrestricted staged whitespace check passed. The 315-test, lint/type/format and installation results are unaffected.
