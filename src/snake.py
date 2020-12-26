import pygame
import random

# --- Globals ---
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Screen size
height = 500
width = 690



# Set the width and height of each snake segment
segment_width = 10#min(height, width) / 40
segment_height = 10#min(height, width) / 40

# Set initial speed
x_change = segment_width
y_change = 0


class Snake():
    """ Class to represent one snake. """

    # Constructor
    def __init__(self, score):
        self.segments = []
        self.spriteslist = pygame.sprite.Group()
        for i in range(17 + score):
            x = (segment_width) * 30 - (segment_width) * i
            y = (segment_height) * 2
            segment = Segment(x, y)
            self.segments.append(segment)
            self.spriteslist.add(segment)
            self.__x_change = segment_width
            self.__y_change = 0

    def set_x_change(self, x_change):
        self.__x_change = x_change 

    def get_x_change(self, x_change):
        return self.__x_change 

    def set_y_change(self, x_change):
        self.__y_change = x_change 

    def get_y_change(self, x_change):
        return self.__y_change 

    def move(self):
        # Figure out where new segment will be
        x = self.segments[0].rect.x + self.__x_change
        y = self.segments[0].rect.y + self.__y_change

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







class Segment(pygame.sprite.Sprite):
    """ Class to represent one segment of a snake. """

    # Constructor
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(GREEN)

        # Set top-left corner of the bounding rectangle to be the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
