<!-- markdownlint-disable MD052 MD034 MD013 -->
# Audit inet-toolbox — 2026-05-17

> Automatisch gegenereerd door audit-tooling. Niet handmatig bewerken; wijzig SKILL.md / reference.md en regenereer.

## Samenvatting

| Status | Aantal | % |
|--------|--------|---|
| UNSUPPORTED_ASSERTION | 12 | 31% |
| CONTRADICTED | 0 | 0% |
| PARTIALLY_GROUNDED | 1 | 3% |
| UNGROUNDED | 25 | 64% |
| NO_SOURCE | 0 | 0% |
| UNVERIFIABLE | 0 | 0% |
| KNOWN_DISCREPANCY | 0 | 0% |
| GROUNDED | 1 | 3% |

*Geverifieerd met sonnet, 2 calls, $0.2221.*

## UNSUPPORTED_ASSERTION — stellige bewering zonder enige bronsteun (mogelijke hallucinatie) (12)

### `inet-toolbox-0002` — SKILL.md:46 *(§ 1. DNSSEC instellen)*

> DNSSEC beveiligt DNS-antwoorden met cryptografische handtekeningen.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DNSSEC

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *De bron bevat geen technische uitleg over DNSSEC of cryptografische handtekeningen.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *De brontekst (alleen de README/landingspagina van de repo) bevat geen inhoudelijke uitleg over DNSSEC of cryptografische handtekeningen.*

### `inet-toolbox-0003` — SKILL.md:64 *(§ 1. DNSSEC instellen)*

> Voor BIND 9 DNSSEC worden twee sleutels gegenereerd: een KSK (Key Signing Key) en een ZSK (Zone Signing Key) met algoritme ECDSAP256SHA256.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DNSSEC / BIND 9

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Geen informatie over BIND 9, KSK, ZSK of ECDSAP256SHA256 in de brontekst.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen inhoud over BIND 9, KSK, ZSK of ECDSAP256SHA256 in de aangeleverde brontekst.*

### `inet-toolbox-0005` — SKILL.md:82 *(§ 1. DNSSEC instellen)*

> NSD gebruikt externe tools voor DNSSEC, zoals ldns of OpenDNSSEC.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DNSSEC / NSD

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Geen informatie over NSD, ldns of OpenDNSSEC in de brontekst.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen inhoud over NSD, ldns of OpenDNSSEC in de aangeleverde brontekst.*

### `inet-toolbox-0007` — SKILL.md:158 *(§ 2. HTTPS/TLS configureren)*

> De Nginx TLS-configuratie bevat `ssl_prefer_server_ciphers off`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** HTTPS/TLS / Nginx

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Geen informatie over ssl_prefer_server_ciphers in de brontekst.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen inhoud over ssl_prefer_server_ciphers in de aangeleverde brontekst.*

### `inet-toolbox-0014` — SKILL.md:265 *(§ 4. DKIM instellen)*

> Postfix wordt aan OpenDKIM gekoppeld via een milter op `inet:localhost:8891`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DKIM / Postfix / OpenDKIM

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Geen informatie over Postfix, OpenDKIM of milter-configuratie in de brontekst.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen inhoud over Postfix/OpenDKIM milter-configuratie in de aangeleverde brontekst.*

### `inet-toolbox-0019` — SKILL.md:328 *(§ 6. DANE instellen)*

> DANE TLSA-record voor SMTP heeft het formaat `_25._tcp.mx.example.nl. IN TLSA 3 1 1 <hash>`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DANE

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Geen informatie over DANE TLSA-records of SMTP-formaten in de brontekst.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen inhoud over TLSA-recordformaat in de aangeleverde brontekst.*

### `inet-toolbox-0022` — SKILL.md:395 *(§ Veelvoorkomende problemen)*

> SPF permerror wordt veroorzaakt door meer dan 10 DNS-lookups in het SPF-record.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** SPF

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Geen informatie over SPF permerror of DNS-lookup limieten in de brontekst.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen inhoud over SPF permerror in de aangeleverde brontekst.*

