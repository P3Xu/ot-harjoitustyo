# Ruokalistageneraattori

Sovelluksen avulla käyttäjät voivat generoida itselleen valmiita ruokalistoja helpottamaan arjen ateriasuunnittelua.

<<<<<<< HEAD
=======
## Releaset:

- [Viikko5](https://github.com/P3Xu/ot-harjoitustyo/releases/tag/viikko5)
- [Viikko6](https://github.com/P3Xu/ot-harjoitustyo/releases/tag/viikko6)

>>>>>>> caa1d46... Updated README
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

Vanhan tekstikäyttöliittymän saa käyntiin komennolla:
```shell
poetry run invoke start-cli
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

