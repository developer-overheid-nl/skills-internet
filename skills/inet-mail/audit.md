<!-- markdownlint-disable MD052 MD034 MD013 -->
# Audit inet-mail — 2026-05-17

> Automatisch gegenereerd door audit-tooling. Niet handmatig bewerken; wijzig SKILL.md / reference.md en regenereer.

## Samenvatting

| Status | Aantal | % |
|--------|--------|---|
| UNSUPPORTED_ASSERTION | 27 | 54% |
| CONTRADICTED | 0 | 0% |
| PARTIALLY_GROUNDED | 6 | 12% |
| UNGROUNDED | 9 | 18% |
| NO_SOURCE | 0 | 0% |
| UNVERIFIABLE | 0 | 0% |
| KNOWN_DISCREPANCY | 0 | 0% |
| GROUNDED | 8 | 16% |

*Geverifieerd met sonnet, 13 calls, $3.1525.*

## UNSUPPORTED_ASSERTION — stellige bewering zonder enige bronsteun (mogelijke hallucinatie) (27)

### `inet-mail-0002` — SKILL.md:27 *(§ Overzicht)*

> SPF, DKIM en DMARC staan op de pas-toe-of-leg-uit-lijst van Forum Standaardisatie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Forum Standaardisatie open standaarden

<details><summary>3x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *De bron vermeldt niets over Forum Standaardisatie of de pas-toe-of-leg-uit-lijst.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 bevat geen informatie over de pas-toe-of-leg-uit-lijst van Forum Standaardisatie.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron is RFC 6376. De pas-toe-of-leg-uit-lijst van Forum Standaardisatie is een Nederlandse beleidsaangelegenheid die buiten scope van deze RFC valt.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *RFC 7208 behandelt geen Forum Standaardisatie of pas-toe-of-leg-uit-lijst.*
</details>

### `inet-mail-0004` — SKILL.md:54 *(§ 1. SPF (Sender Policy Framework))*

> Internet.nl controleert of een SPF-record aanwezig is als DNS TXT-record.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl SPF-test

<details><summary>2x NOT_FOUND + 2x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *De bron noemt SPF maar beschrijft geen specifieke subtests.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 beschrijft DMARC, niet de specifieke werking van internet.nl als testplatform.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *Gaat over internet.nl SPF-test. De bron beschrijft DKIM, niet SPF of internet.nl.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron beschrijft de SPF-standaard zelf, niet wat internet.nl controleert. De bron bevestigt wel dat SPF als DNS TXT-record gepubliceerd moet worden.*
</details>

### `inet-mail-0005` — SKILL.md:55 *(§ 1. SPF (Sender Policy Framework))*

> Internet.nl controleert de correcte syntax van SPF-records.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl SPF-test

<details><summary>2x NOT_FOUND + 2x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Geen informatie over syntax-controle van SPF-records in de bron.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 beschrijft DMARC, niet de specifieke syntaxcontroles van internet.nl.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *Gaat over internet.nl SPF-syntaxcontrole. Buiten scope van RFC 6376.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron beschrijft SPF-syntaxregels uitgebreid, maar zegt niets over wat internet.nl controleert.*
</details>

### `inet-mail-0007` — SKILL.md:57 *(§ 1. SPF (Sender Policy Framework))*

> Internet.nl controleert of het SPF-record eindigt op `-all` (fail) of `~all` (softfail).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl SPF-test

<details><summary>2x NOT_FOUND + 2x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Geen informatie over -all of ~all controle in de bron.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 beschrijft DMARC, niet de specifieke internet.nl-controle op `-all` of `~all`. Wel wordt SPF-beleid algemeen benoemd, maar de claim over internet.nl-testcriteria is buiten scope van deze bron.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *Gaat over SPF -all / ~all mechanisme. Buiten scope van RFC 6376.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *Wat internet.nl controleert valt buiten RFC 7208. De bron bespreekt wel -all en ~all als geldige qualifiers (fail resp. softfail), maar zegt niets over internet.nl-testcriteria.*
</details>

### `inet-mail-0009` — SKILL.md:103 *(§ 2. DKIM (DomainKeys Identified Mail))*

> Internet.nl test of minimaal 1 geldige DKIM-handtekening aanwezig is op de testmail.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl DKIM-test

<details><summary>3x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Geen informatie over specifieke DKIM-subtests in de bron.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 beschrijft DMARC, niet de specifieke werking van internet.nl als testplatform.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De claim gaat over internet.nl's testgedrag. RFC 6376 beschrijft het protocol, niet hoe internet.nl test.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *DKIM en internet.nl vallen buiten scope van RFC 7208.*
</details>

### `inet-mail-0011` — SKILL.md:106 *(§ 2. DKIM (DomainKeys Identified Mail))*

> Internet.nl controleert alleen of een DKIM-record bestaat; de sleutellengte wordt niet getest.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl DKIM-test

<details><summary>3x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Geen informatie over sleutellengte-controle of het ontbreken daarvan in de bron.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 beschrijft DMARC, niet de specifieke internet.nl-testcriteria voor sleutellengte.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De claim gaat over wat internet.nl wel of niet controleert. RFC 6376 beschrijft het protocol, niet de testmethodologie van internet.nl.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *DKIM en internet.nl vallen buiten scope van RFC 7208.*
</details>

