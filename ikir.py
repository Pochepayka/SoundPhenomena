import pygame

# from main import *

# характеристики экрана
WIDTH = 800
HEIGHT = 800
FPS = 10
# Задаем цвета
WHITE = (255, 255, 255)
WHITELE = (200, 200, 200)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 200, 255)
pi = 3.14159236
x_right = []
x_left = []
y = []
h = 10
v1 = 3.3
v2 = 14.5
pygame.init()
pygame.font.init()
pygame.mixer.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Дифракция")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
running = True
n_t = 10
t = h / v1
t_max = t + 10
delta_t = (t_max - t) / n_t
while running:
    clock.tick(FPS)
    sc.fill(WHITE)

   # while t < t_max:
    r_bound1 = v2 * h / (v2 ** 2 - v1 ** 2) ** (0.5)
    r_bound2 = v1 * t
    r = h
    n = 1000
    if r_bound1 < r_bound2:
        r_bound = r_bound1
    else:
        r_bound = r_bound2
    delta = (r_bound - r) / n
    while r < r_bound:
        x_right.append(400 + ((r * r - h * h) ** (0.5)) *
                       (v1 * v1 * r + v1 * v2 * v2 * t - v2 * v2 * r) / v1 / r)
        x_left.append(400 - ((r * r - h * h) ** (0.5)) *
                      (v1 * v1 * r + v1 * v2 * v2 * t - v2 * v2 * r) / v1 / r)
        y.append(-h - v2 * (((r ** 2) * ((v1 ** 2) - (v2 ** 2))
                             + ((v2 * h) ** 2)) ** (0.5)) / (v1 * r) * (t - r / v1))
        r = r + delta
    # команда на рисование
    for i in range(len(x_right)-2 ):
        #print(x_right[i], ' ', 400-y[i])
        pygame.draw.line(sc, GREEN, [x_right[i], 400-y[i]], [x_right[i+1 ], 400-y[i+1 ]], 1)
        pygame.draw.line(sc, GREEN, [x_left[i], 400 - y[i]], [x_left[i+1 ], 400 - y[i+1 ]], 1)
    t = t + delta_t
    x_right = []
    x_left = []
    y = []
    pygame.display.update()
    #all_sprites.update()
    #pygame.display.flip()
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    #


pygame.quit()