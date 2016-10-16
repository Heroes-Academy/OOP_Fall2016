import pygame

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
    pygame.draw.ellipse(screen, BLACK, [96,83,10,10], 0)

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
