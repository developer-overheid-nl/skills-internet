<!-- markdownlint-disable MD052 MD034 MD013 -->
# Audit inet-web — 2026-05-17

> Automatisch gegenereerd door audit-tooling. Niet handmatig bewerken; wijzig SKILL.md / reference.md en regenereer.

## Samenvatting

| Status | Aantal | % |
|--------|--------|---|
| UNSUPPORTED_ASSERTION | 23 | 43% |
| CONTRADICTED | 0 | 0% |
| PARTIALLY_GROUNDED | 6 | 11% |
| UNGROUNDED | 22 | 42% |
| NO_SOURCE | 0 | 0% |
| UNVERIFIABLE | 0 | 0% |
| KNOWN_DISCREPANCY | 0 | 0% |
| GROUNDED | 2 | 4% |

*Geverifieerd met sonnet, 9 calls, $0.9819.*

## UNSUPPORTED_ASSERTION — stellige bewering zonder enige bronsteun (mogelijke hallucinatie) (23)

### `inet-web-0002` — SKILL.md:27 *(§ Overzicht)*

> Alle door internet.nl geteste standaarden staan op de pas-toe-of-leg-uit-lijst van Forum Standaardisatie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl / Forum Standaardisatie

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron maakt geen melding van Forum Standaardisatie of de pas-toe-of-leg-uit-lijst.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *RFC 6797 bevat geen informatie over Forum Standaardisatie of de pas-toe-of-leg-uit-lijst.*

### `inet-web-0003` — SKILL.md:43 *(§ 1. IPv6)*

> Internet.nl test op aanwezigheid van een AAAA-record voor het domein.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl IPv6-test

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron noemt IPv6 als testonderdeel maar gaat niet in op specifieke subtests zoals AAAA-records.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *RFC 6797 gaat over HSTS, niet over IPv6 of AAAA-records.*

### `inet-web-0005` — SKILL.md:45 *(§ 1. IPv6)*

> Internet.nl test of nameservers bereikbaar zijn via IPv6.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl IPv6-test

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron vermeldt geen test op IPv6-bereikbaarheid van nameservers.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *RFC 6797 gaat over HSTS, niet over IPv6-bereikbaarheid van nameservers.*

### `inet-web-0007` — SKILL.md:69 *(§ 2. DNSSEC)*

> Internet.nl test of er een DS-record aanwezig is bij de registrar.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl DNSSEC-test

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron vermeldt geen specifieke subtest op DS-records bij de registrar.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *RFC 6797 gaat over HSTS, niet over DS-records bij registrars.*

### `inet-web-0008` — SKILL.md:70 *(§ 2. DNSSEC)*

> Internet.nl test op geldige RRSIG-handtekeningen en correcte ketenvalidatie (trust chain) bij DNSSEC.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl DNSSEC-test

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron vermeldt geen details over RRSIG-handtekeningen of ketenvalidatie.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *RFC 6797 gaat over HSTS, niet over DNSSEC RRSIG-handtekeningen of ketenvalidatie.*

### `inet-web-0010` — SKILL.md:96 *(§ 3. HTTPS / TLS)*

> TLS 1.0/1.1 geeft een phase-out waarschuwing bij internet.nl; SSL 2.0/3.0 is een harde fout.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl TLS-test

- **NOT_FOUND** (high) — [https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS](https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS)
  - *De brontekst bevat geen informatie over TLS 1.0/1.1 phase-out waarschuwingen of SSL 2.0/3.0 fouten bij internet.nl.*

### `inet-web-0012` — SKILL.md:95 *(§ 3. HTTPS / TLS)*

> Internet.nl test op HTTPS bereikbaarheid en redirect van HTTP naar HTTPS.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl TLS-test

- **NOT_FOUND** (high) — [https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS](https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS)
  - *De brontekst bevat geen informatie over HTTPS-bereikbaarheid of HTTP-naar-HTTPS-redirects.*

### `inet-web-0013` — SKILL.md:98 *(§ 3. HTTPS / TLS)*

> Internet.nl test op een geldig certificaat (keten, geldigheid, hostnaam).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl TLS-test

- **NOT_FOUND** (high) — [https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS](https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS)
  - *De brontekst bevat geen informatie over certificaatvalidatie, keten, geldigheid of hostnaam.*

