# Internet - Claude Code Plugin

[![EUPL-1.2](https://img.shields.io/badge/licentie-EUPL--1.2-blue.svg)](LICENSE)
[![skills](https://img.shields.io/badge/skills-5-green.svg)](#skills)

[Claude Code](https://docs.anthropic.com/en/docs/claude-code) plugin voor moderne internetstandaarden. Test en implementeer compliance met standaarden die getest worden via [internet.nl](https://internet.nl): webstandaarden, mailstandaarden, de batch API en implementatiegidsen.

> **CONCEPT** — Deze plugin is in ontwikkeling en is geen officieel product van internet.nl. De officiële standaarden zijn altijd leidend. Zie de [verantwoording](https://github.com/developer-overheid-nl/skills-marketplace/blob/main/docs/verantwoording.md) en [disclaimer](https://github.com/developer-overheid-nl/skills-marketplace/blob/main/DISCLAIMER.md) voor meer informatie.

## Installeren

```bash
# Via de overheid-plugins marketplace (aanbevolen)
claude plugin marketplace add developer-overheid-nl/skills-marketplace
claude plugin install internet-nl@overheid-plugins

# Per sessie
git clone https://github.com/developer-overheid-nl/skills-internet.git
claude --plugin-dir ./skills-internet
```

## Skills

| Skill | Beschrijving |
|-------|-------------|
| `/inet` | Overzicht internetstandaarden, routing naar sub-skills |
| `/inet-web` | Webstandaarden: HTTPS, TLS, DNSSEC, IPv6, RPKI, security headers, security.txt |
| `/inet-mail` | Mailstandaarden: DMARC, DKIM, SPF, STARTTLS, DANE |
| `/inet-api` | Internet.nl batch API: authenticatie, bulk scans, resultaten |
| `/inet-toolbox` | Stap-voor-stap implementatiegidsen uit de toolbox-wiki |

## Voorbeeldvragen

- "Hoe test ik mijn website op internet.nl?" -> `/inet-web`
- "Hoe configureer ik DMARC voor mijn domein?" -> `/inet-mail`
- "Hoe scan ik 100 domeinen via de API?" -> `/inet-api`
- "Hoe stel ik DANE in voor mijn mailserver?" -> `/inet-toolbox`

## Bronnen

De skills zijn gebaseerd op:
- [internetstandards/Internet.nl](https://github.com/internetstandards/Internet.nl) — test suite
- [internetstandards/Internet.nl-API-docs](https://github.com/internetstandards/Internet.nl-API-docs) — batch API
- [internetstandards/toolbox-wiki](https://github.com/internetstandards/toolbox-wiki) — implementatiegidsen
- [internet.nl](https://internet.nl) — testcriteria per standaard
- [Forum Standaardisatie](https://www.forumstandaardisatie.nl) — status per standaard op de lijst

## Onderdeel van

Deze plugin is onderdeel van de [skills-marketplace](https://github.com/developer-overheid-nl/skills-marketplace) marketplace.

## Disclaimer

**Deze plugin is geen officieel product van [internet.nl](https://internet.nl).** Het is een experimenteel project van [developer.overheid.nl](https://developer.overheid.nl), gebaseerd op publiek beschikbare standaarden en documentatie. De skills zijn informatieve samenvattingen — **niet** de officiële standaarden zelf. De definities op [Forum Standaardisatie](https://www.forumstandaardisatie.nl/open-standaarden) en [internet.nl](https://internet.nl) zijn altijd leidend. Overheidsorganisaties die generatieve AI inzetten dienen te voldoen aan het [Overheidsbreed standpunt voor de inzet van generatieve AI](https://open.overheid.nl/documenten/bc03ce31-0cf1-4946-9c94-e934a62ebe73/file). Zie [DISCLAIMER.md](DISCLAIMER.md) voor de volledige disclaimer.

---

## Licentie

[EUPL-1.2](LICENSE) - European Union Public Licence
