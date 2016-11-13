import pygame

### AN EXAMPLE
class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super(Block, self).__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()


class Entity(pygame.sprite.Sprite):
    def __init__(self, image):
        # Call the parent class (Sprite) constructor
        super(Entity, self).__init__(self)

        # load an image
        self.image = pygame.image.load(image)

        ## get the center of the display

        ## optional:
        # use pos to get the initial x and y
        # pos = pg.display.get_surface().get_rect().center
        # self.rect = self.image.get_rect(center=pos)

        # no x or y
        self.rect = self.image.get_rect()

        # set x and y
        # self.rect.x = 0
        # self.rect.y = 0
