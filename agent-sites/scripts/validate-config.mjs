import { readFile } from "node:fs/promises";
import Ajv2020 from "ajv/dist/2020.js";
import addFormats from "ajv-formats";
const config = JSON.parse(await readFile(new URL("../config/site.config.json", import.meta.url)));
const schema = JSON.parse(await readFile(new URL("../config/site.schema.json", import.meta.url)));
const ajv = new Ajv2020({ allErrors: true, strict: false }); addFormats(ajv);
const validate = ajv.compile(schema);
if (!validate(config)) { console.error(validate.errors); process.exit(1); }
const forbidden = ["StewardEngine", "Harbor", "live MLS feed", "guaranteed board approval"];
const text = JSON.stringify(config);
const found = forbidden.filter((term) => text.toLowerCase().includes(term.toLowerCase()));
if (found.length) { console.error(`Forbidden or misleading terms: ${found.join(", ")}`); process.exit(1); }
console.log(`Valid Realtor config: ${config.agent.name} / ${config.preset}`);
