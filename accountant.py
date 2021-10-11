# Prosty program ksiegowo-magazynowy.
# Program swoja baze i historie operacji przechowuje w pliku tekstowym.
# Oryginalny plik: in.txt.
# Pliki robocze: historia.txt, output.txt.
# Program wywolywany jest z wiersza polecen z jednym z argumentow:
#     saldo, sprzedaz, zakup, konto, magazyn, przeglad.
# Brak argumentu i niewlasciwa liczba argumentow opcjonalnych powoduje blad
# i wyjscie z programu z komunikatem o bledzie.
#  > accontant.py argument [argumenty_opcjonalne]
# Po argumentach nalezy podac przekierowanie wejscia danych ( < in.txt | 
# | < historia.txt) i, ewentualnie, przekierowanie wyjscia danych ( > out.txt |
# | > output.txt) - blad braku przekierowania wejscia nie jest obslugiwany!

import sys
# stale - komunikaty o bledach i informacje
blad_wywolania = 'Bledny argument.\n' \
                 'Uzyj komendy:\n' \
                 '  > [python] accountant.py argument [argumenty_opcjonalne]\n'\
                 '  argument:               saldo, sprzedaz, zakup, konto,'\
                 ' magazyn, przeglad\n' \
                 '  argumenty_opcjonalne:   zaleza od wybranego argumentu'
blad_akcji = 'Niedozwolona akcja! ({})'
blad_argumentow_opcjonalnych_saldo = \
  'Niewlasciwa liczba argumentow dla opcji {}.\n' \
  'Uzyj komendy:\n' \
  '  > [python] accountant.py {} [int_wartosc_w_groszach str_komentarz]'
blad_argumentow_opcjonalnych_zakup_sprzedaz = \
  'Niewlasciwa liczba argumentow dla opcji {}.\n' \
  'Uzyj komendy:\n' \
  '  > [python] accountant.py {} [str_id_produktu int_cena int_ile_sztuk]'
blad_argumentow_opcjonalnych_konto = \
  'Opcja {} nie ma argumentow dodatkowaych.\n' \
  'Uzyj komendy:\n' \
  '  > [python] accountant.py {}'
blad_argumentow_opcjonalnych_przeglad = \
  'Niewlasciwa liczba argumentow dla opcji {}.\n' \
  'Uzyj komendy:\n' \
  '  > [python] accountant.py {} [int_indeks_od int_indeks_do]'
informacja_saldo = \
  'Wyswietlna zostala pelna historia operacji.\n' \
  'Aby dodac nowa pozycje uzyj komendy:\n' \
  '  > [python] accountant.py {} int_wartosc_w_groszach str_komentarz'
informacja_zakup_sprzedaz = \
  'Wyswietlona zostala pelna historia operacji.\n' \
  'Aby dodac nowa pozycje uzyj komendy:\n' \
  '  > [python] accountant.py {} str_id_produktu int_cena int_ile_sztuk'
informacja_przeglad = \
  'Wyswietlona zostala pelna historia operacji.\n' \
  'Aby ograniczyc liste uzyj komendy:\n' \
  '  > [python] accountant.py {} int_indeks_od int_indeks_do'
informacja_magazyn = \
  'Wyswietlony zostal pelny stan magazynu.\n' \
  'Aby ograniczyc liste artykulow uzyj komendy:\n' \
  '  > [python] accountant.py {} str_id_art_1 [str_id_art_2 [...]]'

informacja = ''

# dopuszczalne argumenty wymagane
lista_agumentow = ['saldo', 'sprzedaz', 'zakup', 'konto', 'magazyn', 'przeglad']

# ile argumentow podano w wywolaniu programu
liczba_argumentow = len(sys.argv)

# czy podano argument obligatoryjny i czy jest on poprawny
if liczba_argumentow == 1:
  # nie podano argumentu
  print(blad_wywolania)
