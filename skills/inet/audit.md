<!-- markdownlint-disable MD052 MD034 MD013 -->
# Audit inet — 2026-05-17

> Automatisch gegenereerd door audit-tooling. Niet handmatig bewerken; wijzig SKILL.md / reference.md en regenereer.

## Samenvatting

| Status | Aantal | % |
|--------|--------|---|
| UNSUPPORTED_ASSERTION | 14 | 74% |
| CONTRADICTED | 0 | 0% |
| PARTIALLY_GROUNDED | 3 | 16% |
| UNGROUNDED | 0 | 0% |
| NO_SOURCE | 0 | 0% |
| UNVERIFIABLE | 0 | 0% |
| KNOWN_DISCREPANCY | 0 | 0% |
| GROUNDED | 2 | 11% |

*Geverifieerd met sonnet, 6 calls, $0.3387.*

## UNSUPPORTED_ASSERTION — stellige bewering zonder enige bronsteun (mogelijke hallucinatie) (14)

### `inet-0001` — SKILL.md:24 *(§ Wat is internet.nl?)*

> Internet.nl is een initiatief van de Nederlandse overheid waarmee organisaties kunnen testen of hun website en e-mail voldoen aan moderne internetstandaarden.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl algemeen

- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden](https://www.forumstandaardisatie.nl/open-standaarden)
  - *De brontekst is de algemene lijstpagina van Forum Standaardisatie en bevat geen informatie over internet.nl of wat het initiatief doet.*

### `inet-0002` — SKILL.md:26 *(§ Wat is internet.nl?)*

> De internetstandaarden getest door internet.nl staan op de pas-toe-of-leg-uit-lijst van Forum Standaardisatie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl / Forum Standaardisatie

- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden](https://www.forumstandaardisatie.nl/open-standaarden)
  - *De bron vermeldt het bestaan van de pas-toe-of-leg-uit-lijst maar noemt internet.nl niet en koppelt de geteste standaarden niet aan internet.nl.*

### `inet-0003` — SKILL.md:52 *(§ Webstandaarden)*

> IPv6 heeft de Forum Standaardisatie-status 'Verplicht (pas-toe-of-leg-uit)' voor webstandaarden.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Webstandaarden / Forum Standaardisatie

- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden](https://www.forumstandaardisatie.nl/open-standaarden)
  - *De bron noemt de pas-toe-of-leg-uit-lijst als concept maar somt geen specifieke standaarden zoals IPv6 op.*
- **NOT_FOUND** (high) — [https://internet.nl/about/](https://internet.nl/about/)
  - *De brontekst gaat over wat internet.nl is en wie erachter zit. Forum Standaardisatie-statussen worden niet vermeld.*

### `inet-0004` — SKILL.md:53 *(§ Webstandaarden)*

> DNSSEC heeft de Forum Standaardisatie-status 'Verplicht (pas-toe-of-leg-uit)' en beveiligt DNS-naamresolutie tegen manipulatie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Webstandaarden / Forum Standaardisatie

- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden](https://www.forumstandaardisatie.nl/open-standaarden)
  - *DNSSEC wordt niet genoemd in de brontekst.*
- **NOT_FOUND** (high) — [https://internet.nl/about/](https://internet.nl/about/)
  - *De brontekst gaat over wat internet.nl is en wie erachter zit. Forum Standaardisatie-statussen worden niet vermeld.*

### `inet-0005` — SKILL.md:54 *(§ Webstandaarden)*

> HTTPS (TLS 1.2/1.3) heeft de Forum Standaardisatie-status 'Verplicht (pas-toe-of-leg-uit)'.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Webstandaarden / Forum Standaardisatie

- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden](https://www.forumstandaardisatie.nl/open-standaarden)
  - *HTTPS/TLS wordt niet genoemd in de brontekst.*
- **NOT_FOUND** (high) — [https://internet.nl/about/](https://internet.nl/about/)
  - *De brontekst gaat over wat internet.nl is en wie erachter zit. Forum Standaardisatie-statussen worden niet vermeld.*

### `inet-0006` — SKILL.md:55 *(§ Webstandaarden)*

> HSTS heeft de Forum Standaardisatie-status 'Verplicht (pas-toe-of-leg-uit)' en dwingt browsers HTTPS te gebruiken.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Webstandaarden / Forum Standaardisatie

- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden](https://www.forumstandaardisatie.nl/open-standaarden)
  - *HSTS wordt niet genoemd in de brontekst.*
- **NOT_FOUND** (high) — [https://internet.nl/about/](https://internet.nl/about/)
  - *De brontekst gaat over wat internet.nl is en wie erachter zit. Forum Standaardisatie-statussen worden niet vermeld.*

### `inet-0007` — SKILL.md:56 *(§ Webstandaarden)*

> Security headers (CSP, X-Frame-Options, X-Content-Type-Options, Referrer-Policy) worden getest door internet.nl maar hebben geen Forum Standaardisatie-status.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Webstandaarden / Forum Standaardisatie

- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden](https://www.forumstandaardisatie.nl/open-standaarden)
  - *Security headers worden niet genoemd in de brontekst.*
- **NOT_FOUND** (high) — [https://internet.nl/about/](https://internet.nl/about/)
  - *De brontekst gaat over wat internet.nl is en wie erachter zit. Specifieke testitems of Forum Standaardisatie-statussen worden niet vermeld.*

### `inet-0009` — SKILL.md:58 *(§ Webstandaarden)*

> RPKI heeft de Forum Standaardisatie-status 'Verplicht (pas-toe-of-leg-uit)' en beschermt BGP-routing via Route Origin Validation.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Webstandaarden / Forum Standaardisatie

- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden](https://www.forumstandaardisatie.nl/open-standaarden)
  - *RPKI wordt niet genoemd in de brontekst.*
- **NOT_FOUND** (high) — [https://internet.nl/about/](https://internet.nl/about/)
  - *De brontekst gaat over wat internet.nl is en wie erachter zit. Forum Standaardisatie-statussen worden niet vermeld.*

### `inet-0010` — SKILL.md:64 *(§ Mailstandaarden)*

> SPF heeft de Forum Standaardisatie-status 'Verplicht (pas-toe-of-leg-uit)' en autoriseert verzendende mailservers.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Mailstandaarden / Forum Standaardisatie

- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden](https://www.forumstandaardisatie.nl/open-standaarden)
  - *SPF wordt niet genoemd in de brontekst.*
- **NOT_FOUND** (high) — [https://internet.nl/about/](https://internet.nl/about/)
  - *De brontekst gaat over wat internet.nl is en wie erachter zit. Forum Standaardisatie-statussen worden niet vermeld.*

### `inet-0011` — SKILL.md:65 *(§ Mailstandaarden)*

> DKIM heeft de Forum Standaardisatie-status 'Verplicht (pas-toe-of-leg-uit)' en biedt een digitale handtekening op e-mail.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Mailstandaarden / Forum Standaardisatie

- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden](https://www.forumstandaardisatie.nl/open-standaarden)
  - *DKIM wordt niet genoemd in de brontekst.*
- **NOT_FOUND** (high) — [https://internet.nl/about/](https://internet.nl/about/)
  - *De brontekst gaat over wat internet.nl is en wie erachter zit. Forum Standaardisatie-statussen worden niet vermeld.*

### `inet-0012` — SKILL.md:66 *(§ Mailstandaarden)*

> DMARC heeft de Forum Standaardisatie-status 'Verplicht (pas-toe-of-leg-uit)' en bouwt voort op SPF en DKIM.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Mailstandaarden / Forum Standaardisatie

- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden](https://www.forumstandaardisatie.nl/open-standaarden)
  - *DMARC wordt niet genoemd in de brontekst.*
- **NOT_FOUND** (high) — [https://internet.nl/about/](https://internet.nl/about/)
  - *De brontekst gaat over wat internet.nl is en wie erachter zit. Forum Standaardisatie-statussen worden niet vermeld.*

### `inet-0013` — SKILL.md:67 *(§ Mailstandaarden)*

> STARTTLS + DANE heeft de Forum Standaardisatie-status 'Verplicht (pas-toe-of-leg-uit)'; STARTTLS versleutelt SMTP-verkeer, DANE biedt DNS-gebaseerde certificaatverificatie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Mailstandaarden / Forum Standaardisatie

- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden](https://www.forumstandaardisatie.nl/open-standaarden)
  - *STARTTLS en DANE worden niet genoemd in de brontekst.*
- **NOT_FOUND** (high) — [https://internet.nl/about/](https://internet.nl/about/)
  - *De brontekst gaat over wat internet.nl is en wie erachter zit. Forum Standaardisatie-statussen worden niet vermeld.*

### `inet-0014` — SKILL.md:68 *(§ Mailstandaarden)*

> IPv6 heeft de Forum Standaardisatie-status 'Verplicht (pas-toe-of-leg-uit)' voor mailstandaarden (bereikbaarheid van MX- en nameservers).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Mailstandaarden / Forum Standaardisatie

- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden](https://www.forumstandaardisatie.nl/open-standaarden)
  - *IPv6 voor mailstandaarden wordt niet genoemd in de brontekst.*
- **NOT_FOUND** (high) — [https://internet.nl/about/](https://internet.nl/about/)
  - *De brontekst gaat over wat internet.nl is en wie erachter zit. Forum Standaardisatie-statussen worden niet vermeld.*

### `inet-0015` — SKILL.md:69 *(§ Mailstandaarden)*

> RPKI heeft de Forum Standaardisatie-status 'Verplicht (pas-toe-of-leg-uit)' voor mailstandaarden (Route Origin Validation voor MX- en nameservers).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Mailstandaarden / Forum Standaardisatie

- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden](https://www.forumstandaardisatie.nl/open-standaarden)
  - *RPKI voor mailstandaarden wordt niet genoemd in de brontekst.*
- **NOT_FOUND** (high) — [https://internet.nl/about/](https://internet.nl/about/)
  - *De brontekst gaat over wat internet.nl is en wie erachter zit. Forum Standaardisatie-statussen worden niet vermeld.*

## PARTIALLY_GROUNDED — bron ondersteunt deel van de claim (3)

### `inet-0008` — SKILL.md:57 *(§ Webstandaarden)*

> security.txt heeft de Forum Standaardisatie-status 'Verplicht (pas-toe-of-leg-uit)' en is gedefinieerd in RFC 9116.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Webstandaarden / Forum Standaardisatie

- **PARTIALLY_SUPPORTED** (medium) — [https://www.rfc-editor.org/rfc/rfc9116.txt](https://www.rfc-editor.org/rfc/rfc9116.txt)
  > This document defines a machine-parsable format ("security.txt") to help organizations describe their vulnerability disclosure practices... [published as] RFC 9116
  - *De bron bevestigt dat security.txt gedefinieerd is in RFC 9116. Echter, de Forum Standaardisatie-status 'Verplicht (pas-toe-of-leg-uit)' wordt nergens in de RFC vermeld — dat is een Nederlandse overheidsclassificatie die buiten de scope van dit document valt.*

### `inet-0017` — SKILL.md:79 *(§ Repositories)*

> De documentatie voor de batch API (v2) van internet.nl staat in de repository Internet.nl-API-docs onder CC-BY-4.0 licentie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl repositories / Batch API v2

- **SOURCE_UNAVAILABLE** (high) — [https://raw.githubusercontent.com/internetstandards/Internet.nl/main/LICENSE](https://raw.githubusercontent.com/internetstandards/Internet.nl/main/LICENSE)
  - *Bron status: unreachable*
- **SOURCE_UNAVAILABLE** (high) — [https://raw.githubusercontent.com/internetstandards/Internet.nl/master/LICENSE](https://raw.githubusercontent.com/internetstandards/Internet.nl/master/LICENSE)
  - *Bron status: unreachable*
- **PARTIALLY_SUPPORTED** (medium) — [https://github.com/internetstandards/Internet.nl-API-docs](https://github.com/internetstandards/Internet.nl-API-docs)
  > Documentation on the Internet.nl batch API and web-based dashboard [...] LICENSE-CC-BY-4.0.txt
  - *De bron bevestigt dat de repository Internet.nl-API-docs documentatie bevat over de batch API én een CC-BY-4.0 licentiebestand aanwezig is. De claim noemt specifiek 'v2', maar de bron toont mappen v1.1 en v2.0 zonder expliciet te stellen dat v2 de huidige/hoofdversie is. Het CC-BY-4.0 karakter is ondersteund via het aanwezige licentiebestand, maar niet expliciet als licentietekst vermeld.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)
  - *De brontekst beschrijft de hoofdrepository internetstandards/Internet.nl. Er is geen vermelding van een aparte 'Internet.nl-API-docs' repository of batch API v2 documentatie.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *De brontekst beschrijft de toolbox-wiki repository. Er is geen vermelding van een 'Internet.nl-API-docs' repository of batch API v2 documentatie.*

### `inet-0018` — SKILL.md:80 *(§ Repositories)*

> De implementatiegidsen per standaard en platform staan in de toolbox-wiki repository onder CC-BY-4.0 licentie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl repositories

- **PARTIALLY_SUPPORTED** (medium) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  > This GitHub repository contains several how-to's for providing practical information and guidance on implementing secure and modern Internet Standards. [...] LICENSE-CC-BY-4.0.txt
  - *De bron bevestigt dat de toolbox-wiki implementatiegidsen bevat en dat er een CC-BY-4.0 licentiebestand aanwezig is. De claim dat het 'per standaard en platform' is wordt deels ondersteund (DANE, DKIM, SPF, DMARC how-to's zijn zichtbaar), maar 'per platform' wordt niet expliciet vermeld. De CC-BY-4.0 licentie is aanwezig als bestand maar wordt niet expliciet als de geldende licentie benoemd in de tekst.*
- **SOURCE_UNAVAILABLE** (high) — [https://raw.githubusercontent.com/internetstandards/toolbox-wiki/main/LICENSE](https://raw.githubusercontent.com/internetstandards/toolbox-wiki/main/LICENSE)
  - *Bron status: unreachable*
- **SOURCE_UNAVAILABLE** (high) — [https://raw.githubusercontent.com/internetstandards/toolbox-wiki/master/LICENSE](https://raw.githubusercontent.com/internetstandards/toolbox-wiki/master/LICENSE)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)
  - *De brontekst maakt geen melding van een 'toolbox-wiki' repository of implementatiegidsen per standaard en platform.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl-API-docs](https://github.com/internetstandards/Internet.nl-API-docs)
  - *De brontekst gaat uitsluitend over Internet.nl-API-docs. Er is geen vermelding van een toolbox-wiki repository of implementatiegidsen per standaard en platform.*

## GROUNDED — minstens één bron ondersteunt de claim (2)

<details>
<summary>Klap uit voor alle GROUNDED claims</summary>

### `inet-0016` — SKILL.md:78 *(§ Repositories)*

> De internet.nl testsuite (Python/Django) is gepubliceerd onder Apache-2.0 (code) en CC-BY-4.0 (vertalingen) op GitHub.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl repositories

- **SOURCE_UNAVAILABLE** (high) — [https://raw.githubusercontent.com/internetstandards/Internet.nl/main/LICENSE](https://raw.githubusercontent.com/internetstandards/Internet.nl/main/LICENSE)
  - *Bron status: unreachable*
- **SOURCE_UNAVAILABLE** (high) — [https://raw.githubusercontent.com/internetstandards/Internet.nl/master/LICENSE](https://raw.githubusercontent.com/internetstandards/Internet.nl/master/LICENSE)
  - *Bron status: unreachable*
- **SUPPORTED** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)
  > This project is licensed under the Apache License, Version 2.0 - see the LICENSE-Apache-2.0.txt file for details. The files under the /translations folder are licensed under Attribution 4.0 International (CC BY 4.0) - see the LICENSE-CC-BY-4.0.txt file for details.
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl-API-docs](https://github.com/internetstandards/Internet.nl-API-docs)
  - *De brontekst beschrijft alleen de Internet.nl-API-docs repository en vermeldt niets over de Python/Django testsuite of Apache-2.0 licentie.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *De brontekst gaat over de toolbox-wiki repository, niet over de internet.nl testsuite (Python/Django). Geen informatie over Apache-2.0 of code/vertalingen licenties van de testsuite.*

### `inet-0019` — SKILL.md:73 *(§ Repositories)*

> De broncode en documentatie van internet.nl staan onder de GitHub-organisatie 'internetstandards'.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl repositories

- **SUPPORTED** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)
  > internetstandards / Internet.nl Public
  - *De repository staat expliciet onder de GitHub-organisatie 'internetstandards', zichtbaar in de repository-header 'internetstandards/Internet.nl'.*
- **SUPPORTED** (high) — [https://github.com/internetstandards/Internet.nl-API-docs](https://github.com/internetstandards/Internet.nl-API-docs)
  > internetstandards / Internet.nl-API-docs Public
  - *De repository staat expliciet onder de GitHub-organisatie 'internetstandards', wat de claim bevestigt dat broncode en documentatie onder die organisatie staan.*
- **SUPPORTED** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  > internetstandards / toolbox-wiki Public
  - *De repository staat zichtbaar onder de GitHub-organisatie 'internetstandards', wat de claim bevestigt.*

</details>
