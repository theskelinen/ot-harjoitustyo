import pygame
from sprites.character import Character


class Knight(Character):
    def __init__(self):
        """
        Parametrit:
                    name: hahmo nimi
                    max_hp: maksimi elämäpisteet
                    current_hp: nykyiset elämäpisteet
                    strength: voima, kuinka paljon vahinkoa hahmo tekee
                    multiplier_min: iskuvoiman minimikerroin
                    multiplier_max: iskuvoiman maksimikerroin
                    rect_center: kuvan sijainnin keskittäminen
        """

        self.name = "Knight"
        self.max_hp = 55
        self.current_hp = 55
        self.strength = 13
        self.multiplier_min = -5
        self.multiplier_max = 5
        super().__init__()
        self.rect.center = (200, 600)

    def _load_ready_images(self):
        """
        Metodi "ready" kuvien lataamiseksi. Alla vastaavat metodit muille kuville.

        """

        temp_list = []
        for i in range(0, 8):
            img = pygame.image.load(
                f"src/assets/{self.name}/HeroKnight_Idle_{i}.png").convert_alpha()
            img = pygame.transform.scale(
                img, (img.get_width() * 4, img.get_height() * 4))
            temp_list.append(img)
        self.animation_list.append(temp_list)

    def _load_attack_images(self):
        temp_list = []
        for i in range(0, 8):
            img = pygame.image.load(
                f"src/assets/{self.name}/HeroKnight_Attack3_{i}.png").convert_alpha()
            img = pygame.transform.scale(
                img, (img.get_width() * 4, img.get_height() * 4))
            temp_list.append(img)
        self.animation_list.append(temp_list)

    def _load_hit_images(self):
        temp_list = []
        for i in range(0, 3):
            img = pygame.image.load(
                f"src/assets/{self.name}/HeroKnight_Hurt_{i}.png").convert_alpha()
            img = pygame.transform.scale(
                img, (img.get_width() * 4, img.get_height() * 4))
            temp_list.append(img)
        self.animation_list.append(temp_list)

    def _load_block_images(self):
        temp_list = []
        for i in range(0, 5):
            img = pygame.image.load(
                f"src/assets/{self.name}/HeroKnight_Block_{i}.png").convert_alpha()
            img = pygame.transform.scale(
                img, (img.get_width() * 4, img.get_height() * 4))
            temp_list.append(img)
        self.animation_list.append(temp_list)

    def _load_death_images(self):
        temp_list = []
        for i in range(0, 10):
            img = pygame.image.load(
                f"src/assets/{self.name}/HeroKnight_Death_{i}.png").convert_alpha()
            img = pygame.transform.scale(
                img, (img.get_width() * 4, img.get_height() * 4))
            temp_list.append(img)
        self.animation_list.append(temp_list)

    def _load_run_images(self):
        temp_list = []
        for i in range(0, 10):
            img = pygame.image.load(
                f"src/assets/{self.name}/HeroKnight_Run_{i}.png").convert_alpha()
            img = pygame.transform.scale(
                img, (img.get_width() * 4, img.get_height() * 4))
            temp_list.append(img)
        self.animation_list.append(temp_list)

    def block(self, current_time):
        """
        Metodi iskun torjumiseen

        """

        self.action = 4
        self.frame_index = 0
        self.update_time = current_time

    def run(self, current_time):
        """
        Metodi hahmon juoksemiseen

        """

        self.action = 5
        self.frame_index = 0
        self.update_time = current_time

    def reset(self):
        """
        Metodi hahmon tilan resetoimiseksi

        """

        self.is_alive = True
        self.current_hp = self.max_hp
        self.running = False
        self.rect.center = (200, 600)
        self.kill_count = 0
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
