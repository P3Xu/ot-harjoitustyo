# Vaatimusmäärittely

## Sovelluksen tarkoitus

	Sovelluksen avulla käyttäjät voivat generoida itselleen valmiita ruokalistoja helpottamaan arjen ateriasuunnittelua.

## Käyttäjät

	Sovelluksen luonteesta johtuen sovelluksella on vain normaaleja käyttäjiä.

## Käyttöliittymä

	Näkymät sisäänkirjautumiselle, sekä käyttäjän luonnille. Sitten päänäkymä, jonka lisäksi hieman lisäominaisuuksista riippuen saattaa olla vielä muita sivunäkymiä.    

## Perusversion toiminnallisuus

### Ennen sisäänkirjautumista

	- Käyttäjätunnuksen luonti, jossa käyttäjä voi luoda itselleen tunnuksen järjestelmään
		- Vaatimukset tunnuksen minimipituus 5 merkkiä ja uniikki tunnus; järjestelmä ilmoittaa, mikäli nämä ehdot eivät täyty
	- Kirjautuminen järjestelmään
		- Kirjautuminen onnistuu, jos tunnus on oikein
		- Mikäli tunnusta ei ole olemassa, järjestelmä ilmoittaa siitä

### Kirjautumisen jälkeen

	- Käyttäjä näkee päänäkymän, jossa on ainakin viimeisin generoitu ruokalista.
	- Käyttäjä voi generoida uuden ruokalistan
	- Käyttäjä voi lisätä ruokia kirjastoon, jonka pohjalta lista generoidaan
		- Käyttäjä voi määritellä, mistä raaka-aineista ruoka koostuu
	- Käyttäjä voi asettaa joitain parametrejä listan generoinnille
		- Syödäänkö jotain ruokaa vain yhtenä vai useampana päivänä
		- Syödäänkö jonain päivänä ulkona/noutoruokaa
	- Käyttäjä voi kirjautua ulos järjestelmästä

## Jatkokehitysideoita

Järjestelmään resurssien puitteissa lisättävää toiminnallisuutta:

	- Käyttäjä voi koostaa ostoslistan (ns. kauppalapun) generoidun ruokalistan perusteella
		- Budjetointimahdollisuus; koostaa listan annetulla budjetilla
	- Käyttäjä voi tarkastella vanhoja ruokalistoja
	- Ruokalistojen editointi
	- Statistiikan keruu ja käpistely
	-	
