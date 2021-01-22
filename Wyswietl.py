import pygame
import sys
import Assets as A
from Figura import Figura


class Wyswietl():

    def wyswietlPlansza(self, plansza):
        game_window = pygame.display.set_mode((A.SIZE * 8, A.SIZE * 9), 0, 32)
        pygame.display.set_caption('Warcaby')
        for y in range(A.BOARD_SIZE):
            for x in range(A.BOARD_SIZE):
                if y % 2 != 0:
                    if x % 2 != 0:
                        pygame.draw.rect(game_window, A.WHITE_COLOR, [A.SIZE * y, A.SIZE * x, A.SIZE, A.SIZE])
                    else:
                        pygame.draw.rect(game_window, A.BLACK_COLOR, [A.SIZE * y, A.SIZE * x, A.SIZE, A.SIZE])
                else:
                    if x % 2 != 0:
                        pygame.draw.rect(game_window, A.BLACK_COLOR, [A.SIZE * y, A.SIZE * x, A.SIZE, A.SIZE])
                    else:
                        pygame.draw.rect(game_window, A.WHITE_COLOR, [A.SIZE * y, A.SIZE * x, A.SIZE, A.SIZE])

        for y in range(A.BOARD_SIZE):
            for x in range(A.BOARD_SIZE):
                if type(plansza[x][y]) is Figura:
                    if Figura.getKolor(plansza[x][y]) == "Bialy":
                        if Figura.getWaga(plansza[x][y]) == "Pionek":
                            game_window.blit(A.WHITE_PAWN, (x * A.SIZE, y * A.SIZE))
                            pygame.display.flip()
                        if Figura.getWaga(plansza[x][y]) == "Damka":
                            game_window.blit(A.WHITE_QUEEN, (x * A.SIZE, y * A.SIZE))
                            pygame.display.flip()
                    if Figura.getKolor(plansza[x][y]) == "Czarny":
                        if Figura.getWaga(plansza[x][y]) == "Pionek":
                            game_window.blit(A.BLACK_PAWN, (x * A.SIZE, y * A.SIZE))
                            pygame.display.flip()
                        if Figura.getWaga(plansza[x][y]) == "Damka":
                            game_window.blit(A.BLACK_QUEEN, (x * A.SIZE, y * A.SIZE))
                            pygame.display.flip()
        pygame.display.flip()
        pygame.display.update()

    def wybierzFigureLubPole(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    #pygame.display.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        pos = pygame.mouse.get_pos()
                        pos = pos[0] // A.SIZE, pos[1] // A.SIZE
                        return pos

