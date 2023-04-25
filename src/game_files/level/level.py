import pygame
from sprites.knight import Knight
from sprites.sword import SwordIcon
from game_files.level.room import Room
from game_files.level.level_data import LevelData
from game_files.level.level_action import LevelAction


class Level:
    def __init__(self):
        self.room = Room()
        self.room_background = self._load_room_background()
        self.floor = self._load_floor()
        self.knight = Knight()
        self.sword_icon = SwordIcon()
        self.level_data = LevelData()
        self.level_action = LevelAction(self.level_data)
        self._enemies_list = []
        self.sprites = pygame.sprite.Group()

        self._initialize_sprites()

    def _initialize_sprites(self):
        self._add_sprite(self.knight)
        self._add_enemies()

    def _load_room_background(self):
        img = self.room.room.get("background")
        background = pygame.image.load(
            f"src/assets/Background/{img}.png").convert_alpha()
        background = pygame.transform.scale(background, (1280, 640))
        return background

    def _load_floor(self):
        floor = pygame.image.load(
            "src/assets/Background/ground.png").convert_alpha()
        floor = pygame.transform.scale(floor, (1280, 80))
        return floor

    def _add_enemies(self):
        for key, value in self.room.room.items():
            if key == "enemies":
                try:
                    for enemy in value:
                        self._enemies_list.append(enemy)
                        self._add_sprite(enemy)
                # if only one enemy in a room
                except:
                    self._enemies_list.append(value)
                    self._add_sprite(value)

    def _add_sprite(self, sprite):
        self.sprites.add(sprite)
        self.level_data.total_fighters += 1

    def level_completed(self):
        if len(self._enemies_list) == 0:
            return True

    def update(self):
        current_time = pygame.time.get_ticks()

        # for sprite in self.sprites:

        self.sprites.update(current_time)

        self.sword_icon.update()

        self.level_action.player_action(
            self.sword_icon, self._enemies_list, self.sprites)

        self.level_action.knight_action(self.knight, current_time)

        self.level_action.enemy_action(
            self.knight, self._enemies_list, current_time)

        self.level_data.damage_text_group.update()

        self.level_completed()

    def draw(self, screen):
        screen.blit(self.room_background, (0, 0))
        screen.blit(self.floor, (0, 640))
        self.sprites.draw(screen)
        self.sword_icon.draw(screen)
        self.level_data.damage_text_group.draw(screen)
