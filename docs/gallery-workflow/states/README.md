# Portable session snapshots

Each JSON file contains the unmodified helper `show` response under `state`, plus relative `artifact_files` and `prompt_files` bindings to the public originals. This avoids duplicate image storage in the snapshots.

To resume, create a fresh workspace. For each snapshot, create `.logo-generator/sessions/<state.id>/`, write `state` as `session.json`, and copy each bound original to its matching `state.artifacts[].path` beneath that session directory. The prompt is already stored verbatim in the state; its binding permits an independent byte check. Run the actual helper `show --session <state.id>` before continuing.

All six snapshots were restored and checked through the real helper during T2. No sample is selected or approved. Revisions 1 for Leaflet, Drip, Teum and COMMON and revision 2 for Relay and Sprig are historical snapshots; recheck current state before editing.
