from Figura import Figura
import Assets as A

class Plansza():
    def __init__(self):
        self.plansza = []

    def turaCzyjRuch(self, tura):
        if tura % 2 == 0:
            return "Bialy"
        else:
            return "Czarny"

    def ustawieniePocz(self):
        self.plansza = A.BOARD_SIZE * [0]
        for x in range(A.BOARD_SIZE):
            self.plansza[x] = [0] * A.BOARD_SIZE

        for y in range(3):
            for x in range(A.BOARD_SIZE):
                if y % 2 == 0:
                    if x % 2 == 0:
                        self.plansza[x][y] = A.POLE_BIALE
                    else:
                        None
                        f = Figura()
                        f.setFigura("Czarny", "Pionek")
                        self.plansza[x][y] = f
                else:
                    if x % 2 == 0:
                        f = Figura()
                        f.setFigura("Czarny", "Pionek")
                        self.plansza[x][y] = f
                    else:
                        self.plansza[x][y] = A.POLE_BIALE

        for y in range(3, 5):
            for x in range(A.BOARD_SIZE):
                if y % 2 == 0:
                    if x % 2 == 0:
                        self.plansza[x][y] = A.POLE_BIALE
                    else:
                        self.plansza[x][y] = A.POLE_CZARNE
                else:
                    if x % 2 == 0:
                        self.plansza[x][y] = A.POLE_CZARNE
                    else:
                        self.plansza[x][y] = A.POLE_BIALE

        for y in range(5, A.BOARD_SIZE):
            for x in range(A.BOARD_SIZE):
                if y % 2 == 0:
                    if x % 2 == 0:
                        self.plansza[x][y] = A.POLE_BIALE
                    else:
                        f = Figura()
                        f.setFigura("Bialy", "Pionek")
                        self.plansza[x][y] = f
                else:
                    if x % 2 == 0:
                        f = Figura()
                        f.setFigura("Bialy", "Pionek")
                        self.plansza[x][y] = f
                    else:
                        self.plansza[x][y] = A.POLE_BIALE

    def czyWygrana(self):
        ilosc_bialych = 0
        ilosc_czarnych = 0
        for y in range(A.BOARD_SIZE):
            for x in range(A.BOARD_SIZE):
                if type(self.plansza[x][y]) is Figura and Figura.getKolor(self.plansza[x][y]) == "Bialy":
                    ilosc_bialych += 1
                if type(self.plansza[x][y]) is Figura and Figura.getKolor(self.plansza[x][y]) == "Czarny":
                    ilosc_czarnych += 1

        if ilosc_czarnych == 0:
            print("Koniec, wygrał Bialy")
            return True
        elif ilosc_bialych == 0:
            print("Koniec, wygral Czarny")
            return True
        else:
            return False

    def usunFigure(self, pozycjaFigury):
        xF, yF = pozycjaFigury[0], pozycjaFigury[1]
        if type(self.plansza[xF][yF]) is Figura:
            self.plansza[xF][yF] = A.POLE_CZARNE

    def pionNaDamke(self):
         for y in range(A.BOARD_SIZE):
             for x in range(A.BOARD_SIZE):
                 if type(self.plansza[x][y]) is Figura and Figura.getWaga(self.plansza[x][y]) == "Pionek":
                     if y == 0 and Figura.getKolor(self.plansza[x][y]) == "Bialy":
                            Figura.setWaga(self.plansza[x][y], "Damka")
                     if y == 7 and Figura.getKolor(self.plansza[x][y]) == "Czarny":
                            Figura.setWaga(self.plansza[x][y], "Damka")

