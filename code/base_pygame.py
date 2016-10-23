import pygame


##### INIT SECTION
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
size = (700, 500)
done = False
pygame.init()

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

pygame.display.set_caption("My Game")

#### you can put custom INITs here.


###### WHILE LOOP SECTIOn

# -------- Main Program Loop -----------
while not done:
    #### EVENT CHECK SECTION
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    screen.fill(WHITE)

    #### ACTION SECTION


    #### FINISHING CODE
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
