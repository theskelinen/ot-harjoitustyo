# Testausdokumentti

Ohjelman automatisoidut testit on toteutettu unittestilla. Lisäksi ohjelmaa on testattu manuaalisesti eri tilanteissa.

## Sovelluslogiikan testaus

Sovelluslogiikasta vastaavia luokkia on testattu vastaavasti nimetyillä testitiedostoilla.
GameRunner-luokan testaus on toteutettu luomalla StubStates-luokka, jonka avulla on voitu testata GameRunner-luokan run, update, get_events ja next_state metodeja 
States-luokan testaamiseksi on luotu StubLevel- ja StubEvents-luokat. Level-luokan toimintaa ja LevelAction -luokan toimintaa on testattu niin ikään Stub-luokilla.
Stub-luokkien käyttö on ollut mahdollista, sillä luokkien riippuvuudet on injektoitu hyödyntäen ulkoista "kink" kirjastoa.

## Hahmoluokan testaus

Hahmojen pääluokkaa Characters testataan character_test tiedostossa. Character luokka vastaa pääasiassa hahmojen toiminnasta ja on yhteinen eri hahmojen välillä.
Sprites_test testaa vastaavasti Knight-luokan animaatiolistojen lataamista.

## Testikattavuus

Sovelluksen testikattavuus on 55%.

![testikattavuus](linkki)

## Manuaalinen testaus

Ohjelmaa on testattu manuaalisesti vaatimusmäärittelyn ja käyttöohjeen määrittelemissä tilanteissa.

## Sovellukseen jääneet laatuongelmat

Osa ohjelman toiminnallisuuksista jäi toistaiseksi automatisoitujen testien ulkopuolelle.
Ohjelman lukema data on toistaiseksi kovakoodattua ja siirtyminen tietokannan tai ulkoisen tiedoston lukemiseen vaatii muutoksia sovelluksen rakenteeseen.
