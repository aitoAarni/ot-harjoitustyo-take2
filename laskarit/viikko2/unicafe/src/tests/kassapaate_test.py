import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()

    def test_konstruktori_toiimi(self):
        vastaus = (self.kassa.kassassa_rahaa, self.kassa.edulliset + self.kassa.maukkaat)
        self.assertTupleEqual(vastaus, (100000, 0))

    def test_kateis_osto_toimii_edullisille_kun_raha_riittaa(self):
        vaihto = self.kassa.syo_edullisesti_kateisella(300)
        self.assertTupleEqual((vaihto, self.kassa.edulliset), (60, 1))

    def test_kateis_osto_toimii_edullisille_kun_raha_ei_riita(self):
        vaihto = self.kassa.syo_edullisesti_kateisella(200)
        self.assertTupleEqual((vaihto, self.kassa.edulliset), (200, 0))

    def test_kateis_osto_toimii_kalleille_kun_raha_riittaa(self):
        vaihto = self.kassa.syo_maukkaasti_kateisella(450)
        self.assertTupleEqual((vaihto, self.kassa.maukkaat), (50, 1))

    def test_kateis_osto_toimii_kalleille_kun_raha_ei_riita(self):
        vaihto = self.kassa.syo_maukkaasti_kateisella(200)
        self.assertTupleEqual((vaihto, self.kassa.maukkaat), (200, 0))
    
    def test_kortti_osto_toimii_edullisille_kun_on_saldoa(self):
        self.kortti = Maksukortti(300)
        vastaus = self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertTupleEqual((self.kortti.saldo, vastaus, self.kassa.edulliset), (60, True, 1))

    def test_kortti_osto_toimii_edullisille_kun_saldo_ei_riita(self):
        self.kortti = Maksukortti(200)
        vastaus = self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual((self.kortti.saldo, vastaus, self.kassa.edulliset), (200, False, 0))

    def test_kortti_osto_toimii_kalliisti_kun_on_saldoa(self):
        self.kortti = Maksukortti(450)
        vastaus = self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertTupleEqual((self.kortti.saldo, vastaus, self.kassa.maukkaat), (50, True, 1))

    def test_kortti_osto_toimii_kalliille_kun_saldo_ei_riita(self):
        self.kortti = Maksukortti(200)
        vastaus = self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual((self.kortti.saldo, vastaus, self.kassa.edulliset), (200, False, 0))

    def test_kortin_lataus_toimii_kun_summa_positiivinen(self):
        self.kortti = Maksukortti(0)
        self.kassa.lataa_rahaa_kortille(self.kortti, 100)
        self.assertTupleEqual((self.kassa.kassassa_rahaa, self.kortti.saldo), (100100, 100))
    
    def test_kortin_lataus_toimii_kun_summa_negatiivinen(self):
        self.kortti = Maksukortti(0)
        self.kassa.lataa_rahaa_kortille(self.kortti, -5)
        self.assertTupleEqual((self.kassa.kassassa_rahaa, self.kortti.saldo), (100000, 0))