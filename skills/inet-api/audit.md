<!-- markdownlint-disable MD052 MD034 MD013 -->
# Audit inet-api — 2026-05-17

> Automatisch gegenereerd door audit-tooling. Niet handmatig bewerken; wijzig SKILL.md / reference.md en regenereer.

## Samenvatting

| Status | Aantal | % |
|--------|--------|---|
| UNSUPPORTED_ASSERTION | 34 | 83% |
| CONTRADICTED | 0 | 0% |
| PARTIALLY_GROUNDED | 1 | 2% |
| UNGROUNDED | 6 | 15% |
| NO_SOURCE | 0 | 0% |
| UNVERIFIABLE | 0 | 0% |
| KNOWN_DISCREPANCY | 0 | 0% |
| GROUNDED | 0 | 0% |

*Geverifieerd met sonnet, 2 calls, $0.1587.*

## UNSUPPORTED_ASSERTION — stellige bewering zonder enige bronsteun (mogelijke hallucinatie) (34)

### `inet-api-0002` — SKILL.md:45 *(§ Toegang verkrijgen)*

> Authenticatie bij de internet.nl batch API gaat via HTTP Basic Auth.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API authenticatie

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)
  - *De aangeleverde brontekst is de GitHub README en bevat geen informatie over API-authenticatie.*

### `inet-api-0003` — SKILL.md:52 *(§ API-workflow)*

> De batch API werkt met een poll-model: batch indienen (POST) geeft een request-ID, daarna pollen op status tot 'done', dan resultaten ophalen.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API workflow

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)
  - *Geen informatie over batch API workflow in de aangeleverde brontekst.*

### `inet-api-0004` — SKILL.md:64 *(§ API-endpoints)*

> Batch indienen (web of mail) gaat via POST naar /api/batch/v2/requests.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API endpoints

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0005` — SKILL.md:65 *(§ API-endpoints)*

> Overzicht van eigen requests is opvraagbaar via GET /api/batch/v2/requests.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API endpoints

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0006` — SKILL.md:66 *(§ API-endpoints)*

> Batchstatus opvragen gaat via GET /api/batch/v2/requests/{request_id}.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API endpoints

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0007` — SKILL.md:67 *(§ API-endpoints)*

> Een batch annuleren gaat via PATCH /api/batch/v2/requests/{request_id}.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API endpoints

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0008` — SKILL.md:68 *(§ API-endpoints)*

> Resultaten ophalen gaat via GET /api/batch/v2/requests/{request_id}/results.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API endpoints

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0009` — SKILL.md:69 *(§ API-endpoints)*

> Technische resultaten zijn opvraagbaar via GET /api/batch/v2/requests/{request_id}/results_technical.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API endpoints

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0010` — SKILL.md:70 *(§ API-endpoints)*

> Rapportage-metadata is opvraagbaar via GET /api/batch/v2/metadata/report.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API endpoints

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0011` — SKILL.md:72 *(§ API-endpoints)*

> De base URL van de internet.nl batch API is https://batch.internet.nl.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API endpoints

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0013` — SKILL.md:75 *(§ API-endpoints)*

> Het request_id is een 32-karakter hexadecimale string.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API request_id formaat

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0014` — SKILL.md:99 *(§ Batch indienen)*

> Een batch submit response bevat de velden request_id, request_type en status ('registering').

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API response-formaat

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0015` — SKILL.md:139 *(§ Status opvragen en resultaten ophalen)*

> Mogelijke batchstatussen zijn: registering, running, generating, done, error, cancelled.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API statuswaarden

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0016` — SKILL.md:321 *(§ Categorieen (webtest))*

> De categorie 'appsecpriv' (webtest) omvat security headers en security.txt.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API webtest categorieën

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0017` — SKILL.md:318 *(§ Categorieen (webtest))*

