import pygame
from sprites.character import Character


class DeathBringer(Character):

    """
    Death_Bringer hahmoluokka

    """

    def __init__(self):
        """
        Parametrit: kts. yst. knight luokka.
        """

        self.name = "Death_Bringer"
        self.max_hp = 20
        self.current_hp = 20
        self.strength = 12
        self.multiplier_min = -5
        self.multiplier_max = 5
        super().__init__()
        self.rect.center = (980, 300)

    def _load_ready_images(self):
        temp_list = []
        for i in range(1, 9):
            img = pygame.image.load(
                f"src/assets/{self.name}/Idle/Bringer-of-Death_Idle_{i}.png").convert_alpha()
            img = pygame.transform.scale(
                img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)

    def _load_attack_images(self):
        temp_list = []
        for i in range(1, 11):
            img = pygame.image.load(
                f"src/assets/{self.name}/Attack/Bringer-of-Death_Attack_{i}.png").convert_alpha()
            img = pygame.transform.scale(
                img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)

    def _load_hit_images(self):
        temp_list = []
        for i in range(1, 4):
            img = pygame.image.load(
                f"src/assets/{self.name}/Hurt/Bringer-of-Death_Hurt_{i}.png").convert_alpha()
            img = pygame.transform.scale(
                img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)

    def _load_death_images(self):
        temp_list = []
        for i in range(1, 11):
            img = pygame.image.load(
                f"src/assets/{self.name}/Death/Bringer-of-Death_Death_{i}.png").convert_alpha()
            img = pygame.transform.scale(
                img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)

    def _load_block_images(self):
        pass

    def _load_run_images(self):
        pass
