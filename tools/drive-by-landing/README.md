# Drive-By Lead Capture Page

Mobile-first landing page spec for people standing in front of the sign, sitting in a car, or walking the neighbourhood. The goal is fast answers, low friction, and clean attribution.

## Page promise

“Scan once, get price/photos/showing options, and choose whether you want updates.”

## Required modules

1. **Hero above the fold**
   - 1 compressed listing image or video poster
   - Address/area, price/status when permitted
   - Buttons: Call, Text, Schedule, Photos
2. **Proof bullets**
   - 3–5 factual features: lot, parking, layout, updates, schools/transit with caveats
3. **Lead form**
   - Name, email, mobile, “I want”: showing / open house reminder / similar homes / home value
   - Consent checkbox for SMS/email where required
4. **Gallery preview**
   - 6–9 compressed images, link to full media page
5. **Neighbour block**
   - “Live nearby? Request a value range based on this listing and recent sales.”
6. **Compliance footer**
   - Brokerage, listing attribution, privacy link, opt-out instructions

## Copy template

Headline: **Inside [ADDRESS/AREA] — photos, price, and showing times**

Subhead: Scan-friendly details for buyers and neighbours. No app required.

CTA buttons:
- See full gallery
- Book a private showing
- Get open house reminder
- Check my home value nearby

Form microcopy:

> Tell me what you want and I’ll send the right link. By submitting, you agree to be contacted by [AGENT/BROKERAGE] about this property. Message/data rates may apply. Reply STOP to opt out.

## Implementation checklist

- Keep initial page under 1.5 MB; compress images to WebP/AVIF.
- Use lazy loading below the fold.
- Add UTM parameters for every QR placement: sign, rider, flyer, mailer, open house.
- Add click-to-call and click-to-text links.
- Add GA4 events: `qr_page_view`, `gallery_click`, `call_click`, `form_submit`, `valuation_click`.
- Create thank-you state with the promised link and next question.
- Test on iPhone Safari, Android Chrome, and weak cellular connection.

## CRM automation

- Trigger: form submitted
- Tags: `drive-by`, `listing:[slug]`, selected intent
- Assign owner: listing agent or ISA
- Immediate SMS: “Thanks for scanning [ADDRESS]…”
- Immediate email: full gallery + showing options
- Task: call within 5 minutes during business hours
- If no response: Day 1 reminder, Day 3 similar property, Day 7 value/market update

## Example HTML skeleton

```html
<main>
  <section class="hero">
    <img src="/images/123-main.webp" alt="Exterior of 123 Main Street" loading="eager">
    <p class="eyebrow">Now available in [NEIGHBOURHOOD]</p>
    <h1>See photos, price, and showing times for [ADDRESS]</h1>
    <a href="tel:[PHONE]">Call</a>
    <a href="sms:[PHONE]">Text</a>
    <a href="#form">Get details</a>
  </section>
  <section>
    <h2>Why buyers are noticing it</h2>
    <ul><li>[FEATURE]</li><li>[FEATURE]</li><li>[FEATURE]</li></ul>
  </section>
  <form id="form">
    <label>Name <input name="name" required></label>
    <label>Email <input name="email" type="email"></label>
    <label>Mobile <input name="phone" type="tel"></label>
    <select name="intent"><option>Book a showing</option><option>Open house reminder</option><option>Similar homes</option><option>My home's value</option></select>
    <label><input type="checkbox" required> I agree to be contacted about this property.</label>
    <button>Send me the details</button>
  </form>
</main>
```

## KPIs

- QR scan volume by placement
- Page load under 3 seconds on mobile
- Form conversion 5–15%
- Call/text click rate 3–10%
- Showing requests, buyer consults, valuation requests

## Compliance and APV attribution

Use brokerage-approved listing language and consent notices. Do not use protected-class language or unsupported school/value claims. Public page footer may include:

> Real estate marketing resource by Amazing Photo Video: https://amazingphotovideo.com
