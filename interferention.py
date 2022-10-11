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
pygame.display.set_caption("Интерференция")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
running = True
#---------------------------Main--------------------------------
r=800#макс  радиус
l1=2.5#длина волны 1 (количество волн)
l2=5#длина волны 2 (количество волн)
v1=4#скорость волны 1
v2=2#скорость волны 2
s=1#начальные условия
w=5#ширина волны
b=True#есть ли центр?
ist1=Ist(r,200,400,RED,l1,v1,s,w,b)#первый источник
ist2=Ist(r,600,400,GREEN,l2,v2,s,w,b)#второй источник

#--------------------------Game----------------------------------
while running:
    clock.tick(FPS)
    pi = 3.14
    sc.fill(WHITE)
    #
    ist1.Draw()
    ist2.Draw()
    pygame.draw.rect(sc, WHITELE, (800, 0, 200, 800))
    sc.blit(pygame.font.SysFont('arial', 30).render('l1: '+ str(r/l1), False, (0, 0, 0)), (825, 25))

    sc.blit(pygame.font.SysFont('arial', 30).render('l2: '+ str(r/l2), False, (0, 0, 0)), (825, 50))

    sc.blit(pygame.font.SysFont('arial', 30).render('v1:'+ str(v1), False, (0, 0, 0)), (825, 75))

    sc.blit(pygame.font.SysFont('arial', 30).render('v2:'+ str(v2), False, (0, 0, 0)), (825, 100))
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
