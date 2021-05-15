# Ruokalistageneraattori

Sovelluksen avulla käyttäjät voivat generoida itselleen valmiita ruokalistoja helpottamaan arjen ateriasuunnittelua.

Sovellus on toteutettu Helsingin Yliopiston Tietojenkäsittelytieteiden osaston, kurssin [Ohjelmistotekniikka](https://ohjelmistotekniikka-hy.github.io/) kurssityönä loppukeväästä 2021.
Idea sovellukseen syntyi sattumalta, kun kurssisivulla ehdotetut ideat eivät herättäneet tarpeeksi kiinnostusta ja kaupassa käydessä herää aina se iänikuinen kysymys siitä, että mikä olisi viikon menu. Sovellus siis ratkaisee olemassaolevan arjen ongelman.

## Python-versio

Sovellusta on kehitetty ja sovelluksen toimintaa testattu Pythonin versiolla `3.6.0`. Muiden versioiden toimivuudesta ei välttämättä ole takeita, varsinkaan vanhempien.

## Releaset:

- [Viikko5](https://github.com/P3Xu/ot-harjoitustyo/releases/tag/viikko5)
- [Viikko6](https://github.com/P3Xu/ot-harjoitustyo/releases/tag/viikko6)
- [v1.0](https://github.com/P3Xu/ot-harjoitustyo/releases/tag/v1.0)

## Dokumentaatio

- [Arkkitehtuurikuvaus](https://github.com/P3Xu/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
- [Käyttöohje](https://github.com/P3Xu/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)
- [Testausraportti](https://github.com/P3Xu/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md)
- [Työaikakirjanpito](https://github.com/P3Xu/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
- [Vaatimusmäärittely](https://github.com/P3Xu/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

## Asennus

Sovellus käyttää [Poetrya](https://python-poetry.org/docs/) riippuvuuksien hallintaan.

Ensiksi täytyy asentaa riippuvuudet komennolla:
```shell
poetry install
```

Tämän jälkeen projekti täytyy alustaa komennolla:
```shell
poetry run invoke build
```

Näiden toimenpiteiden jälkeen sovelluksen voi käynnistää komennolla:
```shell
poetry run invoke start
```

Testit voi suorittaa komennolla:
```shell
poetry run invoke test
```

Testikattavuusraportin puolestaan saa ulos (ilmestyy htmlcov -nimiseen hakemistoon) komennolla:
```shell
poetry run invoke coverage-report
```

Pylintin voi ajaa kommennolla:
```shell
poetry run invoke lint
```

## Lähteet

Sovelluksen kehityksessä ja suunnittelussa on käytetty materiaalina paljon erinäisten Python- ja Tkinter-dokumentaatioiden lisäksi kurssin [referenssiprojektia](https://github.com/ohjelmistotekniikka-hy/python-todo-app) sekä virallista [kurssisivua](https://ohjelmistotekniikka-hy.github.io/). Googlea ja Stack Overflowta toki unohtamatta. 
