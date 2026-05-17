<!-- markdownlint-disable MD052 MD034 MD013 -->
# Audit inet-api — 2026-05-17

> Automatisch gegenereerd door audit-tooling. Niet handmatig bewerken; wijzig SKILL.md / reference.md en regenereer.

## Samenvatting

| Status | Aantal | % |
|--------|--------|---|
| UNSUPPORTED_ASSERTION | 31 | 69% |
| CONTRADICTED | 0 | 0% |
| PARTIALLY_GROUNDED | 8 | 18% |
| UNGROUNDED | 6 | 13% |
| NO_SOURCE | 0 | 0% |
| UNVERIFIABLE | 0 | 0% |
| KNOWN_DISCREPANCY | 0 | 0% |
| GROUNDED | 0 | 0% |

*Geverifieerd met sonnet, 2 calls, $0.1735.*

## UNSUPPORTED_ASSERTION — stellige bewering zonder enige bronsteun (mogelijke hallucinatie) (31)

### `inet-api-0002` — SKILL.md:45 *(§ Toegang verkrijgen)*

> Authenticatie voor de batch API gaat via HTTP Basic Auth.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API - authenticatie

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)
  - *De README noemt de batch API niet en geeft geen informatie over authenticatiemechanismen.*

### `inet-api-0003` — SKILL.md:52 *(§ API-workflow)*

> De batch API werkt met een poll-model: batch indienen (POST) geeft een request-ID, daarna polling (GET) tot status 'done', dan resultaten ophalen als JSON.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API - workflow

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)
  - *Geen informatie over de batch API workflow in de aangeleverde brontekst.*

### `inet-api-0004` — SKILL.md:64 *(§ API-endpoints)*

> Batch indienen (web of mail) gebruikt POST op endpoint `/api/batch/v2/requests`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API - endpoints

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0005` — SKILL.md:65 *(§ API-endpoints)*

> Overzicht van eigen requests opvragen gebruikt GET op `/api/batch/v2/requests`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API - endpoints

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0006` — SKILL.md:66 *(§ API-endpoints)*

> Status opvragen gebruikt GET op `/api/batch/v2/requests/{request_id}`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API - endpoints

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0007` — SKILL.md:67 *(§ API-endpoints)*

> Batch annuleren gebruikt PATCH op `/api/batch/v2/requests/{request_id}`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API - endpoints

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0008` — SKILL.md:68 *(§ API-endpoints)*

> Resultaten ophalen gebruikt GET op `/api/batch/v2/requests/{request_id}/results`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API - endpoints

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0009` — SKILL.md:69 *(§ API-endpoints)*

> Technische resultaten ophalen gebruikt GET op `/api/batch/v2/requests/{request_id}/results_technical`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API - endpoints

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0010` — SKILL.md:70 *(§ API-endpoints)*

> Rapportage-metadata ophalen gebruikt GET op `/api/batch/v2/metadata/report`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API - endpoints

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0011` — SKILL.md:72 *(§ API-endpoints)*

> De base URL van de batch API is `https://batch.internet.nl`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API - endpoints

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0012` — SKILL.md:74 *(§ API-endpoints)*

> Het testtype (`"web"` of `"mail"`) wordt meegegeven in de request body, niet in het URL-pad.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API - request-formaat

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0013` — SKILL.md:75 *(§ API-endpoints)*

> Het `request_id` is een 32-karakter hexadecimale string.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API - request_id formaat

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0014` — SKILL.md:139 *(§ Status opvragen en resultaten ophalen)*

> De mogelijke batch-statussen zijn: `registering`, `running`, `generating`, `done`, `error`, `cancelled`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API - statuswaarden

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0017` — SKILL.md:307 *(§ Verdicts)*

> De mogelijke verdict-waarden per test zijn: `passed`, `warning`, `failed`, `info`, `not_tested`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API - verdict-waarden

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0019` — SKILL.md:390 *(§ Veelvoorkomende problemen)*

> HTTP 429 treedt op als het rate limit bereikt is.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API - foutcodes

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0020` — reference.md:8 *(§ API-versie)*

