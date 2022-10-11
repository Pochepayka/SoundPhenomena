import pygame
from IST import *
#import random
import sys

'''#характеристики экрана
WIDTH = 800
HEIGHT = 800
FPS = 10
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (255, 250, 250)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 200, 255)'''
#суета
pygame.init()
pygame.font.init()
pygame.mixer.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Фанпример")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
running = True
#---------------------------Main--------------------------------
s=0#начальные условия
w=5#ширина волны
v=6#скорость
l=10#длина волны
b=True
ist1=Ist(1000,200,400,RED,l,v,s,w,b)#основной источник
ist2=Ist1(1000,400,400,GREEN,l,v,s,w,False,225,-90,False)#источник отражения 1
ist3=Ist1(1000,200,600,GREEN,l,v,s,w,False,0,45,True)#отражение 2 18.435
ist4=Ist1(1000,488,490,YELLOW,l,v,s,w,False,-60,0,False)
#--------------------------Game----------------------------------
while running:
    clock.tick(FPS)
    pi = 3.14
    sc.fill(WHITE)
    #

    ist2.Draw()
    pygame.draw.rect(sc, WHITE, (300, 0, 500, 800))
    ist3.Draw()
    #pygame.draw.rect(sc, WHITE, (200, 500, 100, 100))
    #
    ist1.Draw()
    #pygame.draw.polygon(sc, WHITE, [[500, 500], [500, 800], [800, 800], [800, 500]])
    pygame.draw.rect(sc, WHITE, (500, 500, 300, 300))
    ist4.Draw()
    pygame.draw.rect(sc, BLACK, (300, 500,200, 300))
    pygame.draw.rect(sc, WHITELE, (800, 0, 200, 800))



    sc.blit(pygame.font.SysFont('arial', 30).render('l:'+ str(1000/l), False, (0, 0, 0)), (825, 25))

    sc.blit(pygame.font.SysFont('arial', 30).render('v:'+ str(v), False, (0, 0, 0)), (825, 50))

    sc.blit(pygame.font.SysFont('arial', 30).render('w:'+ str(w), False, (0, 0, 0)), (825, 75))
    #
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    #
    pygame.display.update()
    all_sprites.update()
    pygame.display.flip()
pygame.quit()
