import time
import pygame
import random
from BubbleSort import bubble_sort
from SelectionSort import selection_sort
from InsertionSort import insertion_sort
from MergeSort import merge_sort
WIDTH, HEIGHT = 1200, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Sort in Action")
FPS = 100

GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
PINK = (255, 192, 203)
BROWN = (165, 42, 42)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
AQUA = (100, 200, 200)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
WHITE = (255, 255, 255)
TURQUOISE = (64, 224, 208)


def is_moved(num):
    colour = RED


def gen_array(n):
    array = []
    for _ in range(n):
        array.append(random.randint(1, 200))
    return array


def draw_window(a):
    WIN.fill(BLACK)
    pygame.draw.line(WIN, WHITE, (40, HEIGHT - 50), (WIDTH - 30, HEIGHT - 50), 5)  # y axis
    pygame.draw.line(WIN, WHITE, (50, 50), (50, HEIGHT - 40), 5)  # x axis
    for number in range(len(a)):
        NUM_BAR = a[number] * 400 // max(a)
        bar_width = 800 // (2 * len(a))
        space_width = bar_width * 1.5
        pygame.draw.line(WIN, GREY, (50 + space_width * (number + 1), HEIGHT - 50),
                         (50 + space_width * (number + 1), HEIGHT - NUM_BAR - 50), bar_width)
        # print(a,number)

    pygame.display.update()


def main():
    a = gen_array(200)
    clock = pygame.time.Clock()
    run = True
    sorting_generator = selection_sort(a)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window(a)

        try:
            a = next(sorting_generator)
        except StopIteration:
            time.sleep(1)
            run = False

    pygame.quit()


main()
