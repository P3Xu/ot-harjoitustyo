# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjät voivat generoida itselleen valmiita ruokalistoja helpottamaan arjen ateriasuunnittelua; mitä tänään syötäisiin? 

## Käyttäjät

Sovelluksen luonteesta johtuen sovelluksella on vain normaaleja käyttäjiä.

## Käyttöliittymä

Näkymät sisäänkirjautumiselle, sekä käyttäjän luonnille. Sitten päänäkymä, jossa näkyy generoitu viikon ruokalista sekä toiminnot uuden ruokalistan generoinnille, sekä ruokalajien ja raaka-aineiden lisäämiselle. Ruokalistan generoinnissa näkyy jonkinlainen parametrivalikko. Lisäksi näkyy mahdollisuus kirjautua ulos järjestelmästä.
	- **Tehty:** Tekstipohjainen käyttöliittymä, käyttäjä voi generoida ruokalistan ja tarkastella ruokalajeja sekä raaka-aineita, sekä lisäksi lisätä uusia ruokalajeja kirjastoon, joista menu generoidaan
	- **Viikko 5:** Graafinen alkanut valmistua myös, samat toiminnot kuin tekstipohjaisessakin. Bugeja ainakin sen verran, että tyhjät merkkijonot ja rivinvaihdot menee lisäyksestä toistaiseksi vielä läpi.
## Perusversion toiminnallisuus
- **Update:** Kirjautuminen puuttuu vielä täysin, tällä hetkellä ei ole oikein tiedossa onko edes tarpeellista implementoida
- **Viikko 5:** Sama tilanne yhä
- **Viikko 6:** Kirjautumista alettu implementoimaan. Tällä hetkellä graafinen osuus valmis, mutta pellin alla-toiminnallisuus puuttuu vielä aivan täysin. Aloitettu repositoryn kirjoittaminen sekä controllerin testaus ennen uusia metodeja. 
### Ennen sisäänkirjautumista

- Käyttäjätunnuksen luonti, jossa käyttäjä voi luoda itselleen tunnuksen järjestelmään
	- Vaatimukset tunnuksen minimipituus 5 merkkiä ja uniikki tunnus; järjestelmä ilmoittaa, mikäli nämä ehdot eivät täyty
- Kirjautuminen järjestelmään
	- Kirjautuminen onnistuu, jos tunnus on oikein
	- Mikäli tunnusta ei ole olemassa, järjestelmä ilmoittaa siitä

**Viikko 6:** Käyttäjä voi luoda itselleen käyttäjätunnuksen, mutta virheitä ei vielä havaita eikä käyttäjätunnus tallennus mihinkään.
### Kirjautumisen jälkeen

- Käyttäjä näkee viimeisimmän generoidun ruokalistan, mikäli sellainen on generoitu
	- **Tehty**
- Käyttäjä voi generoida uuden ruokalistan
	- **Tehty**
- Käyttäjä voi lisätä ruokia kirjastoon, jonka pohjalta lista generoidaan
	- Käyttäjä voi määritellä, mistä raaka-aineista ruoka koostuu
		- **Molemmat tehty**
- Käyttäjä voi asettaa joitain parametrejä listan generoinnille
	- Syödäänkö jotain ruokaa vain yhtenä vai useampana päivänä
	- Syödäänkö jonain päivänä ulkona/noutoruokaa
- Käyttäjä voi kirjautua ulos järjestelmästä
**Viikko 6:** No periaatteessa käyttäjä voi kirjautua tällä hetkellä ulos painamalla "Lopeta" :D

Ruokalista luodaan aina viikoksi kerrallaan ja oletusarvoisesti yksi ruokalaji on generoitu aina yhdeksi päiväksi, eli sovellus ei erottele esimerkiksi lounasta ja päivällistä erikseen.
	- **Tällä hetkellä tämä on vielä näin**

**Tilanne:** Projekti laahaa tällä hetkellä hieman jäljessä (omasta) aikataulusta, graafisen käyttöliittymän tekoa ei ole ehditty vielä edes aloittaa. 
	- **Viikko 5:** Graafinen ihan ok mallilla, seuraavaksi mahdollisesti lisää toiminnallisuutta

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
