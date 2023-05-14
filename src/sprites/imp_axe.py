import pygame
from sprites.character import Character


class ImpAxe(Character):

    """
    Imp_axe hahmoluokka

    """

    def __init__(self):
        """
        Parametrit: kts. yst. knight luokka.
        """

        self.name = "Imp_Axe"
        self.max_hp = 30
        self.current_hp = 30
        self.strength = 8
        self.multiplier_min = -2
        self.multiplier_max = 4
        super().__init__()
        self.rect.center = (800, 540)

    def _load_ready_images(self):
        temp_list = []
        for i in range(1, 4):
            img = pygame.image.load(
                f"src/assets/{self.name}/ready_{i}.png").convert_alpha()
            img = pygame.transform.scale(
                img, (img.get_width() * 5, img.get_height() * 5))
            temp_list.append(img)
        self.animation_list.append(temp_list)

    def _load_attack_images(self):
        temp_list = []
        for i in range(1, 7):
            img = pygame.image.load(
                f"src/assets/{self.name}/attack2_{i}.png").convert_alpha()
            img = pygame.transform.scale(
                img, (img.get_width() * 5, img.get_height() * 5))
            temp_list.append(img)
        self.animation_list.append(temp_list)

    def _load_hit_images(self):
        temp_list = []
        for i in range(1, 4):
            img = pygame.image.load(
                f"src/assets/{self.name}/hit_{i}.png").convert_alpha()
            img = pygame.transform.scale(
                img, (img.get_width() * 5, img.get_height() * 5))
            temp_list.append(img)
        self.animation_list.append(temp_list)

    def _load_death_images(self):
        temp_list = []
        for i in range(1, 5):
            img = pygame.image.load(
                f"src/assets/{self.name}/fall_back_{i}.png").convert_alpha()
            img = pygame.transform.scale(
                img, (img.get_width() * 5, img.get_height() * 5))
            temp_list.append(img)
        self.animation_list.append(temp_list)

    def _load_block_images(self):
        pass

    def _load_run_images(self):
        pass
