import pygame
from level import Level
from game_loop import GameLoop
from renderer import Renderer

def main():
    bottom_panel = 150
    screen_width = 1280
    screen_height = 720 + bottom_panel
    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption("Luolasto")

    level = Level()
    renderer = Renderer(screen, level)
    game_loop = GameLoop(renderer)

    pygame.init()
    game_loop.start()


if __name__ == "__main__":
    main()