#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 2.2
import time
def pomiar_czasu(funkcja):
    def zmierz_czas(*args, **kwargs):
        czas = time.time_ns()
        wynik = funkcja(*args, **kwargs)
        czas = time.time_ns() - czas
        print(f"Czas wykonania funkcji {funkcja.__name__}: {czas} nanosekund")
        return wynik
    return zmierz_czas


# In[2]:


# 2.1a
@pomiar_czasu
def zapisz_zadania(manager, nazwa_pliku):
    with open(nazwa_pliku, 'w') as plik:
        for zadanie in manager.lista_zadan:
            plik.write(str(zadanie) + "\n")
        
# 2.1b
@pomiar_czasu
def otworz_zadania(nazwa_pliku):
    manager = ManagerZadan()
    with open(nazwa_pliku, 'r') as plik:
        wiersze = plik.readlines()
        for linia in wiersze:
            if len(linia) == 0:
                continue
            tytul, reszta = linia.split(": ", 1)
            opis, reszta = reszta.split("; termin: ")[0], reszta.split("; termin: ")[1]
            termin_wykonania = reszta.split(" [wykonane]")[0].split(" (")[0]
            wykonane = "[wykonane]" in reszta
            #zadanie
            if " (priorytet: " in reszta:
                priorytet = reszta.split(" (priorytet: ")[1].split(")")[0]
                zadanie = ZadaniePriorytetowe(tytul, opis, termin_wykonania, priorytet)
            elif " (powtarzalność: " in reszta:
                powtarzalnosc = reszta.split(" (powtarzalność: ")[1].split(")")[0]
                zadanie = ZadanieRegularne(tytul, opis, termin_wykonania, powtarzalnosc)
            else:
                zadanie = Zadanie(tytul, opis, termin_wykonania, wykonane)
            if wykonane:
                manager.oznacz_jako_wykonane(zadanie)
            manager.dodaj_zadanie(zadanie)
    return manager


# In[1]:


# 2.4b
#import nbformat
#from nbconvert import HTMLExporter

#def udokumentuj_html(nazwa_pliku):
#    with open(f'{nazwa_pliku}.ipynb', 'r', encoding='utf-8') as plik:
#        zawartosc = nbformat.read(plik, as_version=4)
#    html_exporter = HTMLExporter()
#    (html_wyjscie, zasoby) = html_exporter.from_notebook_node(zawartosc)
#    with open(f'{nazwa_pliku}.html', 'w', encoding='utf-8') as dokument:
#        dokument.write(html_wyjscie)
        
#udokumentuj_html("Zadanie1")
#udokumentuj_html("Zadanie1a")
#udokumentuj_html("Zadanie2")


# In[ ]:


# 2.4b
from nbconvert import PythonExporter
import nbformat
import pydoc

def udokumentuj_py_html(nazwa_pliku):
    with open(f'{nazwa_pliku}.ipynb', 'r', encoding='utf-8') as plik:
        zawartosc = nbformat.read(plik, as_version=4)
    py_exporter = PythonExporter()
    (py_wyjscie, zasoby) = py_exporter.from_notebook_node(zawartosc)
    with open (f'{nazwa_pliku}.py', 'w', encoding='utf-8') as dokument:
        dokument.write(py_wyjscie)
    pydoc.writedoc(nazwa_pliku, f'{nazwa_pliku}.html')

udokumentuj_py_html("Zadanie1")
udokumentuj_py_html("Zadanie2")
udokumentuj_py_html("Zadanie1a")


# In[ ]:




