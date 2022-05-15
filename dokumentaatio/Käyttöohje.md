# Käyttöohje
Lataa projektin viimeisimmän releasen lähdekoodi valitsemalla Assets-osion alta Source code.

## Konfigurointi
Tallennukseen käytettäviä tiedostoja voidaan konfiguroida .env-tiedostossa. Tiedostot luodaan automaattisesti data-hakemistoon, jos niitä ei vielä siellä ole.

## Ohjelman käynnistäminen

Ennen ohjelman käynnistystä asenna riippuvuudet komennolla:

> poetry install

jonka jälkeen suorita alustustoimenpiteet komennolla:

> poetry run invoke setup

Ohjelman voi käynnistää komennolla:

> poetry run invoke start

## Käyttäminen
- Ohjelmaa aukeaa valikkoon, josta voi valita eri karttoja nuolinäppäimillä ja aloittaa pelin
- esc näppäin poistuu pelistä ja välilyönti hyppii pelissä
- Pelissä tarkoitus on päästä maaliin, joka on vihreä
- Pelissä on palikoita joiden päälle voi hypätä ja piikkejä joihin ei saa osua

## Tason luominen
.env tiedostossa ollaa määritelty missä kartat sijaitsevat, mutta oletusarvoisesti ne ovat data kansiossa.
Sinne voi lisätä uusia tiedostoja joihin voi tehdä itse karttoja.
