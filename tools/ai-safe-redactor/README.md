# AI-Safe Redactor

A standalone, browser-local tool for reducing obvious sensitive details in text before sharing it with an AI service.

## Use

Open `index.html` directly in a modern browser. Paste text (or load the fictional sample), select **Redact sensitive details**, then review every replacement before copying or downloading the result.

All processing happens in the page. There are no dependencies, uploads, network requests, analytics, accounts, cookies, or saved history.

## What it flags

The deterministic first pass replaces recognizable emails, phone numbers, likely street addresses, Canadian postal and US ZIP codes, labeled government/account identifiers, access or security details, financial amounts, transaction-sensitive lines, and confidential notes with labeled bracket placeholders.

## Limits

Pattern matching can miss unusual formats, implicit identity clues, names, dates, unit details, metadata, and sensitive combinations of ordinary facts. It can also produce false positives. This tool reduces obvious exposure but cannot guarantee anonymization and is not a substitute for appropriate professional review. Do not rely on it for legal, compliance, privacy, or security decisions.

## Keyboard

Press <kbd>Ctrl</kbd>/<kbd>Command</kbd> + <kbd>Enter</kbd> in the original-text field to run the redactor.

Public resource by [Amazing Photo Video](https://amazingphotovideo.com). The credit appears in the tool interface, not in redacted client text.
