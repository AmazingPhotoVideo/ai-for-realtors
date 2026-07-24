"use strict";

const fs = require("fs");
const vm = require("vm");

class Element {
  constructor(id = "") {
    this.id = id;
    this.value = "";
    this.textContent = "";
    this.innerHTML = "";
    this.disabled = false;
    this.children = [];
    this.listeners = {};
    this.className = "";
  }

  addEventListener(type, fn) { this.listeners[type] = fn; }
  dispatch(type, event = {}) { this.listeners[type]?.({ preventDefault() {}, ...event }); }
  replaceChildren(...nodes) { this.children = nodes; }
  append(...nodes) { this.children.push(...nodes); }
  setAttribute() {}
  focus() {}
  select() {}
  setSelectionRange() {}
  remove() {}
  click() {}
}

const ids = [
  "sourceText", "resultText", "sourceCount", "resultCount", "findingsList", "status",
  "sampleButton", "redactButton", "copyButton", "downloadButton", "clearButton",
];
const elements = Object.fromEntries(ids.map((id) => [id, new Element(id)]));
const document = {
  getElementById(id) { return elements[id]; },
  createElement() { return new Element(); },
  body: new Element("body"),
  execCommand() { return true; },
};
const context = {
  document,
  navigator: { clipboard: { writeText: async () => {} } },
  Blob,
  URL: { createObjectURL: () => "blob:test", revokeObjectURL() {} },
  console,
};

const html = fs.readFileSync("tools/ai-safe-redactor/index.html", "utf8");
const scriptMatch = html.match(/<script>([\s\S]*?)<\/script>/);
if (!scriptMatch) throw new Error("inline redactor script not found");
vm.runInNewContext(scriptMatch[1], context);

function redact(input) {
  elements.sourceText.value = input;
  elements.redactButton.dispatch("click");
  return elements.resultText.value;
}

elements.sampleButton.dispatch("click");
const sampleOutput = redact(elements.sourceText.value);
const sampleSecrets = [
  "14 Cedar Lane", "M4B 1B3", "morgan.lee@example.com", "(416) 555-0147",
  "4821", "9033", "$1,245,000", "$50,000", "0038492017", "Seller will accept less",
];
for (const value of sampleSecrets) {
  if (sampleOutput.includes(value)) throw new Error(`fictional sample leaked: ${value}`);
}
for (const placeholder of [
  "[PROPERTY ADDRESS REDACTED]", "[POSTAL CODE REDACTED]", "[EMAIL REDACTED]",
  "[PHONE REDACTED]", "[ACCESS DETAIL REDACTED]", "[TRANSACTION DETAIL REDACTED]",
  "[CONFIDENTIAL NOTE REDACTED]",
]) {
  if (!sampleOutput.includes(placeholder)) throw new Error(`sample missing: ${placeholder}`);
}
if (!elements.status.textContent.includes("8 potential sensitive items replaced")) {
  throw new Error(`unexpected sample status: ${elements.status.textContent}`);
}

const labeledOutput = redact(
  "SSN: 123-45-6789\nAccount #: A19-33882\nBudget USD 825000\nVisit 90210",
);
for (const placeholder of [
  "[GOVERNMENT ID REDACTED]", "[ACCOUNT ID REDACTED]",
  "[FINANCIAL AMOUNT REDACTED]", "[POSTAL CODE REDACTED]",
]) {
  if (!labeledOutput.includes(placeholder)) throw new Error(`labeled case missing: ${placeholder}`);
}
if (/123-45-6789|A19-33882|825000|90210/.test(labeledOutput)) {
  throw new Error("labeled sensitive value leaked");
}

const commonOutput = redact("Lockbox: 4821\nAccount number 0038492017\nCall 4165550147");
for (const placeholder of [
  "[ACCESS DETAIL REDACTED]", "[ACCOUNT ID REDACTED]", "[PHONE REDACTED]",
]) {
  if (!commonOutput.includes(placeholder)) throw new Error(`common format missing: ${placeholder}`);
}
if (/4821|0038492017|4165550147/.test(commonOutput)) {
  throw new Error("common-format sensitive value leaked");
}

const benign = "MLS 123456789\nOpen house Saturday at 2 PM\nParking: 2-car\nNo account here";
const benignOutput = redact(benign);
if (benignOutput !== benign) throw new Error(`benign text changed: ${JSON.stringify(benignOutput)}`);
if (/Amazing Photo Video|amazingphotovideo/i.test(commonOutput)) {
  throw new Error("public APV credit leaked into generated text");
}

console.log("redactor behavior: PASS");
console.log("sample replacements: 8; common variants: access, account, compact phone; benign case unchanged");
