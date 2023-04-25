import random
import pygame
from game_files.ui.damage_text import DamageText


class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.alive = True
        self.remove_sprite = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        self._initialize_images()
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()

    def _initialize_images(self):
        self._load_ready_images()
        self._load_attack_images()
        self._load_hit_images()
        self._load_death_images()
        self._load_block_images()

    def update(self, current_time):
        animation_cooldown = 140
        self.image = self.animation_list[self.action][self.frame_index]
        if current_time - self.update_time > animation_cooldown:
            self.update_time = current_time
            self.frame_index += 1
            if self.frame_index >= len(self.animation_list[self.action]):
                if self.alive:
                    self.ready(current_time)
                else:
                    self.fall(current_time)

    def ready(self, current_time):
        self.action = 0
        self.frame_index = 0
        self.update_time = current_time

    def hit(self, current_time):
        self.action = 2
        self.frame_index = 0
        self.update_time = current_time

    def block(self, current_time):
        pass

    def attack(self, target, damage_text_group, current_time):
        damage_multiplier = random.randint(
            self.multiplier_min, self.multiplier_max)
        damage = self.strength + damage_multiplier
        target.current_hp -= damage
        if target.current_hp < 1:
            target.current_hp = 0
            target.alive = False
        if target.alive:
            if damage_multiplier < 0:
                target.block(current_time)
            else:
                target.hit(current_time)
        damage_text = DamageText(
            target.rect.centerx, target.rect.y, str(damage), (255, 0, 0))
        damage_text_group.add(damage_text)
        if damage_multiplier == self.multiplier_max:
            critical_hit = DamageText(
                (target.rect.centerx-40), (target.rect.y-40), "CRITICAL HIT", (255, 0, 0))
            damage_text_group.add(critical_hit)
        self.action = 1
        self.frame_index = 0
        self.update_time = current_time

    def fall(self, current_time):
        if self.remove_sprite:
            self.kill()
        self.action = 3
        self.frame_index = 0
        self.update_time = current_time
        self.remove_sprite = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
