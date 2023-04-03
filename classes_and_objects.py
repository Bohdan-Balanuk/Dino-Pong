from pygame import*
from random import randint
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
        self.rect.y -= 5
    
    def move_Down(self):
        self.rect.y += 5

pl1 = 0
pl2 = 0
ball_speed = 0

player1 = Player("Objects/player.png", 50, 300, 50, 150)
player2 = Player("Objects/player.png", 950, 300, 50, 150)

ball = Ball("Objects/ball.png", 500, 350, 50, 50, 3, 3)

ball_direction_x = randint(1,2)
ball_direction_y = randint(1,2)