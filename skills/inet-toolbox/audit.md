<!-- markdownlint-disable MD052 MD034 MD013 -->
# Audit inet-toolbox — 2026-05-17

> Automatisch gegenereerd door audit-tooling. Niet handmatig bewerken; wijzig SKILL.md / reference.md en regenereer.

## Samenvatting

| Status | Aantal | % |
|--------|--------|---|
| UNSUPPORTED_ASSERTION | 11 | 29% |
| CONTRADICTED | 0 | 0% |
| PARTIALLY_GROUNDED | 0 | 0% |
| UNGROUNDED | 26 | 68% |
| NO_SOURCE | 0 | 0% |
| UNVERIFIABLE | 0 | 0% |
| KNOWN_DISCREPANCY | 0 | 0% |
| GROUNDED | 1 | 3% |

*Geverifieerd met sonnet, 2 calls, $0.2159.*

## UNSUPPORTED_ASSERTION — stellige bewering zonder enige bronsteun (mogelijke hallucinatie) (11)

### `inet-toolbox-0001` — SKILL.md:46 *(§ 1. DNSSEC instellen)*

> DNSSEC beveiligt DNS-antwoorden met cryptografische handtekeningen.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DNSSEC

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *De brontekst is uitsluitend een lijst van 3133 domeinen die 100% scoren op de Hall of Fame van internet.nl. Er staat geen technische uitleg over DNSSEC, DANE, SPF, DMARC of andere protocollen.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *De brontekst is de README/landingspagina van de toolbox-wiki GitHub repository. Deze bevat geen technische uitleg over DNSSEC of cryptografische handtekeningen.*

### `inet-toolbox-0008` — SKILL.md:218 *(§ 3. DMARC gefaseerd uitrollen)*

> DMARC fase 1 (monitor) gebruikt `p=none` met een `rua`-adres voor rapportages zonder impact op mailbezorging.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DMARC

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Bron bevat geen technische informatie over DMARC.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen technische DMARC-inhoud over fasen of p=none in de aangeleverde brontekst.*

### `inet-toolbox-0009` — SKILL.md:224 *(§ 3. DMARC gefaseerd uitrollen)*

> DMARC fase 2 gebruikt `p=quarantine` met een `pct`-waarde die geleidelijk verhoogd wordt (10, 25, 50, 100).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DMARC

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Bron bevat geen technische informatie over DMARC.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen technische DMARC-inhoud over p=quarantine of pct-waarden in de aangeleverde brontekst.*

### `inet-toolbox-0010` — SKILL.md:229 *(§ 3. DMARC gefaseerd uitrollen)*

> DMARC fase 3 (streng) gebruikt `p=reject` met `adkim=s` en `aspf=s`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DMARC

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Bron bevat geen technische informatie over DMARC.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen technische DMARC-inhoud over p=reject, adkim=s of aspf=s in de aangeleverde brontekst.*

### `inet-toolbox-0011` — SKILL.md:395 *(§ Veelvoorkomende problemen)*

> SPF permerror treedt op wanneer er meer dan 10 DNS-lookups zijn; oplossing is `include` vervangen door `ip4`/`ip6` waar mogelijk.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** SPF

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Bron bevat geen technische informatie over SPF.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen technische SPF-inhoud over permerror of oplossingen daarvoor in de aangeleverde brontekst.*

### `inet-toolbox-0013` — SKILL.md:361 *(§ 7. IPv6 inschakelen)*

> Nginx luistert op IPv4 én IPv6 wanneer `listen [::]:80` en `listen [::]:443 ssl` worden toegevoegd naast de IPv4 listen-directives.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** IPv6 / Nginx

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Bron bevat geen Nginx-configuratie-informatie.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen technische Nginx/IPv6-inhoud in de aangeleverde brontekst.*

### `inet-toolbox-0021` — SKILL.md:386 *(§ Repositories)*

> Internet.nl code is gepubliceerd onder Apache-2.0; vertalingen onder CC-BY-4.0.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl

