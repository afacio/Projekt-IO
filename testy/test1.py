from Figura import Figura

f1 = Figura()

f1.setFigura("Bialy","Damka")
print(
f1.getWaga(),
f1.getKolor(),
f1.getKolorPrzeciwnika(),
f1.getFlagaBicia(),
f1.getFlagaRuchu(),
)
f1.setFlagaRuchu(True)
f1.setFlagaBicia(False)

print(f1.getFlagaRuchu(),
      f1.getFlagaBicia())