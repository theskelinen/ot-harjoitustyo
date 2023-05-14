from .game_state import GameState


class Splash(GameState):

    """
    Pelitila, joka toimii siirtymänä tasojen välillä

    """

    def __init__(self):
        """
        Parametrit:
                    level_number: tason numero
                    title: tason numerosta kertova teksti
                    title_rect: tekstin asemointi
                    next_state: seuraavan tason nimi
                    time_active: tekstin näkymisestä vastaava aika

        """

        super().__init__()
        self.level_number = 1
        self.title = self.font.render(
            f"Level {self.level_number}", True, self.white)
        self.title_rect = self.title.get_rect(center=self.screen_rect.center)
        self.next_state = "Game"
        self.time_active = 0

    def start(self):
        """
        Metodi vastaa tekstin aktiivisen ajan alustamisesta

        """

        self.time_active = 0

    def update(self):
        """
        Metodi vastaa tilan päivittämisestä

        """

        self.time_active += 30
        if self.time_active >= 4000:
            self.done = True
            self.level_number += 1
            self.title_update()

    def title_update(self):
        """
        Metodi vastaa titlen päivittämisestä

        """

        self.title = self.font.render(
            f"Level {self.level_number}", True, self.white)

    def draw(self, screen):
        """
        Metodi vastaa titlen piirtämisestä

        """

        screen.fill(self.black)
        screen.blit(self.title, self.title_rect)
