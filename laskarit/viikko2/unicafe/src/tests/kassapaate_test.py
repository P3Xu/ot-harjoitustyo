import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(10000)

    def test_luodussa_kassapaatteessa_rahaa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_luodussa_kassapaatteessa_edulliset_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_luodussa_kassapaatteessa_maukkaat_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_maukkaasti_kateisella_rahat_riittaa(self):
        vaihtorahat = self.kassapaate.syo_maukkaasti_kateisella(1000)
        
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(vaihtorahat, 600)
    
    def test_maukkaasti_kateisella_rahat_ei_riita(self):
        vaihtorahat = self.kassapaate.syo_maukkaasti_kateisella(100)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(vaihtorahat, 100)
    
    def test_maukkaasti_kateisella_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(1000)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullisesti_kateisella_rahat_riittaa(self):
        vaihtorahat = self.kassapaate.syo_edullisesti_kateisella(1000)
        
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(vaihtorahat, 760)
    
    def test_edullisesti_kateisella_rahat_ei_riita(self):
        vaihtorahat = self.kassapaate.syo_edullisesti_kateisella(100)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(vaihtorahat, 100)
    
    def test_edullisesti_kateisella_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(1000)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukkaasti_kortilla_rahat_riittaa(self):
        transaktio = self.kassapaate.syo_maukkaasti_kortilla(self.kortti)

        self.assertTrue(transaktio)
        self.assertEqual(self.kortti.saldo, 9600)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_maukkaasti_kortilla_rahat_ei_riita(self):
        self.kortti.ota_rahaa(9900)
        transaktio = self.kassapaate.syo_maukkaasti_kortilla(self.kortti)

        self.assertEqual(self.kortti.saldo, 100)
        self.assertFalse(transaktio)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullisesti_kortilla_rahat_riittaa(self):
        transaktio = self.kassapaate.syo_edullisesti_kortilla(self.kortti)

        self.assertTrue(transaktio)
        self.assertEqual(self.kortti.saldo, 9760)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_edullisesti_kortilla_rahat_ei_riita(self):
        self.kortti.ota_rahaa(9900)
        transaktio = self.kassapaate.syo_edullisesti_kortilla(self.kortti)

        self.assertFalse(transaktio)
        self.assertEqual(self.kortti.saldo, 100)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortin_lataus_kasvattaa_kassaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti,666)

        self.assertEqual(self.kortti.saldo, 10666)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100666)
    
    def test_kortin_lataus_negatiivisella_ei_kasvata_kassaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti,-666)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)