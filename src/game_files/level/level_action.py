import pygame
from kink import inject


@inject
class LevelAction:

    """
    Pelin tason hahmojen toiminnasta vastaava luokka

    Args:
        level_data: tason tilan data
    """

    def __init__(self, level_data):
        self.level_data = level_data

    def player_action(self, sword_icon, enemies_list, sprites):
        """
        Pelaajan toiminnan toteuttamisesta vastaava metodi

        Args:
            sword_icon: hiiren kursorin ikoni
            enemies_list: lista vihollisista
            sprites: tason hahmot

        """

        self.level_data.attack = False
        self.level_data.target = None
        sword_icon.show = False
        pygame.mouse.set_visible(True)
        pos = pygame.mouse.get_pos()
        for count, enemy in enumerate(enemies_list):
            # check if mouse collides with enemy so right target is chosen for health loss
            if enemy.rect.collidepoint(pos) and enemy.is_alive:
                # check if masked rectangles collide with each other for correct hit box
                if pygame.sprite.spritecollide(sword_icon, sprites, False, pygame.sprite.collide_mask):
                    for sprite in sprites:
                        if sprite.name != "Knight":
                            pygame.mouse.set_visible(False)
                            sword_icon.show = True
                    if self.level_data.clicked:
                        self.level_data.attack = True
                        self.level_data.target = enemies_list[count]
                        self.level_data.clicked = False

    def knight_action(self, knight, current_time):
        """
        Pelaajahahmon toiminnasta vastaava metodi

        Args:
            knight: pelaajahahmo
            current_time: nykyhetki

        """

        if knight.is_alive:
            if self.level_data.current_fighter == 1:
                self.level_data.action_cooldown += 1
                if self.level_data.action_cooldown >= self.level_data.action_wait_time:
                    if self.level_data.attack and self.level_data.target is not None:
                        knight.attack(
                            self.level_data.target, self.level_data.damage_text_group, current_time)
                        self.level_data.current_fighter += 1
                        self.level_data.action_cooldown = 0

    def enemy_action(self, knight, enemies_list, current_time):
        """
        Vihollishahmon toiminnasta vastaava metodi

        Args:
            knight: pelaajahahmo
            enemies_list: lista vihollisista
            current_time: nykyhetki

        """

        for count, enemy in enumerate(enemies_list):
            if self.level_data.current_fighter == 2 + count:
                if enemy.is_alive:
                    self.level_data.action_cooldown += 1
                    if self.level_data.action_cooldown >= self.level_data.action_wait_time:
                        if knight.is_alive:
                            enemy.attack(
                                knight, self.level_data.damage_text_group, current_time)
                            self.level_data.current_fighter += 1
                            self.level_data.action_cooldown = 0
                else:
                    self.level_data.current_fighter += 1

            if self.level_data.current_fighter > self.level_data.total_fighters:
                self.level_data.current_fighter = 1
