import sys
import pygame


class GameRunner(object):

    def __init__(self, screen, states, start_state):

        self.screen = screen
        self.states = states
        self.start_state = start_state
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.state_name = None
        self.state = self.states[self.start_state]
        self.state.start()
        self.run()

    def run(self):
        running = True
        while running:
            self.clock.tick(self.fps)
            self.get_events()
            self.update()
            self.draw()
            pygame.display.update()

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.quit()

            self.state.get_event(event)

    def update(self):
        self.state.update()
        if self.state.done:
            self.next_state()

    def next_state(self):
        next_state = self.state.next_state
        self.state.done = False
        self.state_name = next_state
        self.state = self.states[self.state_name]
        self.state.start()

    def quit(self):
        pygame.quit()
        sys.exit()

    def draw(self):
        self.state.draw(self.screen)
