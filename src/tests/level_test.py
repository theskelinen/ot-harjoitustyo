import pygame
import unittest
from game_files.level.level import Level


class StubLevelKnight(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.kill_count = 0
        self.running = False
        self.action = 1
        self.image = pygame.image.load(
            "src/assets/Knight/HeroKnight_Idle_1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (200, 600)

    def reset(self):
        pass


class StubLevelEnemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def reset(self):
        pass


class StubSwordIcon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


class StubLevelData:
    def __init__(self):
        self.damage_text_group = pygame.sprite.Group()
        self.total_fighters = 0

    def restart(self):
        pass


class StubLevelAction:
    def __init__(self, level_data):
        self.level_data = level_data

    def enemy_action(self, knight, enemies_list, current_time):
        pass

    def knight_action(self, knight, current_time):
        pass

    def player_action(self, sword_icon, enemies_list, sprites):
        pass


class StubRoom:
    def __init__(self):
        self.enemy = StubLevelEnemy()
        self.room = {"enemies": self.enemy}


class TestLevel(unittest.TestCase):
    def setUp(self):
        self.room = StubRoom()
        self.knight = StubLevelKnight()
        self.enemy = self.room.enemy
        self.sword_icon = StubSwordIcon()
        self.level_data = StubLevelData()
        self.level_action = StubLevelAction(self.level_data)
        self.sprites = pygame.sprite.Group()

        self.level = Level(self.room, self.knight, self.sword_icon,
                           self.level_data, self.level_action, self.sprites)

    def test_can_add_enemies_to_list(self):
        self.assertEqual(self.level._enemies_list, [self.enemy])

    def test_can_add_sprite_to_sprites(self):
        self.assertEqual(len(self.level.sprites), len(self.sprites))

    def test_can_restart_level(self):
        self.level.failed = True
        self.level.restart()
        self.assertFalse(self.level.failed)