# TODO działa dla pionkow ale czy działa dla Damek ???
    def czyRuchJestMozliwy(self, tura):
        for y in range(A.BOARD_SIZE):
            for x in range(A.BOARD_SIZE):
                if type(self.plansza[x][y]) is Figura:
                    for delta_x, delta_y in A.MOVES:
                        x1, y1 = x + delta_x, y + delta_y
                        if (tura % 2 == 0 and Figura.getKolor(self.plansza[x][y]) == "Bialy") or  Figura.getWaga(self.plansza[x][y]) == "Damka":
                            if not x == 0 and not y == 0 and x - x1 == 1 and y - y1 == 1 and self.plansza[x1][y1] == A.POLE_CZARNE:
                                Figura.setFlagaRuchu(self.plansza[x][y], True)
                                print("[lewo-gora]")

                            if not x == 7 and not y == 0 and x - x1 == -1 and y - y1 == 1 and self.plansza[x1][y1] == A.POLE_CZARNE:
                                Figura.setFlagaRuchu(self.plansza[x][y], True)
                                print("[prawo-gora]")

                        if (not tura % 2 == 0 and Figura.getKolor(self.plansza[x][y]) == "Czarny") or  Figura.getWaga(self.plansza[x][y]) == "Damka":
                            if not x == 7 and not y == 7 and x - x1 == -1 and y - y1 == -1 and self.plansza[x1][y1] == A.POLE_CZARNE:
                                Figura.setFlagaRuchu(self.plansza[x][y], True)
                                print("[prawo-dol]")

                            if not x == 0 and not y == 7 and x - x1 == 1 and y - y1 == -1 and self.plansza[x1][y1] == A.POLE_CZARNE:
                                Figura.setFlagaRuchu(self.plansza[x][y], True)
                                print("[lewo-dol]")

        for y in range(A.BOARD_SIZE):
            for x in range(A.BOARD_SIZE):
                if type(self.plansza[x][y]) is Figura and Figura.getFlagaRuchu(self.plansza[x][y]) == True:
                    return True
        return False

    def czyWybranoFigure(self, pozycjaFigury):
         xM, yM = pozycjaFigury[0], pozycjaFigury[1]
         if type(self.plansza[xM][yM]) is Figura:
             return True
         else:
             return False

    def czyWybranoFigureKoloru(self, pozycjaFigury, kolor):
         xM, yM = pozycjaFigury[0], pozycjaFigury[1]
         if type(self.plansza[xM][yM]) is Figura and Figura.getKolor(self.plansza[xM][yM]) == kolor:
             return True                                    
         else:
             return False

    def czyWybranoFigureZdolnaDoRuchu(self, pozycjaFigury):
        xM, yM = pozycjaFigury[0], pozycjaFigury[1]
        if type(self.plansza[xM][yM]) is Figura and Figura.getFlagaRuchu(self.plansza[xM][yM]) == True:
            return True
        else:
            return False

# TODO działa dla pionkow ale czy działa dla Damek ???
    def czyWybranoPoleZdolneDoRuchu(self, pozycjaFigury, pozycjaPrzesuniecia):
        xF, yF = pozycjaFigury[0], pozycjaFigury[1]
        xP, yP = pozycjaPrzesuniecia[0], pozycjaPrzesuniecia[1]
        if type(self.plansza[xF][yF]) is Figura and self.plansza[xP][yP] == A.POLE_CZARNE:
             for delta_x, delta_y in A.MOVES:
                x1, y1 = xF + delta_x, yF + delta_y
                if Figura.getWaga(self.plansza[xF][yF]) == "Pionek" and Figura.getKolor(self.plansza[xF][yF]) == "Czarny":
                    if (xP == x1 and yP == y1) and yP - yF == 1:
                        return True
                if Figura.getWaga(self.plansza[xF][yF]) == "Pionek" and Figura.getKolor(self.plansza[xF][yF]) == "Bialy":
                    if (xP == x1 and yP == y1) and yP - yF == -1:
                        return True
                if Figura.getWaga(self.plansza[xF][yF]) == "Damka":
                    if xP - xF == yP - yF or xP - xF == -1 * (yP - yF):
                        return True
        return False
