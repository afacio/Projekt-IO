from Plansza import Plansza
from Wyswietl import Wyswietl

import time

class Gra():
    def __init__(self):
        self.plansza = Plansza()
        self.widokPlanszy = Wyswietl()
        self.tura = 0
        self.rozgrywka = True
        self.wybor = True

        self.plansza.ustawieniePocz()
        self.widokPlanszy.wyswietlPlansza(self.plansza.plansza)

    def przebiegGry(self):

        if not self.plansza.czyWygrana():
            self.plansza.resetujFlagi()
            print("Tura nr. ", self.tura)
            self.plansza.pionNaDamke()
            if self.plansza.czyBicieJestMozliwe(self.tura, self.plansza.turaCzyjRuch(self.tura)):
                while(True):
                    if not self.plansza.czyBicieJestMozliwe(self.tura, self.plansza.turaCzyjRuch(self.tura)):
                        break
                    else:
                        while (True):
                            print("Wybierz figurę którą chcesz wykonac bicie")
                            pozycjaFigury = self.widokPlanszy.wybierzFigureLubPole()
                            print(pozycjaFigury)
                            if self.plansza.czyWybranoFigureKoloru(pozycjaFigury, self.plansza.turaCzyjRuch(
                                    self.tura)) and self.plansza.czyWybranoFigureZdolnaDoBicia(pozycjaFigury):
                                break
                        while (True):
                            print("Wybierz miesce końca ruchu")
                            pozycjaPrzesuniecia = self.widokPlanszy.wybierzFigureLubPole()
                            if self.plansza.czyWybranoPoleZdolneDoBicia(pozycjaFigury, pozycjaPrzesuniecia):
                                pozycjaBitejFigury = self.plansza.znajdzFigurePomiedzy(pozycjaFigury, pozycjaPrzesuniecia)
                                if pozycjaBitejFigury:
                                    self.plansza.zmianaPozycjiFigury(pozycjaFigury, pozycjaPrzesuniecia)
                                    self.plansza.usunFigure(pozycjaBitejFigury)
                                    break
                        self.plansza.resetujFlagi()
                        self.widokPlanszy.wyswietlPlansza(self.plansza.plansza)

            elif self.plansza.czyRuchJestMozliwy(self.tura):
                while(True):
                    print("Wybierz figurę którą chcesz się poruszyć")
                    pozycjaFigury = self.widokPlanszy.wybierzFigureLubPole()
                    if self.plansza.czyWybranoFigureKoloru(pozycjaFigury, self.plansza.turaCzyjRuch(self.tura)) and self.plansza.czyWybranoFigureZdolnaDoRuchu(pozycjaFigury):
                        break
                while (True):
                    print("Wybierz miesce końca ruchu")
                    pozycjaPrzesuniecia = self.widokPlanszy.wybierzFigureLubPole()
                    if self.plansza.czyWybranoPoleZdolneDoRuchu(pozycjaFigury, pozycjaPrzesuniecia):
                        self.plansza.zmianaPozycjiFigury(pozycjaFigury, pozycjaPrzesuniecia)
                        break

            else:
                if self.tura % 2 == 0:
                    print("Wygrał gracz Czarny")
                else:
                    print("Wygrał gracz Bialy")
                time.sleep(2)
                exit(0)
        else:
            exit(0)
        self.tura += 1
        self.plansza.resetujFlagi()


g = Gra()
while(True):
    g.przebiegGry()
    g.widokPlanszy.wyswietlPlansza(g.plansza.plansza)