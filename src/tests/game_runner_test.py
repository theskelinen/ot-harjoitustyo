import pygame
import unittest
from unittest.mock import patch
from game_runner import GameRunner


class Screen:
    def __init__(self):
        self.bottom_panel = 150
        self.screen_width = 1280
        self.screen_height = 720 + self.bottom_panel
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))


class StubState:
    def __init__(self):
        self.done = False
        self.font = "nice and stylish"
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.screen_rect = pygame.display.get_surface().get_rect()
        self.event_got = False
        self.updated = False
        self.next_state = "Game"

    def start(self):
        pass

    def update(self):
        self.updated = True

    def get_event(self, event):
        self.event_got = True

    def draw(self, surf):
        pass


class TestGameRunner(unittest.TestCase):
    def setUp(self):
        self.screen = Screen()
        self.clock = pygame.time.Clock()
        self.states = {
            "Menu": StubState(),
            "Game": StubState(),
            "Intro": StubState(),
            "Splash": StubState()
        }
        self.game_runner = GameRunner(
            self.screen, self.states, "Menu", self.clock)

    @patch("game_runner.GameRunner.get_events")
    def test_game_runs(self, replace_get_events_with_quit):
        with self.assertRaises(SystemExit) as cm:
            replace_get_events_with_quit.return_value = self.game_runner.quit()
            self.game_runner.run()
            self.assertEqual(cm.exception.code, 1)

    def test_can_get_events(self):
        self.game_runner.get_events()
        self.assertEqual(self.game_runner.state.event_got, True)

    def test_can_update_state(self):
        self.game_runner.update()
        self.assertEqual(self.game_runner.state.updated, True)

    def test_can_call_next_state(self):
        self.game_runner.state.done = True
        start_state = self.game_runner.state
        self.game_runner.update()
        self.assertNotEqual(self.game_runner.state, start_state)
