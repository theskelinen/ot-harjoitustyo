from .game_state import GameState


class Splash(GameState):
    def __init__(self):
        super(Splash, self).__init__()
        self.title = self.font.render("Luolasto", True, self.white)
        self.title_rect = self.title.get_rect(center=self.screen_rect.center)
        self.next_state = "Game"
        self.time_active = 0

    def update(self):
        self.time_active += 30
        if self.time_active >= 4000:
            self.done = True

    def draw(self, surface):
        surface.fill(self.black)
        surface.blit(self.title, self.title_rect)