- **SOURCE_UNAVAILABLE** (high) — [https://raw.githubusercontent.com/internetstandards/Internet.nl/main/LICENSE](https://raw.githubusercontent.com/internetstandards/Internet.nl/main/LICENSE)
  - *Bron status: unreachable*
- **SOURCE_UNAVAILABLE** (high) — [https://raw.githubusercontent.com/internetstandards/Internet.nl/master/LICENSE](https://raw.githubusercontent.com/internetstandards/Internet.nl/master/LICENSE)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Bron bevat geen licentie-informatie over internet.nl code of vertalingen.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *De brontekst gaat over de toolbox-wiki repository, niet over de Internet.nl codebase zelf. Er is geen vermelding van Apache-2.0 licentie voor Internet.nl code.*

### `inet-toolbox-0027` — reference.md:55 *(§ DNSSEC - geavanceerde configuratie)*

> ECDSAP384SHA384 (algoritme 14) is een goed DNSSEC-algoritme: sterker maar met grotere handtekeningen.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DNSSEC / algoritme-keuze

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Bron bevat geen informatie over DNSSEC algoritme-keuze.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen technische DNSSEC-inhoud over ECDSAP384SHA384 in de aangeleverde brontekst.*

### `inet-toolbox-0028` — reference.md:56 *(§ DNSSEC - geavanceerde configuratie)*

> ED25519 (algoritme 15) is een goed DNSSEC-algoritme: nieuwste en compact.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DNSSEC / algoritme-keuze

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Bron bevat geen informatie over DNSSEC algoritme-keuze.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen technische DNSSEC-inhoud over ED25519 in de aangeleverde brontekst.*

### `inet-toolbox-0029` — reference.md:57 *(§ DNSSEC - geavanceerde configuratie)*

> RSASHA256 (algoritme 8) is voldoende als DNSSEC-algoritme en breed ondersteund.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DNSSEC / algoritme-keuze

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Bron bevat geen informatie over DNSSEC algoritme-keuze.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen technische DNSSEC-inhoud over RSASHA256 in de aangeleverde brontekst.*

### `inet-toolbox-0036` — reference.md:229 *(§ DANE - geavanceerde configuratie)*

> Bij DANE rollover kunnen twee TLSA-records tegelijk gepubliceerd worden: één voor het huidige en één voor het toekomstige certificaat (pre-publish methode).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** DANE / TLSA rollover

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Bron bevat geen informatie over DANE/TLSA rollover methodes.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen technische DANE rollover-inhoud over pre-publish methode in de aangeleverde brontekst.*

## UNGROUNDED — geen bron ondersteunt de claim (26)

### `inet-toolbox-0002` — SKILL.md:315 *(§ 6. DANE instellen)*

> DANE vereist dat DNSSEC actief is op het MX-domein.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** DANE

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Bron bevat geen technische informatie over DANE.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *De brontekst vermeldt DANE als onderwerp van een how-to, maar geeft geen technische vereisten over DNSSEC-afhankelijkheid.*

### `inet-toolbox-0003` — SKILL.md:335 *(§ 6. DANE instellen)*

> Bij DANE met TLSA selector=1 (SPKI) en hergebruik van de privésleutel hoeft het TLSA-record niet te veranderen bij certificaatvernieuwing.

**Type:** normative_requirement  ·  **Modaliteit:** MAY  ·  **Scope:** DANE / TLSA

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Bron bevat geen technische informatie over DANE/TLSA.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen technische inhoud over TLSA selector=1 of sleutelhergebruik in de aangeleverde brontekst.*

### `inet-toolbox-0004` — SKILL.md:336 *(§ 6. DANE instellen)*

> Bij DANE met een nieuwe privésleutel moet het TLSA-record worden bijgewerkt VOOR de certificaatvernieuwing.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** DANE / TLSA

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Bron bevat geen technische informatie over DANE/TLSA.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen technische inhoud over TLSA-record bijwerken bij certificaatvernieuwing in de aangeleverde brontekst.*

### `inet-toolbox-0005` — SKILL.md:298 *(§ 5. SPF-record samenstellen)*

> SPF-records mogen maximaal 10 DNS-lookups bevatten; elke `include`, `a`, `mx` en `redirect` telt als 1 lookup.

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** SPF

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Bron bevat geen technische informatie over SPF.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen technische SPF-inhoud over DNS-lookup limieten in de aangeleverde brontekst.*

### `inet-toolbox-0006` — SKILL.md:300 *(§ 5. SPF-record samenstellen)*

> SPF-records dienen te eindigen met `-all` (fail) of `~all` (softfail).

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** SPF

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Bron bevat geen technische informatie over SPF.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen technische SPF-inhoud over -all of ~all in de aangeleverde brontekst.*

### `inet-toolbox-0007` — SKILL.md:299 *(§ 5. SPF-record samenstellen)*

> Voor SPF wordt aanbevolen `ip4`/`ip6` te gebruiken om DNS-lookups te besparen.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** SPF

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Bron bevat geen technische informatie over SPF.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen technische SPF-inhoud over ip4/ip6 gebruik in de aangeleverde brontekst.*

### `inet-toolbox-0012` — SKILL.md:396 *(§ Veelvoorkomende problemen)*

> DANE TLSA mismatch na certificaatvernieuwing kan worden voorkomen door SPKI (selector=1) te gebruiken en de privésleutel te hergebruiken, of door TLSA vooraf bij te werken.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** DANE / TLSA

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Bron bevat geen technische informatie over DANE/TLSA.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen technische DANE/TLSA-inhoud over mismatch-preventie in de aangeleverde brontekst.*

### `inet-toolbox-0014` — SKILL.md:156 *(§ 2. HTTPS/TLS configureren)*

> De Nginx HTTPS-configuratie gebruikt TLSv1.2 en TLSv1.3 als toegestane protocollen (NCSC-conform).

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** HTTPS/TLS / Nginx

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Bron bevat geen Nginx/TLS-configuratie-informatie.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen technische Nginx TLS-configuratie-inhoud in de aangeleverde brontekst.*

### `inet-toolbox-0015` — SKILL.md:158 *(§ 2. HTTPS/TLS configureren)*

> De Nginx HTTPS-configuratie stelt `ssl_prefer_server_ciphers off` in.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** HTTPS/TLS / Nginx

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Bron bevat geen Nginx/TLS-configuratie-informatie.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen technische Nginx-inhoud over ssl_prefer_server_ciphers in de aangeleverde brontekst.*

### `inet-toolbox-0016` — SKILL.md:160 *(§ 2. HTTPS/TLS configureren)*

> De Nginx HTTPS-configuratie schakelt OCSP Stapling in via `ssl_stapling on` en `ssl_stapling_verify on`.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** HTTPS/TLS / Nginx

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Bron bevat geen Nginx/TLS-configuratie-informatie.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen technische Nginx-inhoud over OCSP Stapling in de aangeleverde brontekst.*

### `inet-toolbox-0017` — SKILL.md:166 *(§ 2. HTTPS/TLS configureren)*

> De aanbevolen HSTS-header voor Nginx is `Strict-Transport-Security: max-age=31536000; includeSubDomains`.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** HTTPS/TLS / HSTS

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Bron bevat geen HSTS-configuratie-informatie.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen technische inhoud over HSTS-headers in de aangeleverde brontekst.*

### `inet-toolbox-0018` — SKILL.md:197 *(§ 2. HTTPS/TLS configureren)*

> Apache HTTPS-configuratie schakelt SSLv3, TLSv1 en TLSv1.1 uit via `SSLProtocol all -SSLv3 -TLSv1 -TLSv1.1`.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** HTTPS/TLS / Apache

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Bron bevat geen Apache/TLS-configuratie-informatie.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen technische Apache TLS-configuratie-inhoud in de aangeleverde brontekst.*

### `inet-toolbox-0019` — SKILL.md:199 *(§ 2. HTTPS/TLS configureren)*

> Apache HTTPS-configuratie stelt `SSLHonorCipherOrder off` in.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** HTTPS/TLS / Apache

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Bron bevat geen Apache/TLS-configuratie-informatie.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen technische Apache-inhoud over SSLHonorCipherOrder in de aangeleverde brontekst.*

### `inet-toolbox-0022` — reference.md:30 *(§ DNSSEC - geavanceerde configuratie)*

> DNSSEC ZSK rollover wordt aanbevolen elke 3 maanden.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** DNSSEC / ZSK rollover

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Bron bevat geen informatie over DNSSEC ZSK rollover.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen technische DNSSEC-inhoud over ZSK rollover frequentie in de aangeleverde brontekst.*

### `inet-toolbox-0023` — reference.md:39 *(§ DNSSEC - geavanceerde configuratie)*

> DNSSEC KSK rollover wordt aanbevolen jaarlijks.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** DNSSEC / KSK rollover

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Bron bevat geen informatie over DNSSEC KSK rollover.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen technische DNSSEC-inhoud over KSK rollover frequentie in de aangeleverde brontekst.*

### `inet-toolbox-0024` — reference.md:35 *(§ DNSSEC - geavanceerde configuratie)*

> Bij ZSK rollover moet na het genereren van de nieuwe sleutel gewacht worden tot de oude TTL verlopen is (24-48 uur) voordat met de nieuwe sleutel ondertekend wordt.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** DNSSEC / ZSK rollover

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Bron bevat geen informatie over DNSSEC ZSK rollover procedures.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen technische DNSSEC-inhoud over ZSK rollover procedure in de aangeleverde brontekst.*

### `inet-toolbox-0025` — reference.md:44 *(§ DNSSEC - geavanceerde configuratie)*

> Bij KSK rollover moet het DS-record van de nieuwe KSK bij de registrar worden gepubliceerd naast het oude voordat de DNSKEY RRset met de nieuwe KSK wordt ondertekend.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** DNSSEC / KSK rollover

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Bron bevat geen informatie over DNSSEC KSK rollover procedures.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen technische DNSSEC-inhoud over KSK rollover en DS-records in de aangeleverde brontekst.*

### `inet-toolbox-0026` — reference.md:59 *(§ DNSSEC - geavanceerde configuratie)*

> ECDSAP256SHA256 (algoritme 13) is het aanbevolen DNSSEC-algoritme voor nieuwe zones vanwege compacte handtekeningen, brede ondersteuning en goede prestaties.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** DNSSEC / algoritme-keuze

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Bron bevat geen informatie over DNSSEC algoritme-keuze.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen technische DNSSEC-inhoud over algoritme-aanbevelingen in de aangeleverde brontekst.*

### `inet-toolbox-0030` — reference.md:89 *(§ HTTPS/TLS - geavanceerde configuratie)*

> Mozilla SSL Configuration Generator adviseert 'Intermediate' voor de beste balans tussen beveiliging en compatibiliteit.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** HTTPS/TLS

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Bron bevat geen informatie over Mozilla SSL Configuration Generator.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen inhoud over Mozilla SSL Configuration Generator in de aangeleverde brontekst.*

### `inet-toolbox-0031` — reference.md:153 *(§ E-mailbeveiliging - geavanceerde configuratie)*

> Postfix uitgaand TLS gebruikt `smtp_tls_security_level = dane` voor DANE-validatie.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** Postfix / DANE / TLS

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Bron bevat geen Postfix/DANE/TLS-configuratie-informatie.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen technische Postfix/DANE-inhoud in de aangeleverde brontekst.*

### `inet-toolbox-0032` — reference.md:160 *(§ E-mailbeveiliging - geavanceerde configuratie)*

> Postfix DANE vereist `smtp_dns_support_level = dnssec`.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Postfix / DANE

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Bron bevat geen Postfix/DANE-configuratie-informatie.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen technische Postfix/DANE-inhoud over smtp_dns_support_level in de aangeleverde brontekst.*

### `inet-toolbox-0033` — reference.md:142 *(§ E-mailbeveiliging - geavanceerde configuratie)*

> Postfix TLS-configuratie sluit SSLv2, SSLv3, TLSv1 en TLSv1.1 uit voor zowel inkomend als uitgaand verkeer.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** Postfix / TLS

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Bron bevat geen Postfix/TLS-configuratie-informatie.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen technische Postfix TLS-configuratie-inhoud in de aangeleverde brontekst.*

### `inet-toolbox-0034` — reference.md:189 *(§ E-mailbeveiliging - geavanceerde configuratie)*

> SPF-flattening is een oplossing wanneer het aantal DNS-lookups de limiet van 10 overschrijdt: IP-adressen direct opnemen of subdomeinen gebruiken.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** SPF

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Bron bevat geen informatie over SPF-flattening.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen technische SPF-inhoud over flattening in de aangeleverde brontekst.*

### `inet-toolbox-0035` — reference.md:239 *(§ DANE - geavanceerde configuratie)*

> Bij DANE voor meerdere MX-servers moet elk MX-domein een eigen TLSA-record hebben onder `_25._tcp.<mx-hostname>`.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** DANE / meerdere MX

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Bron bevat geen informatie over DANE voor meerdere MX-servers.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen technische DANE/TLSA-inhoud over meerdere MX-servers in de aangeleverde brontekst.*

### `inet-toolbox-0037` — reference.md:282 *(§ IPv6 - geavanceerde configuratie)*

> ICMPv6 moet worden toegestaan in de firewall omdat het nodig is voor IPv6.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** IPv6 / firewall

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Bron bevat geen informatie over IPv6 firewall-configuratie.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen technische IPv6/firewall-inhoud over ICMPv6 in de aangeleverde brontekst.*

### `inet-toolbox-0038` — reference.md:122 *(§ HTTPS/TLS - geavanceerde configuratie)*

> Let's Encrypt wildcard-certificaten vereisen een DNS-challenge.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Let's Encrypt / wildcard

- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Bron bevat geen informatie over Let's Encrypt wildcard-certificaten.*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  - *Geen technische inhoud over Let's Encrypt wildcard-certificaten in de aangeleverde brontekst.*

## GROUNDED — minstens één bron ondersteunt de claim (1)

<details>
<summary>Klap uit voor alle GROUNDED claims</summary>

### `inet-toolbox-0020` — SKILL.md:385 *(§ Repositories)*

> De toolbox-wiki is gepubliceerd onder de CC-BY-4.0 licentie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** toolbox-wiki

- **SUPPORTED** (medium) — [https://github.com/internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki)
  > LICENSE-CC-BY-4.0.txt
  - *De repository bevat een bestand genaamd LICENSE-CC-BY-4.0.txt, wat sterk suggereert dat de licentie CC-BY-4.0 is. De exacte licentietekst is niet aangeleverd, maar de bestandsnaam is een directe aanwijzing.*
- **SOURCE_UNAVAILABLE** (high) — [https://raw.githubusercontent.com/internetstandards/toolbox-wiki/main/LICENSE](https://raw.githubusercontent.com/internetstandards/toolbox-wiki/main/LICENSE)
  - *Bron status: unreachable*
- **SOURCE_UNAVAILABLE** (high) — [https://raw.githubusercontent.com/internetstandards/toolbox-wiki/master/LICENSE](https://raw.githubusercontent.com/internetstandards/toolbox-wiki/master/LICENSE)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://internet.nl/halloffame/](https://internet.nl/halloffame/)
  - *Bron bevat geen licentie-informatie over de toolbox-wiki.*

</details>
