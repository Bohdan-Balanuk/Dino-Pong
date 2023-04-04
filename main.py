from pygame import*
from time import time as time1
from random import randint 
from classes_and_objects import* 
import sys

init()
clock = time.Clock()

window = display.set_mode((1050, 750))
display.set_caption('Dino-Pong')
background = transform.scale(image.load("Objects/Поле.png"), (1050, 750))
window.blit(background, (0,0))

gameover = False

while not gameover:
    for ev in event.get():
        if ev.type == QUIT:
            gameover = True
        
        if ev.type == KEYDOWN:
            if ev.key == K_w:
                pl1 = 1
            if ev.key == K_s:
                pl1 = -1

            if ev.key == K_UP:
                pl2 = 1
            if ev.key == K_DOWN:
                pl2 = -1
        
        if ev.type == KEYUP:
            if ev.key == K_w:
                pl1 = 0
            if ev.key == K_s:
                pl1 = 0
            
            if ev.key == K_UP:
                pl2 = 0
            if ev.key == K_DOWN:
                pl2 = 0

    if pl1 == 1 and player1.rect.y >= 0:
        player1.move_Up() 
    if pl1 == -1 and player1.rect.y <= 600:
        player1.move_Down() 

    if pl2 == 1 and player2.rect.y >= 0:
        player2.move_Up() 
    if pl2 == -1 and player2.rect.y <= 600:
        player2.move_Down() 

    if ball_direction_x == 1:
        ball.rect.x -= ball.speed_x
    if ball_direction_x == 2:
        ball.rect.x += ball.speed_x

    if ball_direction_y == 1:
        ball.rect.y += ball.speed_y
    if ball_direction_y == 2:
        ball.rect.y -= ball.speed_y

    if ball.rect.y >= 700:
        ball.speed_y *= -1
    if ball.rect.y <= 0:
        ball.speed_y *= -1
    

    if ball.colliderect(player1):
        ball.speed_x *= -1
    if ball.colliderect(player2):
        ball.speed_x *= -1
    
    
    window.blit(background, (0,0))
    player1.draw_player(window)
    player2.draw_player(window)   
    ball.draw_ball(window)    
    print(ball_speedx, ball_speedy)
    display.update()
    clock.tick(120)