### `inet-mail-0015` — SKILL.md:151 *(§ 3. DMARC (Domain-based Message Authentication, Reporting and Conformance))*

> Internet.nl test of het DMARC-beleid `quarantine` of `reject` is; `none` is onvoldoende voor productie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl DMARC-test

<details><summary>3x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Geen informatie over specifieke DMARC-beleidscontroles in de bron.*
- **NOT_FOUND** (medium) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 beschrijft de DMARC-beleidsopties (none, quarantine, reject) maar bevat geen uitspraak over wat internet.nl als 'voldoende voor productie' beschouwt. De bron beschrijft wel dat 'p=none' geen actie verzoekt, maar dat is een andere claim dan wat internet.nl beoordeelt.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De claim gaat over internet.nl DMARC-testen en DMARC-beleid (quarantine/reject). RFC 6376 behandelt DMARC niet.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *DMARC en internet.nl vallen buiten scope van RFC 7208.*
</details>

### `inet-mail-0016` — SKILL.md:152 *(§ 3. DMARC (Domain-based Message Authentication, Reporting and Conformance))*

> Internet.nl test of een DMARC rapportage-adres (rua) geconfigureerd is.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl DMARC-test

<details><summary>3x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Geen informatie over rua-rapportageadres check in de bron.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 beschrijft DMARC inclusief de rua-tag, maar bevat geen uitspraak over wat internet.nl test.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron is RFC 6376 over DKIM. DMARC wordt niet behandeld in deze RFC.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *DMARC en internet.nl vallen buiten scope van RFC 7208.*
</details>

### `inet-mail-0018` — SKILL.md:156 *(§ 3. DMARC (Domain-based Message Authentication, Reporting and Conformance))*

> Internet.nl scoort alleen DMARC-beleid `quarantine` of `reject` als voldoende.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl DMARC-test

<details><summary>2x NOT_FOUND + 2x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Geen informatie over scoren van DMARC-beleid in de bron.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 beschrijft DMARC-beleid (none, quarantine, reject) maar bevat geen informatie over internet.nl scoringscriteria of wat als 'voldoende' wordt beschouwd.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron is RFC 6376 over DKIM. Internet.nl DMARC-scoring wordt niet behandeld.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron is RFC 7208 over SPF. DMARC en internet.nl scoringslogica komen niet voor in deze spec.*
</details>

### `inet-mail-0019` — SKILL.md:201 *(§ 4. STARTTLS)*

> STARTTLS versleutelt SMTP-verkeer tussen mailservers.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** STARTTLS

<details><summary>2x NOT_FOUND + 2x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *De bron noemt STARTTLS maar geeft geen technische beschrijving van de werking.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 gaat over DMARC. STARTTLS wordt niet besproken in deze bron.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron is RFC 6376 over DKIM. STARTTLS wordt niet behandeld.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *RFC 7208 gaat over SPF, niet over STARTTLS.*
</details>

### `inet-mail-0020` — SKILL.md:204 *(§ 4. STARTTLS)*

> Internet.nl test of MX-servers STARTTLS ondersteunen.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl STARTTLS-test

<details><summary>1x NOT_FOUND + 3x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Geen informatie over specifieke STARTTLS-subtests in de bron.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 beschrijft DMARC, niet internet.nl testmethodologie of STARTTLS-tests.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron is RFC 6376 over DKIM. Internet.nl STARTTLS-tests worden niet behandeld.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *RFC 7208 gaat over SPF, niet over internet.nl STARTTLS-tests.*
</details>

### `inet-mail-0021` — SKILL.md:205 *(§ 4. STARTTLS)*

> Internet.nl test of MX-servers TLS 1.2 of hoger ondersteunen; TLS 1.0/1.1 geeft een phase-out waarschuwing; SSL 2.0/3.0 is een harde fout.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl STARTTLS-test TLS-versies

<details><summary>1x NOT_FOUND + 3x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Geen informatie over TLS-versiecontroles in de bron.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 beschrijft DMARC, niet internet.nl TLS-versietests.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron is RFC 6376 over DKIM. TLS-versievereisten voor MX-servers worden niet behandeld.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *RFC 7208 gaat over SPF, niet over TLS-versievereisten of internet.nl tests.*
</details>

### `inet-mail-0022` — SKILL.md:206 *(§ 4. STARTTLS)*

> Internet.nl test of MX-servers een geldig certificaat hebben voor STARTTLS.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl STARTTLS-test

<details><summary>1x NOT_FOUND + 3x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Geen informatie over certificaatvalidatie in STARTTLS-test in de bron.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 beschrijft DMARC, niet internet.nl certificaatvalidatietests.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron is RFC 6376 over DKIM. Certificaatvalidatie voor STARTTLS wordt niet behandeld.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *RFC 7208 gaat over SPF, niet over certificaatvalidatie bij STARTTLS.*
</details>

### `inet-mail-0023` — SKILL.md:207 *(§ 4. STARTTLS)*

> Internet.nl test of MX-servers geen terugval naar onversleuteld verkeer toestaan.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl STARTTLS-test

<details><summary>1x NOT_FOUND + 3x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Geen informatie over downgrade-protection test in de bron.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 beschrijft DMARC, niet internet.nl downgrade-protectietests.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron is RFC 6376 over DKIM. Downgrade-bescherming voor STARTTLS wordt niet behandeld.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *RFC 7208 gaat over SPF, niet over downgrade-bescherming bij STARTTLS.*
</details>