# TODO ustawia flagi bicia dla pionków przeciwnika
    def czyBicieJestMozliwe(self, tura, kolor):
        for y in range(A.BOARD_SIZE):
            for x in range(A.BOARD_SIZE):
                if type(self.plansza[x][y]) is Figura and Figura.getKolor(self.plansza[x][y]) == kolor:
                    for delta_x, delta_y in A.MOVES:
                        for i in range(A.BOARD_SIZE):
                            x1, y1 = x + i * delta_x, y + i * delta_y  # puste pole badz twoja figura
                            x2, y2 = x + (i + 1) * delta_x, y + (i + 1) * delta_y  # figura do zbicia
                            x3, y3 = x + (i + 2) * delta_x, y + (i + 2) * delta_y  # puste  pole za figurą do zbicia
                            if x not in (0, 1) and y not in (0, 1) and x2 - x1 == -1 and y2 - y1 == -1:
                                if x2 < 1 or y2 < 1:
                                    break
                                if type(self.plansza[x2][y2]) is Figura and Figura.getKolor(self.plansza[x2][y2]) == Figura.getKolorPrzeciwnika(self.plansza[x][y]) and self.plansza[x3][y3] == A.POLE_CZARNE:
                                    if Figura.getWaga(self.plansza[x][y]) == "Pionek" and (x1 == x and y1 == y):
                                        print("TAK:[lewo-gora]", x, y)
                                        Figura.setFlagaBicia(self.plansza[x][y], True)
                                    if Figura.getWaga(self.plansza[x][y]) == "Damka" and (self.plansza[x1][y1] == A.POLE_CZARNE or (x1 == x and y1 == y)):
                                        print("TAK:[lewo-gora]", x, y)
                                        Figura.setFlagaBicia(self.plansza[x][y], True)

                            if x not in (6, 7) and y not in (0, 1) and x2 - x1 == 1 and y2 - y1 == -1:
                                if x2 > 6 or y2 < 1:
                                    break
                                if type(self.plansza[x2][y2]) is Figura and Figura.getKolor(self.plansza[x2][y2]) == Figura.getKolorPrzeciwnika(self.plansza[x][y]) and self.plansza[x3][y3] == A.POLE_CZARNE:
                                    if Figura.getWaga(self.plansza[x][y]) == "Pionek" and (x1 == x and y1 == y):
                                        print("TAK:[prawo-gora]", x, y)
                                        Figura.setFlagaBicia(self.plansza[x][y], True)
                                    if Figura.getWaga(self.plansza[x][y]) == "Damka" and (self.plansza[x1][y1] == A.POLE_CZARNE or (x1 == x and y1 == y)):
                                        print("TAK:[prawo-gora]", x, y)
                                        Figura.setFlagaBicia(self.plansza[x][y], True)

                            if x not in (6, 7) and y not in (6, 7) and x2 - x1 == 1 and y2 - y1 == 1:
                                if x2 > 6 or y2 > 6:
                                    break

                                if type(self.plansza[x2][y2]) is Figura and Figura.getKolor(self.plansza[x2][y2]) == Figura.getKolorPrzeciwnika(self.plansza[x][y]) and self.plansza[x3][y3] == A.POLE_CZARNE:
                                    if Figura.getWaga(self.plansza[x][y]) == "Pionek" and (x1 == x and y1 == y):
                                        print("TAK:[prawo-dol]", x, y)
                                        Figura.setFlagaBicia(self.plansza[x][y], True)
                                    if Figura.getWaga(self.plansza[x][y]) == "Damka" and (self.plansza[x1][y1] == A.POLE_CZARNE or (x1 == x and y1 == y)):
                                        print("TAK:[prawo-dol]", x, y)
                                        Figura.setFlagaBicia(self.plansza[x][y], True)

                            if x not in (0, 1) and y not in (6, 7) and x2 - x1 == -1 and y2 - y1 == 1:
                                if x2 < 1 or y2 > 6:
                                    break
                                if type(self.plansza[x2][y2]) is Figura and Figura.getKolor(self.plansza[x2][y2]) == Figura.getKolorPrzeciwnika(self.plansza[x][y]) and self.plansza[x3][y3] == A.POLE_CZARNE:
                                    if Figura.getWaga(self.plansza[x][y]) == "Pionek" and (x1 == x and y1 == y):
                                        print("TAK:[lewo-dol]", x, y)
                                        Figura.setFlagaBicia(self.plansza[x][y], True)
                                    if Figura.getWaga(self.plansza[x][y]) == "Damka" and (self.plansza[x1][y1] == A.POLE_CZARNE or (x1 == x and y1 == y)):
                                        print("TAK:[lewo-dol]", x, y)
                                        Figura.setFlagaBicia(self.plansza[x][y], True)

        for y in range(A.BOARD_SIZE):
            for x in range(A.BOARD_SIZE):
                if tura % 2 == 0 and type(self.plansza[x][y]) is Figura:
                    if Figura.getKolor(self.plansza[x][y]) == "Bialy" and Figura.getFlagaBicia(self.plansza[x][y]) == True:
                        return True

                if not tura % 2 == 0 and type(self.plansza[x][y]) is Figura:
                    if Figura.getKolor(self.plansza[x][y]) == "Czarny" and Figura.getFlagaBicia(self.plansza[x][y]) == True:
                        return True
        return False

    def czyWybranoFigureZdolnaDoBicia(self, pozycjaFigury):
        xM, yM = pozycjaFigury[0], pozycjaFigury[1]
        if type(self.plansza[xM][yM]) is Figura and Figura.getFlagaBicia(self.plansza[xM][yM]) == True:
            return True
        else:
            return False

