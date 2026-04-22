# Sprint 6 Report

## YouTube link of Sprint 6 Video
https://www.youtube.com/watch?v=nUutb7TemQ8&list=PL7k2t_VNLHXXTMDM3oMTX-YRER4WVLoiR

## What's New (User Facing)
 * Staff maintenance tutorials delivered as both PDF guides and video walkthroughs, covering WordPress content editing, event calendar updates, and contact form management.
 * Video tutorials consolidated into a single unlisted YouTube playlist, so the client can share access via link without exposing the content publicly.
 * Fixed the daily auto-update pipeline so that the chatbot's knowledge base continues to refresh reliably after Hugging Face's recent storage policy change.
 * Updated the final project report to reflect all changes from this sprint.

## Work Summary (Developer Facing)
This was a wrap-up sprint focused on handoff rather than new feature work. The bulk of the effort went into producing the staff tutorials — recording the video walkthroughs, editing them, writing the accompanying PDFs, and organizing the videos into an unlisted YouTube playlist so the client can distribute access internally without making the content public. Midway through the sprint we also discovered that the daily GitHub Actions job had started failing: Hugging Face rolled out a policy change that no longer allows binary files (like our `index.faiss` FAISS index) to be pushed via plain `git push`, and instead requires the new Xet storage backend. Our original deployment step used `git clone` + `git push` to mirror the repo to the HF Space, which broke. We replaced that step with the `huggingface_hub` Python API's `upload_folder()` method, which handles Xet transparently, uploads both the `data/` and `faiss_index/` folders in a single commit, and also reduced the Space rebuild count from two to one per daily run. Finally, we updated the full project report to capture the tutorial deliverables and the pipeline fix.

## Unfinished Work
No planned sprint 6 work was left unfinished. All tutorial deliverables were produced, the pipeline issue was resolved, and the report was updated.

## Completed Issues/User Stories
Here are links to the work completed in this sprint:

 * Staff tutorial PDFs — [ADD NEW MEMBER.pdf](https://github.com/ZY115/SBYEC/blob/main/docs/Reports/ADD%20NEW%20MEMBER.pdf), [Edit members.pdf](https://github.com/ZY115/SBYEC/blob/main/docs/Reports/Edit%20members.pdf), [MailPoet.pdf](https://github.com/ZY115/SBYEC/blob/main/docs/Reports/MailPoet.pdf), [Books at the Buckle page.pdf](https://github.com/ZY115/SBYEC/blob/main/docs/Reports/Books%20at%20the%20Buckle%20page.pdf), [change position or order.pdf](https://github.com/ZY115/SBYEC/blob/main/docs/Reports/change%20position%20or%20order.pdf)
 * Tutorial video playlist (unlisted YouTube) — https://www.youtube.com/watch?v=nUutb7TemQ8&list=PL7k2t_VNLHXXTMDM3oMTX-YRER4WVLoiR
 * Fix daily content update workflow after Hugging Face Xet storage policy change — [.github/workflows/update-content.yml](https://github.com/ZY115/SBYEC/blob/main/.github/workflows/update-content.yml)
 * Update final project report to reflect sprint 6 changes — [04_FinalReport.md](https://github.com/ZY115/SBYEC/blob/main/docs/Reports/04_FinalReport.md)

## Incomplete Issues/User Stories
None — all sprint 6 issues were completed.

## Code Files for Review
Please review the following code files, which were actively developed during this sprint, for quality:
 * [.github/workflows/update-content.yml](https://github.com/ZY115/SBYEC/blob/main/.github/workflows/update-content.yml) — GitHub Actions workflow, migrated from `git push` to `huggingface_hub.HfApi.upload_folder()` for Xet-compatible uploads.

## Retrospective Summary
Here's what went well:
  * The Hugging Face pipeline failure was diagnosed and fixed quickly once we identified the Xet storage change as the root cause.
  * Switching to `upload_folder()` not only fixed the failure but also simplified the workflow — a single upload call replaced the previous clone-and-push sequence, and the HF Space now rebuilds once per day instead of twice.
  * Tutorials were scoped tightly around what the client's staff actually needs to do day-to-day (content edits, events, forms), which kept the recording effort manageable.
  * Setting the YouTube playlist to unlisted addressed the client's privacy expectations without adding any hosting cost.

Here's what we'd like to improve:
  * The pipeline break was only caught because the daily run failed — we did not have any proactive notification set up, so the first signal was a missed update. A failure alert would have caught it sooner.
  * Some of the tutorial retakes could have been avoided with a clearer script/outline before recording.

Here are changes we plan to implement in the next sprint:
  * No further sprints are planned — this was the final delivery sprint. Remaining activities are the client-facing final presentation and project handoff.