### `inet-mail-0026` — SKILL.md:229 *(§ 5. DANE (DNS-based Authentication of Named Entities))*

> Internet.nl test of TLSA-records aanwezig zijn voor MX-servers.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl DANE-test

<details><summary>1x NOT_FOUND + 3x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Geen informatie over TLSA-record aanwezigheidscheck in de bron.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 beschrijft DMARC, niet internet.nl DANE-tests of TLSA-records.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron is RFC 6376 over DKIM. Internet.nl DANE-tests worden niet behandeld.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *RFC 7208 gaat over SPF, niet over internet.nl DANE-tests.*
</details>

### `inet-mail-0027` — SKILL.md:230 *(§ 5. DANE (DNS-based Authentication of Named Entities))*

> Internet.nl test of TLSA-parameters correct zijn voor MX-servers.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl DANE-test

<details><summary>1x NOT_FOUND + 3x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Geen informatie over TLSA-parametercontroles in de bron.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 beschrijft DMARC, niet internet.nl TLSA-parametertests.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron is RFC 6376 over DKIM. TLSA-parametervalidatie wordt niet behandeld.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *RFC 7208 gaat over SPF, niet over TLSA-parametervalidatie.*
</details>

### `inet-mail-0028` — SKILL.md:231 *(§ 5. DANE (DNS-based Authentication of Named Entities))*

> Internet.nl test of DNSSEC actief is op het MX-domein.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl DANE-test

<details><summary>1x NOT_FOUND + 3x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Geen informatie over DNSSEC-controle in DANE-test in de bron.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 beschrijft DMARC, niet internet.nl DNSSEC-tests voor MX-domeinen.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron is RFC 6376 over DKIM. DNSSEC-vereisten voor MX-domeinen worden niet behandeld.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *RFC 7208 gaat over SPF, niet over internet.nl DANE/DNSSEC-tests.*
</details>

### `inet-mail-0032` — SKILL.md:282 *(§ Veelvoorkomende problemen)*

> Een DANE TLSA mismatch treedt op als het certificaat vernieuwd is zonder het TLSA-record bij te werken.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DANE veelvoorkomende problemen

<details><summary>3x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Geen informatie over DANE TLSA mismatch in de bron.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 beschrijft DMARC, niet DANE TLSA-mismatches bij certificaatvernieuwing.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *DANE en TLSA-records worden niet behandeld in deze DKIM-specificatie.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *RFC 7208 gaat over SPF, niet over DANE TLSA mismatches bij certificaatvernieuwing.*
</details>

### `inet-mail-0034` — reference.md:23 *(§ STARTTLS inschakelen)*

> Postfix `smtp_tls_security_level = dane` configureert uitgaande verbindingen om DANE te gebruiken.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Postfix DANE configuratie

<details><summary>3x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Geen informatie over Postfix DANE-configuratie in de bron.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 behandelt geen Postfix-configuratie of DANE.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *Postfix DANE-configuratie wordt niet behandeld in deze DKIM-specificatie.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron is RFC 7208 (SPF-protocol). Postfix DANE-configuratie valt buiten het bereik van deze specificatie.*
</details>

### `inet-mail-0036` — reference.md:95 *(§ Microsoft Exchange / Microsoft 365)*

> SPF voor Microsoft 365 gebruikt het mechanisme `include:spf.protection.outlook.com`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Microsoft 365 SPF-configuratie

<details><summary>4x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Geen informatie over Microsoft 365 SPF-configuratie in de bron.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 behandelt geen Microsoft 365-specifieke SPF-configuratie.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *SPF en Microsoft 365-specifieke configuratie worden niet behandeld in RFC 6376.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron beschrijft de SPF-standaard algemeen maar noemt geen Microsoft 365-specifieke include-mechanismen.*
</details>

### `inet-mail-0037` — reference.md:100 *(§ Microsoft Exchange / Microsoft 365)*

> DKIM voor Microsoft 365 wordt geconfigureerd via het Microsoft 365 Defender-portaal onder Email & Collaboration > Policies > DKIM.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Microsoft 365 DKIM-configuratie

<details><summary>3x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Geen informatie over Microsoft 365 DKIM-configuratie in de bron.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 behandelt geen Microsoft 365 Defender-portaal of DKIM-configuratie daarin.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *Microsoft 365 Defender-portaal en platform-specifieke DKIM-configuratie vallen buiten de scope van RFC 6376.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron is RFC 7208 (SPF-protocol). DKIM-configuratie via Microsoft 365 Defender-portaal valt buiten het bereik van deze specificatie.*
</details>

### `inet-mail-0038` — reference.md:107 *(§ Microsoft Exchange / Microsoft 365)*

> Microsoft 365 DKIM gebruikt CNAME-records die verwijzen naar `selector1-example-nl._domainkey.example.onmicrosoft.com` en `selector2-example-nl._domainkey.example.onmicrosoft.com`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Microsoft 365 DKIM DNS-configuratie

<details><summary>3x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Geen informatie over Microsoft 365 CNAME-records in de bron.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 bevat geen informatie over Microsoft 365 DKIM CNAME-records.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *Microsoft 365-specifieke CNAME-records worden niet behandeld in RFC 6376.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron is RFC 7208 (SPF-protocol). Microsoft 365 DKIM CNAME-records vallen buiten het bereik van deze specificatie.*
</details>

