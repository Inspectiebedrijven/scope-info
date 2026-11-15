# Inspectie-naslag

Naslagwerk over gecertificeerde inspecties van elektrische installaties, zonnestroominstallaties, en elektrische arbeidsmiddelen in Nederland: SCIOS Scope 8, Scope 9, Scope 10 en Scope 12.

Deze repository bevat checklists, een beslisboom, een begrippenlijst en overzichten van termijnen, als Markdown en als CSV of JSON. De bestanden zijn afgeleid van vier informatiesites en vatten samen; de volledige uitleg, met bronnen, staat op de sites zelf:

| Onderwerp | Informatiesite | Map |
|---|---|---|
| SCIOS Scope 8: elektrische installaties (NEN 3140) | [scope8info.nl](https://scope8info.nl) | [scope-8](scope-8/) |
| SCIOS Scope 9: elektrische arbeidsmiddelen | [scope9info.nl](https://scope9info.nl) | [scope-9](scope-9/) |
| SCIOS Scope 10: brandrisico van elektrisch materieel (NTA 8220) | [scope10info.nl](https://scope10info.nl) | [scope-10](scope-10/) |
| SCIOS Scope 12: zonnestroominstallaties | [scope12info.nl](https://scope12info.nl) | [scope-12](scope-12/) |

## Wat u hier vindt

**Algemeen** (over alle onderwerpen heen)

- [Welke inspectie heb ik nodig?](algemeen/welke-inspectie-heb-ik-nodig.md): beslisboom, ook als [JSON](algemeen/beslisboom.json)
- [Termijnen en frequenties](algemeen/termijnen-en-frequenties.md), ook als [CSV](algemeen/termijnen.csv)
- [Begrippenlijst](algemeen/begrippenlijst.md), ook als [CSV](algemeen/begrippen.csv)
- [Classificatie van constateringen](algemeen/classificatie-constateringen.md): rood, oranje, geel en blauw
- [Overzicht van de SCIOS-scopes](algemeen/scios-scopes.csv) (CSV)

**Per onderwerp**

- Scope 10: [kerngegevens](scope-10/README.md), [checklist voorbereiding](scope-10/checklist-voorbereiding.md), [checklist na de inspectie](scope-10/checklist-na-de-inspectie.md), [eisen van verzekeraars](scope-10/eisen-verzekeraars.md)
- Scope 12: [kerngegevens](scope-12/README.md), [checklist voorbereiding en documenten](scope-12/checklist-voorbereiding.md), [checklist na de inspectie](scope-12/checklist-na-de-inspectie.md), [eisen van verzekeraars](scope-12/eisen-verzekeraars.md)
- Scope 8: [kerngegevens](scope-8/README.md), [checklist voorbereiding](scope-8/checklist-voorbereiding.md)
- Scope 9: [kerngegevens](scope-9/README.md), [checklist voorbereiding](scope-9/checklist-voorbereiding.md), [keuringen per arbeidsmiddel](scope-9/keuringen-per-arbeidsmiddel.md)

## Hoe u deze gegevens moet lezen

- **Peildatum.** De bestanden zijn afgeleid van de informatiesites zoals die er op 15 november 2026 stonden. Regels, termijnen en prijzen veranderen; de sites worden vaker bijgewerkt dan deze repository. Bij verschil is de site leidend.
- **Bron per gegeven.** Elk bestand, en in de CSV-bestanden elke regel, noemt de pagina op de informatiesite waar het gegeven vandaan komt en waar de volledige uitleg staat. Welke bronpagina's bij welk bestand horen, staat in [bronnen.csv](bronnen.csv).
- **Geen officiële regels.** Dit is een samenvatting. Voor de officiële regels gelden de SCIOS-certificatieregeling, de normen (zoals NTA 8220, NEN 3140 en NEN 1010) en de wetgeving. Voor wat een verzekeraar eist, is het polisblad leidend.
- **Geen advies.** Aan deze gegevens kunnen geen rechten worden ontleend. Raadpleeg voor uw situatie uw verzekeraar, het bevoegd gezag of een gecertificeerd inspectiebedrijf.

## Doel en afzender

Het doel van deze repository is om informatie over deze inspecties zo transparant en onafhankelijk mogelijk aan te bieden.

De repository wordt uitgegeven door CSIB (Coöperatie Samenwerkende InspectieBedrijven U.A.), met hulp van InspectieDienst Nederland als gecertificeerd inspectiebedrijf. De inhoud is informatief en beveelt geen inspectiebedrijf aan.

## Wijzigingen voorstellen

Iedereen mag wijzigingen voorstellen: een fout, een verouderde regel of een aanvulling. Dat kan via een issue of een pull request in deze repository, of via het contactformulier van de betreffende informatiesite, bijvoorbeeld [scope10info.nl/contact](https://scope10info.nl/contact). Elk voorstel wordt onafhankelijk beoordeeld. Noem bij een voorstel waar mogelijk de bron waarop het steunt.

## Licentie en bronvermelding

De inhoud van deze repository is beschikbaar onder de licentie [Creative Commons Naamsvermelding 4.0 Internationaal (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.nl). U mag de inhoud delen en bewerken, ook commercieel, mits u de bron vermeldt. Zie [LICENTIE.md](LICENTIE.md) en de volledige tekst in [LICENSE](LICENSE).

Vermeld als bron de informatiesite waar het gegeven vandaan komt, met een link naar de bronpagina. Voorbeeld:

> Bron: Scope10Info.nl, "Hoe vaak moet een Scope 10 keuring uitgevoerd worden?", https://scope10info.nl/wat-is-scope-10/hoe-vaak-scope-10 (CC BY 4.0)

SCIOS is een geregistreerde merknaam van Stichting SCIOS. Namen van normen, verzekeraars en andere organisaties worden alleen genoemd om te verwijzen naar wat zij publiceren.
