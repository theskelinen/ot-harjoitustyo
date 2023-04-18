import pygame
import pygame.font
from level import Level
from game_loop import GameLoop
from load_assets import LoadAsset
from renderer import Renderer
from clock import Clock
from sprites.player import Player
from sprites.imp_axe import ImpAxe
from sprites.death_bringer import DeathBringer
from sprites.sword import SwordIcon
from room import Room
from event_queue import EventQueue
from healthbar import HealthBar


def main():
    bottom_panel = 150
    screen_width = 1280
    screen_height = 720 + bottom_panel
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.font.init()
    font = pygame.font.SysFont("Arial", 20)
    red = (255, 0, 0)
    green = (0, 255, 0)

    pygame.display.set_caption("Luolasto")

    player = Player(200, 600, "Knight", 30, 15)
    enemy_1 = ImpAxe(800, 540, "Imp_axe", 25, 4)
    enemy_2 = DeathBringer(980, 300, "Death_Bringer", 25, 5)

    enemies = [enemy_1, enemy_2]

    player_health_bar = HealthBar(
        200, screen_height-bottom_panel + 40, player.hp, player.max_hp)
    enemy_1_health_bar = HealthBar(
        900, screen_height-bottom_panel + 40, enemy_1.hp, enemy_1.max_hp)
    enemy_2_health_bar = HealthBar(
        900, screen_height-bottom_panel + 40, enemy_2.hp, enemy_2.max_hp)

    health_bar_dict = {}
    health_bar_dict[player.name] = player_health_bar
    health_bar_dict[enemy_1.name] = enemy_1_health_bar
    health_bar_dict[enemy_2.name] = enemy_2_health_bar

    room = Room(enemies)
    level = Level(player, room)
    assets = LoadAsset()
    sword_icon = SwordIcon()
    renderer = Renderer(screen, level, assets, sword_icon,
                        health_bar_dict, font, red, green)
    clock = Clock()
    event_queue = EventQueue()
    game_loop = GameLoop(renderer, clock, level, event_queue)

    pygame.init()
    game_loop.start()


if __name__ == "__main__":
    main()