### `inet-mail-0039` — reference.md:122 *(§ Google Workspace)*

> SPF voor Google Workspace gebruikt het mechanisme `include:_spf.google.com`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Google Workspace SPF-configuratie

<details><summary>4x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Geen informatie over Google Workspace SPF-configuratie in de bron.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 behandelt geen Google Workspace SPF-configuratie.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *Google Workspace SPF-configuratie valt buiten de scope van RFC 6376.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron beschrijft de SPF-standaard algemeen maar noemt geen Google Workspace-specifieke include-mechanismen.*
</details>

### `inet-mail-0045` — reference.md:215 *(§ Forensische rapporten (ruf))*

> Niet alle mailproviders versturen forensische DMARC-rapporten (ruf).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DMARC forensische rapportage

<details><summary>3x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Geen informatie over forensische DMARC-rapporten in de bron.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 beschrijft het mechanisme voor forensische rapporten (ruf-tag) maar zegt niets over of mailproviders deze al dan niet versturen in de praktijk.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *DMARC forensische rapporten (ruf) worden niet behandeld in RFC 6376 over DKIM.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron is RFC 7208 (SPF-protocol). DMARC forensische rapportage valt buiten het bereik van deze specificatie.*
</details>

### `inet-mail-0046` — reference.md:241 *(§ TLSA bijwerken bij certificaatvernieuwing)*

> Bij DANE met DANE-EE (3) + SPKI (1) telt alleen de publieke sleutel, niet het volledige certificaat, zodat bij hergebruik van dezelfde privesleutel het TLSA-record niet hoeft te veranderen.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DANE TLSA certificaatvernieuwing

<details><summary>2x NOT_FOUND + 2x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Geen informatie over DANE-EE en sleutelhergebruik in de bron.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 behandelt geen DANE TLSA-records, DANE-EE of SPKI-selectors.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *RFC 6376 gaat over DKIM-handtekeningen, niet over DANE of TLSA-records. De bron bevat geen informatie over DANE-EE, SPKI-selectors of TLSA-certificaatvernieuwing.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron is RFC 7208 (SPF-protocol). DANE TLSA certificaatvernieuwing valt buiten het bereik van deze specificatie.*
</details>

### `inet-mail-0048` — reference.md:262 *(§ MTA-STS configuratie)*

> MTA-STS wordt niet getest door internet.nl en is een aanvullende best practice naast DANE.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** MTA-STS

<details><summary>3x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Geen informatie over MTA-STS in de bron.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 beschrijft uitsluitend DMARC. MTA-STS wordt nergens in de brontekst genoemd.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *RFC 6376 gaat over DKIM-handtekeningen, niet over MTA-STS of internet.nl-tests.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *RFC 7208 behandelt uitsluitend SPF (Sender Policy Framework). MTA-STS wordt nergens in de brontekst genoemd.*
</details>

### `inet-mail-0050` — reference.md:291 *(§ SMTP TLS Reporting (TLSRPT))*

> SMTP TLS Reporting (TLSRPT) gebruikt een DNS TXT-record op `_smtp._tls.example.nl` met formaat `v=TLSRPTv1; rua=mailto:...` om rapporten te ontvangen over TLS-fouten.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** SMTP TLS Reporting (TLSRPT)

<details><summary>3x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Geen informatie over SMTP TLS Reporting in de bron.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *SMTP TLS Reporting (TLSRPT) wordt niet vermeld in RFC 7489. De bron behandelt uitsluitend DMARC-rapportage via rua/ruf tags.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *RFC 6376 gaat over DKIM-handtekeningen, niet over SMTP TLS Reporting (TLSRPT) of bijbehorende DNS-records.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *RFC 7208 behandelt uitsluitend SPF. SMTP TLS Reporting (TLSRPT) en het bijbehorende DNS-record op _smtp._tls worden nergens in de brontekst vermeld.*
</details>

## PARTIALLY_GROUNDED — bron ondersteunt deel van de claim (6)

### `inet-mail-0006` — SKILL.md:56 *(§ 1. SPF (Sender Policy Framework))*

> Internet.nl controleert of SPF maximaal 10 DNS-lookups gebruikt (include, a, mx, redirect).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl SPF-test

- **PARTIALLY_SUPPORTED** (medium) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  > SPF implementations MUST limit the total number of those terms to 10 during SPF evaluation, to avoid unreasonable load on the DNS. If this limit is exceeded, the implementation MUST return "permerror". The following terms cause DNS queries: the "include", "a", "mx", "ptr", and "exists" mechanisms, and the "redirect" modifier.
  - *De bron bevestigt de 10-DNS-lookup-limiet en noemt include, a, mx en redirect als lookup-veroorzakers. De claim over internet.nl die dit controleert valt buiten scope van de bron. De genoemde mechanismen kloppen inhoudelijk, maar de bron noemt ook 'ptr' en 'exists' als lookup-veroorzakers, die de claim weglaat.*
<details><summary>2x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Geen informatie over DNS-lookup limieten in de bron.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 beschrijft DMARC, niet de specifieke SPF-lookup-limietcontrole van internet.nl. De 10-lookup-limiet is onderdeel van de SPF-specificatie (RFC 7208), niet van RFC 7489.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *Gaat over SPF DNS-lookup limiet. Buiten scope van RFC 6376.*
</details>

