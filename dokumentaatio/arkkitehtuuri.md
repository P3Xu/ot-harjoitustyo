# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne noudattaa kerrosarkkitehtuuria. Pakkausrakenteen alustava hahmotelma on seuraavanlainen:

<img src="https://github.com/P3Xu/ot-harjoitustyo/blob/master/dokumentaatio/kaavio.jpg" width="768" height="1024">

Pakkaus _ui_ sisältää sovelluksen käyttöliittymään liittyvän koodin, _services_ sovelluslogiikkaan liittyvän koodin, _repositories_ tietojen tallennukseen liittyvän koodin ja _entitities_ sisältää sovelluksen tietokohteita.

## Käyttöliittymä

Käyttöliittymä sisältää tällä hetkellä viisi erilaista näkymää:
- Kirjautuminen
- Uuden käyttäjän luominen
- Ruokalistan katselu ja generointi
- Kirjastojen hallinta
- Infonäkymä, joka kertoo suoritetun toimenpiteen onnistumisesta

Kaikki näkymät on toteutettu omissa luokissaan. Näkymien välillä vaihdellaan UI-luokasta käsin siten, että luokka vaihtaa aina yhden näkymän kerrallaan näkyviin. UI-luokka antaa kullekin näkymälle parametrina listan metodeistaan muihin näkymiin siirtymistä varten, joista on helppo pyytää tarvittavaa näkymää senhetkisen tilalle.
Käyttöliittymä on pyritty pitämään erillään sovelluslogiikasta ja näin ollen käyttöliittymä käyttää ainoastaan Controller-luokan tarjoamia palveluja.

## Sovelluslogiikka

Controller-luokka on koko sovelluksen ydin, joka hoitaa kaiken organisoinnin. Controller organisoi kaiken pellin alla tapahtuvan toiminnan komentamalla tarvittavia _repository_-luokkia ja tarjoamalla näiden avulla käyttöliittymälle sen tarvitsemia palveluja. 

Loogisen tietomallin keskiössä sovelluksessa toimivat luokat Meal ja Ingredient, sekä myöskin Menu. Myöhemmin on tulossa myös User, kunhan kyseinen piirre valmistuu. Näissä luokissa sijaitsee tiedot ruokalajeista ja niihin liittyvistä raaka-aineista, sekä viikon ruokalistasta. 

## Tiedon tallennus

Tallennuksesta huolehtivat luokat MealRepository sekä MenuRepository. Tiedot tallentuvat SQLite-tietokantaan. Luokat noudattavat Repository -suunnittelumallia.

## Toiminallisuus 

Toiminnallisuudesta on olemassa erittäin alustava sekvenssikaavio, joka päivitetään myöhemmin ajan tasalle ja vastaamaan paremmin sovelluksen toimintaa:

<img src="https://github.com/P3Xu/ot-harjoitustyo/blob/master/dokumentaatio/sekvenssi.jpeg" width="768" height="1024">
