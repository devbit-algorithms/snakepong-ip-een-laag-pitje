import pygame
import random

# --- Globals ---
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Screen size
height = 600
width = 600

# Margin between each segment
segment_margin = 3

# Set the width and height of each snake segment
segment_width = min(height, width) / 40 - segment_margin
segment_height = min(height, width) / 40 - segment_margin

# Set initial speed
x_change = segment_width + segment_margin
y_change = 0


class Snake():
    """ Class to represent one snake. """

    # Constructor
    def __init__(self):
        self.segments = []
        self.spriteslist = pygame.sprite.Group()
        for i in range(15):
            x = (segment_width + segment_margin) * 30 - (segment_width + segment_margin) * i
            y = (segment_height + segment_margin) * 2
            segment = Segment(x, y)
            self.segments.append(segment)
            self.spriteslist.add(segment)

    def move(self):
        # Figure out where new segment will be
        x = self.segments[0].rect.x + x_change
        y = self.segments[0].rect.y + y_change

        # Don't move off the screen
        # At the moment a potential move off the screen means nothing happens, but it should end the game
        if 0 <= x <= width - segment_width and 0 <= y <= height - segment_height:

        # Insert new segment into the list
            segment = Segment(x, y)
            self.segments.insert(0, segment)
            self.spriteslist.add(segment)
        # Get rid of last segment of the snake
        # .pop() command removes last item in list
            old_segment = self.segments.pop()
            self.spriteslist.remove(old_segment)
        else:
            return
        self.eat()




    def grow(self):
        x = self.segments[0].rect.x + x_change
        y = self.segments[0].rect.y + y_change
        segment = Segment(x, y)
        self.segments.insert(len(self.segments), segment)
        self.spriteslist.add(segment)


class Segment(pygame.sprite.Sprite):
    """ Class to represent one segment of a snake. """

    # Constructor
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(WHITE)

        # Set top-left corner of the bounding rectangle to be the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

foodx = random.choice([i for i in range(0, 600, 15)])
foody = random.choice([i for i in range(0, 600, 15)])

class Food():
    def __init__(self):
        self.foodlists = []
        self.foodlist = pygame.sprite.Group()

        fooditem = Food_item(foodx, foody)
        self.foodlists.append(fooditem)
        self.foodlist.add(fooditem)

    def replenish(self):

        newfoodx = random.choice([i for i in range(0, 600, 15)])
        newfoody = random.choice([i for i in range(0, 600, 15)])
        fooditem = Food_item(newfoodx, newfoody)
        self.foodlists.append(fooditem)
        self.foodlist.add(fooditem)



class Food_item(pygame.sprite.Sprite):
    def __init__(self, fx, fy):
        # Call the parent's constructor
        super().__init__()
        # Set height, width
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(RED)

        # Set top-left corner of the bounding rectangle to be the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = fx
        self.rect.y = fy


""" # Call this function so the Pygame library can initialize itself
pygame.init()

# Create a 600x600 sized screen
screen = pygame.display.set_mode([width, height])

# Set the title of the window
pygame.display.set_caption('Snake Game')

# Create an initial snake
my_snake = Snake()
food = Food()

clock = pygame.time.Clock()
done = False """

""" while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Set the direction based on the key pressed
        # We want the speed to be enough that we move a full
        # segment, plus the margin.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = (segment_width + segment_margin) * -1
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = (segment_width + segment_margin)
                y_change = 0
            if event.key == pygame.K_UP:
                x_change = 0
                y_change = (segment_height + segment_margin) * -1
            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = (segment_height + segment_margin)

    # move snake one step
    my_snake.move()
    # -- Draw everything
    # Clear screen
    screen.fill(BLACK)
    my_snake.spriteslist.draw(screen)
    food.foodlist.draw(screen)

    # Flip screen
    pygame.display.flip()

    # Pause
    clock.tick(5) """

pygame.quit()