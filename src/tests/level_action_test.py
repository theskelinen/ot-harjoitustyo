import pygame
import unittest
from unittest.mock import patch
from game_files.level.level_action import LevelAction


class StubKnight(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.name = "Knight"
        self.is_alive = True
        self.attack_value = False
        self.image = pygame.image.load(
            "src/assets/Knight/HeroKnight_Idle_1.png").convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        #self.rect.center = (200, 200)

    def attack(self, target, damage_text_group, current_time):
        self.attack_value = True


class StubDeathBringer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.name = "Death_Bringer"
        self.is_alive = True
        self.attack_value = False
        self.image = pygame.image.load(
            "src/assets/Death_Bringer/Idle/Bringer-of-Death_Idle_1.png").convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = (200, 300)

    def attack(self, target, damage_text_group, current_time):
        self.attack_value = True


class StubImpAxe(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.name = "Imp_axe"
        self.is_alive = True
        self.attack_value = False
        self.image = pygame.image.load(
            "src/assets/Imp_Axe/ready_1.png").convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = (400, 600)

    def attack(self, target, damage_text_group, current_time):
        self.attack_value = True


class StubSwordIcon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.show = False
        self.image = pygame.image.load(
            "src/assets/Others/sword.png").convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = (400, 600)


class StubLevelData:
    def __init__(self, damage_text_group):
        self.current_fighter = 1
        self.total_fighters = 3
        self.action_cooldown = 90
        self.action_wait_time = 90
        self.attack = True
        self.target = "target"
        self.clicked = False
        self.damage_text_group = damage_text_group


class TestLevelAction(unittest.TestCase):
    def setUp(self):
        self.screen = pygame.display.set_mode((800, 1000))
        self.level_data = StubLevelData(pygame.sprite.Group())
        self.time = pygame.time.get_ticks()
        self.level_action = LevelAction(self.level_data)
        self.sword_icon = StubSwordIcon()
        self.knight = StubKnight()
        self.enemy = StubDeathBringer()
        self.enemy_2 = StubImpAxe()
        self.sprites = pygame.sprite.Group(
            self.knight, self.enemy, self.enemy_2)
        self.enemies = [self.enemy, self.enemy_2]

    @patch("pygame.mouse.get_pos")
    def test_player_action_sword_icon_shows(self, mock_mouse_pos):
        mock_mouse_pos.return_value = (200, 300)
        self.level_action.player_action(
            self.sword_icon, self.enemies, self.sprites)
        self.assertEqual(self.sword_icon.show, True)

    def test_knight_can_attack(self):
        self.level_action.knight_action(self.knight, self.time)

        self.assertEqual(self.knight.attack_value, True)

    def test_knight_can_not_attack_if_not_alive(self):
        self.knight.is_alive = False

        self.level_action.knight_action(self.knight, self.time)

        self.assertEqual(self.knight.attack_value, False)

    def test_enemy_can_attack_if_knight_is_alive(self):
        self.level_data.current_fighter = 2
        self.level_action.enemy_action(self.knight, self.enemies, self.time)

        self.assertEqual(self.enemy.attack_value, True)

    def test_enemy_2_can_attack_if_enemy_1_not_alive(self):
        self.level_data.current_fighter = 2
        self.enemy.is_alive = False
        self.level_action.enemy_action(self.knight, self.enemies, self.time)

        self.assertEqual(self.enemy_2.attack_value, True)