### `inet-mail-0010` — SKILL.md:104 *(§ 2. DKIM (DomainKeys Identified Mail))*

> Internet.nl test of de DKIM publieke sleutel beschikbaar is via DNS.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl DKIM-test

- **PARTIALLY_SUPPORTED** (medium) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  > The public key for a signature is needed to complete the verification process. The process of retrieving the public key depends on the query type as defined by the "q=" tag in the DKIM-Signature header field.
  - *RFC 6376 bevestigt dat de publieke sleutel via DNS beschikbaar moet zijn voor verificatie, maar beschrijft niet wat internet.nl specifiek test. Het DNS-opzoekingsaspect wordt volledig ondersteund; het 'internet.nl'-gedeelte is out of scope.*
<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Geen informatie over DKIM DNS-beschikbaarheid check in de bron.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 beschrijft DMARC, niet de specifieke internet.nl-controle op beschikbaarheid van DKIM publieke sleutels.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *DKIM en internet.nl vallen buiten scope van RFC 7208.*
</details>

### `inet-mail-0024` — SKILL.md:222 *(§ 5. DANE (DNS-based Authentication of Named Entities))*

> DANE koppelt TLS-certificaten aan DNS via TLSA-records, beveiligd met DNSSEC.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DANE (DNS-based Authentication of Named Entities)

- **PARTIALLY_SUPPORTED** (low) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  > To reduce the risk of subversion of the DMARC mechanism due to DNS-based exploits, serious consideration should be given to the deployment of DNSSEC in parallel with the deployment of DMARC by both Domain Owners and Mail Receivers.
  - *RFC 7489 noemt DNSSEC als aanbeveling naast DMARC, maar behandelt DANE of TLSA-records niet expliciet. De claim over DANE koppeling via TLSA-records is niet te verifiëren vanuit deze bron.*
<details><summary>1x NOT_FOUND + 2x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *De bron noemt DANE maar geeft geen technische beschrijving van TLSA of DNSSEC-koppeling.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron is RFC 6376 over DKIM. DANE en TLSA-records worden niet behandeld.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *RFC 7208 gaat over SPF, niet over DANE of TLSA-records.*
</details>

### `inet-mail-0041` — reference.md:141 *(§ DKIM key rotation)*

> DKIM key rotation wordt aanbevolen elke 6-12 maanden en vereist een nieuwe selector bij elke rotatie.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** DKIM key rotation

- **PARTIALLY_SUPPORTED** (medium) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  > Signers are ill-advised to reuse selectors for new keys. A better strategy is to assign new keys to new selectors.
  - *De bron ondersteunt dat nieuwe sleutels een nieuwe selector vereisen, maar noemt geen aanbevolen rotatie-interval van 6-12 maanden.*
<details><summary>2x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Geen informatie over DKIM key rotation in de bron.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 behandelt geen DKIM key rotation aanbevelingen of intervallen.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron is RFC 7208 (SPF-protocol). DKIM key rotation valt buiten het bereik van deze specificatie.*
</details>

### `inet-mail-0042` — reference.md:153 *(§ DKIM key rotation)*

> Bij DKIM key rotation moet na het publiceren van het nieuwe DNS-record gewacht worden tot DNS is gepropageerd (controleer TTL) voordat OpenDKIM wordt geconfigureerd.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** DKIM key rotation procedure

- **PARTIALLY_SUPPORTED** (medium) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  > if a domain wishes to change from using a public key associated with selector 'january2005' to a public key associated with selector 'february2005', it merely makes sure that both public keys are advertised in the public-key repository concurrently for the transition period during which email may be in transit prior to verification.
  - *De bron ondersteunt het concept van gelijktijdige publicatie tijdens een transitieperiode, maar noemt niets specifieks over wachten op DNS-propagatie of het controleren van TTL voordat de configuratie wordt gewijzigd.*
<details><summary>2x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Geen informatie over DKIM key rotation procedure in de bron.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 behandelt geen DKIM key rotation procedures of DNS-propagatie stappen.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron is RFC 7208 (SPF-protocol). DKIM key rotation procedure valt buiten het bereik van deze specificatie.*
</details>

### `inet-mail-0044` — reference.md:170 *(§ DMARC-rapportage analyseren)*

> DMARC-aggregaatrapporten worden dagelijks verstuurd als XML (vaak gzipped) en bevatten statistieken over alle e-mail verstuurd namens het domein.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DMARC-rapportage aggregaat

- **PARTIALLY_SUPPORTED** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  > "Visibility comes in the form of daily (or more frequent) Mail Receiver-originated feedback reports that contain aggregate data on message streams relevant to the Domain Owner." en "The aggregate data MUST be an XML file that SHOULD be subjected to GZIP compression."
  - *De bron bevestigt dagelijkse verzending en XML/gzip-formaat. De claim 'statistieken over alle e-mail verstuurd namens het domein' is deels ondersteund; de RFC zegt dat rapporten data bevatten over berichten die het domein claimen, inclusief geslaagde en mislukte authenticatie, maar spreekt niet expliciet van 'alle e-mail verstuurd namens het domein'.*
<details><summary>2x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Geen informatie over DMARC aggregaatrapporten in de bron.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *DMARC-rapportage (aggregaat of anders) wordt niet behandeld in RFC 6376 over DKIM.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron is RFC 7208 (SPF-protocol). DMARC-rapportage valt buiten het bereik van deze specificatie.*
</details>

