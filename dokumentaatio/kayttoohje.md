# Käyttöohje

Lataa projektin viimeisin [versio](https://github.com/P3Xu/ot-harjoitustyo/releases/tag/viikko6) valitsemalla joko _Source code(zip)_ tai _Source code(tar.gz)_.

## Konfigurointi

Tallennukseen käytettävän tietokantatiedoston nimeä voi halutessaan muuttaa _.env_-tiedostossa. Tiedosto luodaan hakemistoon _data_ automaattisesti, mikäli hakemistossa ei vielä sen nimistä tiedostoa ole. 

## Ohjelman käynnistäminen

Ennen ohjelman käynnistämistä tulee asentaa ohjelman riippuvuudet komennolla:

```shell
poetry install
```

Lisäksi tulee suorittaa projektin alustus komennolla:

```shell
poetry run invoke build
```

Näiden toimenpiteiden jälkeen sovelluksen voi käynnistää komennolla:

```shell
poetry run invoke start
```

## Kirjautuminen

Sovelluksen ensimmäinen näkymä on kirjautumisnäkymä. 
Sovellukseen kirjaudutaan syöttämällä käyttäjätunnus ja salasana, jonka jälkeen voi painaa "Kirjaudu sisään" -painiketta.

## Käyttäjän lisääminen

Kirjautumisnäkymästä pääsee luomaan uutta käyttäjää klikkaamalla "Luo uusi käyttäjä" -painiketta. Uudelle käyttäjälle määritellään käyttäjänimi sekä salasana, jonka jälkeen painetaan "Luo käyttäjä" -painiketta. Sovellus palaa kirjautumisnäkymään.

## Sovelluksen käyttäminen

Kirjautumisen jälkeen näkyy viikon ruokalista, mikäli sellainen on jo luotu. Lisäksi on painikkeet, joista voi luoda uuden ruokalistan, hallita ruoka- ja raaka-ainekirjastoa tai lopettaa sovelluksen käytön. "Lopeta" -painike sulkee sovelluksen.

## Kirjastojen hallinta

Kirjastojen hallinnassa voi tarkastella jo lisättyjä ruokalajeja tai raaka-aineita scrollaamalla niiden kenttiä. Kirjastoon voi myös lisätä uuden ruokalajin ja sen raaka-aineet syöttämällä ne "Lisää uusi ruokalaji:"-kohdan merkittyihin kenttiin. Kenttien oletustekstit katoavat kenttiä klikattaessa. Raaka-aineet tulee erotella toisistaan rivinvaihdoilla tähän tyyliin:

Kinkku
Kerma
Pasta

Lopuksi painetaan "Lisää" -painiketta, jolloin näkyviin ilmestyy ikkuna, joka kertoo, onnistuiko lisääminen. 

Alhaalla on painikkeet, joista pääsee takaisin päänäkymään, tai voi lopettaa sovelluksen käytön. "Lopeta" -painike sulkee sovelluksen.
