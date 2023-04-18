import pygame


class Level:
    def __init__(self, player, room):
        self.current_room = room
        self.player = player
        self.room_background = self._load_room_background()
        self.current_fighter = 1
        self.total_fighters = 0
        self.action_cooldown = 0
        self.action_wait_time = 90
        self.attack = False
        self.target = None
        self.clicked = False
        self.enemies_list = []
        self.sprites_list = pygame.sprite.Group()

        self._add_sprite(player)
        self._add_enemy()

    def _load_room_background(self):
        img = self.current_room.room.get("background")
        background = pygame.image.load(
            f"src/assets/Background/{img}.png").convert_alpha()
        background = pygame.transform.scale(background, (1280, 640))
        return background

    def _add_enemy(self):
        for key, value in self.current_room.room.items():
            if key == "enemies":
                for enemy in value:
                    self.enemies_list.append(enemy)
                    self._add_sprite(enemy)

    def _add_sprite(self, sprite):
        self.sprites_list.add(sprite)
        self.total_fighters += 1

    def player_action(self, player, current_time):
        if player.alive:
            if self.current_fighter == 1:
                self.action_cooldown += 1
                if self.action_cooldown >= self.action_wait_time:
                    if self.attack and self.target is not None:
                        player.attack(self.target, current_time)
                        self.current_fighter += 1
                        self.action_cooldown = 0

    def enemy_action(self, player, current_time):
        for count, enemy in enumerate(self.enemies_list):
            if self.current_fighter == 2 + count:
                if enemy.alive:
                    self.action_cooldown += 1
                    if self.action_cooldown >= self.action_wait_time:
                        if player.alive:
                            enemy.attack(player, current_time)
                            self.current_fighter += 1
                            self.action_cooldown = 0
                else:
                    self.current_fighter += 1

            if self.current_fighter > self.total_fighters:
                self.current_fighter = 1
