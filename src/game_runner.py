import sys
import pygame
from kink import inject


@inject
class GameRunner():

    """
    Pelin pyörittämisestä vastaava luokka

    Args:
        screen: peli-ikkuna
        states: pelin eri tilat
        start_state: aloitustila
        clock: pelikello

    """

    def __init__(self, screen, states, start_state, clock):
        """
        Parametrit:
                    screen: näyttö
                    states: sanakirja tiloista
                    start_state: aloitustila
                    clock: pelikello
                    fps: kellotaajuus
                    state_name: tilan nimi
                    state: nykytila
                    state.start: käynnistää aloitustilan
        """

        self.screen = screen
        self.states = states
        self.start_state = start_state
        self.clock = clock
        self.fps = 60
        self.state_name = None
        self.state = self.states[self.start_state]
        self.state.start()

    def run(self):
        """
        Metodi vastaa pelin pyörittämisestä while loopin avulla

        """

        running = True
        while running:
            self.clock.tick(self.fps)
            self.get_events()
            self.update()
            self.draw()
            pygame.display.update()

    def get_events(self):
        """
        Metodi vastaa pelin tapahtumien hakemisesta

        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.quit()

            self.state.get_event(event)

    def update(self):
        """
        Metodi vastaa pelitapahtumien päivittämisestä ja kutsuu tarvittaessa seuraavaa pelitilaa

        """

        self.state.update()
        if self.state.done:
            self.next_state()

    def next_state(self):
        """
        Metodi vastaa seuraavan tilan vaihtamisesta

        """

        next_state = self.state.next_state
        self.state.done = False
        self.state_name = next_state
        self.state = self.states[self.state_name]
        self.state.start()

    def quit(self):
        """
        Metodi sulkee pelin kutsuttaessa

        """

        pygame.quit()
        sys.exit()

    def draw(self):
        """
        Metodi vastaa pelin kuvien ja tapahtumien piirtämisestä

        """

        self.state.draw(self.screen)
