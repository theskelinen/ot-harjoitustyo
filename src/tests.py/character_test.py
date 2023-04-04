#Jostain syystä herjaa "ModuleNotFoundError: No module named 'sprites'", vaikka __init__.py olemassa.
#Siksi path määritelty alkuun näin
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


import unittest
from sprites.character import Character

class TestCharacter(unittest.TestCase):
    def setUp(self):
        self.character = Character(100, 200, "Knight", None, None)

    def test_konstruktori_asettaa_nimen_oikein(self):
        hahmo = self.character
        nimi = hahmo.name

        self.assertEqual(nimi, "Knight")