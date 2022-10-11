import pygame
import sys

# from main import *

# характеристики экрана
WIDTH = 1000
HEIGHT = 800
FPS = 10
# Задаем цвета
WHITE = (255, 255, 255)
WHITELE = (200, 200, 200)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 200, 255)
YELLOW = (250, 240, 30)

pi = 3.14159
sc = pygame.display.set_mode((WIDTH, HEIGHT))


# источник круговой волны
class Ist():
    '''def eee(self):
        rr=self.a'''
    def __init__(self, radius, xPos, yPos, color, length, speed, start, width, box):
        # def __init__(self, radius,x,y,color,length,speed):
        self.r = radius  # Макс. радиус 500
        self.a = start  # счётчик для радиусов 1
        self.x = xPos  # координата центра источника 400
        self.y = yPos  # координата центра источника 400
        self.c = color  # цвет волн RED
        self.sc = sc
        self.l = length  # длина волны 5
        self.sp = speed  # скоорость волны 6
        self.w = width  # ширина полоски
        self.b = box  # есть ли сама точка источника
        self.fff=self.a
    # прорисовка волн
    def Draw(self):
        pygame.draw.circle(self.sc, self.c,
                           (self.x, self.y), 5, 5)
        i1 = self.a
        if i1 >= self.r:
            i1 -= self.r
        pygame.draw.circle(self.sc, self.c,
                           (self.x, self.y), i1, 5)
        if self.l >= 2:
            i2 = i1 + self.r // self.l
            if i2 >= self.r:
                i2 -= self.r
            pygame.draw.circle(self.sc, self.c,
                               (self.x, self.y), i2, 5)
        if self.l >= 3:
            i3 = i2 + self.r // self.l
            if i3 >= self.r:
                i3 -= self.r
            pygame.draw.circle(self.sc, self.c,
                               (self.x, self.y), i3, 5)
        if self.l >= 4:
            i4 = i3 + self.r // self.l
            if i4 >= self.r:
                i4 -= self.r
            pygame.draw.circle(self.sc, self.c,
                               (self.x, self.y), i4, 5)
        if self.l >= 5:
            i5 = i4 + self.r // self.l
            if i5 >= self.r:
                i5 -= self.r
            pygame.draw.circle(self.sc, self.c,
                               (self.x, self.y), i5, 5)
        if self.l >= 6:
            i6 = i5 + self.r // self.l
            if i6 >= self.r:
                i6 -= self.r
            pygame.draw.circle(self.sc, self.c,
                               (self.x, self.y), i6, 5)
        if self.l >= 7:
            i7 = i6 + self.r // self.l
            if i7 >= self.r:
                i7 -= self.r
            pygame.draw.circle(self.sc, self.c,
                               (self.x, self.y), i7, 5)
        if self.l >= 8:
            i8 = i7 + self.r // self.l
            if i8 >= self.r:
                i8 -= self.r
            pygame.draw.circle(self.sc, self.c,
                               (self.x, self.y), i8, 5)
        if self.l >= 9:
            i9 = i8 + self.r // self.l
            if i9 >= self.r:
                i9 -= self.r
            pygame.draw.circle(self.sc, self.c,
                               (self.x, self.y), i9, 5)
        if self.l >= 10:
            i10 = i9 + self.r // self.l
            if i10 >= self.r:
                i10 -= self.r
            pygame.draw.circle(self.sc, self.c,
                               (self.x, self.y), i10, 5)
        if self.l >= 11:
            i11 = i10 + self.r // self.l
            if i11 >= self.r:
                i11 -= self.r
            pygame.draw.circle(self.sc, self.c,
                               (self.x, self.y), i11, 5)
        if self.l >= 12:
            i12 = i11 + self.r // self.l
            if i12 >= self.r:
                i12 -= self.r
            pygame.draw.circle(self.sc, self.c,
                               (self.x, self.y), i12, 5)
        if self.l >= 13:
            i13 = i12 + self.r // self.l
            if i13 >= self.r:
                i13 -= self.r
            pygame.draw.circle(self.sc, self.c,
                               (self.x, self.y), i13, 5)
        if self.l >= 14:
            i14 = i13 + self.r // self.l
            if i14 >= self.r:
                i14 -= self.r
            pygame.draw.circle(self.sc, self.c,
                               (self.x, self.y), i14, 5)
        if self.l >= 15:
            i15 = i14 + self.r // self.l
            if i15 >= self.r:
                i15 -= self.r
            pygame.draw.circle(self.sc, self.c,
                               (self.x, self.y), i15, 5)
        if self.l >= 16:
            i16 = i15 + self.r // self.l
            if i16 >= self.r:
                i16 -= self.r
            pygame.draw.circle(self.sc, self.c,
                               (self.x, self.y), i16, 5)
        if self.l >= 17:
            i17 = i16 + self.r // self.l
            if i17 >= self.r:
                i17 -= self.r
            pygame.draw.circle(self.sc, self.c,
                               (self.x, self.y), i17, 5)
        if self.l >= 18:
            i18 = i17 + self.r // self.l
            if i18 >= self.r:
                i18 -= self.r
            pygame.draw.circle(self.sc, self.c,
                               (self.x, self.y), i18, 5)
        if self.l >= 19:
            i19 = i18 + self.r // self.l
            if i19 >= self.r:
                i19 -= self.r
            pygame.draw.circle(self.sc, self.c,
                               (self.x, self.y), i19, 5)
        if self.l >= 20:
            i20 = i19 + self.r // self.l
            if i20 >= self.r:
                i20 -= self.r
            pygame.draw.circle(self.sc, self.c,
                               (self.x, self.y), i20, 5)

        i1 += self.sp
        self.a = i1
        self.fff=self.a

