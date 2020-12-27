from random import randint
from paddle import Paddle
from ball import Ball
from snake import Snake
from snake import Segment
RED = (255, 255, 255)

def test_ballupdate():
    ball = Ball(RED, 10, 10)
    ball.rect.x = 100
    ball.rect.y = 100
    ball.update()
    assert ball.rect.x == 103
    assert ball.rect.y == 106

def test_ballbounce():
    ball = Ball(RED, 10, 10)
    ball.rect.x = 100
    ball.rect.y = 100
    ball.update()
    ball.bounce()
    ball.update()
    assert ball.rect.x == 100
    assert ball.rect.y >= 98

