import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_oiein_alustettu(self):
        self.assertEqual(str(self.maksukortti), f'saldo: {0.1}')
    
    def test_rahan_lisaaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(str(self.maksukortti), f'saldo: {0.2}')
    
    def test_rahan_ottaminen_toimii(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), f'saldo: {0.05}')
    
    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpiaksi(self):
        self.maksukortti.ota_rahaa(25)
        self.assertEqual(str(self.maksukortti), f'saldo: {0.1}')

    def test_palauttaa_arvon_jos_maksu_onnistui(self):
        oikein, vaarin = self.maksukortti.ota_rahaa(10), self.maksukortti.ota_rahaa(10)
        on_rahaa = oikein == True
        ei_ole_rahaa = vaarin == False
        self.assertEqual(on_rahaa, ei_ole_rahaa)