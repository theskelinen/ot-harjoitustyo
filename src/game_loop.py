import pygame


class GameLoop:
    def __init__(self, renderer, clock, level, event_queue):
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self._level = level
        self._enemies_list = self._level.enemies_list

    def start(self):
        fps = 60
        run = True
        while run:
            current_time = self._clock.get_ticks()

            self._level.attack = False
            self._level.target = None
            self._renderer.show_sword_icon = False
            pygame.mouse.set_visible(True)
            pos = pygame.mouse.get_pos()
            for count, enemy in enumerate(self._enemies_list):
                # check if mouse collides with enemy so right target is chosen for health loss
                if enemy.rect.collidepoint(pos):
                    # check if masked rectangles collide with each other for correct hit box
                    if pygame.sprite.spritecollide(self._renderer._sword_icon, self._level.sprites_list, False, pygame.sprite.collide_mask):
                        pygame.mouse.set_visible(False)
                        self._renderer.show_sword_icon = True
                        if self._level.clicked:
                            self._level.attack = True
                            self._level.target = self._enemies_list[count]
                            self._level.clicked = False

            for sprite in self._level.sprites_list:
                sprite.update(current_time)

            self._renderer._sword_icon.update()

            self._level.player_action(self._level.player, current_time)

            self._level.enemy_action(self._level.player, current_time)

            for event in self._event_queue.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self._level.clicked = True

            self._render()
            self._clock.tick(fps)

    pygame.quit()

    def _render(self):
        self._renderer.render()
