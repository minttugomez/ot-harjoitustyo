import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_kassapaatteen_rahamaara_alussa_oikein(self):
        rahamaara = self.kassapaate.kassassa_rahaa_euroina()
        self.assertEqual(rahamaara, 1000.00)

    def test_myytyjen_lounaiden_maara_alussa_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_toimii_edullinen(self):
        maksu = self.kassapaate.syo_edullisesti_kateisella(300)
        rahamaara = self.kassapaate.kassassa_rahaa_euroina()
        self.assertEqual(maksu, 60)
        self.assertEqual(rahamaara, 1002.40)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateisosto_toimii_maukas(self):
        maksu = self.kassapaate.syo_maukkaasti_kateisella(500)
        rahamaara = self.kassapaate.kassassa_rahaa_euroina()
        self.assertEqual(maksu, 100)
        self.assertEqual(rahamaara, 1004.00)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateisosto_ei_tarpeeksi_rahaa_edullinen(self):
        maksu = self.kassapaate.syo_edullisesti_kateisella(200)
        rahamaara = self.kassapaate.kassassa_rahaa_euroina()
        self.assertEqual(maksu, 200)
        self.assertEqual(rahamaara, 1000.00)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateisosto_ei_tarpeeksi_rahaa_maukas(self):
        maksu = self.kassapaate.syo_maukkaasti_kateisella(300)
        rahamaara = self.kassapaate.kassassa_rahaa_euroina()
        self.assertEqual(maksu, 300)
        self.assertEqual(rahamaara, 1000.00)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttiosto_toimii_edullinen(self):
        onnistui = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        rahamaara = self.kassapaate.kassassa_rahaa_euroina()
        self.assertEqual(onnistui, True)
        self.assertEqual(rahamaara, 1000.00)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_korttiosto_toimii_maukas(self):
        onnistui = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        rahamaara = self.kassapaate.kassassa_rahaa_euroina()
        self.assertEqual(onnistui, True)
        self.assertEqual(rahamaara, 1000.00)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_korttiosto_ei_tarpeeksi_rahaa_edullinen(self):
        maksukortti = Maksukortti(200)
        onnistui = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        rahamaara = self.kassapaate.kassassa_rahaa_euroina()
        self.assertEqual(onnistui, False)
        self.assertEqual(rahamaara, 1000.00)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_korttiosto_ei_tarpeeksi_rahaa_maukas(self):
        maksukortti = Maksukortti(200)
        onnistui = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        rahamaara = self.kassapaate.kassassa_rahaa_euroina()
        self.assertEqual(onnistui, False)
        self.assertEqual(rahamaara, 1000.00)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_lataa_rahaa_kortille(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 200)
        rahamaara = self.kassapaate.kassassa_rahaa_euroina()
        self.assertEqual(rahamaara, 1002.00)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 12.00 euroa")

    def test_lataa_negatiivinen_summa_kortille(self):
        tulos = self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -200)
        rahamaara = self.kassapaate.kassassa_rahaa_euroina()
        self.assertEqual(rahamaara, 1000.00)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
        self.assertEqual(tulos, None)