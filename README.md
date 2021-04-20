# Ruokalistageneraattori

Sovelluksen avulla käyttäjät voivat generoida itselleen valmiita ruokalistoja helpottamaan arjen ateriasuunnittelua.

## Dokumentaatio

- [Työaikakirjanpito](https://github.com/P3Xu/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
- [Vaatimusmäärittely](https://github.com/P3Xu/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](https://github.com/P3Xu/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

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
- invoke saattaa rikkoa joitain rivinvaihtoja välillä, ja backspace ei toimi, mutta korjaantunee graafisen käyttöliittymän myötä.

Testit voi suorittaa komennolla:
```shell
poetry run invoke test
```

Testikattavuusraportin puolestaan saa ulos (ilmestyy htmlcov -nimiseen hakemistoon) komennolla:
```shell
poetry run coverage-report
```
