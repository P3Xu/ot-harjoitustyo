# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjät voivat generoida itselleen valmiita ruokalistoja helpottamaan arjen ateriasuunnittelua; mitä tänään syötäisiin? 

## Käyttäjät

Sovelluksen luonteesta johtuen sovelluksella on vain normaaleja käyttäjiä.

## Käyttöliittymä

Näkymät sisäänkirjautumiselle, sekä käyttäjän luonnille.
Sitten päänäkymä, jossa näkyy generoitu viikon ruokalista sekä toiminnot uuden ruokalistan generoinnille, kauppalistan tulostukselle, sekä ruokalajien ja raaka-aineiden lisäämiselle. Lisäksi näkyy mahdollisuus kirjautua ulos järjestelmästä tai lopettaa ohjelma.
Kauppalistanäkymässä näkyy viikon ruokalista, sen raaka-aineet listassa sekä mahdollisuus tulostaa kauppalista tekstitiedostoon. Lisäksi on painikkeet joilla voi siirtyä takaisin päänäkymään, kirjautua ulos tai lopettaa sovelluksen.
Ruoka-aineiden hallintanäkymässä näkyy ruokalistanäkymä, kaikki käyttäjän ruokalajit ja raaka-aineet omissa listoissaan, sekä syötekentät uusien ruokalajien ja niiden raaka-aineiden lisäämiselle. Lisäksi on painikkeet takaisin päänäkymään, ulos kirjautumiselle sekä sovelluksen lopettamiselle. Hallintanäkymässä on myös mahdollisuus poistaa ruokalajeja tuplaklikkaamalla, jolloin avautuu varmistusnäkymä jossa kysytään käyttäjältä, haluaako tämä varmasti poistaa kyseisen ruokalajin.
Lisäksi on vielä erilaisia viestinäkymiä, joissa sovellus kertoo käyttäjälle, kuinka suoritettu toiminto sujui; onnistuiko vai kohdattiinko ongelmia.

## Perusversion toiminnallisuus

### Ennen sisäänkirjautumista

- Käyttäjätunnuksen luonti, jossa käyttäjä voi luoda itselleen tunnuksen järjestelmään
	- Vaatimukset tunnuksen sekä salasanan minimipituus 5 merkkiä ja uniikki tunnus; järjestelmä ilmoittaa, mikäli nämä ehdot eivät täyty
- Kirjautuminen järjestelmään
	- Kirjautuminen onnistuu, jos tunnus on oikein
	- Mikäli tunnusta ei ole olemassa, järjestelmä ilmoittaa siitä

### Kirjautumisen jälkeen

- Käyttäjä näkee viimeisimmän generoidun ruokalistan, mikäli sellainen on generoitu
- Käyttäjä voi generoida uuden ruokalistan
- Käyttäjä voi tarkastella ja tulostaa itselleen viikon kauppalistan ruokalistan pohjalta
- Käyttäjä voi lisätä ruokia kirjastoon, jonka pohjalta lista generoidaan
	- Käyttäjä voi määritellä, mistä raaka-aineista ruoka koostuu
- Käyttäjä voi poistaa ruokalajeja listasta
- Käyttäjä voi kirjautua ulos järjestelmästä
- Käyttäjä voi lopettaa ohjelman suorituksen

Ruokalista luodaan aina viikoksi kerrallaan ja oletusarvoisesti yksi ruokalaji on generoitu aina yhdeksi päiväksi, eli sovellus ei erottele esimerkiksi lounasta ja päivällistä erikseen.

## Jatkokehitysideoita

Perusversiota voidaan tulevaisuudessa jatkojalostaa esimerkiksi seuraavanlaisesti:
- Käyttäjä voi editoida ruokalajeja
- Ruokalista huomioi erikseen esimerkiksi lounaan ja päivällisen/illallisen
- Käyttäjä voi tarkastella vanhoja ruokalistoja
- Ruokalistojen editointi
- Statistiikan keruu ja käpistely
- Ruokavalioiden huomiointi, esimerkiksi täysin vegaaninen ruokalista jne
- Ruokapäiväkirjan suunnittelu ja seuranta
- [Nightmare](https://doom.fandom.com/wiki/Skill_level):
	- Web-käli ja joku integraatio jossa kauppalistan voi ajaa suoraan K- tai S-ryhmän verkkokauppaan ja tarvitsee painaa vain "Tilaa"