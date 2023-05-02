from kink import inject


@inject
class LevelData:
    def __init__(self, damage_text_group):
        self.current_fighter = 1
        self.total_fighters = 0
        self.action_cooldown = 0
        self.action_wait_time = 90
        self.attack = False
        self.target = None
        self.clicked = False
        self.damage_text_group = damage_text_group
