# Import the pygame library and initialise the game engine
import pygame
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
 
    # --- Game logic should go here
 
 
 
    # --- Drawing code should go here
    # First, clear the screen to black. 
    screen.fill(BLACK)
    #Draw the net


    pygame.draw.line(screen, BLUE, [0, 0], [820,0], 10)
    pygame.draw.line(screen, BLUE, [0, 0], [0,620], 10)
    pygame.draw.line(screen, BLUE, [820, 620], [820,0], 10)
    pygame.draw.line(screen, BLUE, [820, 620], [0,620], 10)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
    # --- Limit to 60 frames per second
    clock.tick(60)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()
