import pygame
import math
import random
import time
pygame.init()
pygame.font.init()
w,h=800,600
screen = pygame.display.set_mode((w,h))
# score
score=0
Timing=0
clock=pygame.time.Clock()

#font
f = pygame.font.Font('freesansbold.ttf',30)
fx=0
fy=0
# sound
def sound():
    crash_sound = pygame.mixer.Sound("g.wav")
    pygame.mixer.music.load('g.wav')
    pygame.mixer.music.play(1)
# caption
pygame.display.set_caption("First game")
img = pygame.image.load("bg.png")
pygame.display.set_icon(img)
run = True
#background image
bg=pygame.image.load("bg.png")
# player 
ship=pygame.image.load("spaceship.png")
px=370
py=480
pchange=0
#bullet 
b=pygame.image.load("bullet.png")
bx=0
by=480
bxchange=0
bychange=5
bullet_state="ready"
#enemy
shipenemy=[]
ex=[]
ey=[]
xchange=[]
ychange=[]
no_e=6
for i in range(no_e):
    shipenemy.append(pygame.image.load("enemy.png"))
    ex.append(random.randint(0,400))
    ey.append(random.randint(0,200))
    xchange.append(1)
    ychange.append(10)

def player(x,y):
    screen.blit(ship,(x,y))

def enemy(x,y,i):
    screen.blit(shipenemy[i],(x,y))
#score
def s(x,y):
    scoreing=f.render("kills:"+str(score),True,(255,255,255))
    screen.blit(scoreing,(x,y))
# time
def times(x,y,Timing):
    time=f.render("Time:"+str(Timing),True,(255,255,255))
    screen.blit(time,(x,y))
#fire
def bullet_fire(x,y):
    #print("function called")
    global bullet_state
    bullet_state="fire"
    screen.blit(b,(x+16,y+10)) 
# define collision
def collision(enemyx,enemyy,bulletx,bullety):
    distance=math.sqrt((math.pow(enemyx-bulletx,2))+(math.pow(enemyy-bullety,2)))
    if distance < 27:
        return True
    else:
        return False

while run:
    screen.fill((255,255,255))
    screen.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                px=px-30
            if event.key==pygame.K_RIGHT:
                px=px+30
            if event.key==pygame.K_UP:
                py=py-30
            if event.key==pygame.K_DOWN:
                py=py+30
            if event.key==pygame.K_SPACE:
                sound()
                if bullet_state is "ready":
                    bx=px
                    bullet_fire(bx,by)
                
    #timing
    Timing=int(pygame.time.get_ticks()/1000)  
    times(0,100,Timing) 
    if Timing > 60:
        time.sleep(3)
        s(400,300)
        run=False      
    # player boundary check
    if px==736 or px>736:
        px=736
    if px<=0:
        px=0
    if py==536 or py>536:
        py=536
    if py<0:
        py=0
    # enemy boundary check
    for i in range(no_e):
        ex[i]=ex[i]+xchange[i]
        if ex[i]<=0:
            xchange[i]=1
            ey[i]=ey[i]+ychange[i]
        if ex[i]>736:
            xchange[i]=-1
            ey[i]=ey[i]+ychange[i]
        if ey[i]<=0:
            ey[i]=0
        if ey[i]>=536:
            ey[i]=536
        #collision detection
        col=collision(ex[i],ey[i],bx,by)
        if col:
            ex[i]=random.randint(0,400)
            ey[i]=random.randint(0,200)
            int(score)
            score=score+1
            # high score
            file1=open("score.txt","w")
            file1.write(str(score))
            file1.close()
        enemy(ex[i],ey[i],i)
    # bullet 
    if by<=0:
        by=py
        bullet_state="ready"
    if bullet_state is "fire":
        bullet_fire(bx,by)
        by=by-bychange
    # R G B 
    s(fx,fy)
    player(px,py)
    pygame.display.update()
    clock.tick(100)
    #pygame.display.update()