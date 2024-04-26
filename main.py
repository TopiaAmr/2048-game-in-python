import itertools
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


class Tile:
    def __init__(self, value, col, row):
        self.value = value
        self.col = col
        self.row = row
        self.x = col * RECT_WIDTH
        self.y = row * RECT_HEIGHT

    def __repr__(self):
        return f"{self.value}"

    COLORS = [
        (224, 255, 255),
        (255, 247, 140),
        (255, 128, 114),
        (160, 179, 113),
        (135, 206, 250),
        (240, 128, 192),
        (152, 251, 152),
        (253, 180, 203),
        (176, 196, 222),
        (178, 223, 138),
        (255, 235, 205),
    ]

    def get_color(self):
        color_index = int(math.log(self.value) - 1)
        return self.COLORS[color_index]

    def draw(self, window):
        color = self.get_color()
        pygame.draw.rect(
            window,
            color,
            (self.x, self.y, RECT_WIDTH, RECT_HEIGHT),
        )
        text = FONT.render(str(self.value), True, FONT_COLOR)
        text_rect = text.get_rect(
            center=(self.x + RECT_WIDTH // 2, self.y + RECT_HEIGHT // 2)
        )
        window.blit(text, text_rect)

    def move(self, row, col):
        self.row = row
        self.col = col

    def set_position(self, x, y):
        self.x = x
        self.y = y


def draw(window, tiles):
    window.fill(BACKGROUND_COLOR)
    for tile in tiles.values():
        tile.draw(window)
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


def get_random_pos(tiles):
    row = None
    col = None

    while True:
        row = random.randrange(0, ROWS)
        col = random.randrange(0, COLS)

        if f"{row}-{col}" not in tiles:
            break

    return row, col


def generate_tiles():
    tiles = {}
    for _ in range(2):
        row, col = get_random_pos(tiles)
        tiles[f"{row}-{col}"] = Tile(2, row, col)
    return tiles


def main(window):
    clock = pygame.time.Clock()
    run = True

    tiles = generate_tiles()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw(window, tiles)


if __name__ == "__main__":
    main(WINDOW)
