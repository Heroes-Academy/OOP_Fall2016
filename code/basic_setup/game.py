import pygame
from settings import *
from heros import *
from walls import *


class Game:
    def __init__(self):
        
        self.walls = []
        self.hero = None
        self.done = False
        
        pygame.init()
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(TITLE)

    def run(self):
        while not self.done:
            #### EVENT CHECK SECTION
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                elif:
                    self.handle_event(event)
                    
            ### clear the screen
            self.screen.fill(WHITE)
        
            #### make the hero move
        
            if self.hero is not None:
                self.hero.update(self.walls)
                self.hero.draw(self.screen)
                
            #### FINISHING CODE
            pygame.display.flip()
            # --- Limit to 60 frames per second
            self.clock.tick(FPS)
        
        # Close the window and quit.
        pygame.quit()
        
    def handle_event(self, event):
        ## any events like keyboard handling should go here 
        pass

    def make_everything(self):
        ## your code for making the things goes here
        ## this should be walls, hero, etc
        pass
        