import pygame
from kink import inject


@inject
class Level:

    """
    Pelin tasosta vastaava luokka

    Args:
        room: huoneen luokkaobjekti
        knight: pelaajahahmon luokkaobjekti
        sword_icon: kursorin ikonin luokkaobjekti
        level_data: tason datan luokkaobjekti
        level_action: tason toiminnan luokkaobjekti
        sprites: sprite-ryhmä
    """

    def __init__(self, room, knight, sword_icon, level_data, level_action, sprites):
        """
        Parametrit:
                room: tason huone
                knight: pelaajahahmo
                sword_icon: kursorin miekkaikoni
                level_data: tason toiminnasta vastaava data
                level_action: tason hahmojen toiminnasta vastaava luokka
                enemies_list: lista tason vihollisista
                sprites: tason spritet
                completed: onko taso läpi vai ei
                failed: onko taso hävitty vai ei
                game_completed: onko peli läpäisty
        """

        self.room = room
        self.knight = knight
        self.sword_icon = sword_icon
        self.level_data = level_data
        self.level_action = level_action
        self._enemies_list = []
        self.sprites = sprites
        self.completed = False
        self.failed = False
        self.game_completed = False

        self.initialize_level()

    def initialize_level(self):
        """
        tason alustaminen

        """

        self.completed = False
        self._add_sprite(self.knight)
        self._add_enemies()
        self.reset_sprites()

    def _add_enemies(self):
        """
        tason vihollisten lisääminen

        """

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
        """
        tason spritejen lisääminen

        """

        self.sprites.add(sprite)
        self.level_data.total_fighters += 1

    def level_complete(self):
        """
        tason läpäisemisen tarkistus ja toteutus

        """

        if self.knight.kill_count == len(self._enemies_list):
            self.knight.running = True
            if self.knight.action == 5:
                self.knight.rect.x += 4.5
            if self.knight.rect.x >= 1280:
                self.knight.running = False
                self.completed = True
                self.level_data.reset()
                self.sprites.empty()
                self._enemies_list = []
                self.game_complete()
                if not self.game_completed:
                    self.room.next_room()

    def game_complete(self):
        """
        pelin läpäisemisen tarkistus

        """

        if self.room.room_number >= 1:
            self.game_completed = True

    def level_fail(self):
        """
        tason häviämisen tarkistus

        """

        if not self.knight.is_alive:
            self.failed = True

    def restart(self):
        """
        tason uudelleenkäynnistys

        """

        if self.failed:
            self.reset_sprites()
            self.level_data.restart()
            self.failed = False

    def reset_sprites(self):
        """
        hahmojen resetointi

        """

        self.knight.reset()
        for enemy in self._enemies_list:
            enemy.reset()

    def update(self):
        """
        tason tilan päivittäminen

        """

        current_time = pygame.time.get_ticks()

        self.sprites.update(current_time)

        self.sword_icon.update()

        self.level_action.player_action(
            self.sword_icon, self._enemies_list, self.sprites)

        self.level_action.knight_action(self.knight, current_time)

        self.level_action.enemy_action(
            self.knight, self._enemies_list, current_time)

        self.level_data.damage_text_group.update()

        self.level_complete()

        self.level_fail()

    def draw(self, screen):
        """
        tason piirtäminen

        """

        self.room.draw(screen)
        self.sprites.draw(screen)
        self.sword_icon.draw(screen)
        self.level_data.damage_text_group.draw(screen)
