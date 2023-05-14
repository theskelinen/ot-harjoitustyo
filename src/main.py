import pygame
from game_runner import GameRunner
from states.game import Game
from states.menu import Menu
from states.splash import Splash
from states.intro import Intro
from states.end_screen import EndScreen
from bootstrap import bootstrap_di

pygame.init()
pygame.display.set_caption("Luolasto")
BOTTOM_PANEL = 150
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720 + BOTTOM_PANEL
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
bootstrap_di()


if __name__ == "__main__":

    states = {
        "Menu": Menu(),
        "Game": Game(),
        "Intro": Intro(),
        "Splash": Splash(),
        "End_Screen": EndScreen()
    }

    game = GameRunner(screen, states, "Intro")
    game.run()
