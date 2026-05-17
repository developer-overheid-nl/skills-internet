<!-- markdownlint-disable MD052 MD034 MD013 -->
# Audit inet-mail — 2026-05-17

> Automatisch gegenereerd door audit-tooling. Niet handmatig bewerken; wijzig SKILL.md / reference.md en regenereer.

## Samenvatting

| Status | Aantal | % |
|--------|--------|---|
| UNSUPPORTED_ASSERTION | 19 | 42% |
| CONTRADICTED | 1 | 2% |
| PARTIALLY_GROUNDED | 7 | 16% |
| UNGROUNDED | 10 | 22% |
| NO_SOURCE | 0 | 0% |
| UNVERIFIABLE | 0 | 0% |
| KNOWN_DISCREPANCY | 0 | 0% |
| GROUNDED | 8 | 18% |

*Geverifieerd met sonnet, 11 calls, $2.4558.*

## UNSUPPORTED_ASSERTION — stellige bewering zonder enige bronsteun (mogelijke hallucinatie) (19)

### `inet-mail-0001` — SKILL.md:27 *(§ Overzicht)*

> SPF, DKIM, DMARC, STARTTLS en DANE staan op de pas-toe-of-leg-uit-lijst van Forum Standaardisatie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Mailstandaarden / Forum Standaardisatie

