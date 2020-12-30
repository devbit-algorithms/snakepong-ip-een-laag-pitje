import pygame
from snake import Snake
from snake import Segment

snake_segment = 10
def test_move_down():
        snake = Snake(0)
        segment = Segment(10 , 10)    
        firstvalue_y = snake.segments[0].rect.y
        firstvalue_x = snake.segments[0].rect.x
        snake.set_x_change(0)
        snake.set_y_change(snake_segment)  
        snake.move()
        assert snake.segments[0].rect.y == firstvalue_y + 10
        assert snake.segments[0].rect.x == firstvalue_x

def test_move_up():
        snake = Snake(0)
        segment = Segment(10 , 10)    
        firstvalue_y = snake.segments[0].rect.y
        firstvalue_x = snake.segments[0].rect.x
        snake.set_x_change(0)
        snake.set_y_change(-snake_segment)  
        snake.move()
        assert snake.segments[0].rect.y == firstvalue_y - 10
        assert snake.segments[0].rect.x == firstvalue_x

def test_move_left():
        snake = Snake(0)
        segment = Segment(10 , 10)    
        firstvalue_y = snake.segments[0].rect.y
        firstvalue_x = snake.segments[0].rect.x
        snake.set_x_change(-snake_segment)
        snake.set_y_change(0) 
        snake.move()
        assert snake.segments[0].rect.y == firstvalue_y
        assert snake.segments[0].rect.x == firstvalue_x - 10

def test_move_right():
        snake = Snake(0)
        segment = Segment(10 , 10)    
        firstvalue_y = snake.segments[0].rect.y
        firstvalue_x = snake.segments[0].rect.x
        snake.set_x_change(snake_segment)
        snake.set_y_change(0) 
        snake.move()
        assert snake.segments[0].rect.y == firstvalue_y
        assert snake.segments[0].rect.x == firstvalue_x + 10

