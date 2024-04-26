import pygame
import random
import math

pygame.init()

FPS = 60

WIDTH, HEIGHT = 800, 800
ROWS = 4
COLS = 4

RECT_HEIGHT = HEIGHT // ROWS
RECT_WIDTH = WIDTH // COLS


OUTLINE_COLOR = (187, 173, 160)
OUTLINE_THICKNESS = 10
BACKGROUND_COLOR = (205, 192, 180)
FONT_COLOR = (119, 110, 101)


FONT = pygame.font.SysFont("comicsans", 60, bold=True)
MOVE_VEL = 20

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048 Game")


def draw(window):
    window.fill(BACKGROUND_COLOR)
    draw_grid(window)
    pygame.display.update()


def draw_grid(window):
    for i in range(1, ROWS):
        pygame.draw.line(
            window,
            OUTLINE_COLOR,
            (0, i * RECT_HEIGHT),
            (WIDTH, i * RECT_HEIGHT),
            OUTLINE_THICKNESS,
        )
    for j in range(1, COLS):
        pygame.draw.line(
            window,
            OUTLINE_COLOR,
            (j * RECT_WIDTH, 0),
            (j * RECT_WIDTH, HEIGHT),
            OUTLINE_THICKNESS,
        )
    pygame.draw.rect(window, OUTLINE_COLOR, (0, 0, WIDTH, HEIGHT), OUTLINE_THICKNESS)


def main(window):
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw(window)


if __name__ == "__main__":
    main(WINDOW)