## UNGROUNDED — geen bron ondersteunt de claim (9)

### `inet-mail-0025` — SKILL.md:226 *(§ 5. DANE (DNS-based Authentication of Named Entities))*

> DANE vereist dat DNSSEC actief is op het domein.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** DANE vereisten

<details><summary>2x NOT_FOUND + 2x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Geen informatie over DANE-vereisten in de bron.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 beschrijft DMARC, niet DANE-vereisten. DNSSEC wordt aanbevolen voor DMARC maar DANE-specifieke vereisten worden niet besproken.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron is RFC 6376 over DKIM. DANE-vereisten worden niet behandeld.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *RFC 7208 gaat over SPF, niet over DANE/DNSSEC-vereisten.*
</details>

### `inet-mail-0029` — SKILL.md:242 *(§ 5. DANE (DNS-based Authentication of Named Entities))*

> De aanbevolen TLSA-parameters voor mail zijn: Certificate Usage 3 (DANE-EE), Selector 1 (SubjectPublicKeyInfo), Matching Type 1 (SHA-256).

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** DANE TLSA-parameters voor mail

<details><summary>2x NOT_FOUND + 2x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Geen informatie over aanbevolen TLSA-parameters in de bron.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 beschrijft DMARC, niet DANE TLSA-parameters (Certificate Usage, Selector, Matching Type).*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron is RFC 6376 over DKIM. DANE TLSA-parameters voor mail worden niet behandeld.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *RFC 7208 gaat over SPF, niet over aanbevolen TLSA-parameters.*
</details>

### `inet-mail-0031` — SKILL.md:280 *(§ Veelvoorkomende problemen)*

> DMARC `p=none` is onvoldoende; overheidsorganisaties moeten overschakelen naar `p=quarantine` of `p=reject`.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** DMARC veelvoorkomende problemen

<details><summary>3x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Geen informatie over DMARC p=none voor overheidsorganisaties in de bron.*
- **NOT_FOUND** (medium) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 beschrijft p=none als een geldig beleid ('The Domain Owner requests no specific action be taken regarding delivery of messages') maar bevat geen normatieve uitspraak dat overheidsorganisaties MOETEN overschakelen naar quarantine of reject. De modality MUST is niet terug te vinden in deze bron.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *Deze bron gaat over DKIM (RFC 6376), niet over DMARC. DMARC-beleid (p=none/quarantine/reject) wordt niet behandeld.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *RFC 7208 gaat over SPF, niet over DMARC-beleid of overheidsverplichtingen.*
</details>

### `inet-mail-0033` — reference.md:17 *(§ STARTTLS inschakelen)*

> Postfix `smtpd_tls_protocols` moet SSLv2, SSLv3, TLSv1 en TLSv1.1 uitsluiten voor inkomende verbindingen.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Postfix STARTTLS configuratie

<details><summary>3x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Geen informatie over Postfix-configuratie in de bron.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 gaat over DMARC als protocol, niet over Postfix-configuratie of TLS-protocollen.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *Postfix-configuratie en TLS-protocollen vallen buiten de scope van RFC 6376.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron is RFC 7208 (SPF-protocol). Postfix TLS-configuratie valt buiten het bereik van deze specificatie.*
</details>

### `inet-mail-0035` — reference.md:27 *(§ STARTTLS inschakelen)*

> Postfix `smtp_dns_support_level = dnssec` is vereist voor DANE-ondersteuning bij uitgaande verbindingen.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Postfix DANE configuratie

<details><summary>3x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Geen informatie over Postfix DNSSEC-configuratie in de bron.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 behandelt geen Postfix-configuratie of DNSSEC-instellingen voor DANE.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *Postfix DNSSEC-configuratie valt buiten de scope van RFC 6376.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron is RFC 7208 (SPF-protocol). Postfix DANE-configuratie valt buiten het bereik van deze specificatie.*
</details>

### `inet-mail-0040` — reference.md:129 *(§ Google Workspace)*

> Google Workspace raadt een DKIM-sleutellengte van 2048-bit aan bij het genereren van een nieuw record.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** Google Workspace DKIM-configuratie

<details><summary>3x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Geen informatie over Google Workspace DKIM-sleutellengte in de bron.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 behandelt geen Google Workspace DKIM-sleutellengte aanbevelingen.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *Google Workspace-specifieke aanbevelingen voor sleutellengte worden niet behandeld. RFC 6376 noemt wel sleutelgroottes maar niet in Google Workspace-context.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron is RFC 7208 (SPF-protocol). Google Workspace DKIM-sleutellengte valt buiten het bereik van deze specificatie.*
</details>

### `inet-mail-0043` — reference.md:163 *(§ DKIM key rotation)*

> Bij DKIM key rotation moet het oude DNS-record pas na 1-2 weken worden verwijderd.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** DKIM key rotation procedure

<details><summary>3x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Geen informatie over verwijderen van oude DKIM DNS-records in de bron.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 behandelt geen DKIM key rotation procedures of timing voor verwijdering van oude records.*
- **NOT_FOUND** (medium) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *RFC 6376 beschrijft een transitieperiode waarbij beide sleutels gelijktijdig beschikbaar zijn, maar noemt geen specifieke termijn van 1-2 weken voor het verwijderen van het oude record.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron is RFC 7208 (SPF-protocol). DKIM key rotation timing valt buiten het bereik van deze specificatie.*
</details>

