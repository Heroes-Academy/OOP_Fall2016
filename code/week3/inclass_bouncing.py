import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def make_ball(startx=0, starty=0, radius=10, xspeed=2, yspeed=2):
    ball_rect = pygame.Rect(startx, starty, radius*2, radius*2)
    ball = dict(ball_rect=ball_rect, xspeed=xspeed, yspeed=yspeed)
    return ball

### Ball = namedtuple("Ball", ['rect', 'speed'])
### ball = Ball(ball_rect, speed)

### ball.rect

def draw_ball(ball, color=(255,0,0), linewidth=2):
    ## use these
    ##### ball.centerx, ball.centery, ball.width
    ball_rect = ball['ball_rect']
    screen = pygame.display.get_surface()
    center = (ball_rect.centerx, ball_rect.centery)
    radius = ball_rect.width // 2
    pygame.draw.circle(screen, color, center, radius, linewidth)

def update_ball(ball):
    screen = pygame.display.get_surface()
    W, H = screen.get_size()
    ## use these:
    ##### ball.left, ball.right, ball.top, ball.bottom
    ## check for boundary collisions
    ## update position
    #ball.x =
    #ball.y =
    ball['speed'] *= -1


pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
done = False
clock = pygame.time.Clock()
###############
# assumed functions:
# 1. make_ball
# 2. draw_ball
# 3. update_ball
num_balls = 3
all_balls = list()
for i in range(num_balls):
    all_balls.append(make_ball(startx=20+i*10,
                               starty=20*i*5,
                               radius=20+i*5))


###############


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    screen.fill(WHITE)

    ##########################

    update_ball(ball)
    draw_ball(ball)


    ##########################

    pygame.display.flip()
    clock.tick(60)

# Close the window and quit.
pygame.quit()
