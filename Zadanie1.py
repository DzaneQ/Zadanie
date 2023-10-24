#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Krok 1
class Zadanie:
    """
    Klasa reprezentująca zadania utworzone przez użytkownika.
    """
    
    def __init__(self, tytul, opis, termin_wykonania, wykonane=False, **kwargs):
        self.tytul = tytul
        self.opis = opis
        self.termin_wykonania = termin_wykonania
        self.wykonane = wykonane
        self.dodatkowe_informacje = kwargs     
        """
        Inicjalizacja zadania
        
        :param self: zadanie do inicjalizacji
        :param tytul: tytuł zadania
        :param opis: opis zadania
        :param termin_wykonania: termin na wykonanie zadania
        :param wykonane: wartość logiczna określająca, czy zadanie jest wykonane
        :param **kwargs: zbiór dodatkowych kluczy reprezentujących dodatkowe informacje o zadaniu
        """
    
    def __str__(self):
        wykonane_str = " [wykonane]" if self.wykonane else ""
        informacje_str = ""
        for key, value in self.dodatkowe_informacje.items():
            informacje_str += f"; {key}: {value}"
        """
        Określenie zadania w formie tekstu
        
        :param self: zadanie, którego dotyczy tekst
        :return: tekst zadania
        """
        return f"{self.tytul}: {self.opis}; termin: {self.termin_wykonania}" + wykonane_str + informacje_str


# In[2]:


# Krok 2
class ZadaniePriorytetowe(Zadanie):
    """
    Klasa reprezentująca zadania priorytetowe utworzone przez użytkownika i magazynowane w systemie.
    """
    
    def __init__(self, tytul, opis, termin_wykonania, priorytet, **kwargs):
        self.tytul = tytul
        self.opis = opis
        self.termin_wykonania = termin_wykonania
        self.wykonane = False
        self.priorytet = priorytet
        self.dodatkowe_informacje = kwargs
        """
        Inicjalizacja zadania priorytetowego
        
        :param self: zadanie do inicjalizacji
        :param tytul: tytuł zadania
        :param opis: opis zadania
        :param termin_wykonania: termin na wykonanie zadania
        :param priorytet: priorytet zadania
        :param **kwargs: zbiór dodatkowych kluczy reprezentujących dodatkowe informacje o zadaniu
        """
        
    def __str__(self):
        wykonane_str = " [wykonane]" if self.wykonane else ""
        informacje_str = ""
        for key, value in self.dodatkowe_informacje.items():
            informacje_str += f"; {key}: {value}"
        """
        Określenie zadania priorytetowego w formie tekstu
        
        :param self: zadanie, którego dotyczy tekst
        :return: tekst zadania
        """
        return f"{self.tytul}: {self.opis}; termin: {self.termin_wykonania}" + wykonane_str + f" (priorytet: {self.priorytet})" + informacje_str
        
class ZadanieRegularne(Zadanie):
    """
    Klasa reprezentująca zadania regularne utworzone przez użytkownika i magazynowane w systemie.
    """
    
    def __init__(self, tytul, opis, termin_wykonania, powtarzalnosc, **kwargs):
        self.tytul = tytul
        self.opis = opis
        self.termin_wykonania = termin_wykonania
        self.wykonane = False
        self.powtarzalnosc = powtarzalnosc
        self.dodatkowe_informacje = kwargs
        """
        Inicjalizacja zadania regularnego
        
        :param self: zadanie do inicjalizacji
        :param tytul: tytuł zadania
        :param opis: opis zadania
        :param termin_wykonania: termin na wykonanie zadania
        :param powtarzalnosc: powtarzalność zadania
        :param **kwargs: zbiór dodatkowych kluczy reprezentujących dodatkowe informacje o zadaniu
        """
        
    def __str__(self):
        wykonane_str = " [wykonane]" if self.wykonane else ""
        informacje_str = ""
        for key, value in self.dodatkowe_informacje.items():
            informacje_str += f"; {key}: {value}"
        """
        Określenie zadania regularnego w formie tekstu
        
        :param self: zadanie, którego dotyczy tekst
        :return: tekst zadania
        """
        return f"{self.tytul}: {self.opis}; termin: {self.termin_wykonania}" + wykonane_str + f" (powtarzalność: {self.powtarzalnosc})" + informacje_str


