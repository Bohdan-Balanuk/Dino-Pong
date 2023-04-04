from pygame import*
from random import randint
from menu import*
class Ball():
    def __init__(self, filename, x, y, width, height, speed_x, speed_y):
        self.rect = Rect(x,y,width,height)
        self.image = transform.scale(image.load(filename), (50, 50))
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed_x = speed_x
        self.speed_y = speed_y

    def draw_ball(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def colliderect(self, rect):
        return self.rect.colliderect(rect)

class Player():
    def __init__(self, filename, x, y, width, height):
        self.rect = Rect(x,y,width,height)
        self.image = transform.scale(image.load(filename), (50, 150))
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def draw_player(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
    def move_Up(self):
        self.rect.y -= 8
    
    def move_Down(self):
        self.rect.y += 8

pl1 = 0
pl2 = 0

player1 = Player("Objects/player.png", 50, 300, 50, 150)
player2 = Player("Objects/player.png", 950, 300, 50, 150)

if choose == 1:
    ball_speedx = 2
    ball_speedy = 2

if choose == 2:
    ball_speedx = 3
    ball_speedy = 3

if choose == 3:
    ball_speedx = 4
    ball_speedy = 4


ball = Ball("Objects/ball.png", 500, 350, 50, 50, ball_speedx, ball_speedy)

ball_direction_x = randint(1,2)
ball_direction_y = randint(1,2)