import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
	def setUp(self):
		self.kortti = Maksukortti(10)

	def test_hello_world(self):
		self.assertEqual("Hello world", "Hello world")

	def test_konstruktori_asettaa_saldon_oikein(self):
		kortti = Maksukortti(10)

		vastaus = str(kortti)

		self.assertEqual(vastaus, "Kortilla on rahaa 10 euroa")

	def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
		kortti = Maksukortti(10)

		kortti.syo_edullisesti()

		self.assertEqual(str(kortti), "Kortilla on rahaa 7.5 euroa")

	def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
		kortti = Maksukortti(10)

		kortti.syo_maukkaasti()

		self.assertEqual(str(kortti), "Kortilla on rahaa 6 euroa")

	def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self):
		kortti = Maksukortti(10)

		kortti.syo_maukkaasti()
		kortti.syo_maukkaasti()
		kortti.syo_edullisesti()

		self.assertEqual(str(kortti), "Kortilla on rahaa 2 euroa")
