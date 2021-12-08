import pygame
import random
import math
from pygame import surface
pygame.init()
w=400
h=600
display=pygame.display.set_mode((w,h))
pygame.display.set_caption("snake game")
fps=30
clock = pygame.time.Clock()
def snake(snake_list):
    for x,y in snake_list:
        pygame.draw.rect(display,(0,0,0),[x,y,20,20])
def collision(sx,sy,fx,fy):
    distance=math.sqrt((math.pow(sx-fx,2))+(math.pow(sy-fy,2)))
    if distance < 15:
        return True
    else:
        return False
def gameloop():
    #score
    score=0
    #snake
    sx=150
    sy=200
    vx=0
    vy=0
    init_velocity = 4
    # snake food
    fx=200#random.randint(20,760)
    fy=300#random.randint(20,560)
    x=10
    y=10
    # snake
    snake_list=[]
    snake_length=1
    game_over= True
    while game_over:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    vx=-init_velocity
                    vy=0
                if event.key==pygame.K_RIGHT:
                    vx=init_velocity
                    vy=0
                if event.key==pygame.K_UP:
                    vy=-init_velocity
                    vx=0
                if event.key==pygame.K_DOWN:
                    vy=init_velocity
                    vx=0
        sx=sx+vx
        sy=sy+vy
        coll=collision(sx,sy,fx,fy)
        if (sx>=390 or sx<=0 )or (sy>=590 or sy<=0):
            print("game over")
            game_over=False
        if coll:
            fx=random.randint(20,380)
            fy=random.randint(20,550)
            snake_length=snake_length+20
            score=score+10
            print(score)
        head=[]
        head.append(sx)
        head.append(sy)
        snake_list.append(head)
        if len(snake_list)>snake_length:
            del snake_list[0]
        for list in snake_list[:-1]:
            if list == head:
                game_over=False
        display.fill((255,255,255))
        snake(snake_list)
        pygame.draw.rect(display,(255,0,0),[fx,fy,20,20])  
        pygame.display.update()
        clock.tick(fps)
gameloop()
pygame.quit()
