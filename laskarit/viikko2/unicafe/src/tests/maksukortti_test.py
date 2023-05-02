import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def kortin_saldo_alussa_oikein(self):
        kortti = Maksukortti()

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")

    def rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.kortti.lataa_rahaa(1000)

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 20.00 euroa")

    def saldo_vahenee_oikein_jos_rahaa_on_tarpeeksi(self):
        self.kortti.syo_edullisesti()

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 2.50 euroa")

    def saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        kortti = Maksukortti(200)
        kortti.syo_edullisesti()

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 2.50 euroa")

    def metodi_palauttaa_true_jos_rahat_riittivat(self):
        self.assertEqual(self.kortti.syo_edullisesti(), True)

    def metodi_palauttaa_false_jos_rahat_eivat_riittaneet(self):
        kortti = Maksukortti(200)

        self.assertEqual(kortti.syo_edullisesti(), False)
