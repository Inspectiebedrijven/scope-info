# Verkeerscijfers van deze repository

Deze branch bevat alleen de bezoekcijfers van de repository zelf. Het naslagwerk staat op de branch [main](https://github.com/Inspectiebedrijven/scope-info).

GitHub bewaart verkeerscijfers 14 dagen. Een workflow legt ze daarom elke maandag vast:

| Bestand | Inhoud |
|---|---|
| [per-dag.csv](per-dag.csv) | Per dag: weergaven, unieke bezoekers, clones en unieke clones |
| [verwijzers.csv](verwijzers.csv) | Per ophaaldatum: vanaf welke sites bezoekers kwamen in de 14 dagen daarvoor |
| [paden.csv](paden.csv) | Per ophaaldatum: de meest bekeken pagina's in de 14 dagen daarvoor |

De cijfers komen uit de GitHub-API voor verkeersgegevens. De lopende dag is bij het ophalen nog niet compleet en wordt bij de volgende run aangevuld.
