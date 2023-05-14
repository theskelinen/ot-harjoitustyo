import pygame
import unittest
from unittest.mock import patch
from states.game import Game


class StubPanel:
    def __init__(self):
        self.name = "paneli"
        self.drawn = False

    def draw(self, screen):
        self.drawn = True


class StubLevel:
    def __init__(self):
        self.name = "leveli"
        self.updated = False
        self.drawn = False
        self.failed = False

    def update(self):
        self.updated = True

    def draw(self, screen):
        self.drawn = True


class StubEvent:
    def __init__(self, event_type, key):
        self.type = event_type
        self.key = key


class TestGameRunner(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.level = StubLevel()
        self.panel = StubPanel()
        self.state = Game(self.level, self.panel)

    def test_can_update_level(self):

        self.state.level.update()
        self.assertTrue(self.state.level.updated)

    def test_can_get_event(self):
        self.state.get_event(StubEvent(pygame.KEYDOWN, pygame.K_m))
        self.assertTrue(self.state.done)

    def test_can_draw(self):
        screen = "screeni"
        self.state.draw(screen)
        self.assertTrue(self.level.drawn)
        self.assertTrue(self.panel.drawn)
