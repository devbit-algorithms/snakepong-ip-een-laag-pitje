# Import the pygame library and initialise the game engine
import pygame
import random
import time

from paddle import Paddle
from ball import Ball

#from snake import Snake


pygame.init()
 
# Define some colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

width = 700
height = 500
# Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()

# Add thepaddles to the list of sprites
all_sprites_list.add(paddleA)
all_sprites_list.add(ball)

# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True
 
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#snake
snake_block = 10
snake_speed = 15
x1 = width / 2
y1 = height / 2
x1_change = 0
y1_change = 0

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, WHITE, [x[0], x[1], snake_block, snake_block])

foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
 
snake_List = []
Length_of_snake = 1
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
    
    
    screen.fill(BLACK)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_z]:
        paddleA.moveUp(5)
    elif keys[pygame.K_s]:
        paddleA.moveDown(5)
    elif keys[pygame.K_UP]:
        y1_change = -snake_block
        x1_change = 0
    elif keys[pygame.K_DOWN]:
        y1_change = snake_block
        x1_change = 0
    elif keys[pygame.K_LEFT]:
        x1_change = -snake_block
        y1_change = 0
    elif keys[pygame.K_RIGHT]:
        x1_change = snake_block
        y1_change = 0

    if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
        game_close = True
    
    x1 += x1_change
    y1 += y1_change

    pygame.draw.rect(screen, GREEN, [foodx, foody, snake_block, snake_block])

    snake_Head = []
    snake_Head.append(x1)
    snake_Head.append(y1)
    snake_List.append(snake_Head)

    if len(snake_List) > Length_of_snake:
        del snake_List[0]
 
    for x in snake_List[:-1]:
        if x == snake_Head:
            game_close = True

    

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
 

    #Detect collisions between the ball and the paddles
    if pygame.sprite.collide_mask(ball, paddleA):
      ball.bounce()
    
    # --- Drawing code should go here
    # First, clear the screen to black. 
 
    #Draw the net
    
    our_snake(snake_block, snake_List)

    # pygame.draw.line(screen, BLUE, [0, 0], [700,0], 10)
    # pygame.draw.line(screen, BLUE, [0, 0], [0,500], 10)
    # pygame.draw.line(screen, BLUE, [0, 617], [820,617], 10)
    # pygame.draw.line(screen, BLUE, [817, 0], [817,620], 10)

    #drawing al the sprites in one go on the screen
    all_sprites_list.draw(screen) 

    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
        Length_of_snake += 1

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

     
    # --- Limit to 60 frames per second
    clock.tick(30)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()