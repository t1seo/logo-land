# Review findings and verified corrections

These local process and installer defects were discovered by independent review of the new Hermes integration. The original failures remain in their reports. The canonical demo and original images did not change while the fixes were made.

| Observed boundary | Correction and evidence |
| --- | --- |
| Launcher leader exits while a descendant remains | Verify and settle the owned groups, including the captured launcher's helper session. [Original code review](review-code.md), [process fix](fix-process.md) |
| Caller interruption leaves a live helper | Reap owned helper groups before returning the original interrupt or timeout. [Process fix](fix-process.md) |
| Nested helper starts outside launcher ownership | Give the helper a separate group in the same session; discover numeric PIDs and recheck exact SID/PGID before signalling. No names, argv or environment are enumerated. [Process fix](fix-process.md) |
| Popen context exit waits beyond the finite deadline | Own the process and streams explicitly, with bounded graceful/forced settlement. [Process fix](fix-process.md) |
| A nested foreign management-marker file is removed on update | Exempt only the root management marker, preserving unknown nested files. [Installer fix](fix-installer.md) |
| An interrupt after either installation rename loses the old payload | Cover both rename boundaries and restore the original payload when possible. [Installer boundary fix](fix-installer-boundary.md) |
| Restoration fails or another file occupies the destination | Preserve the old payload in its recovery directory and retain the original failure; do not overwrite the foreign target or report success. [Installer boundary fix](fix-installer-boundary.md) |
| Repeated SIGINT can interrupt Popen's poll-lock acquisition | Defer the original KeyboardInterrupt over bounded main-thread operations, restore its handler and preserve its object; leave non-main-thread policy unchanged. [Integrated correction](fix-process-integration.md) |

The installer follow-up passed 42 scoped cases, original independent goal/security/code probes and actual SIGINT scenarios on both installed Python versions. The final process correction passed 39 scoped cases, six independent probes and real tmux Ctrl-C, delayed output and worker-thread cases. All registered fixtures, processes, groups, tmux sessions and temporary roots were removed.

The first integrated attempt's two failures share one helper PID; the later color-test failure was its delayed resource warning. No color logic was changed. The final integrated run passed **957 tests in 295.48s**, with strict static checks, actual native installation and exact artifact bindings. [Final gate](final-integration.md).

The temporary root debugging journal is superseded by this record and the linked original reports. It and its task-added local exclude entry are removed before publication. Independent review and publication receipts are recorded separately.
