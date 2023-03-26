import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_kassa_on_luotu_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

        self.assertEqual(self.kassapaate.edulliset, 0)

        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kateisella_toimii_oikein_kun_maksu_riittava(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(240)

        self.assertEqual(vaihtoraha, 0)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000+240)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_maukkaasti_kateisella_toimii_oikein_kun_maksu_riittava(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(vaihtoraha, 0)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000+400)

        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_syo_edullisesti_kateisella_toimii_oikein_kun_maksu_ei_riittava(self):
        rahan_palautus = self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(rahan_palautus, 200)
    
    def test_syo_maukkaasti_kateisella_toimii_oikein_kun_maksu_ei_riittava(self):
        rahan_palautus = self.kassapaate.syo_maukkaasti_kateisella(300)

        self.assertEqual(rahan_palautus, 300)
    
    def test_syo_edullisesti_kortilla_toimii_oikein_kun_rahaa_tarpeeksi(self):
        kortti = Maksukortti(1000)

        veloitus = self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(veloitus, True,)

        self.assertEqual(self.kassapaate.edulliset, 1)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_kortilla_toimii_oikein_kun_rahaa_tarpeeksi(self):
        kortti = Maksukortti(1000)

        veloitus = self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(veloitus, True,)

        self.assertEqual(self.kassapaate.maukkaat, 1)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_syo_edullisesti_kortilla_toimii_oikein_kun_rahaa_ei_tarpeeksi(self):
        kortti = Maksukortti(200)

        veloitus = self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(veloitus, False,)

        self.assertEqual(kortti.saldo, 200)

        self.assertEqual(self.kassapaate.edulliset, 0)
        

    def test_syo_maukkaasti_kortilla_toimii_oikein_kun_rahaa_ei_tarpeeksi(self):
        kortti = Maksukortti(200)

        veloitus = self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(veloitus, False,)

        self.assertEqual(kortti.saldo, 200)

        self.assertEqual(self.kassapaate.maukkaat, 0)


    def test_lataa_rahaa_kortille_toimii_oikein_kun_summa_ei_nolla(self):
        kortti = Maksukortti(200)

        self.kassapaate.lataa_rahaa_kortille(kortti, 1000)

        self.assertEqual(kortti.saldo, 1200)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)
    
    def test_lataa_rahaa_kortille_toimii_oikein_kun_summa_negatiivinen(self):
        kortti = Maksukortti(200)

        self.kassapaate.lataa_rahaa_kortille(kortti, -1000)

        self.assertEqual(kortti.saldo, 200)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)