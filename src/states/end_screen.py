from .game_state import GameState


class EndScreen(GameState):

    """
    Pelitila, joka vastaa pelin päättävästä ruudusta

    """

    def __init__(self):
        """
        Parametrit:
                    title_1: str
                        onnistteluteksti
                    title_2: str
                        käyttäjäohje syötteelle
        """

        super().__init__()
        self.title_1 = self.font.render("Congratulations", True, self.white)
        self.title_2 = self.font.render(
            "You made it outside! Press q to close the game window", True, self.white)

    def draw(self, screen):
        """
        Metodi vastaa tilan titlen piirtämisestä

        """

        screen.fill(self.black)
        screen.blit(self.title_1, (100, 100))
        screen.blit(self.title_2, (100, 140))
