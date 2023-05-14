class HealthBar():

    """
    Elämämittarin luokka

    Args:
        pos_x: mittarin x-koordinaatti
        pos_y: tekstin y-koordinaatti
        current_hp: nyky elämäpisteet
        max_hp: maksimi elämäpisteet
    """

    def __init__(self, pos_x, current_hp, max_hp):
        self.pos_x = pos_x
        self.pos_y = 760
        self.current_hp = current_hp
        self.max_hp = max_hp
