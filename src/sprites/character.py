import random
import pygame
from game_files.ui.damage_text import DamageText


class Character(pygame.sprite.Sprite):

    """
    Hahmojen parent class

    """

    def __init__(self):
        """
        Parametrit:
                    is_alive: onko hahmo hengissä
                    running: juokseeko hahmo
                    kill_count: kukistettujen vihollisten määrä
                    animation_list: lista hahmoanimaatioista
                    frame_index: pitää lukua animaation vaiheesta
                    action: hahmon toiminta
                    update_time: animaation päivitysaika
                    image: hahmoanimaation sen hetkinen kuva
                    mask: kuvan "naamiointi" collision detectiä varten
                    rect: kuvan sijainti ruudulla
        """

        super().__init__()

        self.is_alive = True
        self.running = False
        self.kill_count = 0
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        self._initialize_images()
        self.image = self.animation_list[self.action][self.frame_index]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

    def _initialize_images(self):
        """
        Metodi animaatiokuvien alustamiseksi

        """

        self._load_ready_images()
        self._load_attack_images()
        self._load_hit_images()
        self._load_death_images()
        self._load_block_images()
        self._load_run_images()

    def update(self, current_time):
        """
        Metodi hahmon toiminnan päivittämiseksi

        """

        animation_cooldown = 140
        self.image = self.animation_list[self.action][self.frame_index]
        if current_time - self.update_time > animation_cooldown:
            self.update_time = current_time
            self.frame_index += 1
            if self.frame_index >= len(self.animation_list[self.action]):
                if self.action == 3:
                    self.frame_index = len(
                        self.animation_list[self.action]) - 1
                else:
                    if self.running:
                        self.run(current_time)
                    else:
                        self.ready(current_time)

    def ready(self, current_time):
        """
        Metodi "ready" toiminnon käynnistämiseksi

        """

        self.action = 0
        self.frame_index = 0
        self.update_time = current_time

    def hit(self, current_time):
        """
        Metodi "hit" toiminnon käynnistämiseksi

        """

        self.action = 2
        self.frame_index = 0
        self.update_time = current_time

    def block(self, current_time):
        pass

    def run(self, current_time):
        """
        Metodi "run" toiminnon käynnistämiseksi

        """

        self.action = 0
        self.frame_index = 0
        self.update_time = current_time

    def attack(self, target, damage_text_group, current_time):
        """
        Metodi vastustajan iskemiseksi

        Args:
            target: iskun kohde
            damage_text_group: vahinkotekstin ryhmä
            current_time: iskun hetki
        """

        damage_multiplier = random.randint(
            self.multiplier_min, self.multiplier_max)
        damage = self.strength + damage_multiplier
        target.current_hp -= damage
        if target.current_hp < 1:
            self.kill_count += 1
            target.current_hp = 0
            target.is_alive = False
            target.fall(current_time)
        if target.is_alive:
            if damage_multiplier < 0:
                target.block(current_time)
            else:
                target.hit(current_time)
        damage_text = self.create_dmg_text(
            target.rect.centerx, target.rect.y, str(damage), (255, 0, 0))
        damage_text_group.add(damage_text)
        if damage_multiplier == self.multiplier_max:
            critical_hit = self.create_dmg_text(
                (target.rect.centerx-40), (target.rect.y-40), "CRITICAL HIT", (255, 0, 0))
            damage_text_group.add(critical_hit)
        self.action = 1
        self.frame_index = 0
        self.update_time = current_time

    def create_dmg_text(self, pos_x, pos_y, string, colour):
        """
        Metodi vahinkotekstin luomiseksi

        Args:
            pos_x: tekstin x-koordinaatti
            pos_y: tekstin y-koordinaatti
            string: vahinkoteksti
            colour: tekstin väri
        """

        dmg_text = DamageText(pos_x, pos_y, string, colour)
        return dmg_text

    def fall(self, current_time):
        """
        Metodi "fall" toiminnon käynnistämiseksi

        """

        self.action = 3
        self.frame_index = 0
        self.update_time = current_time

    def reset(self):
        """
        Hahmon tilan resetointi

        """

        self.is_alive = True
        self.current_hp = self.max_hp
        self.kill_count = 0
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

    def draw(self, screen):
        """
        hahmon piirtäminen

        """

        screen.blit(self.image, self.rect)
