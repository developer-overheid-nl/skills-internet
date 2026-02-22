# Internet.nl Plugin

[![EUPL-1.2](https://img.shields.io/badge/licentie-EUPL--1.2-blue.svg)](LICENSE)
[![skills](https://img.shields.io/badge/skills-5-green.svg)](#skills)

[Claude Code](https://docs.anthropic.com/en/docs/claude-code) plugin voor het testen en implementeren van moderne internetstandaarden conform [internet.nl](https://internet.nl). Bevat skills voor webstandaarden, mailstandaarden, de batch API en implementatiegidsen.

## Installeren

```bash
# Via de overheid-plugins marketplace (aanbevolen)
claude plugin marketplace add MinBZK/overheid-claude-plugins
claude plugin install internet-nl@overheid-plugins

# Per sessie
git clone https://github.com/MinBZK/internet-nl-plugin.git
claude --plugin-dir ./internet-nl-plugin
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

Deze plugin is onderdeel van de [overheid-claude-plugins](https://github.com/MinBZK/overheid-claude-plugins) marketplace.

## Licentie

[EUPL-1.2](LICENSE) - European Union Public Licence
