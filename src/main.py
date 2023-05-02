import pygame
from game_runner import GameRunner
from states.game import Game
from states.menu import Menu
from states.splash import Splash
from states.intro import Intro
from bootstrap import bootstrap_di

pygame.init()
bottom_panel = 150
screen_width = 1280
screen_height = 720 + bottom_panel
screen = pygame.display.set_mode((screen_width, screen_height))
bootstrap_di()


if __name__ == "__main__":
    states = {
        "Menu": Menu(),
        "Game": Game(),
        "Intro": Intro(),
        "Splash": Splash()
    }

    game = GameRunner(screen, states, "Menu")
    game.run()