> De webtest categorieën zijn: ipv6, dnssec, tls, appsecpriv en rpki.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API webtest categorieën

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0018` — SKILL.md:327 *(§ Categorieen (mailtest))*

> De mailtest categorieën zijn: ipv6, dnssec, auth (SPF, DKIM, DMARC), tls (STARTTLS, DANE, certificaat) en rpki.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API mailtest categorieën

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0019` — SKILL.md:393 *(§ Veelvoorkomende problemen)*

> Bij grote batches (te veel domeinen tegelijk) kan een timeout optreden; de oplossing is splitsen in kleinere batches van maximaal 5.000 domeinen per batch.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API beperkingen

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0020` — SKILL.md:390 *(§ Veelvoorkomende problemen)*

> HTTP 429 bij de batch API betekent dat de rate limit bereikt is.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API foutcodes

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0021` — reference.md:8 *(§ API-versie)*

> De huidige versie van de internet.nl batch API is v2.

**Type:** version_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API versie

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0022` — reference.md:23 *(§ Authenticatie)*

> De API gebruikt HTTP Basic Authentication via de Authorization-header: Basic base64(gebruikersnaam:wachtwoord).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API authenticatie

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0025` — reference.md:58 *(§ Batch indienen)*

> Het veld 'name' in de batch request body is niet verplicht, heeft een maximum van 255 tekens en is bedoeld voor eigen administratie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API request-formaat

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0028` — reference.md:68 *(§ Beperkingen)*

> Verwerking per gebruiker is sequentieel (FIFO), met 1 actieve batch tegelijk.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API beperkingen

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0029` — reference.md:70 *(§ Beperkingen)*

> De beperkingen (max domeinen, max requests per week, FIFO) zijn vastgelegd in de Terms of Use op GitHub.

**Type:** reference_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API beperkingen

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0030` — reference.md:263 *(§ Foutcodes)*

> HTTP 400 bij de batch API betekent een ongeldige request; de actie is het controleren van het JSON-formaat en verplichte velden.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API foutcodes

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0031` — reference.md:264 *(§ Foutcodes)*

> HTTP 401 bij de batch API betekent niet geautoriseerd; de actie is het controleren van credentials.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API foutcodes

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0032` — reference.md:266 *(§ Foutcodes)*

> HTTP 404 bij de batch API betekent dat de batch niet gevonden is; de actie is het controleren van het request-ID.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API foutcodes

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0033` — reference.md:267 *(§ Foutcodes)*

> HTTP 429 bij de batch API betekent dat de rate limit bereikt is.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API foutcodes

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0034` — reference.md:387 *(§ TLS-velddetails sinds v1.11.0 (API v2.7.0))*

> Vanaf v1.11.0 (API v2.7.0) is het veld 'clientreneg' gewijzigd van boolean naar een string-enum: 'not_allowed' (good), 'allowed_with_low_limit' (info), 'allowed_with_too_high_limit' (failed).

**Type:** version_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API TLS-velden v1.11.0

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0035` — reference.md:388 *(§ TLS-velddetails sinds v1.11.0 (API v2.7.0))*

> Vanaf v1.11.0 (API v2.7.0) heeft het veld 'web_tls_ocsp'/'mail_tls_ocsp' een nieuwe statuswaarde 'not_in_cert' (not_tested) wanneer het certificaat geen OCSP-endpoint bevat; dit wordt niet als fout gerekend.

**Type:** version_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API TLS-velden v1.11.0

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0036` — reference.md:389 *(§ TLS-velddetails sinds v1.11.0 (API v2.7.0))*

> Vanaf v1.11.0 (API v2.7.0) is het nieuwe veld 'web_tls_extended_master_secret'/'mail_tls_extended_master_secret' toegevoegd (RFC 7627) met statussen: 'supported' (good), 'not_supported' (failed), 'na_no_tls_1_2' (good), 'unknown' (not_tested).

**Type:** version_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API TLS-velden v1.11.0

- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc7627.txt](https://www.rfc-editor.org/rfc/rfc7627.txt)
  - *De bron is RFC 7627 zelf (de technische specificatie van de TLS Extended Master Secret extension). De claim gaat over de Internet.nl batch API v1.11.0/v2.7.0 en de specifieke veldnamen, statussen en versienummering in die API. Dat is implementatie-specifieke API-documentatie die niet in deze RFC staat.*

### `inet-api-0037` — reference.md:390 *(§ TLS-velddetails sinds v1.11.0 (API v2.7.0))*

> Vanaf v1.11.0 (API v2.7.0) zijn de statussen 'not_prescribed' en 'not_seclevel' voor 'web_tls_cipher_order' vervallen; verkeerde voorkeur of geen voorkeur is nu allebei 'bad'.

**Type:** version_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API TLS-velden v1.11.0

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0038` — reference.md:391 *(§ TLS-velddetails sinds v1.11.0 (API v2.7.0))*

