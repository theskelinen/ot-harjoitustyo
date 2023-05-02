import pygame
from kink import inject


@inject
class Room:
    def __init__(self, enemies_list):
        self.enemies_list = enemies_list
        self.rooms_list = self._initialize_rooms()
        self.room_number = 1
        self.room = self.rooms_list[self.room_number]
        self.room_background = self.load_room_background()
        self.floor = self.load_floor()

    def _initialize_rooms(self):
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
        self.room_number += 1
        self.room_background = self.load_room_background()

    def draw(self, screen):
        screen.blit(self.room_background, (0, 0))
        screen.blit(self.floor, (0, 640))