> De huidige versie van de batch API is v2.

**Type:** version_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API - versie

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0021` — reference.md:23 *(§ Authenticatie)*

> De API gebruikt HTTP Basic Authentication met het formaat `Authorization: Basic base64(gebruikersnaam:wachtwoord)`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API - authenticatie

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0022` — reference.md:58 *(§ Batch indienen)*

> Het veld `name` in de batch request body is niet verplicht, maximaal 255 tekens, en dient voor eigen administratie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API - request-formaat

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0027` — reference.md:68 *(§ Beperkingen)*

> Verwerking per gebruiker is sequentieel (FIFO, 1 actieve batch tegelijk).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API - beperkingen

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0028` — reference.md:70 *(§ Beperkingen)*

> De beperkingen (max domeinen, max requests per week, sequentiële verwerking) zijn gedocumenteerd in de Terms of Use op GitHub.

**Type:** reference_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API - beperkingen

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0029` — reference.md:263 *(§ Foutcodes)*

> HTTP 400 treedt op bij een ongeldige request; de client moet het JSON-formaat en verplichte velden controleren.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API - foutcodes

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0030` — reference.md:264 *(§ Foutcodes)*

> HTTP 401 treedt op bij ongeldige credentials.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API - foutcodes

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0031` — reference.md:266 *(§ Foutcodes)*

> HTTP 404 treedt op als de batch niet gevonden wordt; het request-ID moet gecontroleerd worden.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API - foutcodes

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0032` — reference.md:267 *(§ Foutcodes)*

> HTTP 429 treedt op als het rate limit bereikt is.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API - foutcodes

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0033` — reference.md:381 *(§ TLS-velddetails sinds v1.11.0 (API v2.7.0))*

> De v1.11.0 release implementeert NCSC TLS-richtlijnen 2025-05 en wijzigt enkele TLS-velden in de batch-resultaten (API v2.7.0).

**Type:** version_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API - TLS-veldwijzigingen v1.11.0

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)
  - *De Changelog.md wordt vermeld in de bestandslijst maar de inhoud ervan is niet aangeleverd in de brontekst.*

### `inet-api-0034` — reference.md:387 *(§ TLS-velddetails sinds v1.11.0 (API v2.7.0))*

> Vanaf API v2.7.0 is `web_tls_clientreneg`/`mail_tls_clientreneg` geen boolean meer maar een enum: `not_allowed` (good), `allowed_with_low_limit` (info, < 10 renegotiations), `allowed_with_too_high_limit` (failed).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API - TLS-veldwijzigingen v2.7.0

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0035` — reference.md:388 *(§ TLS-velddetails sinds v1.11.0 (API v2.7.0))*

> Vanaf API v2.7.0 heeft `web_tls_ocsp`/`mail_tls_ocsp` een nieuwe status `not_in_cert` (not_tested) wanneer het certificaat geen OCSP-endpoint bevat; dit wordt niet als fout gerekend.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API - TLS-veldwijzigingen v2.7.0

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0036` — reference.md:389 *(§ TLS-velddetails sinds v1.11.0 (API v2.7.0))*

> Vanaf API v2.7.0 is `web_tls_extended_master_secret`/`mail_tls_extended_master_secret` een nieuw veld (RFC 7627) met statussen: `supported` (good), `not_supported` (failed), `na_no_tls_1_2` (good), `unknown` (not_tested).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API - TLS-veldwijzigingen v2.7.0

- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7627.txt](https://www.rfc-editor.org/rfc/rfc7627.txt)
  - *De bron is RFC 7627 zelf (de technische specificatie van de Extended Master Secret extensie). De claim gaat over de Internet.nl batch API v2.7.0 en de specifieke veldnamen, statussen en versie-introductie daarvan. Die API-documentatie staat niet in deze RFC.*

### `inet-api-0037` — reference.md:390 *(§ TLS-velddetails sinds v1.11.0 (API v2.7.0))*

> Vanaf API v2.7.0 zijn de statussen `not_prescribed` en `not_seclevel` voor `web_tls_cipher_order` vervallen; verkeerde voorkeur of geen voorkeur is nu allebei `bad`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API - TLS-veldwijzigingen v2.7.0

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0038` — reference.md:391 *(§ TLS-velddetails sinds v1.11.0 (API v2.7.0))*

