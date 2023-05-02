import pygame
from kink import inject


@inject
class Level:
    def __init__(self, room, knight, sword_icon, level_data, level_action, sprites):
        self.room = room
        self.knight = knight
        self.sword_icon = sword_icon
        self.level_data = level_data
        self.level_action = level_action
        self._enemies_list = []
        self.sprites = sprites

        self._initialize_sprites()

    def _initialize_sprites(self):
        self._add_sprite(self.knight)
        self._add_enemies()

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
        self.room.draw(screen)
        self.sprites.draw(screen)
        self.sprites.draw(screen)
        self.sword_icon.draw(screen)
        self.level_data.damage_text_group.draw(screen)
