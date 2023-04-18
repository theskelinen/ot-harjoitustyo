import random
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, name, max_hp, strength):
        super().__init__()

        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.alive = True
        self.remove_sprite = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        self._initialize_images()
        self.image = self.animation_list[self.action][self.frame_index]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)

    def _initialize_images(self):
        self._load_ready_images()
        self._load_attack_images()
        self._load_block_images()
        self._load_hit_images()
        self._load_death_images()

    def _load_ready_images(self):
        temp_list = []
        for i in range(1, 8):
            img = pygame.image.load(
                f"src/assets/{self.name}/HeroKnight_Idle_{i}.png").convert_alpha()
            img = pygame.transform.scale(
                img, (img.get_width() * 4, img.get_height() * 4))
            temp_list.append(img)
        self.animation_list.append(temp_list)

    def _load_attack_images(self):
        temp_list = []
        for i in range(1, 8):
            img = pygame.image.load(
                f"src/assets/{self.name}/HeroKnight_Attack3_{i}.png").convert_alpha()
            img = pygame.transform.scale(
                img, (img.get_width() * 4, img.get_height() * 4))
            temp_list.append(img)
        self.animation_list.append(temp_list)

    def _load_hit_images(self):
        temp_list = []
        for i in range(1, 3):
            img = pygame.image.load(
                f"src/assets/{self.name}/HeroKnight_Hurt_{i}.png").convert_alpha()
            img = pygame.transform.scale(
                img, (img.get_width() * 4, img.get_height() * 4))
            temp_list.append(img)
        self.animation_list.append(temp_list)

    def _load_block_images(self):
        temp_list = []
        for i in range(1, 5):
            img = pygame.image.load(
                f"src/assets/{self.name}/HeroKnight_Block_{i}.png").convert_alpha()
            img = pygame.transform.scale(
                img, (img.get_width() * 4, img.get_height() * 4))
            temp_list.append(img)
        self.animation_list.append(temp_list)

    def _load_death_images(self):
        temp_list = []
        for i in range(1, 10):
            img = pygame.image.load(
                f"src/assets/{self.name}/HeroKnight_Death_{i}.png").convert_alpha()
            img = pygame.transform.scale(
                img, (img.get_width() * 4, img.get_height() * 4))
            temp_list.append(img)
        self.animation_list.append(temp_list)

    def update(self, current_time):
        animation_cooldown = 100
        self.image = self.animation_list[self.action][self.frame_index]
        if current_time - self.update_time > animation_cooldown:
            self.update_time = current_time
            self.frame_index += 1
            if self.frame_index >= len(self.animation_list[self.action]):
                if self.alive:
                    self.ready(current_time)
                else:
                    self.die(current_time)

    def ready(self, current_time):
        self.action = 0
        self.frame_index = 0
        self.update_time = current_time

    def attack(self, target, current_time):
        rand = random.randint(-5, 5)
        damage = self.strength + rand
        target.hp -= damage
        if target.hp < 1:
            target.hp = 0
            target.alive = False
        self.action = 1
        self.frame_index = 0
        self.update_time = current_time

    def die(self, current_time):
        if self.remove_sprite:
            self.kill()
        self.action = 4
        self.frame_index = 0
        self.update_time = current_time
        self.remove_sprite = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)