<details><summary>3x NOT_FOUND + 2x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (low) — [https://www.forumstandaardisatie.nl/open-standaarden](https://www.forumstandaardisatie.nl/open-standaarden)
  - *De brontekst is een navigatie-/lijstpagina van forumstandaardisatie.nl zonder de daadwerkelijke lijst van standaarden. SPF, DKIM, DMARC, STARTTLS en DANE worden niet bij naam genoemd. De pagina verwijst wel naar een 'Pas toe of leg uit'-lijst maar toont de inhoud daarvan niet.*
- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *De brontekst vermeldt de Forum Standaardisatie pas-toe-of-leg-uit-lijst niet.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *De bron is RFC 7489 (technische DMARC-specificatie). De claim gaat over de Nederlandse Forum Standaardisatie pas-toe-of-leg-uit-lijst, wat een Nederlands beleidsregister is dat niet in deze RFC behandeld wordt.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron is RFC 6376 (DKIM technische specificatie). Bevat geen informatie over Forum Standaardisatie of pas-toe-of-leg-uit-lijsten.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron is RFC 7208 (SPF-specificatie). Forum Standaardisatie en de pas-toe-of-leg-uit-lijst worden hier niet behandeld.*
</details>

### `inet-mail-0005` — SKILL.md:57 *(§ 1. SPF (Sender Policy Framework))*

> Internet.nl test of het SPF-record eindigt op `-all` (fail) of `~all` (softfail).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** SPF / internet.nl testcriteria

<details><summary>3x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *De brontekst beschrijft niet of internet.nl test op `-all` of `~all` in SPF-records.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *De claim gaat over internet.nl testcriteria voor SPF `-all`/`~all`. De bron is de DMARC RFC.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron gaat over DKIM, niet over SPF of internet.nl testcriteria.*
- **NOT_FOUND** (medium) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron beschrijft wat '-all' en '~all' betekenen, maar stelt nergens dat SPF-records op '-all' of '~all' moeten eindigen als testcriterium. Dat is een internet.nl-testcriterium, niet iets dat RFC 7208 voorschrijft.*
</details>

### `inet-mail-0008` — SKILL.md:103 *(§ 2. DKIM (DomainKeys Identified Mail))*

> Internet.nl test of minimaal 1 geldige DKIM-handtekening aanwezig is op de testmail.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DKIM / internet.nl testcriteria

<details><summary>2x NOT_FOUND + 2x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *De brontekst noemt DKIM maar geeft geen detail over het testen van DKIM-handtekeningen op testmail.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *De claim gaat over internet.nl testcriteria voor DKIM-handtekeningen. De bron is de DMARC RFC, niet internet.nl documentatie.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron beschrijft de DKIM-standaard zelf, niet de internet.nl testcriteria.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *DKIM wordt niet behandeld in RFC 7208. Dit is een SPF-specificatie.*
</details>

### `inet-mail-0010` — SKILL.md:106 *(§ 2. DKIM (DomainKeys Identified Mail))*

> Internet.nl controleert alleen of een DKIM-record bestaat; de sleutellengte wordt niet getest.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DKIM / internet.nl testcriteria

<details><summary>2x NOT_FOUND + 2x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *De brontekst geeft geen details over wat internet.nl wel of niet controleert bij DKIM.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *De claim gaat over internet.nl testcriteria voor DKIM sleutellengte. De bron is de DMARC RFC.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron beschrijft de DKIM-standaard, niet de internet.nl testcriteria over wel of niet testen van sleutellengte.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *DKIM wordt niet behandeld in RFC 7208.*
</details>

### `inet-mail-0014` — SKILL.md:151 *(§ 3. DMARC (Domain-based Message Authentication, Reporting and Conformance))*

> Internet.nl scoort alleen DMARC `p=quarantine` of `p=reject` als voldoende; `p=none` is onvoldoende.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DMARC / internet.nl testcriteria

<details><summary>3x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *De brontekst vermeldt DMARC maar geeft geen detail over hoe `p=none` versus `p=quarantine`/`p=reject` wordt beoordeeld.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *De bron beschrijft de DMARC-beleidswaarden `none`, `quarantine` en `reject`, maar maakt geen uitspraak over internet.nl scoringscriteria of dat `p=none` als onvoldoende wordt beoordeeld.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron gaat over DKIM, niet over DMARC of internet.nl testcriteria.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *DMARC wordt niet behandeld in RFC 7208.*
</details>

### `inet-mail-0015` — SKILL.md:152 *(§ 3. DMARC (Domain-based Message Authentication, Reporting and Conformance))*

> Internet.nl test of een DMARC rapportage-adres (rua) geconfigureerd is.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DMARC / internet.nl testcriteria

<details><summary>3x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Het testen van een DMARC rua-adres wordt niet beschreven in de brontekst.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *De bron beschrijft de `rua`-tag uitgebreid, maar maakt geen uitspraak over internet.nl testcriteria die controleren of een rua-adres geconfigureerd is.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron gaat over DKIM, niet over DMARC of internet.nl testcriteria.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *DMARC wordt niet behandeld in RFC 7208.*
</details>

### `inet-mail-0019` — SKILL.md:205 *(§ 4. STARTTLS)*

> Internet.nl test of MX-servers TLS 1.2 of hoger ondersteunen; TLS 1.0/1.1 geeft een phase-out waarschuwing en SSL 2.0/3.0 is een harde fout.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** STARTTLS / internet.nl testcriteria

<details><summary>1x NOT_FOUND + 3x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *De brontekst geeft geen detail over TLS-versiecontroles of phase-out waarschuwingen.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *De bron is RFC 7489 (DMARC). TLS-versievereisten voor MX-servers en internet.nl testcriteria worden niet behandeld.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *RFC 6376 gaat over DKIM-signatures, niet over internet.nl TLS-versietests voor MX-servers.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron is RFC 7208 over SPF. TLS-versievereisten en internet.nl testcriteria zijn buiten scope.*
</details>

### `inet-mail-0020` — SKILL.md:206 *(§ 4. STARTTLS)*

> Internet.nl test of MX-servers een geldig certificaat hebben voor STARTTLS.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** STARTTLS / internet.nl testcriteria

<details><summary>1x NOT_FOUND + 3x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Certificaatvalidatie voor STARTTLS wordt niet beschreven in de brontekst.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *De bron is RFC 7489 (DMARC). Certificaatvalidatie voor STARTTLS en internet.nl testcriteria vallen buiten scope.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *RFC 6376 gaat over DKIM-signatures, niet over internet.nl certificaatvalidatie voor STARTTLS.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron is RFC 7208 over SPF. Certificaatvalidatie voor STARTTLS is buiten scope.*
</details>

### `inet-mail-0021` — SKILL.md:207 *(§ 4. STARTTLS)*

> Internet.nl test of MX-servers geen terugval naar onversleuteld verkeer hebben bij STARTTLS.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** STARTTLS / internet.nl testcriteria

<details><summary>1x NOT_FOUND + 3x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Testen op terugval naar onversleuteld verkeer wordt niet beschreven in de brontekst.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *De bron is RFC 7489 (DMARC). Terugval naar onversleuteld verkeer bij STARTTLS wordt niet behandeld.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *RFC 6376 gaat over DKIM-signatures, niet over internet.nl downgrade-tests voor STARTTLS.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron is RFC 7208 over SPF. STARTTLS downgrade-bescherming is buiten scope.*
</details>

### `inet-mail-0023` — SKILL.md:229 *(§ 5. DANE (DNS-based Authentication of Named Entities))*

> Internet.nl test of TLSA-records aanwezig zijn voor MX-servers bij DANE.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DANE / internet.nl testcriteria

<details><summary>1x NOT_FOUND + 3x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Het testen van TLSA-records wordt niet beschreven in de brontekst.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *De bron is RFC 7489 (DMARC). DANE TLSA-records en internet.nl testcriteria worden niet behandeld.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *RFC 6376 gaat over DKIM-signatures, niet over internet.nl DANE/TLSA-tests.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron is RFC 7208 over SPF. DANE TLSA-records en internet.nl testcriteria zijn buiten scope.*
</details>

### `inet-mail-0024` — SKILL.md:230 *(§ 5. DANE (DNS-based Authentication of Named Entities))*

> Internet.nl test of TLSA-records correcte parameters hebben voor DANE.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DANE / internet.nl testcriteria

<details><summary>1x NOT_FOUND + 3x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *TLSA-recordparameters worden niet beschreven in de brontekst.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *De bron is RFC 7489 (DMARC). DANE TLSA-parameters worden niet behandeld.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *RFC 6376 gaat over DKIM-signatures, niet over internet.nl TLSA-parametervalidatie.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron is RFC 7208 over SPF. DANE TLSA-parameters zijn buiten scope.*
</details>

### `inet-mail-0025` — SKILL.md:231 *(§ 5. DANE (DNS-based Authentication of Named Entities))*

> Internet.nl test of DNSSEC actief is op het MX-domein bij DANE.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DANE / internet.nl testcriteria

<details><summary>1x NOT_FOUND + 3x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Het testen van DNSSEC bij DANE wordt niet beschreven in de brontekst.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *De bron is RFC 7489 (DMARC). DNSSEC op MX-domein bij DANE wordt niet behandeld.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *RFC 6376 gaat over DKIM-signatures, niet over internet.nl DNSSEC-tests bij DANE.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron is RFC 7208 over SPF. DNSSEC-vereisten voor DANE zijn buiten scope.*
</details>

### `inet-mail-0027` — SKILL.md:244 *(§ 5. DANE (DNS-based Authentication of Named Entities))*

> DANE Selector `1` staat voor SubjectPublicKeyInfo (publieke sleutel) in TLSA-records.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DANE / TLSA-parameters

<details><summary>1x NOT_FOUND + 3x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *TLSA Selector-waarden worden niet beschreven in de brontekst.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *De bron is RFC 7489 (DMARC). DANE TLSA Selector-waarden worden niet behandeld.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *RFC 6376 gaat over DKIM-signatures, niet over DANE TLSA Selector-waarden.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron is RFC 7208 over SPF. DANE Selector parameters zijn buiten scope.*
</details>

### `inet-mail-0028` — SKILL.md:245 *(§ 5. DANE (DNS-based Authentication of Named Entities))*

> DANE Matching Type `1` staat voor SHA-256 hash in TLSA-records.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DANE / TLSA-parameters

<details><summary>1x NOT_FOUND + 3x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *TLSA Matching Type-waarden worden niet beschreven in de brontekst.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *De bron is RFC 7489 (DMARC). DANE TLSA Matching Type-waarden worden niet behandeld.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *RFC 6376 gaat over DKIM-signatures, niet over DANE TLSA Matching Type-waarden.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron is RFC 7208 over SPF. DANE Matching Type parameters zijn buiten scope.*
</details>

### `inet-mail-0030` — SKILL.md:282 *(§ Veelvoorkomende problemen)*

> Een DANE TLSA mismatch treedt op wanneer een certificaat vernieuwd wordt zonder het TLSA-record bij te werken.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DANE / veelvoorkomende problemen

<details><summary>1x NOT_FOUND + 3x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *DANE TLSA mismatch bij certificaatvernieuwing wordt niet beschreven in de brontekst.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *De bron is RFC 7489 (DMARC). DANE TLSA mismatch bij certificaatvernieuwing wordt niet behandeld.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *RFC 6376 gaat over DKIM-signatures, niet over DANE TLSA mismatch bij certificaatverlenging.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron is RFC 7208 over SPF. DANE TLSA mismatch bij certificaatvernieuwing is buiten scope.*
</details>

### `inet-mail-0040` — reference.md:215 *(§ Forensische rapporten (ruf))*

> Niet alle mailproviders versturen forensische DMARC ruf-rapporten.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DMARC / forensische rapporten

<details><summary>2x NOT_FOUND + 2x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Forensische DMARC ruf-rapporten worden niet beschreven in de brontekst.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 beschrijft het mechanisme voor ruf-rapporten maar stelt nergens expliciet dat niet alle mailproviders forensische rapporten versturen.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron beschrijft DKIM signatures. DMARC forensische rapporten vallen buiten de scope van RFC 6376.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron gaat over SPF. DMARC forensische rapporten worden niet behandeld.*
</details>

### `inet-mail-0041` — reference.md:241 *(§ TLSA bijwerken bij certificaatvernieuwing)*

> Bij DANE met DANE-EE (3) + SPKI (1) telt alleen de publieke sleutel, niet het volledige certificaat; als dezelfde privesleutel wordt hergebruikt bij vernieuwing hoeft het TLSA-record niet te veranderen.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DANE / TLSA-beheer bij certificaatvernieuwing

<details><summary>1x NOT_FOUND + 3x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *DANE-EE SPKI-gedrag bij certificaatvernieuwing wordt niet beschreven in de brontekst.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 gaat over DMARC, niet over DANE TLSA-records of DANE-EE certificaatbeheer.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron beschrijft DKIM signatures. DANE TLSA-records en certificaatbeheer vallen buiten de scope van RFC 6376.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron gaat over SPF. DANE TLSA-records en DANE-EE worden niet behandeld.*
</details>

### `inet-mail-0043` — reference.md:262 *(§ MTA-STS configuratie)*

> MTA-STS wordt niet getest door internet.nl; het is een aanvullende best practice naast DANE.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** MTA-STS / internet.nl

<details><summary>1x NOT_FOUND + 3x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *MTA-STS wordt niet vermeld in de brontekst.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 gaat over DMARC, niet over MTA-STS of internet.nl tests.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron beschrijft DKIM signatures. MTA-STS en internet.nl-testen vallen buiten de scope van RFC 6376.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron gaat over SPF. MTA-STS en internet.nl worden niet behandeld.*
</details>

### `inet-mail-0045` — reference.md:291 *(§ SMTP TLS Reporting (TLSRPT))*

> SMTP TLS Reporting (TLSRPT) gebruikt een DNS TXT-record op `_smtp._tls.example.nl` met formaat `v=TLSRPTv1; rua=mailto:...` om rapporten te ontvangen over TLS-fouten.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** TLSRPT / DNS-record

<details><summary>1x NOT_FOUND + 3x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *SMTP TLS Reporting (TLSRPT) wordt niet beschreven in de brontekst.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 gaat over DMARC, niet over SMTP TLS Reporting (TLSRPT) DNS-records.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron beschrijft DKIM signatures. SMTP TLS Reporting (TLSRPT) valt buiten de scope van RFC 6376.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron gaat over SPF. SMTP TLS Reporting (TLSRPT) en bijbehorende DNS-records worden niet behandeld.*
</details>

## CONTRADICTED — bron spreekt de claim expliciet tegen (1)

### `inet-mail-0006` — SKILL.md:74 *(§ 1. SPF (Sender Policy Framework))*

> Het SPF-mechanisme `include:domein` neemt het SPF-beleid van een ander domein over.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** SPF mechanismen

- **CONTRADICTED** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  > In hindsight, the name "include" was poorly chosen. Only the evaluated result of the referenced SPF record is used, rather than literally including the mechanisms of the referenced record in the first.
  - *De claim zegt dat 'include' het SPF-beleid van een ander domein 'overneemt', maar de bron stelt expliciet dat alleen het evaluatieresultaat wordt gebruikt, niet de mechanismen letterlijk worden overgenomen.*
<details><summary>2x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *SPF-mechanismen worden niet beschreven in de brontekst.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *De claim gaat over het SPF `include:`-mechanisme. De bron is de DMARC RFC, niet de SPF-specificatie (RFC 7208).*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron gaat over DKIM, niet over SPF-mechanismen.*
</details>

## PARTIALLY_GROUNDED — bron ondersteunt deel van de claim (7)

### `inet-mail-0009` — SKILL.md:104 *(§ 2. DKIM (DomainKeys Identified Mail))*

> Internet.nl test of de DKIM publieke sleutel beschikbaar is via DNS.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DKIM / internet.nl testcriteria

- **PARTIALLY_SUPPORTED** (medium) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  > Parameters to the key lookup algorithm are the type of the lookup (the "q=" tag), the domain of the Signer (the "d=" tag of the DKIM-Signature header field), and the selector (the "s=" tag). [...] This document defines a single binding, using DNS TXT RRs to distribute the keys.
  - *De bron bevestigt dat de publieke sleutel via DNS beschikbaar moet zijn (DNS TXT RR), wat de technische basis is van de claim. De bron zegt echter niets over internet.nl testcriteria specifiek.*
<details><summary>1x NOT_FOUND + 2x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *De beschikbaarheid van DKIM publieke sleutels via DNS wordt niet beschreven in de brontekst.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *De claim gaat over internet.nl testcriteria voor DKIM DNS-beschikbaarheid. De bron is de DMARC RFC.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *DKIM wordt niet behandeld in RFC 7208.*
</details>

### `inet-mail-0016` — SKILL.md:154 *(§ 3. DMARC (Domain-based Message Authentication, Reporting and Conformance))*

> Het DMARC-implementatiepad start met `p=none` om rapportages te verzamelen, daarna `p=quarantine` en uiteindelijk `p=reject`.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** DMARC / implementatiepad

- **PARTIALLY_SUPPORTED** (medium) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  > To enable Domain Owners to receive DMARC feedback without impacting existing mail processing, discovered policies of "p=none" SHOULD NOT modify existing mail disposition processing.
  - *De bron ondersteunt impliciet een implementatiepad waarbij `p=none` wordt gebruikt voor monitoring zonder impact op mailaflevering. De specifieke fasering (none → quarantine → reject) als aanbevolen pad wordt niet expliciet als stappenplan beschreven in de bron; de bron beschrijft de `pct`-tag voor geleidelijke uitrol maar noemt niet letterlijk dit drietrapspad.*
<details><summary>1x NOT_FOUND + 2x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Het DMARC-implementatiepad wordt niet beschreven in de brontekst.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *RFC 6376 gaat over DKIM, niet over DMARC. DMARC-beleid (p=none, p=quarantine, p=reject) wordt niet behandeld in deze bron.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *DMARC wordt niet behandeld in RFC 7208.*
</details>

### `inet-mail-0018` — SKILL.md:204 *(§ 4. STARTTLS)*

> Internet.nl test of MX-servers STARTTLS ondersteunen.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** STARTTLS / internet.nl testcriteria

- **PARTIALLY_SUPPORTED** (medium) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  > STARTTLS and DANE : secure mail server connection?
  - *De brontekst bevestigt dat STARTTLS getest wordt, maar geeft geen detail dat dit specifiek MX-servers betreft of wat exact getest wordt.*
<details><summary>3x OUT_OF_SCOPE (klap uit)</summary>

- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *De bron is RFC 7489 (DMARC). STARTTLS en internet.nl testcriteria worden niet behandeld in deze bron.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *RFC 6376 gaat over DKIM-signatures, niet over internet.nl testcriteria voor STARTTLS.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron is RFC 7208 over SPF. STARTTLS en internet.nl testcriteria komen niet voor in deze bron.*
</details>

### `inet-mail-0036` — reference.md:141 *(§ Waarom roteren?)*

> DKIM key rotation wordt aanbevolen elke 6-12 maanden en vereist een nieuwe selector bij elke rotatie.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** DKIM / key rotation

- **PARTIALLY_SUPPORTED** (medium) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  > Signers are ill-advised to reuse selectors for new keys. A better strategy is to assign new keys to new selectors.
  - *De bron ondersteunt het gebruik van nieuwe selectors bij sleutelrotatie, maar noemt geen aanbevolen interval van 6-12 maanden. Dat specifieke tijdsframe is niet terug te vinden in RFC 6376.*
<details><summary>1x NOT_FOUND + 2x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *DKIM key rotation wordt niet beschreven in de brontekst.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 gaat over DMARC, niet over DKIM key rotation intervallen of selectorgebruik.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron gaat over SPF. DKIM key rotation wordt niet behandeld.*
</details>

### `inet-mail-0037` — reference.md:153 *(§ Rotatieprocedure)*

> Bij DKIM key rotation moet na het publiceren van het nieuwe DNS-record worden gewacht tot de DNS is gepropageerd (controleer TTL) voordat de OpenDKIM-configuratie wordt bijgewerkt.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** DKIM / rotatieprocedure

- **PARTIALLY_SUPPORTED** (medium) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  > when rotating to a new key pair, signing should immediately commence with the new private key, and the old public key should be retained for a reasonable validation interval before being removed from the key server.
  - *De bron ondersteunt het concept van wachten met verwijderen van het oude record (retaining for a reasonable validation interval), maar noemt niets specifieks over DNS-propagatie of TTL-controle voorafgaand aan het bijwerken van OpenDKIM-configuratie.*
<details><summary>1x NOT_FOUND + 2x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *DKIM rotatieprocedure wordt niet beschreven in de brontekst.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 gaat over DMARC, niet over DKIM key rotation procedures of DNS propagatie.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron gaat over SPF. DKIM rotatieprocedures en OpenDKIM worden niet behandeld.*
</details>

### `inet-mail-0038` — reference.md:163 *(§ Rotatieprocedure)*

> Bij DKIM key rotation dient 1-2 weken gewacht te worden na activatie van de nieuwe sleutel voordat het oude DNS-record verwijderd wordt.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** DKIM / rotatieprocedure

- **PARTIALLY_SUPPORTED** (medium) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  > the old public key should be retained for a reasonable validation interval before being removed from the key server.
  - *De bron ondersteunt het wachten met verwijderen van het oude record, maar noemt geen specifiek interval van 1-2 weken.*
<details><summary>1x NOT_FOUND + 2x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *DKIM rotatieprocedure wordt niet beschreven in de brontekst.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 gaat over DMARC, niet over wachttijden bij DKIM key rotation.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron gaat over SPF. DKIM key rotation en wachttijden voor DNS-record verwijdering worden niet behandeld.*
</details>

### `inet-mail-0039` — reference.md:170 *(§ Aggregaat rapporten (rua))*

> DMARC-aggregaatrapporten worden dagelijks verstuurd als XML (vaak gzipped) en bevatten statistieken over alle e-mail verstuurd namens het domein.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DMARC / rapportage

- **PARTIALLY_SUPPORTED** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  > Visibility comes in the form of daily (or more frequent) Mail Receiver-originated feedback reports that contain aggregate data on message streams relevant to the Domain Owner. [...] The aggregate data MUST be an XML file that SHOULD be subjected to GZIP compression.
  - *De bron bevestigt dagelijkse verzending, XML-formaat en gzip-compressie. De claim dat rapporten 'statistieken over alle e-mail verstuurd namens het domein' bevatten wordt gedeeltelijk bevestigd: de bron spreekt van 'aggregate data on message streams relevant to the Domain Owner', inclusief berichten die DMARC passeren én falen, maar de formulering 'alle e-mail verstuurd namens het domein' is iets ruimer dan wat de bron stelt.*
<details><summary>1x NOT_FOUND + 2x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *DMARC aggregaatrapporten worden niet beschreven in de brontekst.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron beschrijft DKIM signatures. DMARC-aggregaatrapporten vallen buiten de scope van RFC 6376.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron gaat over SPF. DMARC-rapportage wordt niet behandeld.*
</details>

## UNGROUNDED — geen bron ondersteunt de claim (10)

### `inet-mail-0012` — SKILL.md:108 *(§ 2. DKIM (DomainKeys Identified Mail))*

> 2048-bit RSA is de huidige operationele aanbeveling voor DKIM-sleutels (o.a. NIST, M3AAWG), niet een eis uit RFC 6376.

**Type:** factual_assertion  ·  **Modaliteit:** SHOULD  ·  **Scope:** DKIM / sleutellengte

- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *RFC 6376 noemt alleen de 1024-bit minimumeis. Er wordt geen 2048-bit aanbeveling gedaan, en NIST of M3AAWG worden niet vermeld in deze bron.*

### `inet-mail-0022` — SKILL.md:226 *(§ 5. DANE (DNS-based Authentication of Named Entities))*

> DANE vereist dat DNSSEC actief is op het domein.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** DANE / vereisten

<details><summary>1x NOT_FOUND + 3x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *De eis dat DANE DNSSEC vereist wordt niet beschreven in de brontekst.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *De bron is RFC 7489 (DMARC). DANE en DNSSEC-vereisten worden slechts zijdelings aangehaald in security considerations (sectie 12.3), maar niet als vereiste voor DANE zelf.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *RFC 6376 gaat over DKIM-signatures, niet over DANE/DNSSEC-vereisten.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron is RFC 7208 over SPF. DANE en DNSSEC-vereisten zijn buiten scope.*
</details>

### `inet-mail-0026` — SKILL.md:243 *(§ 5. DANE (DNS-based Authentication of Named Entities))*

> DANE Certificate Usage `3` staat voor DANE-EE (End Entity) en is aanbevolen voor mail.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** DANE / TLSA-parameters

<details><summary>1x NOT_FOUND + 3x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *DANE Certificate Usage types worden niet beschreven in de brontekst.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *De bron is RFC 7489 (DMARC). DANE Certificate Usage parameters worden niet behandeld.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *RFC 6376 gaat over DKIM-signatures, niet over DANE Certificate Usage parameters in TLSA-records.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron is RFC 7208 over SPF. DANE Certificate Usage parameters zijn buiten scope.*
</details>

### `inet-mail-0031` — reference.md:17 *(§ STARTTLS inschakelen)*

> In Postfix dient `smtpd_tls_protocols` SSL v2, SSL v3, TLS 1.0 en TLS 1.1 uit te sluiten voor inkomende verbindingen.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** STARTTLS / Postfix-configuratie

<details><summary>1x NOT_FOUND + 3x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Postfix-configuratiedetails worden niet beschreven in de brontekst.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *De bron is RFC 7489 (DMARC). Postfix-configuratie voor STARTTLS wordt niet behandeld.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron (RFC 6376) beschrijft DKIM signatures. Postfix-configuratie voor STARTTLS/TLS-protocollen valt buiten de scope van deze RFC.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron is RFC 7208 over SPF. Postfix-configuratie voor STARTTLS is buiten scope.*
</details>

### `inet-mail-0032` — reference.md:23 *(§ STARTTLS inschakelen)*

> In Postfix dient `smtp_tls_security_level = dane` ingesteld te worden voor uitgaande DANE-ondersteuning.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** DANE / Postfix-configuratie

<details><summary>1x NOT_FOUND + 3x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Postfix-configuratiedetails worden niet beschreven in de brontekst.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *De bron is RFC 7489 (DMARC). Postfix-configuratie voor DANE wordt niet behandeld.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron beschrijft DKIM signatures. Postfix DANE-configuratie valt buiten de scope van RFC 6376.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron is RFC 7208 over SPF. Postfix-configuratie voor DANE is buiten scope.*
</details>

### `inet-mail-0033` — reference.md:27 *(§ STARTTLS inschakelen)*

> In Postfix dient `smtp_dns_support_level = dnssec` ingesteld te worden voor DANE-ondersteuning.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** DANE / Postfix-configuratie

<details><summary>1x NOT_FOUND + 3x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Postfix-configuratiedetails worden niet beschreven in de brontekst.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 gaat over DMARC, niet over DANE of Postfix-configuratie.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron beschrijft DKIM signatures. Postfix DNSSEC-configuratie voor DANE valt buiten de scope van RFC 6376.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron is RFC 7208 over SPF. DANE en Postfix-configuratie worden niet behandeld.*
</details>

### `inet-mail-0034` — reference.md:95 *(§ SPF voor Microsoft 365)*

> Voor Microsoft 365 wordt het SPF-record `v=spf1 include:spf.protection.outlook.com -all` aanbevolen.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** SPF / Microsoft 365

<details><summary>2x NOT_FOUND + 2x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Microsoft 365 SPF-aanbevelingen worden niet beschreven in de brontekst.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 gaat over DMARC, niet over SPF-records voor Microsoft 365.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron beschrijft DKIM signatures. SPF-records voor Microsoft 365 vallen buiten de scope van RFC 6376.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron behandelt SPF in het algemeen maar noemt geen specifieke records voor Microsoft 365 of spf.protection.outlook.com.*
</details>

### `inet-mail-0035` — reference.md:122 *(§ SPF voor Google Workspace)*

> Voor Google Workspace wordt het SPF-record `v=spf1 include:_spf.google.com -all` aanbevolen.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** SPF / Google Workspace

<details><summary>2x NOT_FOUND + 2x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Google Workspace SPF-aanbevelingen worden niet beschreven in de brontekst.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 gaat over DMARC, niet over SPF-records voor Google Workspace.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron beschrijft DKIM signatures. SPF-records voor Google Workspace vallen buiten de scope van RFC 6376.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron behandelt SPF in het algemeen maar noemt geen specifieke records voor Google Workspace of _spf.google.com.*
</details>

### `inet-mail-0042` — reference.md:240 *(§ TLSA bijwerken bij certificaatvernieuwing)*

> Bij certificaatvernieuwing met DANE dient de pre-publish methode gebruikt te worden: publiceer het TLSA-record van het nieuwe certificaat voordat het actief wordt.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** DANE / TLSA-beheer bij certificaatvernieuwing

<details><summary>1x NOT_FOUND + 3x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *De pre-publish methode voor DANE bij certificaatvernieuwing wordt niet beschreven in de brontekst.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 gaat over DMARC, niet over DANE pre-publish methodes bij certificaatvernieuwing.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron beschrijft DKIM signatures. DANE pre-publish methode bij certificaatvernieuwing valt buiten de scope van RFC 6376.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron gaat over SPF. DANE pre-publish methode voor certificaatvernieuwing wordt niet behandeld.*
</details>

### `inet-mail-0044` — reference.md:267 *(§ Vereisten)*

> MTA-STS vereist een DNS TXT-record op `_mta-sts.example.nl`, een HTTPS-website op `mta-sts.example.nl` met geldig certificaat, en een beleidsbestand op `https://mta-sts.example.nl/.well-known/mta-sts.txt`.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** MTA-STS / vereisten

<details><summary>1x NOT_FOUND + 3x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *MTA-STS vereisten worden niet beschreven in de brontekst.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *RFC 7489 gaat over DMARC, niet over MTA-STS vereisten.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron beschrijft DKIM signatures. MTA-STS vereisten vallen buiten de scope van RFC 6376.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *De bron gaat over SPF. MTA-STS vereisten worden niet behandeld.*
</details>

## GROUNDED — minstens één bron ondersteunt de claim (8)

<details>
<summary>Klap uit voor alle GROUNDED claims</summary>

### `inet-mail-0002` — SKILL.md:54 *(§ 1. SPF (Sender Policy Framework))*

> Internet.nl test of een SPF-record aanwezig is als DNS TXT-record.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** SPF / internet.nl testcriteria

- **SUPPORTED** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  > SPF records MUST be published as a DNS TXT (type 16) Resource Record (RR) [RFC1035] only.
  - *De bron bevestigt dat SPF-records als DNS TXT-record gepubliceerd moeten worden. Internet.nl-specifieke testcriteria staan niet in de bron, maar de technische basis voor de claim wordt volledig ondersteund.*
<details><summary>2x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *De brontekst vermeldt SPF als onderdeel van de test maar geeft geen detail over DNS TXT-record controle.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *De claim gaat over internet.nl testcriteria voor SPF. De bron is de DMARC RFC, niet een SPF-specificatie of internet.nl documentatie.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron gaat over DKIM, niet over SPF of internet.nl testcriteria.*
</details>

### `inet-mail-0003` — SKILL.md:55 *(§ 1. SPF (Sender Policy Framework))*

> Internet.nl test of het SPF-record een correcte syntax heeft.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** SPF / internet.nl testcriteria

- **SUPPORTED** (medium) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  > The check_host() function parses and interprets the SPF record to find a result for the current test. The syntax of the record is validated first, and if there are any syntax errors anywhere in the record, check_host() returns immediately with the result "permerror"
  - *De bron bevestigt dat syntaxvalidatie onderdeel is van SPF-verwerking. De specifieke internetl.nl-testlogica staat niet in de bron, maar de technische grondslag voor syntaxcontrole is aanwezig.*
<details><summary>2x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *Syntaxcontrole van SPF-records wordt niet beschreven in de brontekst.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *De claim gaat over internet.nl testcriteria voor SPF-syntaxvalidatie. De bron is de DMARC RFC.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron gaat over DKIM, niet over SPF of internet.nl testcriteria.*
</details>

### `inet-mail-0004` — SKILL.md:56 *(§ 1. SPF (Sender Policy Framework))*

> Internet.nl test of het SPF-record maximaal 10 DNS-lookups bevat (include, a, mx, redirect).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** SPF / internet.nl testcriteria

- **SUPPORTED** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  > SPF implementations MUST limit the total number of those terms to 10 during SPF evaluation, to avoid unreasonable load on the DNS. If this limit is exceeded, the implementation MUST return "permerror". The following terms cause DNS queries: the "include", "a", "mx", "ptr", and "exists" mechanisms, and the "redirect" modifier.
  - *De bron bevestigt de limiet van 10 DNS-lookups en noemt include, a, mx en redirect expliciet als lookup-veroorzakers. De claim vermeldt niet 'ptr' en 'exists', maar dat is geen tegenspraak.*
<details><summary>2x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *De brontekst bevat geen informatie over het testen van DNS-lookup limieten in SPF.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *De claim gaat over internet.nl testcriteria voor SPF DNS-lookups. De bron is de DMARC RFC.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron gaat over DKIM, niet over SPF of internet.nl testcriteria.*
</details>

### `inet-mail-0007` — SKILL.md:75 *(§ 1. SPF (Sender Policy Framework))*

> Het SPF-mechanisme `redirect=domein` gebruikt het SPF-record van een ander domein.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** SPF mechanismen

- **SUPPORTED** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  > The "redirect" modifier is intended for consolidating both authorizations and policy into a common set to be shared within a single ADMD... If all mechanisms fail to match, and a "redirect" modifier is present, then processing proceeds as follows: The <domain-spec> portion of the redirect section is expanded... Then check_host() is evaluated with the resulting string as the <domain>.
  - *De bron bevestigt dat redirect het SPF-record van een ander domein gebruikt voor verdere evaluatie.*
<details><summary>2x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *SPF redirect-mechanisme wordt niet beschreven in de brontekst.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *De claim gaat over het SPF `redirect=`-mechanisme. De bron is de DMARC RFC, niet de SPF-specificatie.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron gaat over DKIM, niet over SPF-mechanismen.*
</details>

### `inet-mail-0011` — SKILL.md:108 *(§ 2. DKIM (DomainKeys Identified Mail))*

> RFC 6376 vereist minimaal 1024-bit RSA voor langlevende DKIM-sleutels.

**Type:** reference_claim  ·  **Modaliteit:** MUST  ·  **Scope:** DKIM / RFC 6376

- **SUPPORTED** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  > Signers MUST use RSA keys of at least 1024 bits for long-lived keys. Verifiers MUST be able to validate signatures with keys ranging from 512 bits to 2048 bits, and they MAY be able to validate signatures with larger keys.

### `inet-mail-0013` — SKILL.md:150 *(§ 3. DMARC (Domain-based Message Authentication, Reporting and Conformance))*

> Internet.nl test of een DMARC-record aanwezig is op `_dmarc.example.nl`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DMARC / internet.nl testcriteria

- **SUPPORTED** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  > Domain Owner DMARC preferences are stored as DNS TXT records in subdomains named "_dmarc". For example, the Domain Owner of "example.com" would post DMARC preferences in a TXT record at "_dmarc.example.com".
  - *De bron bevestigt dat DMARC-records worden gepubliceerd als DNS TXT-records op `_dmarc.<domein>`. De claim verwijst naar `_dmarc.example.nl` in plaats van `_dmarc.example.com`, maar dit is slechts een ander TLD-voorbeeld; het principe is identiek.*
<details><summary>2x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *De specifieke DMARC-testcriteria, inclusief het `_dmarc`-subdomein, worden niet beschreven in de brontekst.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *De bron gaat over DKIM, niet over DMARC of internet.nl testcriteria.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *DMARC wordt niet behandeld in RFC 7208.*
</details>

### `inet-mail-0017` — SKILL.md:174 *(§ 3. DMARC (Domain-based Message Authentication, Reporting and Conformance))*

> De DMARC-tag `pct` geeft het percentage berichten aan waarop het beleid wordt toegepast (0-100).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DMARC / DNS-record parameters

- **SUPPORTED** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  > pct: (plain-text integer between 0 and 100, inclusive; OPTIONAL; default is 100). Percentage of messages from the Domain Owner's mail stream to which the DMARC policy is to be applied.
<details><summary>1x NOT_FOUND + 2x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *DMARC-tags zoals `pct` worden niet beschreven in de brontekst.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *RFC 6376 gaat over DKIM, niet over DMARC. De DMARC-tag `pct` wordt niet behandeld in deze bron.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  - *DMARC wordt niet behandeld in RFC 7208.*
</details>

### `inet-mail-0029` — SKILL.md:278 *(§ Veelvoorkomende problemen)*

> Een SPF `permerror` wordt veroorzaakt door meer dan 10 DNS-lookups; oplossing is het verminderen van `include`-verwijzingen of direct gebruik van `ip4`/`ip6`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** SPF / veelvoorkomende problemen

- **SUPPORTED** (high) — [https://www.rfc-editor.org/rfc/rfc7208.txt](https://www.rfc-editor.org/rfc/rfc7208.txt)
  > SPF implementations MUST limit the total number of those terms to 10 during SPF evaluation, to avoid unreasonable load on the DNS. If this limit is exceeded, the implementation MUST return "permerror".
  - *De bron bevestigt dat meer dan 10 DNS-lookups leidt tot permerror. De oplossingsrichting (minder include of ip4/ip6 gebruiken) wordt indirect ondersteund door Section 10.1.1 die ip4/ip6 als 'Best record' aanbeveelt boven mx of include.*
<details><summary>1x NOT_FOUND + 2x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-mail/](https://internet.nl/test-mail/)
  - *SPF permerror en oplossingen worden niet beschreven in de brontekst.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7489.txt](https://www.rfc-editor.org/rfc/rfc7489.txt)
  - *De bron is RFC 7489 (DMARC). SPF DNS-lookup limieten en permerror worden niet behandeld in deze bron.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6376.txt](https://www.rfc-editor.org/rfc/rfc6376.txt)
  - *RFC 6376 gaat over DKIM-signatures, niet over SPF permerror of DNS-lookup limieten.*
</details>

</details>