> Vanaf v1.11.0 (API v2.7.0) is het nieuwe veld 'cert_signature_phase_out' toegevoegd in TLS-details, naast 'cert_signature_bad', met een lijst van certificaat-signature-algoritmes op phase-out niveau (warning).

**Type:** version_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API TLS-velden v1.11.0

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0040` — SKILL.md:308 *(§ Verdicts)*

> De verdict-waarden in batch resultaten zijn: 'passed', 'warning', 'failed', 'info', 'not_tested'.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API resultatenstructuur

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0041` — reference.md:383 *(§ TLS-velddetails sinds v1.11.0 (API v2.7.0))*

> De v1.11.0 release is gebaseerd op NCSC TLS-richtlijnen 2025-05.

**Type:** version_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API versie v1.11.0

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)
  - *De aangeleverde brontekst vermeldt wel release 1.11.0 als 'Latest Apr 21, 2026' in de releases-lijst, maar bevat geen inhoudelijke informatie over NCSC TLS-richtlijnen 2025-05 als basis voor die release.*

## PARTIALLY_GROUNDED — bron ondersteunt deel van de claim (1)

### `inet-api-0001` — SKILL.md:25 *(§ Overzicht)*

> De internet.nl batch API maakt het mogelijk om meerdere domeinen tegelijk te testen op internetstandaarden.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Internet.nl batch API algemeen

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **PARTIALLY_SUPPORTED** (medium) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)
  > Internet.nl is an initiative of the Dutch Internet Standards Platform that helps you to check whether your website, email and internet connection use modern and reliable Internet Standards.
  - *De bron bevestigt dat Internet.nl domeinen test op internetstandaarden, maar de batch API als specifieke functionaliteit wordt niet vermeld in de aangeleverde README-tekst.*

## UNGROUNDED — geen bron ondersteunt de claim (6)

### `inet-api-0012` — SKILL.md:74 *(§ API-endpoints)*

> Het testtype ('web' of 'mail') wordt meegegeven in de request body, niet in het URL-pad.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Internet.nl batch API request-formaat

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0023` — reference.md:59 *(§ Batch indienen)*

> Het veld 'type' in de batch request body is verplicht en accepteert de waarden 'web' of 'mail'.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Internet.nl batch API request-formaat

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0024` — reference.md:60 *(§ Batch indienen)*

> Het veld 'domains' in de batch request body is verplicht en is een array van strings.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Internet.nl batch API request-formaat

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0026` — reference.md:66 *(§ Beperkingen)*

> Het maximum aantal domeinen per batch is 5.000.

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** Internet.nl batch API beperkingen

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0027` — reference.md:67 *(§ Beperkingen)*

> Het maximum aantal batch requests per week is 2.

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** Internet.nl batch API beperkingen

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)

### `inet-api-0039` — reference.md:393 *(§ TLS-velddetails sinds v1.11.0 (API v2.7.0))*

> Een client die 'clientreneg' als boolean parseert, breekt op API v2.7.0; de parser moet worden aangepast op string-enum.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Internet.nl batch API migratie v2.7.0

- **SOURCE_UNAVAILABLE** (high) — [https://internet.nl/api/](https://internet.nl/api/)
  - *Bron status: unreachable*
- **NOT_FOUND** (high) — [https://github.com/internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl)
