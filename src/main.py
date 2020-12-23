# Import the pygame library and initialise the game engine
import pygame
from paddle import Paddle

pygame.init()
 
# Define some colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
 
# Open a new window
size = (800+20, 600+20)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()

# Add thepaddles to the list of sprites
all_sprites_list.add(paddleA)

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
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    # if keys[pygame.K_UP]:
    #     snake.moveUp(5)
    # if keys[pygame.K_DOWN]:
    #     snake.moveDown(5)    
    # if keys[pygame.K_UP]:
    #     snake.moveLeft(5)
    # if keys[pygame.K_DOWN]:
    #     snake.moveRight(5) 

    # --- Game logic should go here
    all_sprites_list.update()
 
 
    # --- Drawing code should go here
    # First, clear the screen to black. 
    
    #Draw the net
    screen.fill(BLACK)


    pygame.draw.line(screen, BLUE, [0, 0], [820,0], 10)
    pygame.draw.line(screen, BLUE, [0, 0], [0,620], 10)
    pygame.draw.line(screen, BLUE, [0, 617], [820,617], 10)
    pygame.draw.line(screen, BLUE, [817, 0], [817,620], 10)

    #drawing al the sprites in one go on the screen
    all_sprites_list.draw(screen) 

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
    # --- Limit to 60 frames per second
    clock.tick(60)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()