### `inet-web-0014` — SKILL.md:99 *(§ 3. HTTPS / TLS)*

> Internet.nl test OCSP stapling als niet-scorende melding.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl TLS-test

- **NOT_FOUND** (high) — [https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS](https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS)
  - *De brontekst bevat geen informatie over OCSP stapling.*

### `inet-web-0016` — SKILL.md:204 *(§ 5. Security headers)*

> Internet.nl test op aanwezigheid van de `Content-Security-Policy` header.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl security headers-test

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron vermeldt 'Security options' maar specificeert niet welke headers getest worden.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *RFC 6797 gaat over HSTS, niet over Content-Security-Policy headers.*

### `inet-web-0017` — SKILL.md:205 *(§ 5. Security headers)*

> Internet.nl test op aanwezigheid van de `X-Frame-Options` header.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl security headers-test

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron vermeldt 'Security options' maar specificeert niet welke headers getest worden.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *RFC 6797 gaat over HSTS, niet over X-Frame-Options headers.*

### `inet-web-0018` — SKILL.md:206 *(§ 5. Security headers)*

> Internet.nl test op aanwezigheid van de `X-Content-Type-Options` header.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl security headers-test

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron vermeldt 'Security options' maar specificeert niet welke headers getest worden.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *RFC 6797 gaat over HSTS, niet over X-Content-Type-Options headers.*

### `inet-web-0019` — SKILL.md:207 *(§ 5. Security headers)*

> Internet.nl test op aanwezigheid van de `Referrer-Policy` header.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl security headers-test

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron vermeldt 'Security options' maar specificeert niet welke headers getest worden.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *RFC 6797 gaat over HSTS, niet over Referrer-Policy headers.*

### `inet-web-0021` — SKILL.md:243 *(§ 6. security.txt)*

> Internet.nl test of security.txt bereikbaar is op `/.well-known/security.txt` en de verplichte velden `Contact` en `Expires` bevat.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl security.txt-test

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron noemt security.txt in de kennisbank-sectie maar geeft geen details over vereiste velden of locatie.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *RFC 6797 gaat over HSTS, niet over security.txt of RFC 9116.*

### `inet-web-0024` — SKILL.md:276 *(§ 7. RPKI)*

> Internet.nl controleert of de ROA-status `valid` is (niet `invalid` of `unknown`).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl RPKI-test

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron vermeldt geen details over ROA-statussen (valid/invalid/unknown).*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *De brontekst betreft RFC 6797 (HSTS), niet RPKI of ROA-statussen.*

### `inet-web-0033` — reference.md:28 *(§ Aanbevolen cipher suites (NCSC))*

> Voor TLS 1.3 zijn alleen TLS_AES_128_GCM_SHA256, TLS_AES_256_GCM_SHA384 en TLS_CHACHA20_POLY1305_SHA256 beschikbaar en alle zijn goed.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** TLS 1.3 cipher suites

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron vermeldt niets over TLS 1.3 cipher suites.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *De brontekst betreft RFC 6797 (HSTS), niet TLS 1.3 cipher suite specificaties.*

### `inet-web-0041` — reference.md:46 *(§ Renegotiation en OCSP (NCSC 2025-05))*

> Extended Master Secret (RFC 7627) is een aparte test geworden voor TLS 1.2; ontbreken telt als fout. Voor TLS 1.3 is het niet van toepassing.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** NCSC TLS Security Guidelines 2025-05 / Internet.nl v1.11.0

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS](https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS)
  - *De brontekst bevat geen informatie over Extended Master Secret (RFC 7627) of TLS 1.2/1.3-specifieke testvereisten.*
- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden/tls](https://www.forumstandaardisatie.nl/open-standaarden/tls)
  - *Extended Master Secret (RFC 7627) wordt nergens in de brontekst genoemd. De bron beschrijft het functioneel toepassingsgebied en de lijststatus van TLS maar gaat niet in op specifieke testitems van Internet.nl.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7627.txt](https://www.rfc-editor.org/rfc/rfc7627.txt)
  - *RFC 7627 definieert de Extended Master Secret extensie zelf, maar bevat geen informatie over NCSC TLS Security Guidelines 2025-05, Internet.nl v1.11.0, teststructuur, of de classificatie als aparte test waarbij ontbreken als fout telt. De claim over hoe Internet.nl de EMS-test implementeert en categoriseert valt buiten de scope van deze RFC.*
</details>

### `inet-web-0042` — reference.md:47 *(§ Renegotiation en OCSP (NCSC 2025-05))*

> OCSP stapling wordt niet langer als fout gerekend wanneer het certificaat geen OCSP-endpoint bevat (AIA zonder OCSP URI); in dat geval wordt het als niet-getest gemeld.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** NCSC TLS Security Guidelines 2025-05 / Internet.nl v1.11.0

- **NOT_FOUND** (high) — [https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS](https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS)
  - *De brontekst bevat geen informatie over OCSP stapling-gedrag bij ontbrekend OCSP-endpoint of AIA-velden.*
- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden/tls](https://www.forumstandaardisatie.nl/open-standaarden/tls)
  - *OCSP stapling, AIA, en de specifieke testlogica van Internet.nl v1.11.0 komen niet voor in de brontekst.*

### `inet-web-0045` — reference.md:184 *(§ Preload-lijst)*

> Het `preload` directive voor HSTS is onomkeerbaar op korte termijn.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** HSTS preload-lijst

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron vermeldt niets over de onomkeerbaarheid van het preload directive.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *Het 'preload' directive en de onomkeerbaarheid ervan worden niet behandeld in RFC 6797.*

### `inet-web-0046` — reference.md:211 *(§ Content-Security-Policy (CSP))*

> CSP `frame-ancestors` directive vervangt `X-Frame-Options`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Content-Security-Policy / security headers

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron vermeldt niets over de relatie tussen CSP frame-ancestors en X-Frame-Options.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *RFC 6797 gaat over HSTS en behandelt Content-Security-Policy, frame-ancestors noch X-Frame-Options.*

### `inet-web-0049` — reference.md:260 *(§ Hoe RPKI werkt)*

> Een ROA (Route Origin Authorisation) is een digitaal ondertekende verklaring die een IP-prefix koppelt aan een AS-nummer.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** RPKI / BGP

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron vermeldt niets over ROA's of de koppeling van IP-prefixen aan AS-nummers.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *RFC 6797 behandelt RPKI, ROA's en BGP niet.*

### `inet-web-0050` — reference.md:264 *(§ Hoe RPKI werkt)*

> RPKI-validatiestatus kent drie waarden: `Valid`, `Invalid` en `NotFound`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** RPKI / ROV

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron vermeldt niets over RPKI-validatiestatussen.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *RFC 6797 behandelt RPKI-validatiestatus niet.*

### `inet-web-0051` — reference.md:271 *(§ ROA aanmaken)*

> ROA's worden aangemaakt in het RIPE NCC-portaal voor Europese netwerken via https://my.ripe.net.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** RPKI / RIPE NCC

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron vermeldt niets over RIPE NCC of het aanmaken van ROA's.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *RFC 6797 behandelt ROA's, RIPE NCC noch my.ripe.net.*

## PARTIALLY_GROUNDED — bron ondersteunt deel van de claim (6)

### `inet-web-0001` — SKILL.md:26 *(§ Overzicht)*

> Internet.nl test websites op IPv6, DNSSEC, HTTPS/TLS, HSTS, security headers, security.txt en RPKI.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl websitetest

- **PARTIALLY_SUPPORTED** (medium) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  > After you enter a domain name of a website, we will test if the website offers support for the modern Internet Standards below. IPv6 : reachable via modern address? DNSSEC : domain name signed? HTTPS : secure connection? Security options : security options set? RPKI : route authorisation?
  - *De bron bevestigt IPv6, DNSSEC, HTTPS, Security options en RPKI. HSTS en security.txt worden niet expliciet als subtests genoemd in de bron (alleen 'Security options' als verzamelnaam).*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *RFC 6797 gaat uitsluitend over HSTS. Het beschrijft niet wat internet.nl test.*

### `inet-web-0004` — SKILL.md:44 *(§ 1. IPv6)*

> Internet.nl test of de webserver bereikbaar is via IPv6.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl IPv6-test

- **PARTIALLY_SUPPORTED** (medium) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  > IPv6 : reachable via modern address?
  - *De bron bevestigt dat bereikbaarheid via IPv6 getest wordt, maar specificeert niet dat het om de webserver gaat.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *RFC 6797 gaat over HSTS, niet over IPv6-bereikbaarheid van webservers.*

### `inet-web-0006` — SKILL.md:68 *(§ 2. DNSSEC)*

> Internet.nl test of de DNS-zone is gesigneerd met DNSSEC.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl DNSSEC-test

- **PARTIALLY_SUPPORTED** (medium) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  > DNSSEC : domain name signed?
  - *De bron bevestigt dat DNSSEC getest wordt (domein gesigneerd), maar specificeert niet expliciet dat het om de DNS-zone gaat.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *RFC 6797 gaat over HSTS, niet over DNSSEC-zone-ondertekening.*

### `inet-web-0015` — SKILL.md:176 *(§ 4. HSTS)*

> Internet.nl vereist de `Strict-Transport-Security` header met een `max-age` van minimaal 31536000 (1 jaar).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** internet.nl HSTS-test

- **PARTIALLY_SUPPORTED** (medium) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  > The HSTS header field below stipulates that the HSTS Policy is to remain in effect for one year (there are approximately 31536000 seconds in a year), and the policy applies only to the domain of the HSTS Host issuing it: Strict-Transport-Security: max-age=31536000
  - *RFC 6797 bevestigt dat 31536000 seconden overeenkomt met één jaar en geeft dit als voorbeeld, maar stelt geen minimumwaarde voor max-age verplicht. De eis dat internet.nl specifiek een minimum van 31536000 vereist staat niet in deze RFC — dat is een internet.nl-testbeleid, niet een RFC-vereiste.*
- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron noemt security options als testcategorie maar geeft geen details over HSTS-vereisten of max-age waarden.*

### `inet-web-0023` — SKILL.md:275 *(§ 7. RPKI)*

> Internet.nl test RPKI door te controleren of er een geldig ROA-record aanwezig is voor het IP-adres van de webserver.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl RPKI-test

- **PARTIALLY_SUPPORTED** (low) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  > RPKI : route authorisation?
  - *De bron bevestigt dat RPKI getest wordt, maar vermeldt niet specifiek ROA-records of IP-adressen van de webserver.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *De brontekst betreft RFC 6797 (HSTS), niet RPKI of ROA-records. Geen relevante inhoud voor deze claim.*

### `inet-web-0040` — reference.md:45 *(§ Renegotiation en OCSP (NCSC 2025-05))*

> Secure renegotiation (RFC 5746) blijft verplicht.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** NCSC TLS Security Guidelines 2025-05 / Internet.nl v1.11.0

- **PARTIALLY_SUPPORTED** (medium) — [https://www.rfc-editor.org/rfc/rfc5746.txt](https://www.rfc-editor.org/rfc/rfc5746.txt)
  > Servers SHOULD NOT allow clients to renegotiate without using this extension. Many servers can mitigate this attack simply by refusing to renegotiate at all.
  - *RFC 5746 definieert het secure renegotiation mechanisme en stelt dat servers het MOETEN implementeren voor de initiële handshake ('even servers that do not support renegotiation MUST implement the minimal version of the extension described in this document for initial handshakes'). De RFC ondersteunt de technische basis van de claim, maar de claim verwijst specifiek naar NCSC TLS Security Guidelines 2025-05 / Internet.nl v1.11.0 als normatieve context. De RFC zelf spreekt van SHOULD NOT (servers mogen renegotiatie toestaan mits via de extensie), niet van een absolute verplichting. De verplichtstelling als zodanig ('verplicht') is een beleidsinterpretatie die de RFC deels maar niet volledig dekt.*
- **NOT_FOUND** (high) — [https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS](https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS)
  - *De brontekst bevat geen informatie over secure renegotiation (RFC 5746).*
- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden/tls](https://www.forumstandaardisatie.nl/open-standaarden/tls)
  - *De brontekst verwijst naar NCSC TLS-richtlijnen en Internet.nl als hulpmiddelen, maar bevat geen inhoudelijke specificaties over secure renegotiation (RFC 5746) of verplichtingen daaromtrent.*

## UNGROUNDED — geen bron ondersteunt de claim (22)

### `inet-web-0009` — SKILL.md:89 *(§ 3. HTTPS / TLS)*

> Internet.nl vereist TLS 1.2 of 1.3 met sterke cipher suites.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** internet.nl TLS-test

- **NOT_FOUND** (high) — [https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS](https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS)
  - *De brontekst bevat alleen een pagina-layout met downloadlinks voor TLS-richtlijnen. Er staat geen inhoudelijke informatie over internet.nl-testvereisten of specifieke TLS-versies.*

### `inet-web-0011` — SKILL.md:97 *(§ 3. HTTPS / TLS)*

> Internet.nl test op sterke cipher suites; RC4, 3DES, NULL en export ciphers zijn niet toegestaan.

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** internet.nl TLS-test / cipher suites

- **NOT_FOUND** (high) — [https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS](https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS)
  - *De brontekst bevat geen informatie over cipher suite vereisten of verboden ciphers.*

### `inet-web-0022` — SKILL.md:245 *(§ 6. security.txt)*

> Digitale ondertekening (PGP) van security.txt is aanbevolen.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** security.txt / RFC 9116

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron vermeldt niets over PGP-ondertekening van security.txt.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *RFC 6797 gaat over HSTS, niet over PGP-ondertekening van security.txt.*

### `inet-web-0025` — reference.md:13 *(§ Aanbevolen cipher suites (NCSC))*

> NCSC adviseert TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 als aanbevolen (voorkeur) cipher suite voor TLS 1.2.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** NCSC TLS Security Guidelines / TLS 1.2 cipher suites

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron vermeldt niets over NCSC TLS-richtlijnen of specifieke cipher suites.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *De brontekst betreft RFC 6797 (HSTS), niet NCSC TLS-richtlijnen of cipher suites.*

### `inet-web-0026` — reference.md:14 *(§ Aanbevolen cipher suites (NCSC))*

> NCSC adviseert TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 als aanbevolen (voorkeur) cipher suite voor TLS 1.2.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** NCSC TLS Security Guidelines / TLS 1.2 cipher suites

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron vermeldt niets over NCSC TLS-richtlijnen of specifieke cipher suites.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *De brontekst betreft RFC 6797 (HSTS), niet NCSC TLS-richtlijnen of cipher suites.*

### `inet-web-0027` — reference.md:15 *(§ Aanbevolen cipher suites (NCSC))*

> NCSC adviseert TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 als aanbevolen (voorkeur) cipher suite voor TLS 1.2.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** NCSC TLS Security Guidelines / TLS 1.2 cipher suites

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron vermeldt niets over NCSC TLS-richtlijnen of specifieke cipher suites.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *De brontekst betreft RFC 6797 (HSTS), niet NCSC TLS-richtlijnen of cipher suites.*

### `inet-web-0028` — reference.md:16 *(§ Aanbevolen cipher suites (NCSC))*

> NCSC adviseert TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 als aanbevolen (voorkeur) cipher suite voor TLS 1.2.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** NCSC TLS Security Guidelines / TLS 1.2 cipher suites

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron vermeldt niets over NCSC TLS-richtlijnen of specifieke cipher suites.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *De brontekst betreft RFC 6797 (HSTS), niet NCSC TLS-richtlijnen of cipher suites.*

### `inet-web-0029` — reference.md:17 *(§ Aanbevolen cipher suites (NCSC))*

> NCSC adviseert TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256 als aanbevolen (voorkeur) cipher suite voor TLS 1.2.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** NCSC TLS Security Guidelines / TLS 1.2 cipher suites

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron vermeldt niets over NCSC TLS-richtlijnen of specifieke cipher suites.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *De brontekst betreft RFC 6797 (HSTS), niet NCSC TLS-richtlijnen of cipher suites.*

### `inet-web-0030` — reference.md:18 *(§ Aanbevolen cipher suites (NCSC))*

> NCSC adviseert TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256 als aanbevolen (voorkeur) cipher suite voor TLS 1.2.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** NCSC TLS Security Guidelines / TLS 1.2 cipher suites

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron vermeldt niets over NCSC TLS-richtlijnen of specifieke cipher suites.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *De brontekst betreft RFC 6797 (HSTS), niet NCSC TLS-richtlijnen of cipher suites.*

### `inet-web-0031` — reference.md:25 *(§ Aanbevolen cipher suites (NCSC))*

> Cipher suites met RC4, 3DES, NULL, EXPORT, DES of MD5 zijn niet toegestaan volgens NCSC.

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** NCSC TLS Security Guidelines / cipher suites

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron vermeldt niets over verboden cipher suites of NCSC-richtlijnen.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *De brontekst betreft RFC 6797 (HSTS), niet NCSC-richtlijnen over verboden cipher suites.*

### `inet-web-0032` — reference.md:26 *(§ Aanbevolen cipher suites (NCSC))*

> TLS_RSA_* cipher suites zijn niet toegestaan vanwege ontbreken van forward secrecy.

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** NCSC TLS Security Guidelines / cipher suites

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron vermeldt niets over TLS_RSA_* cipher suites of forward secrecy.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *De brontekst betreft RFC 6797 (HSTS), niet forward secrecy-vereisten of TLS_RSA_* cipher suites.*

### `inet-web-0034` — reference.md:35 *(§ Certificaatvereisten)*

> TLS-certificaten vereisen minimaal 2048-bit RSA of 256-bit ECDSA sleutellengte.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** TLS certificaatvereisten

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron vermeldt niets over sleutellengtes voor TLS-certificaten.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *De brontekst betreft RFC 6797 (HSTS), niet sleutellengtes voor TLS-certificaten.*

### `inet-web-0035` — reference.md:36 *(§ Certificaatvereisten)*

> TLS-certificaten vereisen SHA-256 of hoger als hash-algoritme.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** TLS certificaatvereisten

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron vermeldt niets over hash-algoritmen voor TLS-certificaten.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *De brontekst betreft RFC 6797 (HSTS), niet hash-algoritme-vereisten voor TLS-certificaten.*

### `inet-web-0036` — reference.md:37 *(§ Certificaatvereisten)*

> TLS-certificaten vereisen een geldige keten naar een vertrouwde root CA.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** TLS certificaatvereisten

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron vermeldt niets over certificaatketens of vertrouwde root CA's.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *De brontekst betreft RFC 6797 (HSTS). Hoewel HSTS vertrouwde certificaatketens veronderstelt, specificeert de RFC geen expliciete eis voor een geldige keten naar een vertrouwde root CA als certificaatvereiste.*

### `inet-web-0037` — reference.md:38 *(§ Certificaatvereisten)*

> De hostnaam moet aanwezig zijn in het Subject Alternative Name (SAN) veld van het TLS-certificaat.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** TLS certificaatvereisten

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron vermeldt niets over Subject Alternative Name velden in certificaten.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *De brontekst betreft RFC 6797 (HSTS), niet Subject Alternative Name (SAN)-vereisten voor TLS-certificaten.*

### `inet-web-0038` — reference.md:44 *(§ Renegotiation en OCSP (NCSC 2025-05))*

> Met de NCSC TLS-richtlijnen van mei 2025 (geïmplementeerd in Internet.nl v1.11.0) is client-initiated renegotiation acceptabel mits het aantal beperkt blijft tot minder dan 10 per verbinding.

**Type:** normative_requirement  ·  **Modaliteit:** MAY  ·  **Scope:** NCSC TLS Security Guidelines 2025-05 / Internet.nl v1.11.0

- **NOT_FOUND** (high) — [https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS](https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS)
  - *De brontekst is een webpagina met uitsluitend downloadlinks naar PDF-documenten. De inhoud van de TLS-richtlijnen 2025-05 zelf is niet aangeleverd; claims over renegotiation-limieten kunnen hier niet worden geverifieerd.*
- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden/tls](https://www.forumstandaardisatie.nl/open-standaarden/tls)
  - *De brontekst behandelt TLS algemeen (versies 1.2 en 1.3, toepassingsgebied, adoptieadviezen) maar bevat geen informatie over client-initiated renegotiation, NCSC TLS-richtlijnen van mei 2025, of Internet.nl v1.11.0.*

### `inet-web-0039` — reference.md:44 *(§ Renegotiation en OCSP (NCSC 2025-05))*

> Onbeperkte client renegotiation blijft een fout vanwege DoS-risico.

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** NCSC TLS Security Guidelines 2025-05 / Internet.nl v1.11.0

- **NOT_FOUND** (high) — [https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS](https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS)
  - *De brontekst bevat geen inhoudelijke richtlijnen over client renegotiation of DoS-risico's.*
- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden/tls](https://www.forumstandaardisatie.nl/open-standaarden/tls)
  - *De brontekst bevat geen informatie over client renegotiation, DoS-risico's in die context, of de specifieke NCSC/Internet.nl versie-scope van de claim.*

### `inet-web-0043` — reference.md:173 *(§ Preload-lijst)*

> HSTS preloading vereist een `max-age` van minimaal 31536000, de `includeSubDomains` directive én de `preload` directive.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** HSTS preload-lijst / hstspreload.org

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron vermeldt niets over HSTS preloading of bijbehorende vereisten.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *RFC 6797 definieert HSTS maar beschrijft geen preload-vereisten. Het 'preload' directive wordt niet vermeld in deze spec. De minimale max-age van 31536000 voor preloading is een vereiste van hstspreload.org, niet van RFC 6797. De spec noemt wel max-age=31536000 als voorbeeld van een jaar, maar niet als preload-vereiste.*

### `inet-web-0044` — reference.md:171 *(§ Preload-lijst)*

> HSTS preloading vereist een geldig TLS-certificaat en redirect van HTTP naar HTTPS op hetzelfde domein.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** HSTS preload-lijst / hstspreload.org

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron vermeldt niets over HSTS preloading of bijbehorende vereisten.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *RFC 6797 beschrijft geen preload-vereisten. Geldig TLS-certificaat en HTTP-naar-HTTPS redirect als preload-voorwaarden staan niet in deze spec.*

### `inet-web-0048` — reference.md:231 *(§ Verplichte velden)*

> Het `Expires` veld in security.txt moet een datum in ISO 8601 formaat bevatten en mag maximaal 1 jaar vooruit liggen.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** security.txt / RFC 9116

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron vermeldt niets over het Expires-veld in security.txt of ISO 8601 formaat.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *RFC 6797 gaat over HSTS en behandelt security.txt niet.*

### `inet-web-0052` — SKILL.md:239 *(§ 6. security.txt)*

> security.txt staat op de pas-toe-of-leg-uit-lijst en de overheid moet een Coordinated Vulnerability Disclosure (CVD) beleid hebben.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** security.txt / Forum Standaardisatie / CVD

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron vermeldt niets over Forum Standaardisatie, CVD-beleid of verplichtingen voor de overheid.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *RFC 6797 behandelt security.txt, de pas-toe-of-leg-uit-lijst noch CVD-beleid niet.*

### `inet-web-0053` — SKILL.md:306 *(§ Veelvoorkomende problemen)*

> Het `Expires` veld in security.txt mag maximaal 1 jaar vooruit liggen; een verlopen bestand is een bekend probleem.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** security.txt / RFC 9116

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron vermeldt niets over het Expires-veld of verlopen security.txt bestanden.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *RFC 6797 behandelt security.txt en het Expires-veld niet.*

## GROUNDED — minstens één bron ondersteunt de claim (2)

<details>
<summary>Klap uit voor alle GROUNDED claims</summary>

### `inet-web-0020` — SKILL.md:236 *(§ 6. security.txt)*

> security.txt is gestandaardiseerd als RFC 9116 en moet bereikbaar zijn op `/.well-known/security.txt`.

**Type:** reference_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** security.txt / RFC 9116

- **SUPPORTED** (high) — [https://www.rfc-editor.org/rfc/rfc9116.txt](https://www.rfc-editor.org/rfc/rfc9116.txt)
  > For web-based services, organizations MUST place the "security.txt" file under the "/.well-known/" path, e.g., https://example.com/.well-known/security.txt as per [RFC8615] of a domain name or IP address.
  - *De RFC-nummering (9116) blijkt uit de documentheader en IANA-sectie: 'URI suffix: security.txt ... Specification document(s): RFC 9116'.*

### `inet-web-0047` — reference.md:229 *(§ Verplichte velden)*

> RFC 9116 definieert `Contact` (minimaal 1) en `Expires` als verplichte velden in security.txt.

**Type:** reference_claim  ·  **Modaliteit:** MUST  ·  **Scope:** security.txt / RFC 9116

- **SUPPORTED** (high) — [https://www.rfc-editor.org/rfc/rfc9116.txt](https://www.rfc-editor.org/rfc/rfc9116.txt)
  > The "Contact" field [...] MUST always be present in a "security.txt" file. [...] The "Expires" field [...] This field MUST always be present and MUST NOT appear more than once.

</details>