### `inet-mail-0047` — reference.md:240 *(§ TLSA bijwerken bij certificaatvernieuwing)*

> Bij DANE certificaatvernieuwing moet de pre-publish methode worden gebruikt: publiceer het TLSA-record van het nieuwe certificaat voordat het actief wordt.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** DANE TLSA certificaatvernieuwing

<details><summary>2x NOT_FOUND + 2x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Geen informatie over pre-publish methode voor DANE in de bron.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 behandelt geen DANE certificaatvernieuwing of pre-publish methodes.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *RFC 6376 gaat over DKIM-handtekeningen, niet over DANE of de pre-publish methode voor TLSA-records.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron is RFC 7208 (SPF-protocol). DANE pre-publish methode valt buiten het bereik van deze specificatie.*
</details>

### `inet-mail-0049` — reference.md:267 *(§ MTA-STS configuratie)*

> MTA-STS vereist een DNS TXT-record op `_mta-sts.example.nl`, een HTTPS-website op `mta-sts.example.nl` met geldig certificaat, en een beleidsbestand op `https://mta-sts.example.nl/.well-known/mta-sts.txt`.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** MTA-STS vereisten

<details><summary>3x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Geen informatie over MTA-STS vereisten in de bron.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 gaat over DMARC, niet over MTA-STS. Geen enkel onderdeel van de MTA-STS vereisten (DNS TXT-record op _mta-sts, HTTPS-website, beleidsbestand) wordt behandeld.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *RFC 6376 gaat over DKIM-handtekeningen, niet over MTA-STS-vereisten zoals DNS TXT-records of beleidsbestanden.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *RFC 7208 behandelt uitsluitend SPF. MTA-STS, DNS TXT-records op _mta-sts, en bijbehorende HTTPS-vereisten komen niet voor in de brontekst.*
</details>

## GROUNDED — minstens één bron ondersteunt de claim (8)

<details>
<summary>Klap uit voor alle GROUNDED claims</summary>

### `inet-mail-0001` — SKILL.md:26 *(§ Overzicht)*

> Internet.nl test e-maildomeinen op SPF, DKIM, DMARC, STARTTLS en DANE.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl mailtest

- **SUPPORTED** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  > After you enter a domain name of an email service, we will test if the email service offers support for the modern Internet Standards below. [...] DMARC, DKIM and SPF : authenticity marks against email phishing? STARTTLS and DANE : secure mail server connection?
- **PARTIALLY_SUPPORTED** (medium) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  > DMARC is a scalable mechanism by which a mail-originating organization can express domain-level policies and preferences for message validation, disposition, and reporting... The following mechanisms for determining Authenticated Identifiers are supported in this version of DMARC: [DKIM]... [SPF]
  - *RFC 7489 behandelt alleen DMARC (en de relatie met SPF en DKIM). STARTTLS en DANE worden in deze bron niet vermeld. De claim over internet.nl als testplatform wordt ook niet bevestigd.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron is RFC 6376 (DKIM specificatie). Internet.nl's testscope (SPF, DKIM, DMARC, STARTTLS, DANE) wordt hier niet behandeld.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron is RFC 7208, de SPF-specificatie. Internet.nl wordt niet genoemd; DKIM, DMARC, STARTTLS en DANE vallen buiten scope van deze bron.*

### `inet-mail-0003` — SKILL.md:50 *(§ 1. SPF (Sender Policy Framework))*

> SPF specificeert welke mailservers e-mail mogen versturen namens een domein via een DNS TXT-record.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** SPF (Sender Policy Framework)

- **SUPPORTED** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  > [SPF], which can authenticate both the domain found in an [SMTP] HELO/EHLO command (the HELO identity) and the domain found in an SMTP MAIL command (the MAIL FROM identity)... Domain Owner constructs an SPF policy and publishes it in its DNS database as per [SPF].
  - *De bron bevestigt dat SPF via DNS gepubliceerd wordt en aangeeft welke mailservers mogen versturen namens een domein. Het DNS TXT-record formaat wordt impliciet bevestigd via de verwijzing naar SPF-publicatie in DNS.*
- **SUPPORTED** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  > SPF-compliant domain publishes valid SPF records as described in Section 3. These records authorize the use of the relevant domain names in the "HELO" and "MAIL FROM" identities by the MTAs specified therein. [...] SPF records MUST be published as a DNS TXT (type 16) Resource Record (RR)
- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *De bron noemt SPF enkel als categorie, maar geeft geen technische beschrijving van hoe SPF werkt.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron gaat over DKIM, niet over SPF (Sender Policy Framework). SPF wordt in RFC 6376 niet gedefinieerd of beschreven.*

### `inet-mail-0008` — SKILL.md:99 *(§ 2. DKIM (DomainKeys Identified Mail))*

> DKIM voorziet e-mail van een cryptografische handtekening via een DNS-publicsleutel die de ontvangende mailserver verifieert.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DKIM (DomainKeys Identified Mail)