# TODO działa dla pionkow ale czy działa dla Damek ???
    def czyWybranoPoleZdolneDoBicia(self, pozycjaFigury, pozycjaPrzesuniecia):
        xF, yF = pozycjaFigury[0], pozycjaFigury[1]
        xP, yP = pozycjaPrzesuniecia[0], pozycjaPrzesuniecia[1]
        if type(self.plansza[xF][yF]) is Figura and self.plansza[xP][yP] == A.POLE_CZARNE:
            for delta_x, delta_y in A.MOVES:
                x1, y1 = xF + delta_x, yF + delta_y #figura przeciwnika
                x2, y2 = xF + 2 * delta_x, yF + 2 * delta_y #puste pole
                if type(self.plansza[x1][y1]) is Figura and Figura.getKolorPrzeciwnika(self.plansza[xF][yF]) == Figura.getKolor(self.plansza[x1][y1]):
                    if Figura.getWaga(self.plansza[xF][yF]) == "Pionek" and xP == x2 and yP == y2:
                        return True
                    if Figura.getWaga(self.plansza[xF][yF]) == "Damka" and (xP - xF == yP - yF or xP - xF == -1 * (yP - yF)):
                        return True
        return False

    def zmianaPozycjiFigury(self, pozycjaFigury, pozycjaPrzesuniecia):
        xF, yF = pozycjaFigury[0], pozycjaFigury[1]
        xP, yP = pozycjaPrzesuniecia[0], pozycjaPrzesuniecia[1]
        if type(self.plansza[xF][yF]) is Figura and self.plansza[xP][yP] == A.POLE_CZARNE:
            self.plansza[xP][yP] = self.plansza[xF][yF]
            self.plansza[xF][yF] = A.POLE_CZARNE

    def resetujFlagi(self):
        for y in range(A.BOARD_SIZE):
            for x in range(A.BOARD_SIZE):
                if type(self.plansza[x][y]) is Figura:
                    Figura.setFlagaRuchu(self.plansza[x][y], False)
                    Figura.setFlagaBicia(self.plansza[x][y], False)

# TODO działa dla pionkow ale czy działa dla Damek ???
    def znajdzFigurePomiedzy(self, pozycjaFigury, pozycjaPrzesuniecia):
        xF, yF = pozycjaFigury[0], pozycjaFigury[1]
        xP, yP = pozycjaPrzesuniecia[0], pozycjaPrzesuniecia[1]
        if type(self.plansza[xF][yF]) is Figura and self.plansza[xP][yP] == A.POLE_CZARNE:
            for delta_x, delta_y in A.MOVES:
                x1, y1 = xF + delta_x, yF + delta_y
                x2, y2 = xF + 2 * delta_x, yF + 2 * delta_y
                if type(self.plansza[x1][y1]) is Figura and Figura.getKolorPrzeciwnika(self.plansza[xF][yF]) == Figura.getKolor(self.plansza[x1][y1]):
                    if Figura.getWaga(self.plansza[xF][yF]) == "Pionek" and (xP == x2 and yP == y2):
                        return [x1, y1]
                    if Figura.getWaga(self.plansza[xF][yF]) == "Damka" and (xP - xF == yP - yF or xP - xF == -1 * (yP - yF)):
                        return [x1, y1]
        return False