# щели
class Slit():
    def __init__(self, n, d):
        self.n = n
        self.d = d
        self.sc = sc

    def Draw(self):
        # pygame.draw.rect(self.sc, WHITE, (400, 0, 400, 800))
        # pygame.draw.rect(self.sc, BLACK, (780, 10, 10, 780))
        pygame.draw.rect(self.sc, BLACK, (395, 0, 10, 800))
        if self.n == 1:
            pygame.draw.rect(self.sc, WHITE, (395, 400 - self.d / 2, 10, self.d))
        if self.n == 2:
            pygame.draw.rect(self.sc, WHITE, (395, 400 - self.d * 1.5, 10, self.d))
            pygame.draw.rect(self.sc, WHITE, (395, 400 + self.d / 2, 10, self.d))
        if self.n == 3:
            pygame.draw.rect(self.sc, WHITE, (395, 400 - self.d * 2.5, 10, self.d))
            pygame.draw.rect(self.sc, WHITE, (395, 400 + self.d * 1.5, 10, self.d))
            pygame.draw.rect(self.sc, WHITE, (395, 400 - self.d / 2, 10, self.d))


# источник волн (сектoр)
class Ist1():
    def __init__(self, radius, xPos, yPos, color, length, speed, start, width, box, start_angle, stop_angle, dop):
        self.r = radius  # Макс. радиус 500
        self.a = start  # счётчик для радиусов -350
        self.x = xPos  # координата центра источника 400
        self.y = yPos  # координата центра источника 400
        self.c = color  # цвет волн RED
        self.sc = pygame.display.set_mode((WIDTH, HEIGHT))
        self.l = length  # длина волны 5
        self.sp = speed  # скоорость волны 6
        self.an1 = start_angle  # начальный угол сектора
        self.an2 = stop_angle  # конечный угол сектора
        self.w = width  # ширина полоски
        self.b = box  # есть ли сама точка
        self.d = dop

    def Draw(self):

        col = self.c
        col1 = self.c
        col2 = self.c
        col3 = self.c
        col4 = self.c
        col5 = self.c
        col6 = self.c
        col7 = self.c
        col8 = self.c
        col9 = self.c
        col10 = self.c
        col11 = self.c
        col12 = self.c
        col13 = self.c
        col14 = self.c
        col15 = self.c
        col16 = self.c
        col17 = self.c
        col18 = self.c
        col19 = self.c
        col20 = self.c
        '''if self.d:
            if i1<=141.42:
                col1=WHITE
            else:
                col1=col'''

        if self.b:
            pygame.draw.circle(self.sc, self.c,
                               (self.x, self.y), 5, self.w)
        i1 = self.a
        if i1 >= self.r:
            i1 -= self.r
        if self.d:
            if i1 <= 141.42:
                col1 = WHITE
            else:
                col1 = col
        pygame.draw.arc(self.sc, col1,
                        [self.x - i1, self.y - i1, 2 * i1, 2 * i1],
                        self.an1 * pi / 180, self.an2 * pi / 180, self.w)
        if self.l >= 2:

            i2 = i1 + self.r // self.l
            if i2 >= self.r:
                i2 -= self.r
            if self.d:
                if i2 <= 141.42:
                    col2 = WHITE
                else:
                    col2 = col
            pygame.draw.arc(self.sc, col2,
                            [self.x - i2, self.y - i2, 2 * i2, 2 * i2],
                            self.an1 * pi / 180, self.an2 * pi / 180, self.w)
        if self.l >= 3:
            i3 = i2 + self.r // self.l
            if i3 >= self.r:
                i3 -= self.r
            if self.d:
                if i3 <= 141.42:
                    col3 = WHITE
                else:
                    col3 = col
            pygame.draw.arc(self.sc, col3,
                            [self.x - i3, self.y - i3, 2 * i3, 2 * i3],
                            self.an1 * pi / 180, self.an2 * pi / 180, self.w)
        if self.l >= 4:
            i4 = i3 + self.r // self.l
            if i4 >= self.r:
                i4 -= self.r
            if self.d:
                if i4 <= 141.42:
                    col4 = WHITE
                else:
                    col4 = col
            pygame.draw.arc(self.sc, col4,
                            [self.x - i4, self.y - i4, 2 * i4, 2 * i4],
                            self.an1 * pi / 180, self.an2 * pi / 180, self.w)
        if self.l >= 5:
            i5 = i4 + self.r // self.l
            if i5 >= self.r:
                i5 -= self.r
            if self.d:
                if i5 <= 141.42:
                    col5 = WHITE
                else:
                    col5 = col
            pygame.draw.arc(self.sc, col5,
                            [self.x - i5, self.y - i5, 2 * i5, 2 * i5],
                            self.an1 * pi / 180, self.an2 * pi / 180, self.w)
        if self.l >= 6:
            i6 = i5 + self.r // self.l
            if i6 >= self.r:
                i6 -= self.r
            if self.d:
                if i6 <= 141.42:
                    col6 = WHITE
                else:
                    col6 = col
            pygame.draw.arc(self.sc, col6,
                            [self.x - i6, self.y - i6, 2 * i6, 2 * i6],
                            self.an1 * pi / 180, self.an2 * pi / 180, self.w)
        if self.l >= 7:
            i7 = i6 + self.r // self.l
            if i7 >= self.r:
                i7 -= self.r
            if self.d:
                if i7 <= 141.42:
                    col7 = WHITE
                else:
                    col7 = col
            pygame.draw.arc(self.sc, col7,
                            [self.x - i7, self.y - i7, 2 * i7, 2 * i7],
                            self.an1 * pi / 180, self.an2 * pi / 180, self.w)
        if self.l >= 8:
            i8 = i7 + self.r // self.l
            if i8 >= self.r:
                i8 -= self.r
            if self.d:
                if i8 <= 141.42:
                    col8 = WHITE
                else:
                    col8 = col
            pygame.draw.arc(self.sc, col8,
                            [self.x - i8, self.y - i8, 2 * i8, 2 * i8],
                            self.an1 * pi / 180, self.an2 * pi / 180, self.w)
        if self.l >= 9:
            i9 = i8 + self.r // self.l
            if i9 >= self.r:
                i9 -= self.r
            if self.d:
                if i9 <= 141.42:
                    col9 = WHITE
                else:
                    col9 = col
            pygame.draw.arc(self.sc, col9,
                            [self.x - i9, self.y - i9, 2 * i9, 2 * i9],
                            self.an1 * pi / 180, self.an2 * pi / 180, self.w)
        if self.l >= 10:
            i10 = i9 + self.r // self.l
            if i10 >= self.r:
                i10 -= self.r
            if self.d:
                if i10 <= 141.42:
                    col10 = WHITE
                else:
                    col10 = col
            pygame.draw.arc(self.sc, col10,
                            [self.x - i10, self.y - i10, 2 * i10, 2 * i10],
                            self.an1 * pi / 180, self.an2 * pi / 180, self.w)
        if self.l >= 11:
            i11 = i10 + self.r // self.l
            if i11 >= self.r:
                i11 -= self.r
            if self.d:
                if i11 <= 141.42:
                    col11 = WHITE
                else:
                    col11 = col
            pygame.draw.arc(self.sc, col11,
                            [self.x - i11, self.y - i11, 2 * i11, 2 * i11],
                            self.an1 * pi / 180, self.an2 * pi / 180, self.w)
        if self.l >= 12:
            i12 = i11 + self.r // self.l
            if i12 >= self.r:
                i12 -= self.r
            if self.d:
                if i12 <= 141.42:
                    col12 = WHITE
                else:
                    col12 = col
            pygame.draw.arc(self.sc, col12,
                            [self.x - i12, self.y - i12, 2 * i12, 2 * i12],
                            self.an1 * pi / 180, self.an2 * pi / 180, self.w)
        if self.l >= 13:
            i13 = i12 + self.r // self.l
            if i13 >= self.r:
                i13 -= self.r
            if self.d:
                if i13 <= 141.42:
                    col13 = WHITE
                else:
                    col13 = col
            pygame.draw.arc(self.sc, col13,
                            [self.x - i13, self.y - i13, 2 * i13, 2 * i13],
                            self.an1 * pi / 180, self.an2 * pi / 180, self.w)
        if self.l >= 14:
            i14 = i13 + self.r // self.l
            if i14 >= self.r:
                i14 -= self.r
            if self.d:
                if i14 <= 141.42:
                    col14 = WHITE
                else:
                    col14 = col
            pygame.draw.arc(self.sc, col14,
                            [self.x - i14, self.y - i14, 2 * i14, 2 * i14],
                            self.an1 * pi / 180, self.an2 * pi / 180, self.w)
        if self.l >= 15:
            i15 = i14 + self.r // self.l
            if i15 >= self.r:
                i15 -= self.r
            if self.d:
                if i15 <= 141.42:
                    col15 = WHITE
                else:
                    col15 = col
            pygame.draw.arc(self.sc, col15,
                            [self.x - i15, self.y - i15, 2 * i15, 2 * i15],
                            self.an1 * pi / 180, self.an2 * pi / 180, self.w)
        if self.l >= 16:
            i16 = i15 + self.r // self.l
            if i16 >= self.r:
                i16 -= self.r
            if self.d:
                if i16 <= 141.42:
                    col16 = WHITE
                else:
                    col16 = col
            pygame.draw.arc(self.sc, col16,
                            [self.x - i16, self.y - i16, 2 * i16, 2 * i16],
                            self.an1 * pi / 180, self.an2 * pi / 180, self.w)
        if self.l >= 17:
            i17 = i16 + self.r // self.l
            if i17 >= self.r:
                i17 -= self.r
            if self.d:
                if i17 <= 141.42:
                    col17 = WHITE
                else:
                    col17 = col
            pygame.draw.arc(self.sc, col17,
                            [self.x - i17, self.y - i17, 2 * i17, 2 * i17],
                            self.an1 * pi / 180, self.an2 * pi / 180, self.w)
        if self.l >= 18:
            i18 = i17 + self.r // self.l
            if i18 >= self.r:
                i18 -= self.r
            if self.d:
                if i18 <= 141.42:
                    col18 = WHITE
                else:
                    col18 = col
            pygame.draw.arc(self.sc, col18,
                            [self.x - i18, self.y - i18, 2 * i18, 2 * i18],
                            self.an1 * pi / 180, self.an2 * pi / 180, self.w)
        if self.l >= 19:
            i19 = i18 + self.r // self.l
            if i19 >= self.r:
                i19 -= self.r
            if self.d:
                if i19 <= 141.42:
                    col19 = WHITE
                else:
                    col19 = col
            pygame.draw.arc(self.sc, col19,
                            [self.x - i19, self.y - i19, 2 * i19, 2 * i19],
                            self.an1 * pi / 180, self.an2 * pi / 180, self.w)
        if self.l >= 20:
            i20 = i19 + self.r // self.l
            if i20 >= self.r:
                i20 -= self.r
            if self.d:
                if i20 <= 141.42:
                    col20 = WHITE
                else:
                    col20 = col
            pygame.draw.arc(self.sc, col20,
                            [self.x - i20, self.y - i20, 2 * i20, 2 * i20],
                            self.an1 * pi / 180, self.an2 * pi / 180, self.w)
        i1 += self.sp
        self.a = i1


