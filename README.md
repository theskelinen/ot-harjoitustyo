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

<mark>poetry install</mark>

2. Suorita alustus:

<mark>poetry run invoke build</mark>

3. Käynnistä sovellus:

<mark>poetry run invoke start</mark>

## Ohjelman suorittaminen

Suorittaminen tapahtuu komennolla:

<mark>poetry run invoke start</mark>

Testit suoritetaan komennolla:

<mark>poetry run invoke test</mark>

Testikattavuus generoidaan komennolla:

<mark>poetry run invoke coverage-report</mark>

Raportti generoituu hakemistoon "htmlcov".

