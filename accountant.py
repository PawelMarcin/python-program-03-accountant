import sys

# ile argumentow podano w wywolaniu programu:
argumenty = len(sys.argv)
historia = None

# nie podano argumentu (poza nazwa programu):
if argumenty == 1:
  print('Nie podano argumentow.')
  print('  >  accountant.py argument lista_argumentow_opcjonalnych')
# opcja saldo:
elif sys.argv[1] == 'saldo':
  # podano za malo lub za duzo argumentow:
  if argumenty != 4 and argumenty > 2:
    print('Niewlasciwa liczba argumentow.')
    print('  >  accountant.py saldo wartosc_w_groszach komentarz')
  # podano wlasciwa ilosc argumentow:
  else:
    # jesli liczba argumentow 2 to tylko wyswietla "historie" z pliku
    # jesli liczba argumentow 4 to dopisuje argumenty do listy i wyswietla
    # uzupelniona liste
    saldo = list()
    while True:
      historia = input()
      if historia == 'saldo':
        saldo.append(int(input()))
        saldo.append(input())
      if historia == 'stop':
        break
    if argumenty == 4:
      saldo.append(int(sys.argv[2]))
      saldo.append(sys.argv[3])
    # wyswietlenie listy:
    for i in range(0, len(saldo), 2):
      print('saldo')
      print(saldo[i])
      print(saldo[i+1])
    # podano tylko argument 'saldo':
    if argumenty == 2:
      print('Wyswietlona zostala tylko historia operacji.')
      print('Aby dodac kolejna pozycje podaj dwa kolejne argumenty:')
      print('  >  accountant.py saldo wartosc_w_groszach komentarz')
# opcja sprzedaz:
elif sys.argv[1] == 'sprzedaz':
  # podano za malo lub za duzo argumentow:
  if argumenty != 5:
    print('Niewlasciwa liczba argumentow.')
    print('  >  accountant.py sprzedaz id_produktu cena ilosc')
  # podano wlasciwa ilosc argumentow:
  else:
    pass
# opcja zakup:
elif sys.argv[1] == 'zakup':
  # podano za malo lub za duzo argumentow:
  # podano wlasciwa ilosc argumentow:
  pass
# opcja konto:
elif sys.argv[1] == 'konto':
  # podano za malo lub za duzo argumentow:
  # podano wlasciwa ilosc argumentow:
  pass
# opcja magazyn:
elif sys.argv[1] == 'magazyn':
  # podano za malo lub za duzo argumentow:
  # podano wlasciwa ilosc argumentow:
  pass
# opcja przeglad:
elif sys.argv[1] == 'przeglad':
  # podano za malo lub za duzo argumentow:
  # podano wlasciwa ilosc argumentow:
  pass
# w kazdym innym przypadku:
else:
  print('Cos poszlo nie tak!')
  print('  >  accountant.py argument lista_argumentow_opcjonalnych')
  pass