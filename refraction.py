import pygame
from IST import *
# import random
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
# суета
pygame.init()
pygame.font.init()
pygame.mixer.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Рефракция")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
running = True
# ---------------------------Main--------------------------------
l = 10  # длина волны
v1 = 5  # скорость основной волны
v2 = 3  # скорость прeломлённоё волны
s = 400  # начальные условия
w = 5  # ширина волны
r_max = 1000

# touch
h = 200
v_1 = v1
v_2 = v2
number = 0

# don't touch
sin_a = [[]]
sin_b = [[]]
x_pos = [[]]
y = [[]]
x_neg = [[]]
radius = [h]
t_collision_last = [0]
t_collision_prev = [0]
sin_a_clone = 0
w = 5
m = [0]
pos = [0]  # счетчик для начала преломления

b = True  # есть центр?

# qqq = Ist(0,0,0,0,0,0,0,0,0)
ist1 = Ist(1000, 400, 200, RED, l, v1, s, w, b)  # основной источник
ist2 = Ist(1000, 400, 600, GREEN, l, v1, s, w, b)  # источник отражения
#Ref1 = Ref(v1, v2, w, l, h, ist1, 1000)
# ref1=Ref(v1,v2,w,l)

# --------------------------Game----------------------------------
while running:
    clock.tick(FPS)
    pi = 3.14
    sc.fill(WHITE)
    #
    ist1.Draw()
    ist2.Draw()
    pygame.draw.rect(sc, BLUE, (0, 400, 800, 400))
    for number in range(len(radius)):
        pos[number] += v_1
    if pos[0] >= h:

        for number in range(len(radius)):

            # итерируем по радиусам
            sin_a[number].append(((radius[number] ** 2 - h ** 2) ** 0.5) / radius[number])
            sin_b[number].append((v_2 / v_1) * sin_a[number][-1])
            sin_a_clone = sin_a[number][-1]
            if sin_a_clone < v_1 / v_2:

                t_collision_prev[number] = t_collision_last[number]
                t_collision_last[number] = (radius[number] - h) / v_1
                x_pos[number].append(2 * h + radius[number] * sin_a[number][-1])
                x_neg[number].append(2 * h - radius[number] * sin_a[number][-1])
                y[number].append(2 * h)
                for i in range(len(sin_a[number]) - 1):
                    x_pos[number][i] += v_2 * sin_b[number][i] * (t_collision_last[number] - t_collision_prev[number])
                    y[number][i] += v_2 * ((1 - sin_b[number][i] ** 2) ** 0.5) * (
                                t_collision_last[number] - t_collision_prev[number])
                    x_neg[number][i] -= v_2 * sin_b[number][i] * (t_collision_last[number] - t_collision_prev[number])
                # использование с какого-то момента "фантомного" времени коллизии позволяет сделать так,
                # что между соседними кадрами отрисовки для всех кривых проходит одинаковое количество времени

            else:
                m[number] += 1
                t_collision_prev[number] = t_collision_last[number]
                t_collision_last[number] = (radius[number] - h) / v_1
                for i in range(len(sin_a[number]) - m[number]):
                    x_pos[number][i] += v_2 * sin_b[number][i] * (t_collision_last[number] - t_collision_prev[number])
                    y[number][i] += v_2 * ((1 - sin_b[number][i] ** 2) ** 0.5) * (
                                t_collision_last[number] - t_collision_prev[number])
                    x_neg[number][i] -= v_2 * sin_b[number][i] * (t_collision_last[number] - t_collision_prev[number])
            radius[number] += v_1
            if pos[number] >= h + v1:
                for i in range(len(x_pos[number]) - 1):
                    pygame.draw.line(sc, YELLOW, [x_pos[number][i], y[number][i]],
                                     [x_pos[number][i + 1], y[number][i + 1]],
                                     w)
                    pygame.draw.line(sc, YELLOW, [x_neg[number][i], y[number][i]],
                                     [x_neg[number][i + 1], y[number][i + 1]],
                                     w)
            if radius[-1] >= h + r_max / l:
                # увеличить счетчик глобального цикла (number) на 1 (radius[i], x_pos[j][i], etc.)
                radius.append(h)
                sin_a.append([])
                sin_b.append([])
                x_pos.append([])
                x_neg.append([])
                y.append([])
                pos.append(h)
                t_collision_last.append(0)
                t_collision_prev.append(0)
                m.append(0)

    pygame.draw.rect(sc, WHITELE, (800, 0, 200, 800))
    sc.blit(pygame.font.SysFont('arial', 30).render('l:'+ str(1000/l), False, (0, 0, 0)), (825, 25))

    #sc.blit(pygame.font.SysFont('arial', 30).render('v:'+ str(v), False, (0, 0, 0)), (825, 50))

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
