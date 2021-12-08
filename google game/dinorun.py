import pygame
import math
# screen ka
W=800
H=400
clock=pygame.time.Clock()
screen=pygame.display.set_mode((W,H))
pygame.display.set_caption("Dino Run")
#background ka 
bgimage=pygame.image.load("bg3.jpg")
bgx=0
bgy=0
#dino ka 
d2=pygame.image.load("dra2.png")
d3=pygame.image.load("dra3.png")
d4=pygame.image.load("dra4.png")
d5=pygame.image.load("dra5.png")
dino2=pygame.transform.scale(d2,(50,50))
dino3=pygame.transform.scale(d3,(50,50))
dino4=pygame.transform.scale(d4,(50,50))
dino5=pygame.transform.scale(d5,(50,50))
dinox=80
dinoy=125
walktemp=0
walk=[dino2,dino2,dino2,dino2,dino3,dino3,dino3,dino3,
        dino4,dino4,dino4,dino4,dino5,dino5,dino5,dino5,dino5]
dinorun=False
# tree ka 
tree=pygame.image.load("tree5.png")
tree1=pygame.image.load("tree5.png")
tree2=pygame.image.load("tree4.png")
tree3=pygame.image.load("tree3.png")
tree4=pygame.image.load("tree1.png")
treex=100
treey=120
treex1=treex+400
treey1=treey+5
temp=0
gravity=3
jumpcon=False
game=True
def ifcollision(x1,y1,x2,y2):
    if x2+400 < x1+50 < x2+400+30 and y2 < y1+50 < y2+50:
        return True
    else :
        return False
def gamerun(game,dinox,dinoy,bgx,bgy,temp,treex,treey,walk,walktemp,dinorun,gravity,jumpcon):
    while game:
        vx=0
        vy=0
        jump=3
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                        temp=5
                        dinorun=True
                        print(dinox,dinoy)
                        print("tree",treex,treey)
                if event.key==pygame.K_SPACE:
                        jumpcon=True    
        bgx=bgx-temp
        treex=treex-temp
        #print(bgx,temp)
        if bgx < -800:
            bgx=0
        if treex < -2400:
            treex=400
        screen.fill((255,255,255))
        if dinorun==True:
            walktemp=walktemp+1
            if walktemp >= len(walk):
                walktemp=0
        if dinoy < 126 and dinoy > 30 and jumpcon==True:
            dinoy=dinoy-jump
        else:
            jumpcon=False
        if dinoy < 125 and jumpcon==False:
            dinoy=dinoy+gravity
        #collision for tree1
        if treex < -290 and treex > -340 and dinoy > 70:
            game=False
        #collision for  tree2
        if treex < -290-400 and treex > -340-400 and dinoy > 70:
            game=False
        #collision for  tree3
        if treex < -290-800 and treex > -340-800 and dinoy > 70:
            game=False
        #collision for  tree4
        if treex < -290-1200 and treex > -340-1200 and dinoy > 70:
           game=False
        #collision for  tree5
        if treex < -290-1600 and treex > -340-1600 and dinoy > 70:
           game=False
        
        screen.blit(bgimage,(bgx,bgy))
        screen.blit(bgimage,(bgx+800,bgy))
        screen.blit(walk[walktemp],(dinox,dinoy))
        screen.blit(tree,(treex+400,treey+5))
        screen.blit(tree1,(treex+800,treey+5))
        screen.blit(tree2,(treex+1200,treey))
        screen.blit(tree3,(treex+1600,treey-15))
        screen.blit(tree4,(treex+2000,treey+5))
        pygame.display.update()
        clock.tick(100)
gamerun(game,dinox,dinoy,bgx,bgy,temp,treex,treey,walk,walktemp,dinorun,gravity,jumpcon)