- **SUPPORTED** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  > [DKIM], which provides a domain-level identifier in the content of the 'd=' tag of a validated DKIM-Signature header field... Submission service passes relevant details to the DKIM signing module in order to generate a DKIM signature to be applied to the message.
  - *De bron bevestigt dat DKIM een cryptografische handtekening toevoegt via een DNS-gepubliceerde sleutel die de ontvangende mailserver verifieert.*
- **SUPPORTED** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  > DKIM permits a person, role, or organization that owns the signing domain to claim some responsibility for a message by associating the domain with the message. Assertion of responsibility is validated through a cryptographic signature and by querying the Signer's domain directly to retrieve the appropriate public key.
- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *De bron noemt DKIM enkel als categorie zonder technische beschrijving.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *DKIM wordt niet behandeld in RFC 7208; dit is een SPF-specificatie.*

### `inet-mail-0012` — SKILL.md:107 *(§ 2. DKIM (DomainKeys Identified Mail))*

> RFC 6376 vereist minimaal 1024-bit RSA voor langlevende DKIM-sleutels.

**Type:** reference_claim  ·  **Modaliteit:** MUST  ·  **Scope:** DKIM RFC 6376

- **SUPPORTED** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  > Signers MUST use RSA keys of at least 1024 bits for long-lived keys. Verifiers MUST be able to validate signatures with keys ranging from 512 bits to 2048 bits, and they MAY be able to validate signatures with larger keys.

### `inet-mail-0013` — SKILL.md:108 *(§ 2. DKIM (DomainKeys Identified Mail))*

> 2048-bit RSA is de huidige operationele aanbeveling voor DKIM-sleutels (o.a. NIST, M3AAWG), niet een eis uit RFC 6376.

**Type:** factual_assertion  ·  **Modaliteit:** SHOULD  ·  **Scope:** DKIM sleutellengte aanbeveling

- **SUPPORTED** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  > Signers MUST use RSA keys of at least 1024 bits for long-lived keys.
  - *RFC 6376 schrijft alleen 1024-bit als minimum voor. De claim dat 2048-bit een aanbeveling is van NIST/M3AAWG en níet een eis uit RFC 6376 is correct: de bron noemt geen 2048-bit eis of aanbeveling, alleen een minimum van 1024-bit.*

### `inet-mail-0014` — SKILL.md:150 *(§ 3. DMARC (Domain-based Message Authentication, Reporting and Conformance))*

> Het DMARC-record staat op `_dmarc.example.nl` als DNS TXT-record.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DMARC DNS-record

- **SUPPORTED** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  > Domain Owner DMARC preferences are stored as DNS TXT records in subdomains named '_dmarc'. For example, the Domain Owner of 'example.com' would post DMARC preferences in a TXT record at '_dmarc.example.com'.
  - *De bron bevestigt exact dit patroon, met 'example.com' als voorbeeld. De claim gebruikt 'example.nl' maar het principe is identiek.*
<details><summary>2x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *De bron geeft geen technische details over DMARC DNS-records.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De claim gaat over DMARC DNS-records (_dmarc.example.nl). RFC 6376 gaat over DKIM; DMARC wordt niet behandeld.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *DMARC wordt niet behandeld in RFC 7208.*
</details>

### `inet-mail-0017` — SKILL.md:154 *(§ 3. DMARC (Domain-based Message Authentication, Reporting and Conformance))*

> DMARC implementatiepad: start met `p=none` om rapportages te verzamelen, schakel daarna over naar `quarantine` en uiteindelijk `reject`.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** DMARC gefaseerde uitrol

- **SUPPORTED** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  > The owner of the domain 'example.com' has deployed SPF and DKIM on its messaging infrastructure. The owner wishes to begin using DMARC with a policy that will solicit aggregate feedback from receivers without affecting how the messages are processed... ('p=none')... The Domain Owner accomplishes this by constructing a policy record... Receivers should quarantine messages from this Organizationa...
  - *De bron illustreert expliciet het gefaseerde implementatiepad: beginnen met p=none voor rapportages, dan quarantine, en de reject-optie wordt ook beschreven als eindstadium.*
<details><summary>2x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Geen implementatieadvies of fasering voor DMARC in de bron.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron is RFC 6376 over DKIM. DMARC-implementatiepad wordt niet behandeld.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *DMARC-implementatieadvies valt buiten scope van RFC 7208.*
</details>

### `inet-mail-0030` — SKILL.md:278 *(§ Veelvoorkomende problemen)*

> Een SPF `permerror` wordt veroorzaakt door meer dan 10 DNS-lookups; oplossing is minder `include`-verwijzingen en direct gebruik van `ip4`/`ip6`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** SPF veelvoorkomende problemen

- **SUPPORTED** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  > SPF implementations MUST limit the total number of those terms to 10 during SPF evaluation, to avoid unreasonable load on the DNS. If this limit is exceeded, the implementation MUST return "permerror".
  - *De bron bevestigt dat overschrijding van 10 DNS-lookups een permerror oplevert. De oplossingsrichting (minder includes, direct ip4/ip6) wordt impliciet ondersteund door Section 10.1.1 die ip4/ip6 als 'Best record' aanbeveelt.*
<details><summary>2x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Geen informatie over SPF permerror of DNS-lookup problemen in de bron.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 beschrijft DMARC. SPF permerror door meer dan 10 DNS-lookups wordt niet behandeld in deze bron.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron is RFC 6376 over DKIM. SPF en DNS-lookup limieten worden niet behandeld.*
</details>

</details>
