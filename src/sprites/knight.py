from sprites.character import Character
import pygame


class Knight(Character):
    def __init__(self):
        self.name = "Knight"
        self.max_hp = 100
        self.current_hp = 100
        self.strength = 10
        self.multiplier_min = -5
        self.multiplier_max = 5
        super().__init__()
        self.rect.center = (200, 600)

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

    def block(self, current_time):
        self.action = 4
        self.frame_index = 0
        self.update_time = current_time
