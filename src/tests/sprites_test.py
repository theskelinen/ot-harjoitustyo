import unittest
from sprites.knight import Knight
from sprites.imp_axe import ImpAxe
from sprites.death_bringer import DeathBringer


class TestSprite(unittest.TestCase):
    def setUp(self):
        self.knight = Knight()
        self.death_bringer = DeathBringer()
        self.imp_axe = ImpAxe()

    def test_knight_ready_images(self):
        self.assertEqual(len(self.knight.animation_list[0]), 8)

    def test_knight_attack_image(self):
        self.assertEqual(len(self.knight.animation_list[1]), 8)

    def test_knight_hit_images(self):
        self.assertEqual(len(self.knight.animation_list[2]), 3)

    def test_knight_block_images(self):
        self.assertEqual(len(self.knight.animation_list[3]), 10)

    def test_knight_death_images(self):
        self.assertEqual(len(self.knight.animation_list[4]), 5)

    def test_death_bringer_ready_images(self):
        self.assertEqual(len(self.death_bringer.animation_list[0]), 8)

    def test_death_bringer_attack_image(self):
        self.assertEqual(len(self.death_bringer.animation_list[1]), 10)

    def test_death_bringer_hit_images(self):
        self.assertEqual(len(self.death_bringer.animation_list[2]), 3)

    def test_death_bringer_death_images(self):
        self.assertEqual(len(self.death_bringer.animation_list[3]), 10)

    def test_imp_axe_ready_images(self):
        self.assertEqual(len(self.imp_axe.animation_list[0]), 3)

    def test_imp_axe_attack_image(self):
        self.assertEqual(len(self.imp_axe.animation_list[1]), 6)

    def test_imp_axe_hit_images(self):
        self.assertEqual(len(self.imp_axe.animation_list[2]), 3)

    def test_imp_axe_death_images(self):
        self.assertEqual(len(self.imp_axe.animation_list[3]), 4)