### `inet-toolbox-0023` — SKILL.md:396 *(§ Veelvoorkomende problemen)*

> DANE TLSA mismatch na certificaatvernieuwing wordt veroorzaakt door een niet-bijgewerkt TLSA-record; oplossing is SPKI (selector=1) met hergebruik privésleutel of vooraf TLSA updaten.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DANE

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Geen informatie over DANE TLSA mismatch of SPKI in de brontekst.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen inhoud over DANE TLSA mismatch of SPKI in de aangeleverde brontekst.*

### `inet-toolbox-0028` — reference.md:54 *(§ DNSSEC - geavanceerde configuratie)*

> ECDSAP256SHA256 heeft algoritme-code 13 in DNSSEC.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DNSSEC / algoritme-keuze

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Geen informatie over DNSSEC algoritme-codes in de brontekst.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen inhoud over DNSSEC algoritme-codes in de aangeleverde brontekst.*

### `inet-toolbox-0029` — reference.md:56 *(§ DNSSEC - geavanceerde configuratie)*

> ED25519 heeft algoritme-code 15 in DNSSEC.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DNSSEC / algoritme-keuze

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Geen informatie over ED25519 of algoritme-code 15 in de brontekst.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen inhoud over ED25519 algoritme-code in de aangeleverde brontekst.*

### `inet-toolbox-0030` — reference.md:153 *(§ E-mailbeveiliging - geavanceerde configuratie)*

> Postfix `smtp_tls_security_level = dane` configureert uitgaand SMTP voor DANE-verificatie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DANE / Postfix TLS

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Geen informatie over Postfix smtp_tls_security_level in de brontekst.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen inhoud over Postfix smtp_tls_security_level in de aangeleverde brontekst.*

### `inet-toolbox-0039` — SKILL.md:386 *(§ Repositories)*

> Internet.nl testsuite is gepubliceerd onder Apache-2.0 (code) en CC-BY-4.0 (vertalingen).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl / licentie

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *De bron vermeldt alleen versienummer v1.11.0 van internet.nl, maar geen licentie-informatie. De Hall of Fame pagina bevat geen verwijzing naar Apache-2.0 of CC-BY-4.0.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *De brontekst gaat over de toolbox-wiki repository, niet over de Internet.nl testsuite zelf. Geen informatie over Apache-2.0 of licenties van Internet.nl code/vertalingen.*

## PARTIALLY_GROUNDED — bron ondersteunt deel van de claim (1)

### `inet-toolbox-0001` — SKILL.md:26 *(§ Overzicht)*

> De toolbox-wiki bevat implementatiegidsen voor alle standaarden die internet.nl test.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** inet-toolbox skill / toolbox-wiki

- **PARTIALLY_SUPPORTED** (medium) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  > Quick access: DANE how-to, DKIM how-to, SPF how-to, DMARC how-to, Parked domain how-to
  - *De bron toont how-to's voor DANE, DKIM, SPF, DMARC en parked domains. Internet.nl test ook DNSSEC, IPv6, HTTPS/TLS en andere standaarden waarvoor geen how-to's zichtbaar zijn in deze README. De claim 'alle standaarden' is dus te sterk.*
- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *De brontekst is de Hall of Fame pagina van internet.nl met een lijst van domeinen die 100% scoren. Er is geen informatie over een toolbox-wiki of implementatiegidsen.*

## UNGROUNDED — geen bron ondersteunt de claim (25)

### `inet-toolbox-0004` — SKILL.md:73 *(§ 1. DNSSEC instellen)*

> Na het genereren van DNSSEC-sleutels in BIND 9 moet het DS-record gepubliceerd worden bij de domeinregistrar.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** DNSSEC / BIND 9

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Geen informatie over DS-records of domeinregistrars in de brontekst.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen inhoud over DS-records of domeinregistrars in de aangeleverde brontekst.*

