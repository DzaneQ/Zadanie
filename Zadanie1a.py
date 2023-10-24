#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Krok 5/6
get_ipython().run_line_magic('run', 'Zadanie1.ipynb')
get_ipython().run_line_magic('run', 'Zadanie2.ipynb')

try:
    manager = otworz_zadania("manager.txt")
    print("Wczytano plik.")
except FileNotFoundError:
    manager = ManagerZadan()

print("Wybierz opcję:")
print("a. Dodaj zadanie")
print("b. Usuń zadanie")
print("c. Oznacz jako wykonane")
print("d. Edytuj zadanie")
while True:
    print("Lista zadań:")
    if (len(manager.lista_zadan) == 0):
        print("Brak zadań")
    for i in range(len(manager.lista_zadan)):
        print(str(i+1)+". "+str(manager.lista_zadan[i]), sep='')
    try:
        inp = input("Wpisz literę opcji: ")
        if (inp == 'a'):
            tytul = input("Wpisz tytuł: ")
            opis = input("Wpisz opis: ")
            year = input("Wpisz rok wykonania: ")
            month = input("Wpisz miesiąc wykonania: ")
            day = input("Wpisz dzień wykonania: ")
            date = year+'\\'+month+'\\'+day.strip()
            option = input("Wpisz literę czy zadanie ma być: a. regularne; b. priorytetowe? ")
            if (option == 'a'):
                repeat = input("Co ile czasu ma być zadanie powtarzane? ")
                manager.dodaj_zadanie(ZadanieRegularne(tytul, opis, date, repeat, status="nowe"))
            elif (option == 'b'):
                priority = input("Jaki priorytet ma być przydzielony zadaniowi? ")
                manager.dodaj_zadanie(ZadaniePriorytetowe(tytul, opis, date, priority, status="nowe"))
            else:
                manager.dodaj_zadanie(Zadanie(tytul,opis,date, status="nowe"))
            sortuj_zadanie(manager, manager.lista_zadan[len(manager.lista_zadan)-1])
            zapisz_zadania(manager, "manager.txt")
        if (inp == 'b'):
            number = int(input("Wybierz numer zadania do usunięcia: "))
            if (number < len(manager.lista_zadan) + 1 and number > 0):
                manager.usun_zadanie(manager.lista_zadan[number-1])
                zapisz_zadania(manager, "manager.txt")
        if (inp == 'c'):
            number = int(input("Oznacz numer zadania jako wykonane: "))
            if (number < len(manager.lista_zadan) + 1 and number > 0):
                manager.oznacz_jako_wykonane(manager.lista_zadan[number-1])
                zapisz_zadania(manager, "manager.txt")
        if (inp == 'd'):
            number = int(input("Wpisz numer zadania do edycji: "))
            if (number < len(manager.lista_zadan) + 1 and number > 0):
                tytul = input("Wpisz tytuł: ")
                opis = input("Wpisz opis: ")
                year = input("Wpisz rok wykonania: ")
                month = input("Wpisz miesiąc wykonania: ")
                day = input("Wpisz dzień wykonania: ")
                date = year+'\\'+month+'\\'+day.strip()
                manager.edytuj_zadanie(manager.lista_zadan[number-1], tytul, opis, date, status="zmienione")
                sortuj_zadanie(manager, manager.lista_zadan[number-1])
                zapisz_zadania(manager, "manager.txt")
    except KeyboardInterrupt:
        break


# In[ ]:





# In[ ]:




