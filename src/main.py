# Import the pygame library and initialise the game engine
import pygame
from random import randint


from paddle import Paddle
from ball import Ball

from snake import Snake
from snake import Segment


pygame.init()

 
# Define some colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

width= 700
heigth = 500

score = 0


 
# Open a new window
size = (width, heigth)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

goal = Paddle(BLUE, 10, 500)
goal.rect.x = 0
goal.rect.y = 0

ball = Ball(RED, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

snake = Snake()
segment = Segment(10 , 10)
snake_segment = 10
snake_counter = 0

#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()

# Add thepaddles to the list of sprites
all_sprites_list.add(paddleA)
all_sprites_list.add(ball)
all_sprites_list.add(goal)

# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True
 
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: #pressing x to quit game
                    carryOn=False

    #Moving the paddles when the user uses the arrow keys (player A) or "W/S" keys (player B) 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_z]:
        paddleA.moveUp(7)
    if keys[pygame.K_s]:
        paddleA.moveDown(7)
    if keys[pygame.K_UP]:
        snake.set_x_change(0)
        snake.set_y_change(-snake_segment)  
    if keys[pygame.K_DOWN]:
        snake.set_x_change(0)
        snake.set_y_change(snake_segment)  
    if keys[pygame.K_LEFT]:
        snake.set_x_change(-snake_segment)
        snake.set_y_change(0)
    if keys[pygame.K_RIGHT]:
        snake.set_x_change(snake_segment)
        snake.set_y_change(0)  

    if(snake_counter == 2):
        snake.move()
        snake_counter = 0
    snake_counter = snake_counter + 1
    # --- Game logic should go here
    all_sprites_list.update()

    if ball.rect.x>=690:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1] 
 
    # --- Drawing code should go here
    # First, clear the screen to black. 
    if pygame.sprite.collide_mask(ball, paddleA):
        ball.bounce()

    for segment in snake.segments:
        if pygame.sprite.collide_mask(segment, ball):
            ball.bounce()

    if pygame.sprite.collide_mask(ball, goal):
        score = score + 1
        ball.rect.x = randint(50,300)
        ball.rect.y = randint(50,250)
        ball.velocity[0] = -ball.velocity[0]
        



    #Draw the net
    screen.fill(BLACK)

    #drawing al the sprites in one go on the screen
    all_sprites_list.draw(screen) 
    snake.spriteslist.draw(screen)

    #pygame.draw.line(screen, BLUE, [0, 0], [0,500], 15)

    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
    # --- Limit to 60 frames per second
    clock.tick(60)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()