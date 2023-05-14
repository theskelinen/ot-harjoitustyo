from kink import inject


@inject
class LevelData:

    """
    Pelin tason datasta vastaava luokka

    Args:
        damage_text_group: vahinkotekstin ryhmä
        you_died: "you died" kuva
    """

    def __init__(self, damage_text_group, you_died):
        """
        Parametrit:
                current_fighter: lyöntivuorossa oleva hahmo
                total_fighters: kaikki tason hahmot
                action_cooldown: hahmon toiminnan latautumisaika
                action_wait_time: hahmon vuoron latautumisaika
                attack: iskeekö hahmo vai ei
                target: iskun kohde
                clicked: onko pelaaja klikannut hiirellä
                damage_text_group: vahinkotekstin ryhmä
                you_died: "you died" kuva
        """

        self.current_fighter = 1
        self.total_fighters = 0
        self.action_cooldown = 0
        self.action_wait_time = 90
        self.attack = False
        self.target = None
        self.clicked = False
        self.damage_text_group = damage_text_group
        self.you_died = you_died

    def restart(self):
        """
        tason datan alustus uudelleenkäynnistyksen myötä

        """

        self.current_fighter = 1
        self.action_cooldown = 0

    def reset(self):
        """
        tason datan alustus tason läpäisyn myötä

        """

        self.current_fighter = 1
        self.action_cooldown = 0
        self.total_fighters = 0
        self.action_cooldown = 0
        self.action_wait_time = 90
        self.attack = False
        self.target = None
        self.clicked = False
