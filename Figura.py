class Figura():
    def __init__(self):
        self._kolor = None #Bialy lub Czarny
        self._kolorPrzeciwnika = None
        self._waga = None #Pionek lub Damka
        self._czyMoznaRuszyc = False
        self._czyMoznaBic = False

    def setFigura(self, kolor, waga):
        if kolor == "Bialy" or kolor == "Czarny":
            self._kolor = kolor
        else:
            print("Zle wprowadzony kolor")
            exit(1)

        if waga == "Pionek" or waga == "Damka":
            self._waga = waga
        else:
            print("Nieznany rodzaj figury")
            exit(1)

        if self._kolor == "Bialy":
            self._kolorPrzeciwnika = "Czarny"
        elif self._kolor == "Czarny":
            self._kolorPrzeciwnika = "Bialy"

    def setWaga(self, waga):
        if waga == "Pionek" or waga == "Damka":
            self._waga = waga
        else:
            print("Nieznany rodzaj figury")
            exit(1)

    def setFlagaRuchu(self, b):
        if type(b) is bool:
            self._czyMoznaRuszyc = b


    def setFlagaBicia(self, b):
        if type(b) is bool:
            self._czyMoznaBic = b

    def getKolor(self):
        return self._kolor

    def getKolorPrzeciwnika(self):
        return self._kolorPrzeciwnika

    def getWaga(self):
        return self._waga

    def getFlagaRuchu(self):
        return self._czyMoznaRuszyc

    def getFlagaBicia(self):
        return self._czyMoznaBic
