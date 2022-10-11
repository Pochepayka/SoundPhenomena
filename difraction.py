import pygame
from IST import *
from input import *
import sys
#import random

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
pygame.display.set_caption("Дифракция")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
running = True

#---------------------------Main--------------------------------
n=1#количество щелей
d=100#дифракционная переменная(???) длина щели
r=1000#максимальный радиус волн
s=-350#начальные условия
w=5#ширина волны
b=True#есть центр?
x1_1=400# p
y1_1=400# o
x2_1=400# s
y2_1=400# i
x3_1=400# t
y3_1=400# i
x4_1=400# o
y4_1=400# n

x1_2=400# p
y1_2=400# o
x2_2=400# s
y2_2=400# i
x3_2=400# t
y3_2=400# i
x4_2=400# o
y4_2=400# n
l=20#длина волн
v=2#скорость волн
x=50#координаты...
y=400#...главного источника
if n == 1:
    y1_1 = 400-d/2
    x1_1 = 400
    y1_2 = 400+d/2
    x1_2 = 400
if n == 2:
    x1_1 = 400
    y1_1 = 400 + 1.5*d
    x2_1 = 400
    y2_1 = 400 - 1.5*d
    x1_2 = 400
    y1_2 = 400 + 0.5*d
    x2_2 = 400
    y2_2 = 400 - 0.5*d
if n == 3:
    x1_1 = 400
    y1_1 = 400 + 2.5*d
    x2_1 = 400
    y2_1 = 400 - 1.5*d
    x3_1 = 400
    y3_1 = 400+0.5*d
    x1_2 = 400
    y1_2 = 400 + 1.5*d
    x2_2 = 400
    y2_2 = 400 - 2.5*d
    x3_2 = 400
    y3_2 = 400-0.5*d


ist0=Ist1(r,x,y,RED,l,v,1,w,b,-45,45,False)#основной источник
slit1=Slit(n,d)#щели
ist1_1=Ist1(r,x1_1,y1_1,YELLOW,l,v,s,w,False,-45,45,False)#1-ый источник 1-ой щели
ist2_1=Ist1(r,x2_1,y2_1,YELLOW,l,v,s,w,False,-45,45,False)#1-ой источник 2-ой щели
ist3_1=Ist1(r,x3_1,y3_1,YELLOW,l,v,s,w,False,-45,45,False)#1-ый источник 3-ой щели
#ist4_1=Ist1(r,x4_1,y4_1,RED,l,v,s,w,False,-45,,False)#доп-ый источник доп-ой щели
ist1_2=Ist1(r,x1_2,y1_2,YELLOW,l,v,s,w,False,-45,45,False)#2-ой источник 1-ой щели
ist2_2=Ist1(r,x2_2,y2_2,YELLOW,l,v,s,w,False,-45,45,False)#2-ой источник 2-ой щели
ist3_2=Ist1(r,x3_2,y3_2,YELLOW,l,v,s,w,False,-45,45,False)#2-ой источник 3-ей щели
#ist4_2=Ist1(r,x4_2,y4_2,RED,l,v,s,w,False,-45,45,False)#доп-ый источник доп-ой щели
#--------------------------Game----------------------------------
#f1=pygame.font.SysFont('arial',36)
#text1=f1.render('n:',False,(0,0,0))
#sc.blit(text1,(825,25))
#text2=f1.render('d:',False,(0,0,0))


while running:
    clock.tick(FPS)
    sc.fill(WHITE)

    #
    ist0.Draw()
    slit1.Draw()
    pygame.draw.rect(sc, WHITE, (405, 0, 400, 800))
    if n==1:
        ist1_1.Draw()
        ist1_2.Draw()
    if n==2:
        ist1_1.Draw()
        ist2_1.Draw()
        ist1_2.Draw()
        ist2_2.Draw()
    if n==3:
        ist1_1.Draw()
        ist2_1.Draw()
        ist3_1.Draw()
        ist1_2.Draw()
        ist2_2.Draw()
        ist3_2.Draw()
    pygame.draw.rect(sc, BLACK, (790, 10, 10, 780))
    pygame.draw.rect(sc, WHITELE, (800,0, 200, 800))
    sc.blit(pygame.font.SysFont('arial', 30).render('n:'+ str(n), False, (0, 0, 0)), (825, 25))

    sc.blit(pygame.font.SysFont('arial', 30).render('d:'+ str(d), False, (0, 0, 0)), (825, 50))

    sc.blit(pygame.font.SysFont('arial', 30).render('l: '+ str(r/l), False, (0, 0, 0)), (825, 75))

    sc.blit(pygame.font.SysFont('arial', 30).render('v: '+ str(v), False, (0, 0, 0)), (825, 100))

    sc.blit(pygame.font.SysFont('arial', 30).render('w: '+ str(w), False, (0, 0, 0)), (825, 125))
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