### `inet-toolbox-0006` — SKILL.md:155 *(§ 2. HTTPS/TLS configureren)*

> De Nginx TLS-configuratie dient `ssl_protocols TLSv1.2 TLSv1.3` te gebruiken (NCSC-conform).

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** HTTPS/TLS / Nginx

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Geen Nginx TLS-configuratie informatie in de brontekst.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen inhoud over Nginx TLS-configuratie in de aangeleverde brontekst.*

### `inet-toolbox-0008` — SKILL.md:166 *(§ 2. HTTPS/TLS configureren)*

> Nginx HSTS-header moet `max-age=31536000; includeSubDomains` bevatten.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** HTTPS/TLS / Nginx / HSTS

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Geen informatie over HSTS-headers of max-age in de brontekst.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen inhoud over Nginx HSTS-configuratie in de aangeleverde brontekst.*

### `inet-toolbox-0009` — SKILL.md:197 *(§ 2. HTTPS/TLS configureren)*

> Apache TLS-configuratie sluit SSLv3, TLSv1 en TLSv1.1 uit via `SSLProtocol all -SSLv3 -TLSv1 -TLSv1.1`.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** HTTPS/TLS / Apache

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Geen informatie over Apache TLS-configuratie in de brontekst.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen inhoud over Apache TLS-configuratie in de aangeleverde brontekst.*

### `inet-toolbox-0010` — SKILL.md:203 *(§ 2. HTTPS/TLS configureren)*

> Apache HSTS-header moet `max-age=31536000; includeSubDomains` bevatten.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** HTTPS/TLS / Apache / HSTS

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Geen informatie over Apache HSTS-headers in de brontekst.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen inhoud over Apache HSTS-configuratie in de aangeleverde brontekst.*

### `inet-toolbox-0011` — SKILL.md:218 *(§ 3. DMARC gefaseerd uitrollen)*

> DMARC wordt gefaseerd uitgerold: eerst p=none (monitor), dan p=quarantine met oplopende pct, dan p=reject.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** DMARC

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Geen informatie over DMARC-uitrol of policies in de brontekst.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen inhoud over DMARC-uitrolstrategie in de aangeleverde brontekst. Er is alleen een verwijzing naar DMARC-how-to.md, maar de inhoud daarvan is niet aangeleverd.*

### `inet-toolbox-0012` — SKILL.md:222 *(§ 3. DMARC gefaseerd uitrollen)*

> In de monitor-fase van DMARC-uitrol wordt 2 tot 4 weken gewacht om rapporten te analyseren voordat de policy wordt aangescherpt.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** DMARC

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Geen informatie over DMARC monitor-fase of wachttijden in de brontekst.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen inhoud over DMARC monitor-fase of wachttijden in de aangeleverde brontekst.*

### `inet-toolbox-0013` — SKILL.md:245 *(§ 4. DKIM instellen)*

> Een DKIM RSA-sleutelpaar heeft minimaal 2048 bits.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** DKIM

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Geen informatie over DKIM RSA-sleutellengte in de brontekst.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen inhoud over DKIM sleutellengte in de aangeleverde brontekst.*

### `inet-toolbox-0015` — SKILL.md:298 *(§ 5. SPF-record samenstellen)*

> SPF mag maximaal 10 DNS-lookups bevatten; elke `include`, `a`, `mx` en `redirect` telt als 1 lookup.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** SPF

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Geen informatie over SPF DNS-lookup limieten in de brontekst.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen inhoud over SPF DNS-lookup limiet in de aangeleverde brontekst.*

### `inet-toolbox-0016` — SKILL.md:300 *(§ 5. SPF-record samenstellen)*

> SPF-records moeten eindigen met `-all` (fail) of `~all` (softfail).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** SPF

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Geen informatie over SPF -all of ~all in de brontekst.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen inhoud over SPF -all of ~all in de aangeleverde brontekst.*