> Vanaf API v2.7.0 is `cert_signature_phase_out` een nieuw veld in TLS-details, naast het bestaande `cert_signature_bad`, met een lijst van certificaat-signature-algoritmes op phase-out niveau (warning).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API - TLS-veldwijzigingen v2.7.0

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0045` — reference.md:389 *(§ TLS-velddetails sinds v1.11.0 (API v2.7.0))*

> Het `extended_master_secret`-veld (RFC 7627) is nieuw in API v2.7.0.

**Type:** reference_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API - TLS-veldwijzigingen v2.7.0

- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7627.txt](https://www.rfc-editor.org/rfc/rfc7627.txt)
  - *De bron is RFC 7627, een IETF-standaard. De claim over wanneer het veld nieuw werd geïntroduceerd in de Internet.nl batch API (v2.7.0) valt buiten het bereik van deze RFC.*

## PARTIALLY_GROUNDED — bron ondersteunt deel van de claim (8)

### `inet-api-0001` — SKILL.md:25 *(§ Overzicht)*

> De internet.nl batch API maakt het mogelijk om meerdere domeinen tegelijk te testen op internetstandaarden.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API - algemeen

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **PARTIALLY_SUPPORTED** (medium) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)
  > Internet.nl is an initiative of the Dutch Internet Standards Platform that helps you to check whether your website, email and internet connection use modern and reliable Internet Standards.
  - *De bron bevestigt dat Internet.nl domeinen test op internetstandaarden, maar de batch API (meerdere domeinen tegelijk) wordt in deze README niet expliciet beschreven.*

### `inet-api-0015` — SKILL.md:317 *(§ Categorieen (webtest))*

> De webtest-resultaten bevatten per domein categorieën: `ipv6`, `dnssec`, `tls`, `appsecpriv`, `rpki`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API - webtest categorieën

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **PARTIALLY_SUPPORTED** (low) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)
  > Currently the following modern internet standards are considered within scope: IPv6 (modern address), DNSSEC (signed domain), HTTPS (secure website connection), website security options (such as security headers), STARTTLS and DANE (secure mail server connection), DMARC+DKIM+SPF (anti-spoofing), and RPKI (secure routing).
  - *De bron noemt IPv6, DNSSEC, HTTPS/TLS, security headers en RPKI als testgebieden, wat de categorieën ipv6, dnssec, tls, appsecpriv en rpki deels ondersteunt. Maar de koppeling aan specifieke batch API-categorienamen staat niet in de bron.*

### `inet-api-0016` — SKILL.md:327 *(§ Categorieen (mailtest))*

> De mailtest-resultaten bevatten per domein categorieën: `ipv6`, `dnssec`, `auth`, `tls`, `rpki`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API - mailtest categorieën

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **PARTIALLY_SUPPORTED** (low) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)
  > Currently the following modern internet standards are considered within scope: IPv6 (modern address), DNSSEC (signed domain), STARTTLS and DANE (secure mail server connection), DMARC+DKIM+SPF (anti-spoofing), and RPKI (secure routing).
  - *De bron noemt de standaarden die overeenkomen met de mailtest-categorieën ipv6, dnssec, auth (SPF/DKIM/DMARC), tls en rpki, maar koppelt ze niet expliciet aan batch API-categorienamen.*

### `inet-api-0040` — SKILL.md:319 *(§ Categorieen (webtest))*

> De webtest categorie `ipv6` test IPv6-bereikbaarheid (AAAA-records, nameservers).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API - webtest categorieën

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **PARTIALLY_SUPPORTED** (low) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)
  > Currently the following modern internet standards are considered within scope: IPv6 (modern address), DNSSEC (signed domain)...
  - *De bron noemt IPv6 als testgebied maar vermeldt AAAA-records of nameservers niet expliciet. De koppeling aan de batch API categorie ipv6 staat niet in de bron.*

### `inet-api-0041` — SKILL.md:322 *(§ Categorieen (webtest))*

> De webtest categorie `appsecpriv` test security headers en security.txt.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API - webtest categorieën

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **PARTIALLY_SUPPORTED** (low) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)
  > Currently the following modern internet standards are considered within scope: ... HTTPS (secure website connection), website security options (such as security headers)...
  - *Security headers worden als testgebied bevestigd, maar security.txt en de specifieke categorienaam appsecpriv staan niet in de bron.*

### `inet-api-0042` — SKILL.md:331 *(§ Categorieen (mailtest))*

> De mailtest categorie `auth` test SPF, DKIM en DMARC.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API - mailtest categorieën

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **PARTIALLY_SUPPORTED** (low) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)
  > Currently the following modern internet standards are considered within scope: ... DMARC+DKIM+SPF (anti-spoofing)...
  - *SPF, DKIM en DMARC worden bevestigd als testgebied. De koppeling aan de batch API categorienaam auth staat niet in de bron.*

### `inet-api-0043` — SKILL.md:332 *(§ Categorieen (mailtest))*

> De mailtest categorie `tls` test STARTTLS, DANE en het certificaat.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API - mailtest categorieën

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **PARTIALLY_SUPPORTED** (low) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)
  > Currently the following modern internet standards are considered within scope: ... STARTTLS and DANE (secure mail server connection)...
  - *STARTTLS en DANE worden bevestigd. Het certificaat als onderdeel van de tls-categorie staat niet expliciet in de bron. De categorienaam tls staat niet in de bron.*

### `inet-api-0044` — SKILL.md:323 *(§ Categorieen (webtest))*

> De webtest categorie `rpki` test RPKI Route Origin Validation.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API - webtest categorieën

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **PARTIALLY_SUPPORTED** (low) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)
  > Currently the following modern internet standards are considered within scope: ... RPKI (secure routing).
  - *RPKI wordt bevestigd als testgebied. Route Origin Validation als specifieke term en de koppeling aan de batch API categorienaam rpki staan niet in de bron.*

## UNGROUNDED — geen bron ondersteunt de claim (6)

### `inet-api-0018` — SKILL.md:393 *(§ Veelvoorkomende problemen)*

> Het maximale aantal domeinen per batch is 5.000.

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** Internet.nl batch API - beperkingen

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0023` — reference.md:59 *(§ Batch indienen)*

> Het veld `type` in de batch request body is verplicht en accepteert de waarden `"web"` of `"mail"`.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Internet.nl batch API - request-formaat

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0024` — reference.md:60 *(§ Batch indienen)*

> Het veld `domains` in de batch request body is verplicht en bevat een array van te testen domeinen.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Internet.nl batch API - request-formaat

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0025` — reference.md:66 *(§ Beperkingen)*

> Het maximale aantal domeinen per batch is 5.000.

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** Internet.nl batch API - beperkingen

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0026` — reference.md:67 *(§ Beperkingen)*

> Het maximale aantal batch requests per week is 2.

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** Internet.nl batch API - beperkingen

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0039` — reference.md:393 *(§ TLS-velddetails sinds v1.11.0 (API v2.7.0))*

> Een client die `clientreneg` als boolean parseert, breekt op API v2.7.0; de parser moet worden aangepast op string-enum.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Internet.nl batch API - migratie v2.7.0

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)
