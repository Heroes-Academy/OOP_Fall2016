import pygame
from settings import *
from hero import *
from walls import *


class Game:
    def __init__(self):

        self.walls = None
        self.hero = None
        self.done = False

        pygame.init()
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(TITLE)

    def setup(self):
        self.hero = Hero(WIDTH/2,HEIGHT/2,10,10)
        self.walls = Walls()
        self.walls.platform_level()

    def run(self):
        while not self.done:
            #### EVENT CHECK SECTION
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                if self.hero is not None:
                    self.hero.handle_event(event)
                ## extra stuff will go here

            ### clear the screen
            self.screen.fill(WHITE)

            if self.walls is not None:
                self.walls.draw(self.screen)
                walls = self.walls.walls
            else:
                walls = []


            ## extra stuff will go here
            if self.hero is not None:
                self.hero.update(walls)
                self.hero.draw(self.screen)


            #### update the display and move forward 1 frame
            pygame.display.flip()
            # --- Limit to 60 frames per second
            self.clock.tick(FPS)
        pygame.quit()

game = Game()
game.setup()
game.run()