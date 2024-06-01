import time
import pygame
import random
from BubbleSort import bubble_sort
from SelectionSort import selection_sort
from InsertionSort import insertion_sort
from BogoSort import bogo_sort

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
        array.append(random.randint(1, 500))
    return array


def single_draw(a):
    WIN.fill(BLACK)
    pygame.draw.line(WIN, WHITE, (40, HEIGHT - 50), (WIDTH - 30, HEIGHT - 50), 5)  # x axis
    pygame.draw.line(WIN, WHITE, (40, 40), (40, HEIGHT - 40), 5)  # y axis
    for number in range(len(a)):
        NUM_BAR = a[number] * (HEIGHT - 70) // max(a)
        bar_width = WIDTH // (2 * len(a))
        space_width = 2
        pygame.draw.line(WIN, WHITE, (50 + space_width * (number + 1), HEIGHT - 50),
                         (50 + space_width * (number + 1), HEIGHT - NUM_BAR - 50), bar_width)

    pygame.display.update()


def double_draw(a1, a2):
    WIN.fill(BLACK)
    pygame.draw.line(WIN, WHITE, (40, 40), (40, HEIGHT - 40), 5)  # y axis
    pygame.draw.line(WIN, WHITE, (40, HEIGHT // 2), (WIDTH - 30, HEIGHT // 2), 5)  # x axis in the middle of screen

    for number in range(len(a1)):
        a1_NUM_BAR = a1[number] * (HEIGHT - 70) // 2 // max(a1)
        a2_NUM_BAR = a2[number] * (HEIGHT - 70) // 2 // max(a1)
        bar_width = WIDTH // (2 * len(a1))
        space_width = 2
        pygame.draw.line(WIN, WHITE, (50 + space_width * (number + 1), HEIGHT // 2),
                         (50 + space_width * (number + 1), HEIGHT // 2 - a1_NUM_BAR), bar_width)
        pygame.draw.line(WIN, WHITE, (50 + space_width * (number + 1), HEIGHT // 2),
                         (50 + space_width * (number + 1), HEIGHT // 2 + a2_NUM_BAR), bar_width)

    pygame.display.update()


def main():

    draw_mode = input("SORTING ALGORITHMS\n\nnChoose draw mode (single/double): ").lower()
    num_numbers = int(input("Enter the number of random numbers for the array: "))
    if draw_mode not in ['single', 'double']:
        print("Invalid draw mode. Defaulting to single draw.")
        draw_mode = 'single'

    pygame.init()

    a = gen_array(num_numbers)
    b = a.copy()
    clock = pygame.time.Clock()
    run = True

    sorting_generator1 = selection_sort(a)
    sorting_generator2 = insertion_sort(b)

    generator1_finished = False
    generator2_finished = False

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if draw_mode == 'double':
            double_draw(a, b)
            pygame.display.set_caption("Double Draw")
        else:
            single_draw(a)
            pygame.display.set_caption("Single Draw")

        try:
            a = next(sorting_generator1)
        except StopIteration:
            generator1_finished = True

        try:
            b = next(sorting_generator2)
        except StopIteration:
            generator2_finished = True

        if generator1_finished and generator2_finished:
            time.sleep(2)
            run = False

    pygame.quit()


main()

