from pygame.rect import Rect
from settings import *
import pygame

class Hero:
    def __init__(self, x, y, w, h):
        ''' The hero constructor function '''
        self.rect = Rect(x, y, w, h)
        self.dx = 0
        self.dy = 9
        self.ddy = 0
        self.bouncy = False
        self.update_gravity = True
        ## other things could/should go here

    def move_right(self, step_size=SPEEDX):
        ''' Move the hero to the right '''
        self.rect.x += step_size

    def move_left(self, step_size=SPEEDX):
        ''' Move the hero to the left '''
        self.rect.x -= step_size

    def move_up(self, step_size=SPEEDY):
        ''' Move the hero up '''
        self.rect.y -= step_size

    def move_down(self, step_size=SPEEDY):
        ''' Move the hero down '''
        self.rect.y += step_size

    def move_x(self):
        self.rect.x += self.dx

    def move_y(self):
        self.rect.y += self.dy

    def drift(self, others=None):
        ''' drift across the screen

        Note: the implementation should drift x and drift y separately
              After the drift in x, it should check for x collisions
              After the drift in y, it should check for y collisions
        '''
        if others is None:
            others = []
        self.drift_x()
        for other in others:
            self.handle_xcollision(other)
        self.drift_y()
        for other in others:
            self.handle_ycollision(other)

    def drift_x(self):
        ''' Handle the drift in x '''
        self.move_x()

    def drift_y(self):
        ''' Handle the drift in y '''
        self.move_y()

    def collides_with(self, other_rect):
        ''' return true if there is a collision '''
        return self.rect.colliderect(other_rect)

    def handle_xcollision(self, other_rect):
        ''' handle collisions going left and right '''
        if self.collides_with(other_rect):
            if self.dx > 0 and self.rect.right > other_rect.left:
                self.rect.right = other_rect.left
                if self.bouncy:
                    self.dx *= -1
            elif self.dx < 0 and self.rect.left < other_rect.right:
                self.rect.left = other_rect.right
                if self.bouncy:
                    self.dx *= -1
            else:
                print("weird collision...")

    def handle_ycollision(self, other_rect):
        ''' handle collisions going up and dowon '''
        if self.collides_with(other_rect):
            if self.dy > 0 and self.rect.bottom > other_rect.top:
                self.rect.bottom = other_rect.top
                if self.bouncy:
                    self.dy *= -1
            elif self.dy < 0 and self.rect.top < other_rect.bottom:
                self.rect.top = other_rect.bottom
                if self.bouncy:
                    self.dy *= -1
            else:
                print("weird collision...")

    def update(self, walls):
        ''' move and check for collisions '''
        self.drift(walls)
        if self.update_gravity:
            self.ddy = 0.8 * self.ddy + 0.2 * 9
            self.dy = min(max(self.dy + self.ddy,-9), 9)

    def draw(self, screen):
        ''' draw the hero '''
        pygame.draw.rect(screen, BLACK, self.rect)

    def handle_event(self, event):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.dx -= SPEEDX
                elif event.key == pygame.K_RIGHT:
                    self.dx += SPEEDX
                elif event.key == pygame.K_SPACE:
                    self.ddy = -9 #max(self.dy-12, -15)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.dx += SPEEDX
                elif event.key == pygame.K_RIGHT:
                    self.dx -= SPEEDX