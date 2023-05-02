## Viikko 3

- Pelin karkea perusrunko luotu ja pelistä tulostuu tällä hetkellä staattinen kuva
- Luotu Level-luokka, joka vastaa pelin huoneen/tason luomisesta
- Luotu Character luokka, joka vastaa pelihahmon luomisesta
- Luotu Renderer luokka, joka vastaa pelin kuvien piirtämisestä
- Luotu GameLoop luokka, joka vastaa pelin silmukan pyörittämisestä

## Viikko 4

- Hahmot nyt animoituja
- Pelin sovelluslogiikkaa kehitetty, vihollisia voi lyödä ja viholliset lyövät takaisin
- Pelihahmoa voi ohjata lyömään vihollista hiiren avulla
- Hahmoille luotu healthbarit ja ne toimivat hahmojen healthpointien mukaisesti
- Pelihahmot kuolevat ja poistuvat ruudulta healthpointien pudotessa nollaan


## Viikko 5

- Pelistä on tehty state-engine pohjainen, mikä mahdollistaa pelin tilan vaihtamisen (valikot, intro)
- Pelihahmojen animaatioita on lisätty, nyt pelihahmo torjuu epäonnistunita vastustajan iskuja ja hahmot heilahtavat osumasta
- Iskusta generoituu ruudulle damagen määrän kertova teksti ja lisähuomio, mikäli isku oli kriittinen

## Viikko 6

- Otettu uusi python kirjasto "kink" käyttöön riippuvuuksien injektoimiseksi ja tulevan testauksen helpottamiseksi
