# Luolasto

Luolasto on vuoropohjainen RPG, jossa pelaajan tehtävänä on löytää ulos vihamielisiä otuksia täynnä olevasta luolasta.

## Python-versio

Sovellus on kehitetty Python versiolla 3.10. Vanhempien versioiden kanssa voi ilmetä ongelmia.

## Dokumentaatio

- [vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
- [työaikakirjanpito](dokumentaatio/tuntikirjanpito.md)
- [changelog](dokumentaatio/changelog.md)
- [arkkitehtuurikuvaus](dokumentaatio/arkkitehtuuri.md)
- [releases](https://github.com/theskelinen/ot-harjoitustyo/releases)

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