else:
  # podano co najmniej jeden argument (argument wymagany)
  argument = sys.argv[1]
  # czy podany argument jest dopuszczalny
  if argument not in lista_agumentow:
    # nie, argument nie jest dopuszczalny
    print(blad_wywolania)
  # niewlascwa liczba argumentow dla opcji saldo
  elif argument == 'saldo' and liczba_argumentow > 2 and liczba_argumentow != 4:
    print(blad_argumentow_opcjonalnych_saldo.format(argument, argument))
  # niewlasciwa liczba argumentow dla opcji przeglad
  elif argument == 'przeglad' and liczba_argumentow > 2 \
    and liczba_argumentow != 4:
    print(blad_argumentow_opcjonalnych_przeglad.format(argument, argument))
  # niewlasciwa liczba argumentow dla opcji zakup / sprzedaz
  elif argument in ['sprzedaz', 'zakup'] and liczba_argumentow > 2 \
    and liczba_argumentow != 5:
    print(blad_argumentow_opcjonalnych_zakup_sprzedaz.format(argument, argument))
  # niewlasciwa liczba argumentow dla opcji konto
  elif argument == 'konto' and liczba_argumentow > 2:
    print(blad_argumentow_opcjonalnych_konto.format(argument, argument))
  # tak, argument jest poprawny i liczba argumentow opcjonalnych jest poprawna
  else:
    # wczytanie historii z pliku
    historia = []
    while True:
      akcja = input()
      # koniec pliku z historia i wyjscie z petli
      if akcja == 'stop':
        break
      # blad akcji w pliku z historia, dozwolone: saldo, zakup, sprzedaz
      # - wyjscie z petli
      elif akcja not in ['saldo', 'sprzedaz', 'zakup']:
        print(blad_akcji.format(akcja))
        break
      # wszystko OK, wczytanie historii do listy
      else:
        akcje = []
        if akcja == 'saldo':
          akcje.append(akcja)
          akcje.append(int(input()))
          akcje.append(input())
        else:
          akcje.append(akcja)
          akcje.append(input())
          akcje.append(int(input()))
          akcje.append(int(input()))
      historia.append(akcje)
    # ustalenie biezacego salda i stanow magazynowych
    saldo = 0
    stan_magazynu = dict()
    for i in historia:
      if i[0] == 'saldo':
        saldo += i[1]
      elif i[0] == 'sprzedaz':
        saldo += i[2] * i[3]
        if not stan_magazynu.get(i[1]):
          stan_magazynu.update({i[1]: 0})
        stan_magazynu[i[1]] -= i[3]
      else:
        saldo -= i[2] * i[3]
        if not stan_magazynu.get(i[1]):
          stan_magazynu.update({i[1]: 0})
        stan_magazynu[i[1]] += i[3]

    # czy drukowac podsumowanie/historie
    drukuj_historie = True
    # zakres wydruku podsumowania/historii
    indeks_od = 0
    indeks_do = len(historia)

    # ewentualne dodanie do listy operacji argumentow z linii polecen i magia
    if argument == 'saldo':
      # nie podano argumentow opcjonalnych
      if liczba_argumentow == 2:
        informacja = informacja_saldo.format(argument)
      # dodanie argumentow opcjonalnych (liczba_argumentow == 4)
      else:
        akcje = [argument, int(sys.argv[2]), sys.argv[3]]
        if saldo + akcje[1] >= 0:
          historia.append(akcje)
          saldo += akcje[1]
          indeks_do = len(historia)
        else:
          print('Przekroczono dostepny limit srodkow.')
          drukuj_historie = False
    elif argument == 'sprzedaz':
      # nie podano argumentow opcjonalnych
      if liczba_argumentow == 2:
        informacja = informacja_zakup_sprzedaz.format(argument)
      # dodanie argumentow opcjonalnych (liczba_argumentow == 5)
      else:
        akcje = [argument, sys.argv[2], int(sys.argv[3]), int(sys.argv[4])]
        s = stan_magazynu.get(akcje[1])
        if not s:
          s = 0
        if akcje[3] > s:
          print('Brak wystarczajacej ilosci artykulu {} na stanie.'
                .format(akcje[1]))
          drukuj_historie = False
        elif akcje[2] < 0 or akcje[3] < 0:
          print('Cena lub liczba sztuk nie moze byc ujemna.')
          drukuj_historie = False
        else:
          historia.append(akcje)
          indeks_do = len(historia)
          saldo += akcje[2] * akcje[3]
          stan_magazynu[akcje[1]] -= akcje[3]
    elif argument == 'zakup':
      # nie podano argumentow opcjonalnych
      if liczba_argumentow == 2:
        informacja = informacja_zakup_sprzedaz.format(argument)
      # dodanie argumentow opcjonalnych (liczba_argumentow == 5)
      else:
        akcje = [argument, sys.argv[2], int(sys.argv[3]), int(sys.argv[4])]
        koszt = akcje[2] * akcje[3]
        if koszt > saldo:
          print('Przekroczono dostepny limit srodkow.')
          drukuj_historie = False
        elif akcje[2] < 0 or akcje[3] < 0:
          print('Cena lub liczba sztuk nie moze byc ujemna.')
          drukuj_historie = False
        else:
          historia.append(akcje)
          indeks_do = len(historia)
          saldo -= koszt
          if not stan_magazynu.get(akcje[1]):
            stan_magazynu.update({akcje[1]: 0})
          stan_magazynu[akcje[1]] += akcje[3]
    elif argument == 'przeglad':
      # nie podano argumentow opcjonalnych
      if liczba_argumentow == 2:
        informacja = informacja_przeglad.format(argument)
      # podano argumenty opcjonalne (liczba argumentow == 4)
      else:
        indeks_od = int(sys.argv[2])
        indeks_do = int(sys.argv[3]) + 1
        if indeks_do > len(historia):
          indeks_do = len(historia)
    elif argument == 'magazyn':
      drukuj_historie = False
      # nie podano argumentow opcjonalnych
      if liczba_argumentow == 2:
        informacja = informacja_magazyn.format(argument)
        for k in stan_magazynu.keys():
          print(k + ': ' + str(stan_magazynu[k]))
      # podano argumenty opcjonalne (liczba_argumentow > 2)
      else:
        for k in sys.argv[2:]:
          v = stan_magazynu.get(k)
          if not v:
            v = 0
          print(k + ': ' + str(v))
    elif argument == 'konto':
      drukuj_historie = False
      print(saldo)

    if drukuj_historie:
      for i in range(indeks_od, indeks_do):
        for j in historia[i]:
          print(j)

      print('stop')

    if informacja:
      print()
      print(informacja)
