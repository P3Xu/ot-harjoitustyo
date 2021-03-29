# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjät voivat generoida itselleen valmiita ruokalistoja helpottamaan arjen ateriasuunnittelua; mitä tänään syötäisiin? 

## Käyttäjät

Sovelluksen luonteesta johtuen sovelluksella on vain normaaleja käyttäjiä.

## Käyttöliittymä

Näkymät sisäänkirjautumiselle, sekä käyttäjän luonnille. Sitten päänäkymä, jossa näkyy generoitu viikon ruokalista sekä toiminnot uuden ruokalistan generoinnille, ruokalajien ja raaka-aineiden lisäämiselle. Ruokalistan generoinnissa näkyy jonkinlainen parametrivalikko. Lisäksi näkyy mahdollisuus kirjautua ulos järjestelmästä.

## Perusversion toiminnallisuus

### Ennen sisäänkirjautumista

- Käyttäjätunnuksen luonti, jossa käyttäjä voi luoda itselleen tunnuksen järjestelmään
	- Vaatimukset tunnuksen minimipituus 5 merkkiä ja uniikki tunnus; järjestelmä ilmoittaa, mikäli nämä ehdot eivät täyty
- Kirjautuminen järjestelmään
	- Kirjautuminen onnistuu, jos tunnus on oikein
	- Mikäli tunnusta ei ole olemassa, järjestelmä ilmoittaa siitä

### Kirjautumisen jälkeen

- Käyttäjä näkee viimeisimmän generoidun ruokalistan, mikäli sellainen on generoitu
- Käyttäjä voi generoida uuden ruokalistan
- Käyttäjä voi lisätä ruokia kirjastoon, jonka pohjalta lista generoidaan
	- Käyttäjä voi määritellä, mistä raaka-aineista ruoka koostuu
- Käyttäjä voi asettaa joitain parametrejä listan generoinnille
	- Syödäänkö jotain ruokaa vain yhtenä vai useampana päivänä
	- Syödäänkö jonain päivänä ulkona/noutoruokaa
- Käyttäjä voi kirjautua ulos järjestelmästä

Ruokalista luodaan aina viikoksi kerrallaan ja oletusarvoisesti yksi ruokalaji on generoitu aina yhdeksi päiväksi, eli sovellus ei erottele esimerkiksi lounasta ja päivällistä erikseen.

## Jatkokehitysideoita

Järjestelmään resurssien puitteissa lisättävää toiminnallisuutta:

- Ruokalista huomioi erikseen esimerkiksi lounaan ja päivällisen/illallisen
- Käyttäjä voi koostaa ostoslistan (ns. kauppalapun) generoidun ruokalistan perusteella
	- Budjetointimahdollisuus; koostaa listan annetulla budjetilla
- Käyttäjä voi tarkastella vanhoja ruokalistoja
- Ruokalistojen editointi
- Statistiikan keruu ja käpistely
- Ruokavalioiden huomiointi, esimerkiksi täysin vegaaninen ruokalista jne
- Ruokapäiväkirjan suunnittelu ja seuranta