# In[3]:


# Krok 3   
class ManagerZadan:
    """
    Klasa reprezentująca manager, w którym magazynowane są zadania.
    """
    
    def __init__(self):
        self.lista_zadan = []
        """
        Inicjalizacja managera zadań i utworzenie listy
        
        :param self: zainicjalizowany manager
        """
        
    def dodaj_zadanie(self, zadanie):
        self.lista_zadan.append(zadanie)
        """
        Tworzy zadanie
        
        :param self: manager, do którego ma być dodane zadanie
        :param zadanie: zadanie, które ma być dodane
        """
        
    def usun_zadanie(self, zadanie):
        index = self.lista_zadan.index(zadanie)
        del self.lista_zadan[index]
        """
        Usuwa zadanie
        
        :param self: manager, z którego ma być usunięte zadanie
        :param zadanie: zadanie, które ma być usunięte
        """
        
    def oznacz_jako_wykonane(self, zadanie):
        zadanie.wykonane = True
        """
        Oznacza zadanie jako wykonane
        
        :param self: manager, w którym znajduje się zadanie
        :param zadanie: zadanie, które ma być oznaczone jako wykonane
        """
        
    def edytuj_zadanie(self, zadanie, nowy_tytul, nowy_opis, nowy_termin, **kwargs):
        zadanie.tytul = nowy_tytul
        zadanie.opis = nowy_opis
        zadanie.termin_wykonania = nowy_termin
        zadanie.dodatkowe_informacje = kwargs      
        """
        Edytuje zadanie
        
        :param self: manager, w którym znajduje się zadanie do edycji
        :param zadanie: zadanie, które ma być edytowane
        :param nowy_tytul: nowy tytuł zadania
        :param nowy_opis: nowy opis zadania
        :param nowy_termin: nowy termin zadania
        :param **kwargs: zbiór dodatkowych kluczy reprezentujących dodatkowe informacje o zadaniu
        """
# Krok 4
    def __contains__(self, zadanie):
        """
        Sprawdza, czy w managerze znajduje się dane zadanie.
        
        :param self: manager, w którym szukane jest zadanie
        :param zadanie: wyszukiwane zadanie
        :return: wartość logiczna sprawdzająca, czy w managerze znajduje się zadanie
        """
        return zadanie in self.lista_zadan


# In[4]:


# Krok 7
def wartosc_terminu(zadanie):
    wartosci = zadanie.termin_wykonania.split("\\")
    wartosci = [int(i) for i in wartosci]
    """
    Wyznaczenie wartości terminu zadanie w formie liczbowej dla sortowania.

    :param zadanie: zadanie, którego termin jest określany
    :return: wartość liczbowa zadania ze względu na termin
    """
    return (wartosci[0] * 372) + (wartosci[1] * 31) + wartosci[2]

def sortuj_zadanie(manager, zadanie):
    wartosc = wartosc_terminu(zadanie)
    if zadanie in manager:
        manager.usun_zadanie(zadanie)
    for i in range(len(manager.lista_zadan)):
        if wartosc_terminu(manager.lista_zadan[i]) > wartosc_terminu(zadanie):
            manager.lista_zadan.insert(i, zadanie)
            break;
    if not zadanie in manager:
        manager.dodaj_zadanie(zadanie)
    """
    Funkcja sortowania zadania w managerze według terminu od najbliższego do najdalszego.

    :param manager: manager, w którym zadanie jest sortowane
    :param zadanie: zadanie podlegające sortowaniu
    """


# In[ ]:




