import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_arvo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(200)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 12.00 euroa")

    def test_saldo_vahenee_oikein_jos_rahaa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(200)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 8.00 euroa")

    def test_saldo_ei_vahene_jos_rahaa_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1200)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_metodi_palauttaa_true_jos_rahaa_on_tarpeeksi(self):
        status = self.maksukortti.ota_rahaa(200)
        self.assertEqual(status, True)

    def test_metodi_palauttaa_true_jos_rahaa_ei_tarpeeksi(self):
        status = self.maksukortti.ota_rahaa(1200)
        self.assertEqual(status, False)

    def test_saldo_euroina_toimii_oikein(self):
        saldo_euroina = self.maksukortti.saldo_euroina()
        self.assertEqual(saldo_euroina, 10)