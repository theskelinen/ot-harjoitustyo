# Luolasto

Luolasto on vuoropohjainen RPG, jossa pelaajan tehtävänä on löytää ulos vihamielisiä otuksia täynnä olevasta luolasta.

## Python-versio

Sovellus on kehitetty Python versiolla 3.10. Vanhempien versioiden kanssa voi ilmetä ongelmia.

## Dokumentaatio

- [vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
- [työaikakirjanpito](dokumentaatio/tuntikirjanpito.md)
- [changelog](dokumentaatio/changelog.md)

## Asennus

1. Asenna riippuvuudet komennolla:

==poetry install==

2. Suorita alustus:

- poetry run invoke build

3. Käynnistä sovellus:

- poetry run invoke start

## Ohjelman suorittaminen

Suorittaminen tapahtuu komennolla:

- poetry run invoke start

Testit suoritetaan komennolla:

- poetry run invoke test

Testikattavuus generoidaan komennolla:

- poetry run invoke coverage-report

Raportti generoituu hakemistoon "htmlcov".

