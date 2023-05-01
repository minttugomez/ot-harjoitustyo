import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(1000)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")

    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_edullisesti()

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 7.50 euroa")

    def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_maukkaasti()

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 6.00 euroa")

    def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self):
        kortti = Maksukortti(200)
        kortti.syo_edullisesti()

        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")

    def test_kortille_voi_ladata_rahaa(self):
        self.kortti.lataa_rahaa(2500)

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 35.00 euroa")

    def test_kortin_saldo_ei_ylita_maksimiarvoa(self):
        self.kortti.lataa_rahaa(20000)

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 150.00 euroa")

    def test_syo_maukkaasti_ei_vie_arvoa_negatiiviseksi(self):
        kortti = Maksukortti(200)
        kortti.syo_maukkaasti()

        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")

    def test_negatiivisen_summan_lataaminen_ei_muuta_saldoa(self):
        self.kortti.lataa_rahaa(-1000)

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")

    def test_kortilla_voi_ostaa_edullisen_lounaan(self):
        kortti = Maksukortti(250)
        kortti.syo_edullisesti()

        self.assertEqual(str(kortti), "Kortilla on rahaa 0.00 euroa")

    def test_kortilla_voi_ostaa_maukkaan_lounaan(self):
        kortti = Maksukortti(400)
        kortti.syo_maukkaasti()

        self.assertEqual(str(kortti), "Kortilla on rahaa 0.00 euroa")

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
