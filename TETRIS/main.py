from settings import *
from sys import exit

# componens
from game import Game

class Main:
    def __init__(self):

        # general
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Tetris')

        # components
        self.game = Game()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # display
            self.display_surface.fill(GRAY)

            self.game.run()

            # updating game
            pygame.display.update()
            self.clock.tick(60)


if __name__ == '__main__':
    main = Main()
    main.run()
