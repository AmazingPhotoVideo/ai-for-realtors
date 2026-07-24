"use client";
import { useState } from "react";
import { site } from "@/lib/site";
export function ContactForm() {
  const [sent, setSent] = useState(false);
  if (sent) return <div className="form-success" role="status"><strong>Thank you.</strong><p>This demo captured your request locally. Connect Convex using the included CRM starter before publishing.</p></div>;
  return <form className="contact-form" onSubmit={(event) => { event.preventDefault(); setSent(true); }}>
    <label>Name<input name="name" required autoComplete="name" /></label>
    <label>Email<input name="email" required type="email" autoComplete="email" /></label>
    <label>Phone<input name="phone" type="tel" autoComplete="tel" /></label>
    <label>What can we help with?<select name="intent" required defaultValue=""><option value="" disabled>Select one</option><option>Buying</option><option>Selling / valuation</option><option>Relocating</option><option>Other</option></select></label>
    <label>Message<textarea name="message" rows={4} required /></label>
    <label className="check"><input name="consent" type="checkbox" required /> <span>{site.consent.requiredLabel}</span></label>
    <label className="check"><input name="marketingConsent" type="checkbox" /> <span>{site.consent.marketingOptionalLabel}</span></label>
    <button type="submit">Send request</button><p className="fine">{site.copy.contactNote}</p>
  </form>;
}
