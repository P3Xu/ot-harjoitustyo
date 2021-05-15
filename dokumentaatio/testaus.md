# Testausdokumentti

Sovellusta on testattu kattavasti automaattisilla yksikkö- ja integraatiotesteillä. Lisäksi sovellusta on testattu myös manuaalisesti.

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka

Sovelluksen logiikasta vastaa pääosin `Controller`-luokka, jota testataan testiluokilla [TestControlServiceAsIntegration](https://github.com/P3Xu/ot-harjoitustyo/blob/master/src/tests/services/controller_integration_test.py) ja [TestControlServiceAsUnit](https://github.com/P3Xu/ot-harjoitustyo/blob/master/src/tests/services/controller_unit_test.py). Yksikkötestissä `Controller`-luokalle injektoidaan riippuvuuksiksi tarvittavat repository-objektit, jotka tallentavat tiedot `.env.test`-tiedostossa määriteltyyn tietokantatiedostoon. Integraatiotestissä testataan `Controller`-luokan, repository-luokkien sekä tietokohteiden toimintaa siten, että luokka käyttää konkreettisia riippuvuuksiaan kuten normaalissa käytössäänkin. Myös integraatiotestissä tiedon tallennus tapahtuu `.env.test`-tiedostossa määriteltyyn, erilliseen testaus-tietokantaan. 
`Controller`-luokka pyytää ruokalistan generoinnin `GeneratorService`-luokalta, jota testataan testiluokalla [TestGeneratorService](https://github.com/P3Xu/ot-harjoitustyo/blob/master/src/tests/services/generator_test.py). Generaattorille injektoidaan riippuvuuksina käytettävä testi-repository sekä testikäyttäjä.

### Repository-luokat

Repository-luokkia on testattu seuraavasti:

- `LibraryRepository`-luokkaa testaa testiluokka [TestLibraryRepository](https://github.com/P3Xu/ot-harjoitustyo/blob/master/src/tests/repositories/library_repository_test.py)
- `MealRepository`-luokkaa testaa testiluokka [TestMealRepository](https://github.com/P3Xu/ot-harjoitustyo/blob/master/src/tests/repositories/meal_repository_test.py)
- `MenuRepository`-luokkaa testaa testiluokka [TestMenuRepository](https://github.com/P3Xu/ot-harjoitustyo/blob/master/src/tests/repositories/menu_repository_test.py)
- `UserRepository`-luokkaa testaa testiluokka [TestUserRepository](https://github.com/P3Xu/ot-harjoitustyo/blob/master/src/tests/repositories/user_repository_test.py)

Lisäksi kolmen jälkimmäisen luokan käyttämää yhteistä `InputOutput`-luokkaa testaa testiluokka [TestInputOutput](https://github.com/P3Xu/ot-harjoitustyo/blob/master/src/tests/repositories/io_test.py).

`LibraryRepository`a lukuunottamatta kaikki saavat testeissä injektoituna riippuvuutena `InputOutput`-olion. Näissäkin testeissä tiedon tallennus tapahtuu `.env.test`-tiedostossa määriteltyyn testitietokantaan.

### Testauskattavuus

Sovelluksen käyttöliittymä jätettiin automaattitestauksen ulkopuolelle. Käyttöliittymää lukuunottamatta sovelluksen testauksen haarautumakattavuus on 98%.

![](./pictures/coverage_report.png)

Testeissä ei testattu `build.py` eikä `init_*.py`-tiedostojen suorittamista komentoriviltä, sillä se ei ole sovelluksen toiminnan kannalta oleellista. `Controller`in toimintaa ei myöskään testattu ilman sisäänkirjautumista, sillä sovellus vaatii toimiakseen kirjautuneen käyttäjän.

## Järjestelmätestaus

Sovelluksen järjestelmätestausta on suoritettu lähinnä manuaalisesti. 

### Asennus ja konfigurointi

Sovelluksen järjestelmätestausta on suoritettu [käyttöohjeen](https://github.com/P3Xu/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md) mukaisesti lähinnä muutamassa eri Linux-ympäristössä, sekä hieman myös Windows-ympäristössä. 

Testauksessa on kokeiltu, että `.env`-tiedostossa tehdyt muutokset toimivat oikein. 

Sovellusta on testattu suoraan alustustoimenpiteiden jälkeen, sekä niin, että tietoja on tallennettu jo sovelluksen aiemmilla käynnistyskerroilla.

### Toiminnallisuudet

Kaikki [käyttöohjeessa](https://github.com/P3Xu/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md) sekä [määrittelydokumentissa](https://github.com/P3Xu/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md) luetellut toiminnallisuudet on kokeiltu läpi. Lisäksi on yritetty myös syöttää virheellisiä arvoja sekä duplikaatteja. 

## Sovellukseen jääneitä laatuongelmia

Sovelluksessa ei ole tällä hetkellä havaittuja laatuongelmia.
