import pygame
from kink import di
from sprites.knight import Knight
from sprites.imp_axe import ImpAxe
from sprites.death_bringer import DeathBringer
from sprites.sword import SwordIcon
from game_files.level.room import Room
from game_files.level.level import Level
from game_files.level.level_data import LevelData
from game_files.level.level_action import LevelAction
from game_files.ui.healthbar import HealthBar
from game_files.ui.panel import Panel


def bootstrap_di():

    """
    Tämä funktio alustaa dependancy injection containerin

    """    

    panel_img = load_panel()

    you_died_img = load_you_died()

    font = pygame.font.SysFont("Verdana", 20)

    clock = pygame.time.Clock()

    knight = Knight()

    imp_axe = ImpAxe()

    death_bringer = DeathBringer()

    enemies = [imp_axe, death_bringer]

    sword_icon = SwordIcon()

    sprites = pygame.sprite.Group()

    damage_text_group = pygame.sprite.Group()

    room = Room(enemies)

    level_data = LevelData(damage_text_group, you_died_img)

    level_action = LevelAction(level_data)

    level = Level(room, knight, sword_icon, level_data, level_action, sprites)

    hb_dict = {knight.name: HealthBar(200, knight.current_hp, knight.max_hp),
               imp_axe.name: HealthBar(900, imp_axe.current_hp, imp_axe.max_hp,),
               death_bringer.name: HealthBar(900, death_bringer.current_hp, death_bringer.max_hp)}

    panel = Panel(sprites, font, hb_dict, panel_img)

    di["panel_img"] = panel_img

    di["font"] = font

    di["clock"] = clock

    di["knight"] = knight

    di["enemies"] = enemies

    di["sword_icon"] = sword_icon

    di["sprites"] = sprites

    di["damage_text_group"] = damage_text_group

    di["room"] = room

    di["level_data"] = level_data

    di["level_action"] = level_action

    di["level"] = level

    di["hb_dict"] = hb_dict

    di["panel"] = panel


def load_panel():
    panel = pygame.image.load(
        "src/assets/Panel/panel.png").convert_alpha()
    panel = pygame.transform.scale(panel, (1280, 150))
    return panel


def load_you_died():
    img = pygame.image.load(
        "src/assets/Others/you_died.png").convert_alpha()
    img = pygame.transform.scale(
        img, (img.get_width() * 0.7, img.get_height() * 0.7))
    return img
