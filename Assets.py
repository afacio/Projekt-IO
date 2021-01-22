import pygame
SIZE = 80

WHITE_PAWN = pygame.transform.scale(pygame.image.load("../pawn_white.png"), (SIZE, SIZE))
BLACK_PAWN = pygame.transform.scale(pygame.image.load("../pawn_black.png"), (SIZE, SIZE))
WHITE_QUEEN = pygame.transform.scale(pygame.image.load("../queen_white.png"), (SIZE, SIZE))
BLACK_QUEEN = pygame.transform.scale(pygame.image.load("../queen_black.png"), (SIZE, SIZE))

SIZE = 80
BOARD_SIZE = 8
WHITE_COLOR = [200, 200, 200]
BLACK_COLOR = [100, 100, 100]

POLE_BIALE = 0
POLE_CZARNE = 1

MOVES = [
    (-1, -1),
    (+1, -1),
    (+1, +1),
    (-1, +1),
]