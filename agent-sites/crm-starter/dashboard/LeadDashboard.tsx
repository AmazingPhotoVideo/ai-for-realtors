"use client";

import { useState } from "react";
import { useMutation, useQuery } from "convex/react";
import { api } from "../convex/_generated/api";
import type { Id } from "../convex/_generated/dataModel";

const statuses = ["new", "attempted", "connected", "appointment", "active", "closed", "nurture", "lost"] as const;
const intents = ["buy", "sell", "valuation", "relocate", "invest", "other"] as const;
const csvSafe = (value: unknown) => {
  let cell = String(value ?? "");
  if (/^[=+\-@\t\r]/.test(cell)) cell = `'${cell}`;
  return `"${cell.replaceAll('"', '""')}"`;
};

export function LeadDashboard() {
  const [search, setSearch] = useState("");
  const [source, setSource] = useState("");
  const [status, setStatus] = useState("");
  const [intent, setIntent] = useState("");
  const [followUpBefore, setFollowUpBefore] = useState("");
  const [selected, setSelected] = useState<Id<"leads"> | null>(null);
  const leads = useQuery(api.leads.list, {
    search: search || undefined,
    source: source || undefined,
    status: (status || undefined) as any,
    intent: (intent || undefined) as any,
    followUpBefore: followUpBefore ? new Date(`${followUpBefore}T23:59:59`).getTime() : undefined,
  });

  const exportCsv = () => {
    if (!leads) return;
    const fields = ["name", "email", "phone", "source", "intent", "status", "nextFollowUpAt", "estimatedTransactionValue", "estimatedCommission", "currency"];
    const csv =
      "\ufeff" +
      [fields, ...leads.map((lead) => fields.map((field) => (lead as any)[field]))]
        .map((row) => row.map(csvSafe).join(","))
        .join("\n");
    const link = document.createElement("a");
    link.href = URL.createObjectURL(new Blob([csv], { type: "text/csv;charset=utf-8" }));
    link.download = "realtor-leads.csv";
    link.click();
    URL.revokeObjectURL(link.href);
  };

  return (
    <section aria-labelledby="crm-title">
      <header><h1 id="crm-title">Lead workspace</h1><p>Transaction value and commission are internal estimates only.</p></header>
      <div className="filters">
        <label>Search<input value={search} onChange={(event) => setSearch(event.target.value)} /></label>
        <label>Source<input value={source} onChange={(event) => setSource(event.target.value)} placeholder="website" /></label>
        <label>Status<select value={status} onChange={(event) => setStatus(event.target.value)}><option value="">All</option>{statuses.map((value) => <option key={value}>{value}</option>)}</select></label>
        <label>Intent<select value={intent} onChange={(event) => setIntent(event.target.value)}><option value="">All</option>{intents.map((value) => <option key={value}>{value}</option>)}</select></label>
        <label>Follow up by<input type="date" value={followUpBefore} onChange={(event) => setFollowUpBefore(event.target.value)} /></label>
        <button type="button" onClick={exportCsv}>Export filtered CSV</button>
      </div>
      <table>
        <thead><tr><th>Name</th><th>Intent / source</th><th>Status</th><th>Next follow-up</th><th>Internal estimates</th></tr></thead>
        <tbody>{leads?.map((lead) => <tr key={lead._id}><td><button type="button" onClick={() => setSelected(lead._id)}>{lead.name}</button><br /><small>{lead.email}</small></td><td>{lead.intent}<br /><small>{lead.source}</small></td><td>{lead.status}</td><td>{lead.nextFollowUpAt ? new Date(lead.nextFollowUpAt).toLocaleDateString() : "—"}</td><td>{lead.estimatedTransactionValue ?? "—"} / {lead.estimatedCommission ?? "—"} {lead.currency ?? ""}</td></tr>)}</tbody>
      </table>
      {selected && leads && <Editor id={selected} lead={leads.find((lead) => lead._id === selected)} close={() => setSelected(null)} />}
    </section>
  );
}

function Editor({ id, lead, close }: { id: Id<"leads">; lead: any; close: () => void }) {
  const update = useMutation(api.leads.update);
  const addActivity = useMutation(api.leads.addActivity);
  const [note, setNote] = useState("");
  if (!lead) return null;
  return (
    <aside aria-label={`Edit ${lead.name}`}>
      <button type="button" onClick={close}>Close</button>
      <h2>{lead.name}</h2>
      <label>Status<select value={lead.status} onChange={(event) => update({ id, status: event.target.value as any })}>{statuses.map((value) => <option key={value}>{value}</option>)}</select></label>
      <label>Next follow-up<input type="date" onChange={(event) => update({ id, nextFollowUpAt: event.target.value ? new Date(`${event.target.value}T12:00:00`).getTime() : undefined })} /></label>
      <label>Internal transaction estimate<input type="number" min="0" onBlur={(event) => update({ id, estimatedTransactionValue: Number(event.target.value) || undefined })} /></label>
      <label>Internal commission estimate<input type="number" min="0" onBlur={(event) => update({ id, estimatedCommission: Number(event.target.value) || undefined })} /></label>
      <form onSubmit={(event) => { event.preventDefault(); if (note.trim()) { void addActivity({ id, kind: "note", text: note }); setNote(""); } }}>
        <label>Activity note<textarea value={note} onChange={(event) => setNote(event.target.value)} /></label>
        <button>Add note</button>
      </form>
      <ol>{lead.activity.map((activity: any, index: number) => <li key={index}><b>{activity.kind}</b> {activity.text} <small>{new Date(activity.at).toLocaleString()} · {activity.by}</small></li>)}</ol>
      <details><summary>Consent evidence</summary><pre>{JSON.stringify(lead.consent, null, 2)}</pre></details>
    </aside>
  );
}
