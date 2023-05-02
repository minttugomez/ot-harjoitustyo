import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
	self.paate = Kassapaate()
	self.kortti = Maksukortti(1000)

    def rahamaara_oikein(self):
	self.assertEqual(self.kassassa_rahaa, 100000)

    def myydyt_edulliset_lounaat_oikein(self):
	self.assertEqual(self.edulliset, 0)

    def myydyt_edulliset_lounaat_oikein(self):
        self.assertEqual(self.maukkaat, 0)

    def kateisella_voi_ostaa_edullisen_lounaan(self):
	self.paate.syo_edullisesti_kateisella(240)
	
	self.assertEqual(self.kassassa_rahaa, 100240)
	self.assertEqual(self.edulliset, 1)
	self.assertEqual(self.maukkaat, 0)

    def kateisella_voi_ostaa_maukkaan_lounaan(self):
        self.paate.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassassa_rahaa, 100400)
        self.assertEqual(self.edulliset, 0)
        self.assertEqual(self.maukkaat, 1)

    def vaihtorahan_suuruus_oikein(self):
	self.assertEqual(self.paate.syo_edullisesti_kateisella(300), 60)
	self.assertEqual(self.paate.syo_maukkaasti_kateisella(500), 100)

    def kateismaksu_ei_onnistu_mikali_maksu_ei_riittava_edullinen_lounas(self):
	self.paate.syo_edullisesti_kateisella(200)
	
	self.assertEqual(self.kassassa_rahaa, 100000)
	self.assertEqual(self.edulliset, 0)
	self.assertEqual(self.paate.syo_edullisesti_kateisella(200), 200)

    def kateismaksu_ei_onnistu_mikali_maksu_ei_riittava(self):
        self.paate.syo_maukkaasti_kateisella(200)

        self.assertEqual(self.kassassa_rahaa, 100000)
        self.assertEqual(self.maukkaat, 0)
        self.assertEqual(self.paate.syo_maukkaasti_kateisella(200), 200)

    def korttiosto_toimii_edullinen_lounas(self):
	self.paate.syo_edullisesti_kortilla(self.kortti)
	
	self.assertEqual(self.kortti.kortilla_rahaa, 760)
	self.assertEqual(self.paate.edulliset, 1)
	self.assertEqual(self.paate.maukkaat, 0)
	self.assertEqual(self.paate.syo_edullisesti_kortilla(self.kortti), True)
	self.assertEqual(self.paate.kassassa_rahaa, 100000)

    def korttiosto_toimii_maukas_lounas(self):
	self.paate.syo_maukkaasti_kortilla(self.kortti)

	self.assertEqual(self.kortti.kortilla_rahaa, 600)
	self.assertEqual(self.paate.edulliset, 0)
	self.assertEqual(self.paate.maukkaat, 1)
	self.assertEqual(self.paate.syo_maukkaasti_kortilla(self.kortti), True)
	self.assertEqual(self.paate.kassassa_rahaa, 100000)

    def korttiosto_epaonnistuu_oikein_edullinen_lounas(self):
	kortti = Maksukortti(100)
	self.paate.syo_edullisesti_kortilla(kortti)

	self.assertEqual(kortti.kortilla_rahaa, 100)
        self.assertEqual(self.paate.edulliset, 0)
        self.assertEqual(self.paate.maukkaat, 0)
        self.assertEqual(self.paate.syo_edullisesti_kortilla(self.kortti), False)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)

    def korttiosto_epaonnistuu_oikein_maukas_lounas(self):
	kortti = Maksukortti(100)
        self.paate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(kortti.kortilla_rahaa, 100)
        self.assertEqual(self.paate.edulliset, 0)
        self.assertEqual(self.paate.maukkaat, 0)
        self.assertEqual(self.paate.syo_maukkaasti_kortilla(self.kortti), False)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)

    def kortille_lataaminen_toimii_oikein(self):
	self.paate.lataa_rahaa_kortille(self.kortti, 1000)

	self.assertEqual(self.kortti.kortilla_rahaa, 2000)
	self.assertEqual(self.paate.kassassa_rahaa, 101000)
