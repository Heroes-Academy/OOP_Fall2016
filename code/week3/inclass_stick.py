import pygame


def draw_stickman(specs):
    center = (specs['centerx'], specs['centery'])
    BASE_COLOR = specs['BASE_COLOR']# assume color is passed in
    HEAD_COLOR = specs['HEAD_COLOR'] # assume color is passed in
    screen = specs['screen'] # assume screen is passed in
    ## legs
    leg_endpoint = (0,0) #how to calculate this?
    pygame.draw.line(screen, BASE_COLOR, center, leg_endpoint, 2)


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

### STICK FIGURE VARIABLE

stick_specs = dict(centerx=100, centery=100, linewidth=2,
                   torso_height=10, leg_offsetx=5, leg_offsety=10,
                   arm_offsetx=7, arm_offsety=0, head_radius=5)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)

    # head
    pygame.draw.circle(screen, BLACK, , 0)

    # Legs
    pygame.draw.line(screen, BLACK, [100,100], [105,110], 2)
    pygame.draw.line(screen, BLACK, [100,100], [95,110], 2)

    # Body
    pygame.draw.line(screen, RED, [100,100], [100,90], 2)

    # Arms
    pygame.draw.line(screen, RED, [100,90], [104,100], 2)
    pygame.draw.line(screen, RED, [100,90], [96,100], 2)

    pygame.display.flip()

    clock.tick(60)

# Close the window and quit.
pygame.quit()
