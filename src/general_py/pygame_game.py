import sys, pygame
from pygame.locals import *

class PygameGame:
    def __init__(self):
        pygame.init()
        self.size = self.width, self.height = 640, 480
        self.black = 0, 0, 0
        self.screen = pygame.display.set_mode(self.size)

    def run(self):
        while 1:
            for event in pygame.event.get():
                if event.type == QUIT: sys.exit()

            self.screen.fill(self.black)
            pygame.display.flip()

if __name__ == '__main__':
    game = PygameGame()
    game.run()