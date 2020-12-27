from random import randint
from paddle import Paddle
from ball import Ball
from snake import Snake
from snake import Segment
WHITE = (255, 255, 255)


def test_paddlemoveDown():
    paddleA = Paddle(WHITE, 10, 100)
    y = paddleA.rect.y
    paddleA.moveDown(10)
    y_change = paddleA.rect.y
    assert y == 0
    assert y_change == 10

def test_paddlemoveUp():
    paddleA = Paddle(WHITE, 10, 100)
    paddleA.rect.y = 20
    y = paddleA.rect.y
    paddleA.moveUp(10)
    y_change = paddleA.rect.y
    assert y == 20
    assert y_change == 10
