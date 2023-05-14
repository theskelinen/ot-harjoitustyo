import pygame
import unittest
from unittest.mock import patch
from sprites.character import Character


class StubKnight(Character):
    def __init__(self):
        self.state_ready = False
        self.state_fall = False
        self.max_hp = 100
        self.current_hp = 100
        self.strength = 20
        self.multiplier_min = -5
        self.multiplier_max = 5
        super().__init__()

    def _initialize_images(self):
        self.image = pygame.image.load(
            "src/assets/Knight/HeroKnight_Idle_1.png").convert_alpha()
        self.animation_list = [[self.image, self.image, self.image], [
            self.image, self.image, self.image], [
            self.image, self.image, self.image], [
            self.image, self.image, self.image]]
        self.frame_index = 2

    def draw(self, screen):
        pass

    def ready(self, current_time):
        self.state_ready = True


class StubTarget(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.is_alive = True
        self.max_hp = 100
        self.current_hp = 100
        self.image = pygame.image.load(
            "src/assets/Death_Bringer/Idle/Bringer-of-Death_Idle_1.png").convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = (200, 300)

    def block(self, time):
        pass

    def fall(self, time):
        pass

    def hit(self, time):
        pass


class StubSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


class TestCharacter(unittest.TestCase):
    def setUp(self):
        self.screen = pygame.display.set_mode((800, 1000))
        self.test_character = StubKnight()
        self.test_target = StubTarget()
        self.damage_text_group = pygame.sprite.Group()
        self.time = 1000

    def test_update_call_ready_if_is_alive(self):
        self.test_character.update(self.time)
        self.assertEqual(self.test_character.state_ready, True)

    def test_if_fallen_ready_is_not_called(self):
        self.test_character.fall(self.time)
        self.test_character.update(self.time)
        self.assertFalse(self.test_character.state_ready)

    @patch("sprites.character.Character.create_dmg_text")
    def test_character_attack_depletes_target_hp(self, mock_create_dmg_text):
        mock_create_dmg_text.return_value = StubSprite()
        self.test_character.attack(
            self.test_target, self.damage_text_group, self.time)
        self.assertNotEqual(self.test_target.current_hp,
                            self.test_target.max_hp)

    @patch("sprites.character.Character.create_dmg_text")
    def test_target_can_die_from_attack(self, mock_create_dmg_text):
        mock_create_dmg_text.return_value = StubSprite()
        self.test_target.current_hp = 1
        self.test_character.attack(
            self.test_target, self.damage_text_group, self.time)
        self.assertEqual(self.test_target.is_alive, False)
