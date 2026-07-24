# Consent-safe Open House QR Generator

A working, dependency-free, browser-local generator for open-house QR signage and review-ready consent language.

Open [`index.html`](./index.html) directly in a modern browser. No install, build step, server, account, or internet connection is required.

## What works locally

The standalone page:

- accepts configurable property, agent, brokerage, check-in URL, property-packet URL, privacy URL/contact, retention period, and optional marketing-purpose text;
- generates a standards-valid QR code in-browser (error-correction level M) with a four-module quiet zone;
- renders a letter-size, two-sided table tent suitable for folding and printing;
- provides the check-in URL as a visible no-camera fallback;
- creates suggested operational packet-request language, a separate **unchecked** optional-marketing consent, a represented-buyer routing warning, and a confirmation/receipt template;
- copies the check-in link or generated language;
- downloads the QR as SVG and prints the table tent; and
- clears the form without retaining its contents.

The tool has no network requests, analytics, cookies, storage, external scripts, external fonts, or persistence. All input and output remain in the open browser tab.

## What still requires integration

This page **does not create a visitor form, collect visitor details, deliver a packet, send email/SMS, write consent records, or connect to a CRM**. A production deployment requires:

1. A brokerage-approved form or CRM endpoint at the check-in URL.
2. Separate handling for the operational packet request and optional marketing consent.
3. An optional marketing checkbox that is never preselected.
4. Consent evidence appropriate to each channel and jurisdiction (for example: disclosure version, affirmative choice, timestamp, source, sender identity, and revocation status).
5. A confirmation/receipt sent or shown by the production system.
6. Privacy, retention, security, accessibility, agency, and records-management review.
7. Represented-buyer routing that avoids buyer-agency solicitation and follows local rules and brokerage policy.

The packet URL belongs in the operational confirmation path. Do not make packet access conditional on marketing consent.

## Use

1. Download or clone this repository.
2. Open `tools/open-house-qr/index.html` in Chrome, Safari, Firefox, or Edge.
3. Choose **Load fictional sample** to inspect the output, or enter approved production values.
4. Choose **Generate**.
5. Review all language with the brokerage and counsel/compliance resources as appropriate.
6. Test the QR with at least two camera/scanner apps and verify the exact destination.
7. Choose **Download QR (SVG)** for another approved layout, or **Print table tent** and print at 100% scale.
8. Confirm the live check-in endpoint correctly separates packet delivery from optional marketing consent before public use.

> The sample values and `example.com` links are fictional placeholders and are not a working visitor-data endpoint.

## Suggested production form structure

### Required or operational fields

Keep fields proportionate to the stated visit purpose. A brokerage might request:

- first name;
- an email address or mobile number needed to deliver the requested packet;
- represented / unrepresented / prefer not to say; and
- acknowledgement of the operational packet-request and privacy language.

Avoid describing operational delivery as marketing consent. If represented, route property, showing, and offer questions through the visitor's representative where required.

### Optional marketing choice

Place optional marketing consent separately, explain the specific purpose and channels, and leave it unchecked. The generated wording is a drafting aid—not legal advice or a jurisdiction-complete disclosure. Add applicable sender identity, recurring/automated message terms, frequency, message/data rates, STOP/HELP instructions, unsubscribe method, and links to required policies.

### Receipt and retention

The live form/CRM should record the visitor's actual selection and provide a confirmation that distinguishes:

- the requested packet or visit administration;
- whether optional marketing consent was granted; and
- how to ask a privacy question, withdraw marketing consent, or exercise applicable data rights.

Delete or anonymize data according to the stated retention period and brokerage policy. Do not share identifiable visitor data with sellers beyond what is lawful, disclosed, and approved.

## Verification for maintainers

The file is intentionally self-contained. Useful checks after edits:

```bash
# Confirm there are no remote runtime assets or persistence APIs.
rg 'src="https?://|href="https?://.*stylesheet|fetch\(|XMLHttpRequest|localStorage|sessionStorage|indexedDB' tools/open-house-qr/index.html

# Extract inline scripts and syntax-check them with Node.
python3 - <<'PY'
from pathlib import Path
import re
html = Path('tools/open-house-qr/index.html').read_text()
scripts = re.findall(r'<script[^>]*>(.*?)</script>', html, re.S)
Path('/tmp/open-house-qr.js').write_text('\n'.join(scripts))
PY
node --check /tmp/open-house-qr.js
```

Also generate the fictional sample, scan its QR, print-preview the tent, and exercise every button.

## QR implementation and license

The embedded QR encoder is [`qrcode-generator`](https://github.com/kazuhikoarase/qrcode-generator) by Kazuhiko Arase, included directly so the page works offline. It is licensed under the MIT License; its copyright and license notice remain in `index.html`. The implementation is based on JIS X 0510. “QR Code” is a registered trademark of DENSO WAVE INCORPORATED.

## APV attribution

A small [Amazing Photo Video](https://amazingphotovideo.com) credit appears on the public generator and printable table tent. It is intentionally absent from the private follow-up/receipt copy.