class Ref:

    def __init__(self, v1, v2, width, length, r_max ):
        self.v1 = v1
        self.v2 = v2
        self.l = length
        self.w = width
        self.sc = sc
        self.h = 200
        #self.a = True
        #self.t = 0
        self.m = 0
        self.pos = 0
        self.radius_i = self.h
        self.sin_a = []
        self.sin_b = []
        self.x_pos = []
        self.y = []
        self.x_neg = []
        self.t_collision_last = 0
        self.sin_a_clone = 0
    def Draw(self):



        self.pos += self.v1
        if self.pos > self.h:

            # итерируем по радиусам
            self.sin_a.append(((self.radius_i ** 2 - self.h ** 2) ** 0.5) / self.radius_i)
            self.sin_b.append((self.v2 / self.v1) * self.sin_a[-1])
            sin_a_clone = self.sin_a[-1]
            if sin_a_clone < self.v1 / self.v2:

                self.t_collision_prev = self.t_collision_last
                self.t_collision_last = (self.radius_i - self.h) / self.v1
                self.x_pos.append(2 * self.h + self.radius_i * self.sin_a[-1])
                self.x_neg.append(2 * self.h - self.radius_i * self.sin_a[-1])
                self.y.append(2 * self.h)
                for i in range(len(self.sin_a) - 1):
                    self.x_pos[i] += self.v2 * self.sin_b[i] * (self.t_collision_last - self.t_collision_prev)
                    self.y[i] += self.v2 * ((1 - self.sin_b[i] ** 2) ** 0.5) * (self.t_collision_last - self.t_collision_prev)
                    self.x_neg[i] -= self.v2 * self.sin_b[i] * (self.t_collision_last - self.t_collision_prev)
                # использование с какого-то момента "фантомного" времени коллизии позволяет сделать так,
                # что между соседними кадрами отрисовки для всех кривых проходит одинаковое количество времени

            else:
                self.m += 1
                self.t_collision_prev = self.t_collision_last
                self.t_collision_last = (self.radius_i - self.h) / self.v1
                for i in range(len(self.sin_a) - self.m):
                    self.x_pos[i] += self.v2 * self.sin_b[i] * (self.t_collision_last - self.t_collision_prev)
                    self.y[i] += self.v2 * ((1 - self.sin_b[i] ** 2) ** 0.5) * (self.t_collision_last - self.t_collision_prev)
                    self.x_neg[i] -= self.v2 * self.sin_b[i] * (self.t_collision_last - self.t_collision_prev)
            self.radius_i += self.v1
            if self.pos > self.h + self.v1:
                for i in range(len(self.x_pos) - 1):
                    pygame.draw.line(sc, YELLOW, [self.x_pos[i], self.y[i]], [self.x_pos[i + 1], self.y[i + 1]],
                                     self.w)
                    pygame.draw.line(sc, YELLOW, [self.x_neg[i], self.y[i]], [self.x_neg[i + 1], self.y[i + 1]],
                                     self.w)


