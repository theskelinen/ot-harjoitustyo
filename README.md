# Luolasto

Luolasto on vuoropohjainen RPG, jossa pelaajan tehtävänä on kukistaa vastustajat luolasta ulos pääsemiseksi.

## Python-versio

Sovellus on kehitetty Python versiolla 3.10. Vanhempien versioiden kanssa voi ilmetä ongelmia.

## Dokumentaatio

- [Käyttöohje](dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti](dokumentaatio/testausdokumentti.md)
- [Työaikakirjanpito](dokumentaatio/tuntikirjanpito.md)
- [Changelog](dokumentaatio/changelog.md)
- [Releases](https://github.com/theskelinen/ot-harjoitustyo/releases)

## Asennus

1. Asenna riippuvuudet komennolla:

- poetry install

2. Käynnistä sovellus:

- poetry run invoke start

## Ohjelman suorittaminen

Suorittaminen tapahtuu komennolla:

- poetry run invoke start

Testit suoritetaan komennolla:

- poetry run invoke test

Testikattavuus generoidaan komennolla:

- poetry run invoke coverage-report

- raportti generoituu hakemistoon "htmlcov"

Pylint tarkistusten suoritukseen käytetään komentoa:

- poetry run invoke lint
