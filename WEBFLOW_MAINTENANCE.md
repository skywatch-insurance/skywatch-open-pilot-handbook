# Webflow maintenance

The public Webflow implementation of the SkyWatch Open Pilot Handbook lives in the **SkyWatch Website** project (`skywatch-new`) on the **SkyWatch's Workspace** account.

- Webflow page: `SkyWatch Open Pilot Handbook`
- Page ID: `6a8359c984d0b0f891d6afee`
- Staging: <https://skywatch-new.webflow.io/skywatch-open-pilot-handbook>
- Production: <https://www.skywatch.ai/skywatch-open-pilot-handbook>
- Repository: <https://github.com/skywatch-insurance/skywatch-open-pilot-handbook>

## Editing model

The page intentionally uses small, separated Webflow Code Embed blocks so the approved standalone page can be maintained without changing its visual system:

1. Base styles
2. Page markup
3. Behavior and interactions
4. Mobile parity overrides

Keep `index.html` in this repository as the source-of-truth reference. When content or styling changes, apply the corresponding change in Webflow and here in the same update. Prefer isolated overrides for small fixes; merge them into the base styles during larger planned revisions.

## Publishing workflow

1. Make the change on the Webflow page.
2. Publish to `skywatch-new.webflow.io` only.
3. Check desktop and mobile layouts, navigation, video playback, FAQ behavior, and GitHub links.
4. Publish to `www.skywatch.ai` only after the staging version is approved.

Do not replace GitHub contribution calls to action with ZIP-download messaging. The page should consistently present SkyWatch Co-Pilot as an open-source skill and invite the aviation community to contribute.
