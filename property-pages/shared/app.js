(() => {
  "use strict";
  const listing = JSON.parse(document.querySelector("#listing-data").textContent);
  const brand = JSON.parse(document.querySelector("#branding-data").textContent);
  const q = (selector, root = document) => root.querySelector(selector);
  const qa = (selector, root = document) => [...root.querySelectorAll(selector)];
  const text = (role, value) => qa(`[data-role="${role}"]`).forEach((el) => { el.textContent = value ?? ""; });
  const hide = (section, hidden = true) => qa(`[data-section="${section}"]`).forEach((el) => { el.hidden = hidden; });
  const safeHttp = (url) => { try { const parsed = new URL(url, location.href); return parsed.protocol === "https:" || (parsed.origin === location.origin && ["http:", "https:"].includes(parsed.protocol)); } catch { return false; } };
  const displayAddress = () => {
    const a = listing.address;
    if (a.display === "custom") return a.customLabel;
    if (a.display === "street_only") return a.street;
    if (a.display === "city_only") return [a.locality, a.region].filter(Boolean).join(", ");
    return [a.street, a.locality, a.region].filter(Boolean).join(", ");
  };
  const money = (p) => new Intl.NumberFormat(brand.locale || "en-CA", { style: "currency", currency: p.currency || "CAD", maximumFractionDigits: 0 }).format(p.amount);
  const setLink = (role, href) => qa(`[data-role="${role}"]`).forEach((el) => { if (href) el.href = href; else el.hidden = true; });
  document.documentElement.style.setProperty("--brand", brand.colors.primary);
  document.documentElement.style.setProperty("--accent", brand.colors.accent);
  if (brand.colors.surface) document.documentElement.style.setProperty("--surface", brand.colors.surface);

  text("address", displayAddress()); text("status", listing.status); text("description", listing.description);
  text("location-label", listing.location.label); text("agent-name", listing.agent.name); text("brokerage", listing.agent.brokerage);
  text("agent-title", listing.agent.title || "Real Estate Representative");
  const p = listing.price || {}; hide("price", !p.visible); if (p.visible) text("price", money(p));
  const hero = listing.media.gallery[0]; qa('[data-role="hero-image"]').forEach((img) => { img.src = hero.src; img.alt = hero.alt; });

  const specs = [
    [listing.specs?.bedrooms, "Beds"], [listing.specs?.bathrooms, "Baths"],
    [listing.specs?.interiorSize && `${listing.specs.interiorSize.toLocaleString()} ${listing.specs.interiorUnit || "sq ft"}`, "Interior"],
    [listing.specs?.parking, "Parking"], [listing.specs?.propertyType, "Property"]
  ].filter(([value]) => value !== undefined && value !== null && value !== "");
  qa('[data-role="specs"]').forEach((box) => { box.innerHTML = ""; specs.forEach(([value, label]) => { const item = document.createElement("div"); item.innerHTML = `<strong></strong><span></span>`; q("strong", item).textContent = value; q("span", item).textContent = label; box.append(item); }); });
  qa('[data-role="features"]').forEach((list) => { list.innerHTML = ""; listing.features.forEach((feature) => { const li = document.createElement("li"); li.textContent = feature; list.append(li); }); });

  const dialog = q("#lightbox"); const lightboxImage = q("#lightbox-image"); const lightboxCaption = q("#lightbox-caption"); let lastFocus;
  const closeLightbox = () => { if (dialog.open) dialog.close(); };
  qa('[data-role="gallery"]').forEach((grid) => { grid.innerHTML = ""; listing.media.gallery.forEach((image, index) => { const button = document.createElement("button"); button.type = "button"; button.className = "gallery-card"; button.setAttribute("aria-label", `Open image ${index + 1}: ${image.alt}`); const img = document.createElement("img"); img.src = image.src; img.alt = image.alt; img.loading = index > 2 ? "lazy" : "eager"; button.append(img); button.addEventListener("click", () => { lastFocus = button; lightboxImage.src = image.src; lightboxImage.alt = image.alt; lightboxCaption.textContent = image.caption || image.alt; dialog.showModal(); q("[data-close]", dialog).focus(); }); grid.append(button); }); });
  q("[data-close]", dialog)?.addEventListener("click", closeLightbox); dialog?.addEventListener("click", (event) => { if (event.target === dialog) closeLightbox(); }); dialog?.addEventListener("close", () => lastFocus?.focus());

  const mediaLinks = [{ key: "videoUrl", label: "Watch the film" }, { key: "tour3dUrl", label: "Explore the 3D tour" }, { key: "floorPlanUrl", label: "View the floor plan" }].filter(({key}) => listing.media[key] && safeHttp(listing.media[key]));
  hide("media", !mediaLinks.length); qa('[data-role="media-links"]').forEach((box) => { box.innerHTML = ""; mediaLinks.forEach(({key, label}) => { const a = document.createElement("a"); a.className = "button button-secondary"; a.href = listing.media[key]; a.target = "_blank"; a.rel = "noopener noreferrer"; a.textContent = label; box.append(a); }); });

  const opens = listing.openHouses || []; hide("open-houses", !opens.length); qa('[data-role="open-houses"]').forEach((box) => { box.innerHTML = ""; opens.forEach((item) => { const card = document.createElement("article"); const start = new Date(item.start); const end = new Date(item.end); card.innerHTML = `<strong></strong><span></span>`; q("strong", card).textContent = start.toLocaleDateString(brand.locale || "en-CA", { weekday: "long", month: "long", day: "numeric" }); q("span", card).textContent = `${start.toLocaleTimeString([], {hour: "numeric", minute: "2-digit"})}–${end.toLocaleTimeString([], {hour: "numeric", minute: "2-digit"})}${item.note ? ` · ${item.note}` : ""}`; box.append(card); }); });
  const map = listing.location.mapUrl; hide("map", !map || !safeHttp(map)); if (map && safeHttp(map)) setLink("map-link", map);
  setLink("phone", `tel:${listing.agent.phone.replace(/[^+\d]/g, "")}`); text("phone-label", listing.agent.phone);
  setLink("email", `mailto:${encodeURIComponent(listing.agent.email)}`); text("email-label", listing.agent.email);
  if (listing.agent.website && safeHttp(listing.agent.website)) setLink("agent-website", listing.agent.website); else qa('[data-role="agent-website"]').forEach((el) => el.hidden = true);
  qa('[data-role="disclaimers"]').forEach((box) => { box.innerHTML = ""; listing.disclaimers.forEach((line) => { const p = document.createElement("p"); p.textContent = line; box.append(p); }); });

  const formSection = q('[data-section="form"]'); const form = q("#lead-form");
  if (!brand.form.enabled) formSection.hidden = true;
  else {
    q("#consent-text").textContent = brand.form.consentText;
    form.addEventListener("submit", async (event) => {
      event.preventDefault(); const status = q("#form-status"); const submit = q('[type="submit"]', form); const values = Object.fromEntries(new FormData(form));
      values.property = displayAddress(); values.page = location.href; values.submittedAt = new Date().toISOString();
      submit.disabled = true; status.textContent = "Sending…";
      if (brand.form.endpoint && safeHttp(brand.form.endpoint)) {
        try { const response = await fetch(brand.form.endpoint, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(values) }); if (!response.ok) throw new Error("Request failed"); form.reset(); status.textContent = brand.form.successMessage || "Thank you — your request has been sent."; }
        catch { status.textContent = "We could not send the form. Opening your email app instead."; emailFallback(values); }
        finally { submit.disabled = false; }
      } else { emailFallback(values); status.textContent = "Your email app has been opened to finish sending."; submit.disabled = false; }
    });
  }
  function emailFallback(values) { const to = brand.form.fallbackEmail || listing.agent.email; const body = Object.entries(values).filter(([key]) => key !== "consent").map(([key, value]) => `${key}: ${value}`).join("\n"); location.href = `mailto:${encodeURIComponent(to)}?subject=${encodeURIComponent(`Property inquiry: ${displayAddress()}`)}&body=${encodeURIComponent(body)}`; }

  if (brand.analytics?.enabled) {
    if (brand.analytics.provider === "plausible" && /^[a-z0-9.-]+$/i.test(brand.analytics.siteId || "")) { const s = document.createElement("script"); s.defer = true; s.dataset.domain = brand.analytics.siteId; s.src = "https://plausible.io/js/script.js"; document.head.append(s); }
    if (brand.analytics.provider === "google" && /^G-[A-Z0-9]+$/i.test(brand.analytics.siteId || "")) { const id = brand.analytics.siteId; const s = document.createElement("script"); s.async = true; s.src = `https://www.googletagmanager.com/gtag/js?id=${encodeURIComponent(id)}`; document.head.append(s); window.dataLayer = window.dataLayer || []; window.gtag = function(){window.dataLayer.push(arguments)}; window.gtag("js", new Date()); window.gtag("config", id, { anonymize_ip: true }); }
  }
  qa('[data-year]').forEach((el) => el.textContent = new Date().getFullYear());
})();