### `inet-toolbox-0017` — SKILL.md:299 *(§ 5. SPF-record samenstellen)*

> Gebruik `ip4`/`ip6` in SPF om DNS-lookups te besparen.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** SPF

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Geen informatie over SPF ip4/ip6 mechanismen in de brontekst.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen inhoud over ip4/ip6 mechanismen in SPF in de aangeleverde brontekst.*

### `inet-toolbox-0018` — SKILL.md:315 *(§ 6. DANE instellen)*

> DANE vereist dat DNSSEC actief is op het MX-domein.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** DANE

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Geen informatie over DANE of DNSSEC-vereisten in de brontekst.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen inhoud over DANE-vereisten of DNSSEC-afhankelijkheid in de aangeleverde brontekst.*

### `inet-toolbox-0020` — SKILL.md:335 *(§ 6. DANE instellen)*

> Bij DANE met hergebruik van dezelfde privésleutel hoeft het TLSA-record niet te veranderen bij certificaatvernieuwing.

**Type:** normative_requirement  ·  **Modaliteit:** MAY  ·  **Scope:** DANE

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Geen informatie over DANE certificaatvernieuwing of privésleutelhergebruik in de brontekst.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen inhoud over DANE privésleutel hergebruik in de aangeleverde brontekst.*

### `inet-toolbox-0021` — SKILL.md:336 *(§ 6. DANE instellen)*

> Bij DANE met een nieuwe sleutel moet het TLSA-record worden bijgewerkt VOOR de certificaatvernieuwing.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** DANE

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Geen informatie over DANE TLSA-record updates bij sleutelwisseling in de brontekst.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen inhoud over TLSA-update timing bij certificaatvernieuwing in de aangeleverde brontekst.*

### `inet-toolbox-0024` — reference.md:30 *(§ DNSSEC - geavanceerde configuratie)*

> ZSK rollover wordt aanbevolen elke 3 maanden.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** DNSSEC / key rollover

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Geen informatie over ZSK rollover-intervallen in de brontekst.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen inhoud over ZSK rollover-interval in de aangeleverde brontekst.*

### `inet-toolbox-0025` — reference.md:39 *(§ DNSSEC - geavanceerde configuratie)*

> KSK rollover wordt aanbevolen jaarlijks.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** DNSSEC / key rollover

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Geen informatie over KSK rollover-intervallen in de brontekst.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen inhoud over KSK rollover-interval in de aangeleverde brontekst.*

### `inet-toolbox-0026` — reference.md:44 *(§ DNSSEC - geavanceerde configuratie)*

> Bij KSK rollover moet het nieuwe DS-record bij de registrar gepubliceerd worden (naast het oude) voordat de DNSKEY RRset met de nieuwe KSK wordt ondertekend.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** DNSSEC / KSK rollover

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Geen informatie over KSK rollover-procedure of DS-records in de brontekst.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen inhoud over KSK rollover-procedure in de aangeleverde brontekst.*

### `inet-toolbox-0027` — reference.md:59 *(§ DNSSEC - geavanceerde configuratie)*

> ECDSAP256SHA256 (algoritme 13) is het aanbevolen algoritme voor nieuwe DNSSEC-zones vanwege compacte handtekeningen, brede ondersteuning en goede prestaties.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** DNSSEC / algoritme-keuze

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Geen informatie over ECDSAP256SHA256 of aanbevolen DNSSEC-algoritmen in de brontekst.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen inhoud over ECDSAP256SHA256 als aanbevolen algoritme in de aangeleverde brontekst.*

### `inet-toolbox-0031` — reference.md:160 *(§ E-mailbeveiliging - geavanceerde configuratie)*

> Postfix `smtp_dns_support_level = dnssec` is vereist voor DANE-ondersteuning bij uitgaand SMTP.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** DANE / Postfix TLS

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Geen informatie over Postfix smtp_dns_support_level in de brontekst.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen inhoud over Postfix smtp_dns_support_level in de aangeleverde brontekst.*

