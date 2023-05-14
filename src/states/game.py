import pygame
from kink import inject
from .game_state import GameState


@inject
class Game(GameState):

    """
    Pelitila, joka vastaa pelin tason hallinnasta

    Args:
        level: pelitaso
        panel: paneeli

    """

    def __init__(self, level, panel):
        """
        Parametrit:
                    level: pelitaso
                    panel: näyttöpaneeli
                    next_state: seuraavan tilan nimi
                    title: tilan teksti
                    title_rect: tilan tekstin asemointi
        """

        super().__init__()
        self.level = level
        self.panel = panel
        self.next_state = "Intro"
        self.title = self.font.render(
            "Press (r)estart or q(uit)", True, self.white)
        self.title_rect = self.title.get_rect(center=self.screen_rect.center)

    def start(self):
        """
        Metodi vastaa uuden tason käynnistämisestä

        """

        if self.level.completed:
            self.level.initialize_level()
        else:
            pass

    def update(self):
        """
        Metodi vastaa tason päivittämisestä

        """

        self.level.update()
        if self.level.completed:
            if self.level.game_completed:
                self.done = True
                self.next_state = "End_Screen"
            else:
                self.done = True
                self.next_state = "Intro"

    def get_event(self, event):
        """
        Metodi vastaa pelitapahtumista ja käyttäjän syötteistä

        """

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                self.next_state = "Menu"
                self.done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                self.level.restart()

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.level.level_data.clicked = True

    def draw(self, screen):
        """
        Metodi vastaa tason ja paneelin piirtämisestä

        """

        self.level.draw(screen)
        self.panel.draw(screen)
        if self.level.failed:
            screen.blit(self.level.level_data.you_died, (285, 0))
            screen.blit(self.title, self.title_rect)
