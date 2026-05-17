<!-- markdownlint-disable MD052 MD034 MD013 -->
# Audit inet — 2026-05-17

> Automatisch gegenereerd door audit-tooling. Niet handmatig bewerken; wijzig SKILL.md / reference.md en regenereer.

## Samenvatting

| Status | Aantal | % |
|--------|--------|---|
| UNSUPPORTED_ASSERTION | 14 | 70% |
| CONTRADICTED | 0 | 0% |
| PARTIALLY_GROUNDED | 1 | 5% |
| UNGROUNDED | 0 | 0% |
| NO_SOURCE | 0 | 0% |
| UNVERIFIABLE | 0 | 0% |
| KNOWN_DISCREPANCY | 0 | 0% |
| GROUNDED | 5 | 25% |

*Geverifieerd met sonnet, 6 calls, $0.3397.*

## UNSUPPORTED_ASSERTION — stellige bewering zonder enige bronsteun (mogelijke hallucinatie) (14)

### `inet-0001` — SKILL.md:24 *(§ Wat is internet.nl?)*

> Internet.nl is een initiatief van de Nederlandse overheid waarmee organisaties kunnen testen of hun website en e-mail voldoen aan moderne internetstandaarden.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl platform

- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden](https://www.forumstandaardisatie.nl/open-standaarden)
  - *De brontekst beschrijft de website van Forum Standaardisatie over open standaarden. Internet.nl wordt nergens vermeld.*

### `inet-0002` — SKILL.md:26 *(§ Wat is internet.nl?)*

> De standaarden getest door internet.nl staan op de pas-toe-of-leg-uit-lijst van Forum Standaardisatie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl / Forum Standaardisatie

- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden](https://www.forumstandaardisatie.nl/open-standaarden)
  - *Internet.nl wordt niet vermeld in de brontekst. De bron bevestigt wel dat er een 'pas-toe-of-leg-uit'-lijst bestaat, maar legt geen koppeling met internet.nl.*

### `inet-0003` — SKILL.md:52 *(§ Webstandaarden)*

> IPv6 heeft de Forum Standaardisatie-status 'Verplicht (pas-toe-of-leg-uit)' voor webstandaarden.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** IPv6 / Forum Standaardisatie webstandaarden

- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden](https://www.forumstandaardisatie.nl/open-standaarden)
  - *IPv6 wordt niet specifiek genoemd in de brontekst. De bron is een navigatiepagina zonder inhoudelijke details over individuele standaarden.*
- **NOT_FOUND** (high) — [https://internet.nl/about/](https://internet.nl/about/)
  - *De brontekst beschrijft wat internet.nl is en wie eraan meewerkt, maar bevat geen informatie over Forum Standaardisatie-statussen of specifieke standaarden zoals IPv6.*

### `inet-0004` — SKILL.md:53 *(§ Webstandaarden)*

> DNSSEC heeft de Forum Standaardisatie-status 'Verplicht (pas-toe-of-leg-uit)' en beveiligt DNS-naamresolutie tegen manipulatie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DNSSEC / Forum Standaardisatie webstandaarden

- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden](https://www.forumstandaardisatie.nl/open-standaarden)
  - *DNSSEC wordt niet vermeld in de brontekst.*
- **NOT_FOUND** (high) — [https://internet.nl/about/](https://internet.nl/about/)
  - *De brontekst noemt DNSSEC niet en bevat geen Forum Standaardisatie-statusinformatie.*

### `inet-0005` — SKILL.md:54 *(§ Webstandaarden)*

> HTTPS (TLS 1.2/1.3) heeft de Forum Standaardisatie-status 'Verplicht (pas-toe-of-leg-uit)'.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** HTTPS/TLS / Forum Standaardisatie webstandaarden

- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden](https://www.forumstandaardisatie.nl/open-standaarden)
  - *HTTPS/TLS wordt niet vermeld in de brontekst.*
- **NOT_FOUND** (high) — [https://internet.nl/about/](https://internet.nl/about/)
  - *HTTPS/TLS wordt niet vermeld in de brontekst. Geen Forum Standaardisatie-informatie aanwezig.*

### `inet-0006` — SKILL.md:55 *(§ Webstandaarden)*

> HSTS heeft de Forum Standaardisatie-status 'Verplicht (pas-toe-of-leg-uit)' en dwingt browsers HTTPS te gebruiken.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** HSTS / Forum Standaardisatie webstandaarden

- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden](https://www.forumstandaardisatie.nl/open-standaarden)
  - *HSTS wordt niet vermeld in de brontekst.*
- **NOT_FOUND** (high) — [https://internet.nl/about/](https://internet.nl/about/)
  - *HSTS wordt niet vermeld in de brontekst.*

### `inet-0007` — SKILL.md:56 *(§ Webstandaarden)*

> Security headers (CSP, X-Frame-Options, X-Content-Type-Options, Referrer-Policy) worden getest door internet.nl maar hebben geen Forum Standaardisatie-status.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Security headers / internet.nl webstandaarden

- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden](https://www.forumstandaardisatie.nl/open-standaarden)
  - *Security headers (CSP, X-Frame-Options, etc.) worden niet vermeld in de brontekst.*
- **NOT_FOUND** (high) — [https://internet.nl/about/](https://internet.nl/about/)
  - *Security headers (CSP, X-Frame-Options, etc.) worden niet vermeld in de brontekst.*

### `inet-0009` — SKILL.md:58 *(§ Webstandaarden)*

> RPKI (Route Origin Validation) heeft de Forum Standaardisatie-status 'Verplicht (pas-toe-of-leg-uit)' en beschermt BGP-routing.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** RPKI / Forum Standaardisatie webstandaarden

- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden](https://www.forumstandaardisatie.nl/open-standaarden)
  - *RPKI wordt niet vermeld in de brontekst.*
- **NOT_FOUND** (high) — [https://internet.nl/about/](https://internet.nl/about/)
  - *RPKI wordt niet vermeld in de brontekst.*

### `inet-0010` — SKILL.md:64 *(§ Mailstandaarden)*

> SPF heeft de Forum Standaardisatie-status 'Verplicht (pas-toe-of-leg-uit)' en autoriseert verzendende mailservers.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** SPF / Forum Standaardisatie mailstandaarden

- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden](https://www.forumstandaardisatie.nl/open-standaarden)
  - *SPF wordt niet vermeld in de brontekst.*
- **NOT_FOUND** (high) — [https://internet.nl/about/](https://internet.nl/about/)
  - *SPF wordt niet vermeld in de brontekst. De bron noemt SMTP alleen als voorbeeld van een bekende e-mailprotocol, zonder Forum Standaardisatie-statusinformatie.*

### `inet-0011` — SKILL.md:65 *(§ Mailstandaarden)*

> DKIM heeft de Forum Standaardisatie-status 'Verplicht (pas-toe-of-leg-uit)' en plaatst een digitale handtekening op e-mail.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DKIM / Forum Standaardisatie mailstandaarden

- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden](https://www.forumstandaardisatie.nl/open-standaarden)
  - *DKIM wordt niet vermeld in de brontekst.*
- **NOT_FOUND** (high) — [https://internet.nl/about/](https://internet.nl/about/)
  - *DKIM wordt niet vermeld in de brontekst.*

### `inet-0012` — SKILL.md:66 *(§ Mailstandaarden)*

> DMARC heeft de Forum Standaardisatie-status 'Verplicht (pas-toe-of-leg-uit)' en bouwt voort op SPF en DKIM.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DMARC / Forum Standaardisatie mailstandaarden

- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden](https://www.forumstandaardisatie.nl/open-standaarden)
  - *DMARC wordt niet vermeld in de brontekst.*
- **NOT_FOUND** (high) — [https://internet.nl/about/](https://internet.nl/about/)
  - *DMARC wordt niet vermeld in de brontekst.*

### `inet-0013` — SKILL.md:67 *(§ Mailstandaarden)*

> STARTTLS + DANE heeft de Forum Standaardisatie-status 'Verplicht (pas-toe-of-leg-uit)'; STARTTLS versleutelt SMTP-verkeer en DANE biedt DNS-gebaseerde certificaatverificatie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** STARTTLS + DANE / Forum Standaardisatie mailstandaarden

- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden](https://www.forumstandaardisatie.nl/open-standaarden)
  - *STARTTLS en DANE worden niet vermeld in de brontekst.*
- **NOT_FOUND** (high) — [https://internet.nl/about/](https://internet.nl/about/)
  - *STARTTLS en DANE worden niet vermeld in de brontekst.*

### `inet-0014` — SKILL.md:68 *(§ Mailstandaarden)*

> IPv6 heeft de Forum Standaardisatie-status 'Verplicht (pas-toe-of-leg-uit)' voor de bereikbaarheid van MX- en nameservers.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** IPv6 / Forum Standaardisatie mailstandaarden

- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden](https://www.forumstandaardisatie.nl/open-standaarden)
  - *IPv6 voor MX- en nameservers wordt niet vermeld in de brontekst.*
- **NOT_FOUND** (high) — [https://internet.nl/about/](https://internet.nl/about/)
  - *IPv6 voor MX- en nameservers wordt niet vermeld in de brontekst.*

### `inet-0015` — SKILL.md:69 *(§ Mailstandaarden)*

> RPKI heeft de Forum Standaardisatie-status 'Verplicht (pas-toe-of-leg-uit)' voor MX- en nameservers.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** RPKI / Forum Standaardisatie mailstandaarden

- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden](https://www.forumstandaardisatie.nl/open-standaarden)
  - *RPKI voor MX- en nameservers wordt niet vermeld in de brontekst.*
- **NOT_FOUND** (high) — [https://internet.nl/about/](https://internet.nl/about/)
  - *RPKI voor MX- en nameservers wordt niet vermeld in de brontekst.*

## PARTIALLY_GROUNDED — bron ondersteunt deel van de claim (1)

### `inet-0008` — SKILL.md:57 *(§ Webstandaarden)*

> security.txt heeft de Forum Standaardisatie-status 'Verplicht (pas-toe-of-leg-uit)' en is gedefinieerd in RFC 9116.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** security.txt / Forum Standaardisatie webstandaarden

- **PARTIALLY_SUPPORTED** (high) — [https://www.rfc-editor.org/rfc/rfc9116.txt](https://www.rfc-editor.org/rfc/rfc9116.txt)
  > This document defines a machine-parsable format ("security.txt") to help organizations describe their vulnerability disclosure practices... RFC 9116
  - *De bron bevestigt dat security.txt gedefinieerd is in RFC 9116. De claim over de Forum Standaardisatie-status 'Verplicht (pas-toe-of-leg-uit)' wordt niet vermeld in deze bron — dat is een Nederlandse overheids-classificatie die buiten de scope van de RFC valt.*

## GROUNDED — minstens één bron ondersteunt de claim (5)

<details>
<summary>Klap uit voor alle GROUNDED claims</summary>

### `inet-0016` — SKILL.md:78 *(§ Repositories)*

> De internet.nl testsuite (Internet.nl repository) is gepubliceerd onder Apache-2.0 licentie voor code en CC-BY-4.0 voor vertalingen.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl repository licenties

- **SUPPORTED** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)
  > This project is licensed under the Apache License, Version 2.0 - see the LICENSE-Apache-2.0.txt file for details. The files under the /translations folder are licensed under Attribution 4.0 International (CC BY 4.0) - see the LICENSE-CC-BY-4.0.txt file for details.
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl-API-docs](https://github.com/internetstandards/Internet.nl-API-docs)
  - *De brontekst is de GitHub-pagina van de Internet.nl-API-docs repository en bevat geen informatie over de licentie van de internet.nl testsuite (het hoofdrepository). Er wordt alleen een LICENSE-CC-BY-4.0.txt bestand genoemd voor deze docs-repo zelf.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *De bron vermeldt alleen CC-BY-4.0 (zichtbaar in het bestandsoverzicht: LICENSE-CC-BY-4.0.txt), maar gaat over de toolbox-wiki, niet over de internet.nl testsuite. Apache-2.0 en vertalingen worden niet genoemd.*

### `inet-0017` — SKILL.md:79 *(§ Repositories)*

> De Internet.nl-API-docs repository (documentatie voor de batch API v2) is gepubliceerd onder de CC-BY-4.0 licentie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl Batch API v2 documentatie

- **SUPPORTED** (medium) — [https://github.com/internetstandards/Internet.nl-API-docs](https://github.com/internetstandards/Internet.nl-API-docs)
  > LICENSE-CC-BY-4.0.txt
  - *De brontekst toont een bestand genaamd 'LICENSE-CC-BY-4.0.txt' in de Internet.nl-API-docs repository. Dit is een sterke indicatie dat de CC-BY-4.0 licentie van toepassing is, hoewel de volledige licentietekst niet in de verstrekte bron staat.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)
  - *De bron beschrijft alleen de Internet.nl repository zelf, niet een aparte API-docs repository. Geen informatie over de licentie van die repository.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *De bron behandelt de toolbox-wiki repository, niet de Internet.nl-API-docs repository. De CC-BY-4.0 licentie voor die specifieke repo wordt hier niet bevestigd.*

### `inet-0018` — SKILL.md:80 *(§ Repositories)*

> De toolbox-wiki repository (implementatiegidsen per standaard en platform) is gepubliceerd onder de CC-BY-4.0 licentie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl toolbox-wiki licentie

- **SUPPORTED** (medium) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  > LICENSE-CC-BY-4.0.txt (bestandsnaam zichtbaar in repository bestandsoverzicht van internetstandards/toolbox-wiki)
  - *De aanwezigheid van LICENSE-CC-BY-4.0.txt in de repository impliceert sterk de CC-BY-4.0 licentie, maar de licentie wordt nergens expliciet als tekst vermeld in de aangeleverde brontekst. Confidence medium omdat het een bestandsnaam is, geen uitgeschreven licentievermelding.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)
  - *De bron beschrijft alleen de Internet.nl repository zelf, niet een aparte toolbox-wiki repository. Geen informatie over de licentie van die repository.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl-API-docs](https://github.com/internetstandards/Internet.nl-API-docs)
  - *De brontekst behandelt uitsluitend de Internet.nl-API-docs repository. Er is geen informatie over een toolbox-wiki repository of de licentie daarvan.*

### `inet-0019` — SKILL.md:78 *(§ Repositories)*

> De internet.nl testsuite is gebouwd met Python/Django.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl technische implementatie

- **SUPPORTED** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)
  > Python 3 (main programming language) Django (web framework)
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl-API-docs](https://github.com/internetstandards/Internet.nl-API-docs)
  - *De brontekst bevat geen informatie over de technische implementatie (Python/Django) van de internet.nl testsuite.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *De bron gaat over de toolbox-wiki (implementatiegidsen voor mailstandaarden), niet over de technische implementatie van de testsuite. Python/Django wordt niet vermeld.*

### `inet-0020` — SKILL.md:73 *(§ Repositories)*

> De broncode en documentatie van internet.nl staan onder de GitHub-organisatie 'internetstandards'.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl GitHub organisatie

- **SUPPORTED** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)
  > internetstandards / Internet.nl Public
  - *De repository URL en header tonen duidelijk dat de code staat onder de GitHub-organisatie 'internetstandards'.*
- **SUPPORTED** (high) — [https://github.com/internetstandards/Internet.nl-API-docs](https://github.com/internetstandards/Internet.nl-API-docs)
  > internetstandards / Internet.nl-API-docs Public
  - *De brontekst toont duidelijk dat de repository onder de GitHub-organisatie 'internetstandards' staat: 'internetstandards / Internet.nl-API-docs'.*
- **SUPPORTED** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  > internetstandards / toolbox-wiki Public
  - *De repository staat expliciet onder de GitHub-organisatie 'internetstandards', zoals zichtbaar in de repository-naam en navigatie.*

</details>
