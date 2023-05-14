import pygame
from kink import inject


@inject
class Room:

    """
    Luokka, joka vastaa huoneesta

    Args:
        enemies_list: lista vihollisista

    """

    def __init__(self, enemies_list):
        """
        Parametrit:
                    enemies_list: lista vihollisista
                    rooms_list: lista alustetuista huoneista
                    room_number: nykyisen huoneen numero
                    room: nykyinen huone
                    room_background: huoneen tausta
                    floor: huoneen lattia
        """

        self.enemies_list = enemies_list
        self.rooms_list = self._initialize_rooms()
        self.room_number = 0
        self.room = self.rooms_list[self.room_number]
        self.room_background = self.load_room_background()
        self.floor = self.load_floor()

    def _initialize_rooms(self):
        """
        huoneen alustaminen

        """

        list_of_rooms = []
        for i in range(2):
            enemies = self.enemies_list
            if i == 0:
                enemies = self.enemies_list[i]
            background = f"background_{i}"
            room = {"background": background,
                    "enemies": enemies
                    }
            list_of_rooms.append(room)
        return list_of_rooms

    def load_room_background(self):
        img = self.room.get("background")
        background = pygame.image.load(
            f"src/assets/Background/{img}.png").convert_alpha()
        background = pygame.transform.scale(background, (1280, 640))
        return background

    def load_floor(self):
        floor = pygame.image.load(
            "src/assets/Background/ground.png").convert_alpha()
        floor = pygame.transform.scale(floor, (1280, 80))
        return floor

    def next_room(self):
        """
        seuraavan huoneen lataaminen

        """

        self.room_number += 1
        self.room = self.rooms_list[self.room_number]
        self.room_background = self.load_room_background()

    def draw(self, screen):
        screen.blit(self.room_background, (0, 0))
        screen.blit(self.floor, (0, 640))