### `inet-toolbox-0032` — reference.md:142 *(§ E-mailbeveiliging - geavanceerde configuratie)*

> Postfix TLS sluit SSLv2, SSLv3, TLSv1 en TLSv1.1 uit via `smtpd_tls_protocols = !SSLv2, !SSLv3, !TLSv1, !TLSv1.1`.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** HTTPS/TLS / Postfix

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Geen informatie over Postfix TLS-protocollen of smtpd_tls_protocols in de brontekst.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen inhoud over Postfix smtpd_tls_protocols in de aangeleverde brontekst.*

### `inet-toolbox-0033` — reference.md:191 *(§ E-mailbeveiliging - geavanceerde configuratie)*

> SPF-flattening is een oplossing wanneer je tegen de 10 DNS-lookup limiet aanloopt: vervang `include` door directe ip4:/ip6: regels.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** SPF

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Geen informatie over SPF-flattening in de brontekst.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen inhoud over SPF-flattening in de aangeleverde brontekst.*

### `inet-toolbox-0034` — reference.md:239 *(§ DANE - geavanceerde configuratie)*

> Bij DANE voor meerdere MX-servers moet elke MX een eigen TLSA-record hebben onder `_25._tcp.<mx-hostname>`.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** DANE / meerdere MX-servers

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Geen informatie over DANE met meerdere MX-servers in de brontekst.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen inhoud over DANE voor meerdere MX-servers in de aangeleverde brontekst.*

### `inet-toolbox-0035` — reference.md:230 *(§ DANE - geavanceerde configuratie)*

> Voor DANE-rollover kunnen meerdere TLSA-records tegelijk gepubliceerd worden: het huidige en het toekomstige certificaat naast elkaar.

**Type:** normative_requirement  ·  **Modaliteit:** MAY  ·  **Scope:** DANE / certificaatrollover

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Geen informatie over DANE-rollover of meerdere TLSA-records in de brontekst.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen inhoud over DANE-rollover met meerdere TLSA-records in de aangeleverde brontekst.*

### `inet-toolbox-0036` — reference.md:281 *(§ IPv6 - geavanceerde configuratie)*

> ICMPv6 moet geaccepteerd worden in de firewall (nftables) omdat het nodig is voor IPv6-werking.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** IPv6 / firewall

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Geen informatie over IPv6, ICMPv6 of nftables in de brontekst.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen inhoud over ICMPv6 of nftables in de aangeleverde brontekst.*

### `inet-toolbox-0037` — reference.md:122 *(§ HTTPS/TLS - geavanceerde configuratie)*

> Let's Encrypt wildcard-certificaten vereisen een DNS-challenge (`--preferred-challenges dns`).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** HTTPS/TLS / Let's Encrypt

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Geen informatie over Let's Encrypt wildcard-certificaten of DNS-challenges in de brontekst.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen inhoud over Let's Encrypt wildcard-certificaten of DNS-challenge in de aangeleverde brontekst.*

## GROUNDED — minstens één bron ondersteunt de claim (1)

<details>
<summary>Klap uit voor alle GROUNDED claims</summary>

### `inet-toolbox-0038` — SKILL.md:385 *(§ Repositories)*

> De toolbox-wiki is gepubliceerd onder de CC-BY-4.0 licentie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** toolbox-wiki / licentie

- **SUPPORTED** (medium) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  > LICENSE-CC-BY-4.0.txt
  - *De repository bevat een bestand genaamd LICENSE-CC-BY-4.0.txt, wat sterk impliceert dat de CC-BY-4.0 licentie van toepassing is. De bestandsnaam is geen expliciete verklaring, maar is voldoende directe aanwijzing. Confidence medium omdat de volledige licentietekst niet is weergegeven.*
- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Geen informatie over licenties van de toolbox-wiki in de brontekst.*

</details>
