<!-- markdownlint-disable MD052 MD034 MD013 -->
# Audit inet-web — 2026-05-17

> Automatisch gegenereerd door audit-tooling. Niet handmatig bewerken; wijzig SKILL.md / reference.md en regenereer.

## Samenvatting

| Status | Aantal | % |
|--------|--------|---|
| UNSUPPORTED_ASSERTION | 21 | 48% |
| CONTRADICTED | 0 | 0% |
| PARTIALLY_GROUNDED | 7 | 16% |
| UNGROUNDED | 15 | 34% |
| NO_SOURCE | 0 | 0% |
| UNVERIFIABLE | 0 | 0% |
| KNOWN_DISCREPANCY | 0 | 0% |
| GROUNDED | 1 | 2% |

*Geverifieerd met sonnet, 10 calls, $0.9982.*

## UNSUPPORTED_ASSERTION — stellige bewering zonder enige bronsteun (mogelijke hallucinatie) (21)

### `inet-web-0002` — SKILL.md:27 *(§ Overzicht)*

> Alle door internet.nl geteste standaarden staan op de pas-toe-of-leg-uit-lijst van Forum Standaardisatie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Forum Standaardisatie / internet.nl

<details><summary>2x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron maakt geen melding van Forum Standaardisatie of de pas-toe-of-leg-uit-lijst.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *De claim gaat over het Forum Standaardisatie en de pas-toe-of-leg-uit-lijst. RFC 6797 behandelt dit niet.*
- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden](https://www.forumstandaardisatie.nl/open-standaarden)
  - *De brontekst is een navigatiepagina van Forum Standaardisatie zonder inhoudelijke details over welke specifieke standaarden op de 'pas-toe-of-leg-uit'-lijst staan of over de relatie met internet.nl. Er is geen informatie over internet.nl of de geteste standaarden in de aangeleverde tekst.*
</details>

### `inet-web-0003` — SKILL.md:42 *(§ 1. IPv6)*

> Internet.nl test of een AAAA-record aanwezig is voor het domein.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl IPv6-test

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron beschrijft niet op detailniveau welke subtests worden uitgevoerd binnen de IPv6-test. AAAA-records worden niet vermeld.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *De claim gaat over de IPv6-test van internet.nl (AAAA-records). RFC 6797 gaat over HSTS, niet over IPv6.*

### `inet-web-0005` — SKILL.md:44 *(§ 1. IPv6)*

> Internet.nl test of nameservers bereikbaar zijn via IPv6.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl IPv6-test

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron noemt geen subtest over IPv6-bereikbaarheid van nameservers.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *De claim gaat over de IPv6-bereikbaarheidstest van nameservers via internet.nl. Buiten scope van RFC 6797.*

### `inet-web-0007` — SKILL.md:69 *(§ 2. DNSSEC)*

> Internet.nl test of een DS-record aanwezig is bij de registrar.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl DNSSEC-test

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *DS-records of registrar-gerelateerde subtests worden niet vermeld in de bron.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *De claim gaat over DS-records en DNSSEC-registrar-configuratie. Buiten scope van RFC 6797.*

### `inet-web-0008` — SKILL.md:70 *(§ 2. DNSSEC)*

> Internet.nl test op geldige RRSIG-handtekeningen en correcte ketenvalidatie (trust chain) voor DNSSEC.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl DNSSEC-test

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *RRSIG-handtekeningen en trust chain validatie worden niet vermeld in de bron.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *De claim gaat over RRSIG-handtekeningen en DNSSEC trust chain validatie. Buiten scope van RFC 6797.*

### `inet-web-0010` — SKILL.md:95 *(§ 3. HTTPS / TLS)*

> Internet.nl test op HTTPS bereikbaarheid en redirect van HTTP naar HTTPS.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl HTTPS/TLS-test

- **NOT_FOUND** (high) — [https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS](https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS)
  - *De brontekst bevat geen informatie over internet.nl HTTPS-bereikbaarheid of redirects.*

### `inet-web-0011` — SKILL.md:96 *(§ 3. HTTPS / TLS)*

> TLS 1.0/1.1 geeft een phase-out waarschuwing bij internet.nl; SSL 2.0/3.0 is een harde fout.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl HTTPS/TLS-test

- **NOT_FOUND** (high) — [https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS](https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS)
  - *De brontekst bevat geen informatie over TLS 1.0/1.1 phase-out of SSL 2.0/3.0 fouten bij internet.nl.*

### `inet-web-0013` — SKILL.md:98 *(§ 3. HTTPS / TLS)*

> Internet.nl test op een geldig certificaat (keten, geldigheid, hostnaam).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl HTTPS/TLS-test

- **NOT_FOUND** (high) — [https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS](https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS)
  - *De brontekst bevat geen informatie over certificaatvalidatie of internet.nl testmethodiek.*

### `inet-web-0014` — SKILL.md:99 *(§ 3. HTTPS / TLS)*

> OCSP stapling wordt door internet.nl getest als niet-scorende melding.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl HTTPS/TLS-test

- **NOT_FOUND** (high) — [https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS](https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS)
  - *De brontekst bevat geen informatie over OCSP stapling of internet.nl testscores.*

### `inet-web-0016` — SKILL.md:204 *(§ 5. Security headers)*

> Internet.nl test op aanwezigheid van de `Content-Security-Policy` header.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl security headers-test

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *Content-Security-Policy wordt niet apart vermeld. De bron noemt alleen 'Security options' als categorie.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *De claim gaat over de Content-Security-Policy header. RFC 6797 behandelt alleen HSTS.*

### `inet-web-0017` — SKILL.md:205 *(§ 5. Security headers)*

> Internet.nl test op aanwezigheid van de `X-Frame-Options` header.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl security headers-test

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *X-Frame-Options wordt niet vermeld in de bron.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *De claim gaat over de X-Frame-Options header. Buiten scope van RFC 6797.*

### `inet-web-0018` — SKILL.md:206 *(§ 5. Security headers)*

> Internet.nl test op aanwezigheid van de `X-Content-Type-Options` header.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl security headers-test

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *X-Content-Type-Options wordt niet vermeld in de bron.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *De claim gaat over de X-Content-Type-Options header. Buiten scope van RFC 6797.*

### `inet-web-0019` — SKILL.md:207 *(§ 5. Security headers)*

> Internet.nl test op aanwezigheid van de `Referrer-Policy` header.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl security headers-test

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *Referrer-Policy wordt niet vermeld in de bron.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *De claim gaat over de Referrer-Policy header. Buiten scope van RFC 6797.*

### `inet-web-0021` — SKILL.md:243 *(§ 6. security.txt)*

> Internet.nl test of security.txt bereikbaar is op `/.well-known/security.txt` en de verplichte velden `Contact` en `Expires` bevat.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl security.txt-test

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *security.txt en de vereiste velden Contact en Expires worden niet vermeld in de bron.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *De claim gaat over security.txt (RFC 9116) en de vereiste velden daarin. Buiten scope van RFC 6797.*

### `inet-web-0023` — SKILL.md:275 *(§ 7. RPKI)*

> Internet.nl test of een ROA-record aanwezig is voor het IP-adres van de webserver en of de ROA geldig is (valid, niet invalid of unknown).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl RPKI-test

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *ROA-records en RPKI-validatiestatus worden niet op detailniveau beschreven. De bron noemt RPKI slechts als testcategorie.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *RFC 6797 gaat over HSTS; RPKI en ROA-records worden niet behandeld.*

### `inet-web-0029` — reference.md:28 *(§ Aanbevolen cipher suites (NCSC))*

> Voor TLS 1.3 zijn alleen TLS_AES_128_GCM_SHA256, TLS_AES_256_GCM_SHA384 en TLS_CHACHA20_POLY1305_SHA256 beschikbaar als cipher suites.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** TLS 1.3 cipher suites

- **OUT_OF_SCOPE** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron gaat over de internet.nl websitetest in het algemeen, niet over TLS 1.3 cipher suite specificaties.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *RFC 6797 behandelt TLS 1.3 cipher suites niet; de spec dateert van november 2012.*

### `inet-web-0036` — reference.md:46 *(§ Renegotiation en OCSP (NCSC 2025-05))*

> Extended Master Secret (RFC 7627) is een aparte test geworden voor TLS 1.2; ontbreken telt als fout. Voor TLS 1.3 is dit niet van toepassing.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** NCSC TLS Security Guidelines 2025-05 / Internet.nl v1.11.0

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS](https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS)
  - *De brontekst bevat geen inhoud over Extended Master Secret (RFC 7627) of TLS 1.2/1.3 specifieke tests.*
- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden/tls](https://www.forumstandaardisatie.nl/open-standaarden/tls)
  - *Extended Master Secret (RFC 7627) wordt niet vermeld in de brontekst.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7627.txt](https://www.rfc-editor.org/rfc/rfc7627.txt)
  - *De brontekst is RFC 7627 zelf (de technische specificatie van Extended Master Secret). De claim gaat over hoe Internet.nl v1.11.0 / NCSC TLS Security Guidelines 2025-05 EMS als aparte test classificeren en of ontbreken als fout telt. RFC 7627 bevat geen informatie over testclassificaties, scorebeleid of versie-specifieke testkaders van Internet.nl of NCSC. De constatering dat EMS niet van toepassing is op TLS 1.3 staat ook niet in deze RFC (TLS 1.3 bestaat überhaupt niet in dit document uit 2015). OUT_OF_SCOPE zou ook verdedigbaar zijn, maar de bron is niet per se de verkeerde categorie — hij dekt simpelweg de claim niet.*
</details>

### `inet-web-0037` — reference.md:47 *(§ Renegotiation en OCSP (NCSC 2025-05))*

> OCSP stapling wordt niet langer als fout gerekend wanneer het certificaat zelf geen OCSP-endpoint bevat (AIA zonder OCSP URI); in dat geval wordt het als niet-getest gemeld.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** NCSC TLS Security Guidelines 2025-05 / Internet.nl v1.11.0

- **NOT_FOUND** (high) — [https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS](https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS)
  - *De brontekst bevat geen inhoud over OCSP stapling, AIA-extensies of testgedrag bij ontbrekende OCSP URI.*
- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden/tls](https://www.forumstandaardisatie.nl/open-standaarden/tls)
  - *OCSP stapling, AIA, of OCSP URI worden niet behandeld in de brontekst.*

### `inet-web-0041` — reference.md:211 *(§ Content-Security-Policy (CSP))*

> CSP `frame-ancestors` directive vervangt `X-Frame-Options`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Content-Security-Policy

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *CSP frame-ancestors als vervanging van X-Frame-Options wordt niet vermeld in de bron.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *RFC 6797 behandelt Content-Security-Policy en frame-ancestors niet.*

### `inet-web-0043` — reference.md:260 *(§ Hoe RPKI werkt)*

> Een RPKI ROA (Route Origin Authorisation) is een digitaal ondertekende verklaring die een IP-prefix koppelt aan een AS-nummer.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** RPKI

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De definitie van een ROA als digitaal ondertekende verklaring die een IP-prefix koppelt aan een AS-nummer wordt niet vermeld in de bron.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *RFC 6797 behandelt RPKI en ROA niet; de bron gaat uitsluitend over HSTS.*

### `inet-web-0044` — reference.md:264 *(§ Hoe RPKI werkt)*

> RPKI validatiestatus kent drie waarden: `Valid` (BGP-aankondiging komt overeen met een ROA), `Invalid` (conflicteert met een ROA) en `NotFound` (geen ROA gevonden).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** RPKI Route Origin Validation

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De drie RPKI validatiestatussen (Valid, Invalid, NotFound) worden niet vermeld in de bron.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *De bron is RFC 6797, die uitsluitend gaat over HTTP Strict Transport Security (HSTS). RPKI (Resource Public Key Infrastructure) en Route Origin Validation worden nergens in deze bron behandeld.*

## PARTIALLY_GROUNDED — bron ondersteunt deel van de claim (7)

### `inet-web-0001` — SKILL.md:26 *(§ Overzicht)*

> Internet.nl test websites op IPv6, DNSSEC, HTTPS/TLS, HSTS, security headers, security.txt en RPKI.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl websitetest

- **PARTIALLY_SUPPORTED** (medium) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  > After the test is finished, you are directed to a test report. The report contains an overall percentage score and results per test section and per subtest.
  - *De bron noemt IPv6, DNSSEC, HTTPS, Security options en RPKI expliciet als testcategorieën. HSTS als aparte subtest en security.txt worden niet apart benoemd, maar vallen vermoedelijk onder 'Security options'. De specifieke opsomming 'HSTS, security headers, security.txt' staat niet letterlijk in de bron.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *Deze bron is RFC 6797 (HSTS-specificatie). De claim gaat over de internet.nl testtool en welke standaarden daarin getest worden. Dat onderwerp wordt niet behandeld in deze RFC.*

### `inet-web-0004` — SKILL.md:43 *(§ 1. IPv6)*

> Internet.nl test of de webserver bereikbaar is via IPv6.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl IPv6-test

- **PARTIALLY_SUPPORTED** (medium) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  > IPv6 : reachable via modern address?
  - *De bron bevestigt dat bereikbaarheid via IPv6 wordt getest, maar noemt niet expliciet de webserver als specifiek testobject.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *De claim gaat over de IPv6-bereikbaarheidstest van internet.nl. Buiten scope van RFC 6797.*

### `inet-web-0006` — SKILL.md:68 *(§ 2. DNSSEC)*

> Internet.nl test of de DNS-zone is gesigneerd met DNSSEC.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** internet.nl DNSSEC-test

- **PARTIALLY_SUPPORTED** (medium) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  > DNSSEC : domain name signed?
  - *De bron bevestigt dat DNSSEC-ondertekening van het domein wordt getest, maar noemt niet specifiek het testen van de DNS-zone.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *De claim gaat over de DNSSEC-test van internet.nl. RFC 6797 behandelt DNSSEC niet.*

### `inet-web-0015` — SKILL.md:175 *(§ 4. HSTS)*

> Internet.nl test op aanwezigheid van de `Strict-Transport-Security` header en een `max-age` van minimaal 31536000 (1 jaar).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** internet.nl HSTS-test

- **PARTIALLY_SUPPORTED** (medium) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  > The HSTS header field below stipulates that the HSTS Policy is to remain in effect for one year (there are approximately 31536000 seconds in a year), and the policy applies only to the domain of the HSTS Host issuing it: Strict-Transport-Security: max-age=31536000
  - *RFC 6797 bevestigt dat de Strict-Transport-Security header bestaat en dat 31536000 seconden één jaar is, en gebruikt dit als voorbeeldwaarde. De RFC specificeert echter geen minimale max-age waarde — dat is een internetstandaard-testcriterium van internet.nl zelf, niet iets dat RFC 6797 normatief vereist. De aanwezigheid van de header en het max-age-mechanisme worden ondersteund; de eis van 'minimaal 31536000' als testdrempel niet.*
- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *Strict-Transport-Security header en max-age vereisten worden niet vermeld in de bron.*

### `inet-web-0032` — reference.md:37 *(§ Certificaatvereisten)*

> TLS-certificaten vereisen een geldige keten naar een vertrouwde root CA en de hostnaam in Subject Alternative Name (SAN).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** TLS certificaatvereisten

- **PARTIALLY_SUPPORTED** (medium) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  > When connecting to a Known HSTS Host, the UA MUST terminate the connection [...] if there are any errors [...] with the underlying secure transport. For example, this includes any errors found in certificate validity checking [...] as well as via TLS server identity checking [RFC6125].
  - *De bron bevestigt indirect dat certificaatketenvalidatie en host-identiteitscontrole vereist zijn (fouten leiden tot verbindingsafbreking), maar vermeldt Subject Alternative Name (SAN) niet expliciet. De eis over 'geldige keten naar vertrouwde root CA' wordt impliciet ondersteund via Section 8.4, maar SAN-vereiste staat niet in de bron.*
- **OUT_OF_SCOPE** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron gaat over de internet.nl websitetest in het algemeen, niet over certificaatketen- of SAN-vereisten.*

### `inet-web-0038` — reference.md:173 *(§ Preload-lijst)*

> Voor HSTS preloading is een `max-age` van minimaal 31536000 vereist, samen met `includeSubDomains` en `preload` directive.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** HSTS preload-lijst

- **PARTIALLY_SUPPORTED** (medium) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  > The HSTS header field below stipulates that the HSTS Policy is to remain in effect for one year (there are approximately 31536000 seconds in a year): Strict-Transport-Security: max-age=31536000
  - *De bron bevestigt dat max-age=31536000 overeenkomt met één jaar en beschrijft includeSubDomains als optionele directive. Het 'preload' directive wordt echter nergens in RFC 6797 vermeld — dat is een latere toevoeging buiten deze spec. Daardoor is de claim over het preload-vereiste NIET_GEVONDEN in deze bron, maar het max-age-gedeelte en includeSubDomains worden wel ondersteund.*
- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *HSTS preload-vereisten worden niet vermeld in de bron.*

### `inet-web-0042` — reference.md:229 *(§ Verplichte velden)*

> RFC 9116 definieert `Contact` en `Expires` als verplichte velden in security.txt; `Expires` moet in ISO 8601-formaat zijn en maximaal 1 jaar vooruit.

**Type:** reference_claim  ·  **Modaliteit:** MUST  ·  **Scope:** security.txt / RFC 9116

- **PARTIALLY_SUPPORTED** (high) — [https://www.rfc-editor.org/rfc/rfc9116.txt](https://www.rfc-editor.org/rfc/rfc9116.txt)
  > This field MUST always be present in a "security.txt" file. [...] The "Expires" field [...] This field MUST always be present and MUST NOT appear more than once. [...] It is RECOMMENDED that the value of this field be less than a year into the future to avoid staleness.
  - *Contact en Expires als verplichte velden worden volledig ondersteund. Het ISO 8601-formaat voor Expires is ook correct (via RFC 3339 die de Internet-profielen van ISO 8601 definieert). Echter: de claim stelt dat Expires 'maximaal 1 jaar vooruit' MOET zijn, terwijl de RFC dit slechts RECOMMENDS ('It is RECOMMENDED that the value of this field be less than a year into the future'). Dat is een verschil in vereistingsniveau: RECOMMENDED vs. de MUST die de claim impliceert.*

## UNGROUNDED — geen bron ondersteunt de claim (15)

### `inet-web-0009` — SKILL.md:89 *(§ 3. HTTPS / TLS)*

> Internet.nl vereist TLS 1.2 of 1.3 met sterke cipher suites.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** internet.nl HTTPS/TLS-test

- **NOT_FOUND** (high) — [https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS](https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS)
  - *De brontekst bevat alleen een pagina-listing van de NCSC TLS-richtlijnen documenten (PDF links, data, errata). Er staat geen inhoudelijke informatie over internet.nl vereisten of TLS-versies.*

### `inet-web-0012` — SKILL.md:97 *(§ 3. HTTPS / TLS)*

> Internet.nl test op sterke cipher suites; RC4, 3DES, NULL en export ciphers zijn niet toegestaan.

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** internet.nl HTTPS/TLS-test

- **NOT_FOUND** (high) — [https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS](https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS)
  - *De brontekst bevat geen inhoudelijke specificaties over cipher suites of verboden algoritmen.*

### `inet-web-0022` — SKILL.md:245 *(§ 6. security.txt)*

> Digitale ondertekening (PGP) van security.txt is aanbevolen.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** security.txt / RFC 9116

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *PGP-ondertekening van security.txt wordt niet vermeld in de bron.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *De claim gaat over PGP-ondertekening van security.txt conform RFC 9116. Buiten scope van RFC 6797.*

### `inet-web-0024` — SKILL.md:306 *(§ Veelvoorkomende problemen)*

> security.txt heeft `Expires` als verplicht veld; een verlopen datum geeft een fout bij internet.nl.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** internet.nl security.txt-test

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *Expires als verplicht veld voor security.txt wordt niet vermeld in de bron.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *RFC 6797 gaat over HSTS; security.txt en het Expires-veld worden niet behandeld.*

### `inet-web-0025` — reference.md:13 *(§ Aanbevolen cipher suites (NCSC))*

> Het NCSC adviseert TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256, TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384, TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 en TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 als voorkeurs-cipher suites voor TLS 1.2.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** NCSC TLS Security Guidelines / TLS 1.2

- **OUT_OF_SCOPE** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron gaat over de internet.nl websitetest in het algemeen, niet over NCSC TLS Security Guidelines of specifieke cipher suites.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *RFC 6797 specificeert geen cipher suites; NCSC TLS-richtlijnen worden niet behandeld.*

### `inet-web-0026` — reference.md:17 *(§ Aanbevolen cipher suites (NCSC))*

> Het NCSC adviseert TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256 en TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256 als voorkeurs-cipher suites voor TLS 1.2.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** NCSC TLS Security Guidelines / TLS 1.2

- **OUT_OF_SCOPE** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron gaat over de internet.nl websitetest in het algemeen, niet over NCSC TLS Security Guidelines of ChaCha20-gebaseerde cipher suites.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *RFC 6797 specificeert geen cipher suites; ChaCha20-POLY1305 wordt niet vermeld.*

### `inet-web-0027` — reference.md:21 *(§ Aanbevolen cipher suites (NCSC))*

> TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256 en TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256 zijn voldoende cipher suites voor TLS 1.2 (niet voorkeur).

**Type:** normative_requirement  ·  **Modaliteit:** MAY  ·  **Scope:** NCSC TLS Security Guidelines / TLS 1.2

- **OUT_OF_SCOPE** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron gaat over de internet.nl websitetest in het algemeen, niet over NCSC TLS Security Guidelines of CBC-gebaseerde cipher suites.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *RFC 6797 specificeert geen cipher suites of hun classificatie.*

### `inet-web-0028` — reference.md:25 *(§ Aanbevolen cipher suites (NCSC))*

> Cipher suites met RC4, 3DES, NULL, EXPORT, DES, MD5 en TLS_RSA_* zijn niet toegestaan (geen forward secrecy).

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** NCSC TLS Security Guidelines

- **OUT_OF_SCOPE** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron gaat over de internet.nl websitetest in het algemeen, niet over verboden cipher suites of NCSC TLS Security Guidelines.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *RFC 6797 verbiedt geen specifieke cipher suites; dit valt buiten de scope van de bron.*

### `inet-web-0030` — reference.md:35 *(§ Certificaatvereisten)*

> TLS-certificaten vereisen minimaal 2048-bit RSA of 256-bit ECDSA.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** TLS certificaatvereisten

- **OUT_OF_SCOPE** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron gaat over de internet.nl websitetest in het algemeen, niet over minimale sleutellengtes voor TLS-certificaten.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *RFC 6797 stelt geen minimale sleutellengte-eisen voor certificaten.*

### `inet-web-0031` — reference.md:36 *(§ Certificaatvereisten)*

> TLS-certificaten vereisen SHA-256 of hoger als hash-algoritme.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** TLS certificaatvereisten

- **OUT_OF_SCOPE** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De bron gaat over de internet.nl websitetest in het algemeen, niet over hash-algoritme vereisten voor TLS-certificaten.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *RFC 6797 stelt geen hash-algoritme-eisen voor certificaten.*

### `inet-web-0033` — reference.md:44 *(§ Renegotiation en OCSP (NCSC 2025-05))*

> Met de NCSC TLS-richtlijnen van mei 2025 (geïmplementeerd in Internet.nl v1.11.0) is client-initiated renegotiation acceptabel mits de server het aantal renegotiations beperkt tot minder dan 10 per verbinding.

**Type:** normative_requirement  ·  **Modaliteit:** MAY  ·  **Scope:** NCSC TLS Security Guidelines 2025-05 / Internet.nl v1.11.0

- **NOT_FOUND** (high) — [https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS](https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS)
  - *De brontekst is alleen de downloadpagina; de PDF-inhoud van de NCSC TLS-richtlijnen 2025-05 is niet aangeleverd. Er is geen tekst over client-initiated renegotiation beschikbaar.*
- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden/tls](https://www.forumstandaardisatie.nl/open-standaarden/tls)
  - *De brontekst betreft de Forum Standaardisatie pagina voor TLS in het algemeen. Er is geen informatie over client-initiated renegotiation, limieten daarvoor, of specifieke NCSC TLS-richtlijnen van mei 2025 of Internet.nl v1.11.0.*

### `inet-web-0034` — reference.md:44 *(§ Renegotiation en OCSP (NCSC 2025-05))*

> Onbeperkte client renegotiation blijft een fout (DoS-risico) bij internet.nl.

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** NCSC TLS Security Guidelines 2025-05 / Internet.nl v1.11.0

- **NOT_FOUND** (high) — [https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS](https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS)
  - *De brontekst bevat geen inhoudelijke specificaties over renegotiation-limieten of DoS-risico's.*
- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden/tls](https://www.forumstandaardisatie.nl/open-standaarden/tls)
  - *De brontekst bevat geen informatie over client renegotiation of DoS-risico's daarvan bij Internet.nl.*

### `inet-web-0035` — reference.md:45 *(§ Renegotiation en OCSP (NCSC 2025-05))*

> Secure renegotiation (RFC 5746) blijft verplicht.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** NCSC TLS Security Guidelines 2025-05

<details><summary>2x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS](https://www.ncsc.nl/en/transport-layer-security/ICT-beveiligingsrichtlijnen-voor-TLS)
  - *De brontekst bevat geen inhoud over RFC 5746 of secure renegotiation vereisten.*
- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden/tls](https://www.forumstandaardisatie.nl/open-standaarden/tls)
  - *RFC 5746 of secure renegotiation worden niet genoemd in de brontekst.*
- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc5746.txt](https://www.rfc-editor.org/rfc/rfc5746.txt)
  - *De bron is RFC 5746 zelf (de technische specificatie), niet de NCSC TLS Security Guidelines 2025-05. RFC 5746 definieert secure renegotiation maar zegt niets over of de NCSC het verplicht stelt in haar richtlijnen. De claim gaat over een beleids-/richtlijndocument van NCSC, niet over de RFC.*
</details>

### `inet-web-0039` — reference.md:170 *(§ Preload-lijst)*

> Voor opname in de HSTS preload-lijst zijn een geldig TLS-certificaat en redirect van HTTP naar HTTPS op hetzelfde domein vereist.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** HSTS preload-lijst

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *HSTS preload-lijst vereisten worden niet vermeld in de bron.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *RFC 6797 beschrijft de HSTS preload-lijst alleen als concept (Section 12.3) maar stelt geen formele vereisten voor opname, zoals geldig TLS-certificaat of HTTP-naar-HTTPS-redirect op hetzelfde domein.*

### `inet-web-0040` — reference.md:184 *(§ Preload-lijst)*

> Het `preload` directive voor HSTS is onomkeerbaar op korte termijn; alle subdomeinen moeten HTTPS ondersteunen voordat dit wordt ingeschakeld.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** HSTS preload-lijst

- **NOT_FOUND** (high) — [https://internet.nl/test-site/](https://internet.nl/test-site/)
  - *De onomkeerbaarheid van HSTS preload en de subdomein-eis worden niet vermeld in de bron.*
- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc6797.txt](https://www.rfc-editor.org/rfc/rfc6797.txt)
  - *Het 'preload' directive wordt in RFC 6797 niet gedefinieerd. De onomkeerbaarheid van preloading en subdomain-HTTPS-vereiste komen niet voor in deze bron.*

## GROUNDED — minstens één bron ondersteunt de claim (1)

<details>
<summary>Klap uit voor alle GROUNDED claims</summary>

### `inet-web-0020` — SKILL.md:236 *(§ 6. security.txt)*

> security.txt is gestandaardiseerd in RFC 9116 en moet bereikbaar zijn op `/.well-known/security.txt`.

**Type:** reference_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** security.txt / RFC 9116

- **SUPPORTED** (high) — [https://www.rfc-editor.org/rfc/rfc9116.txt](https://www.rfc-editor.org/rfc/rfc9116.txt)
  > For web-based services, organizations MUST place the "security.txt" file under the "/.well-known/" path, e.g., https://example.com/.well-known/security.txt as per [RFC8615] of a domain name or IP address.
  - *RFC 9116 is inderdaad de standaard voor security.txt en verplicht de /.well-known/security.txt locatie voor webdiensten.*

</details>
