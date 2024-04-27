"""Napisz program służący do pracy z danymi studentów.
Dane, wprowadzane przez użytkownika:
Imię, Nazwisko, Wiek, Kierunek studiów, Średnia z przedmiotów humanistycznych (od 1.0 do 6.0), Średnia z
przedmiotów ścisłych (od 1.0 do 6.0), Nazwa uniwersytetu, Numer telefonu
Przykład:
Anna, Nowak, 22, Informatyka, 4.0, 5.0, AGH, 123123123
Dodatkowe wymagania:
1. Należy obliczyć średnią z obydwu wprowadzanych przez użytkownika i traktować ją jako średnią
semestralną.
2. Wszystkie dane wraz ze średnią semestralną należy wypisać na ekran.
Sprawdzanie danych:
1. Weryfikacja czy imię, nazwisko, kierunek studiów składają się wyłącznie z liter.
2. Weryfikacja czy wiek jest większy od zera.
3. Weryfikacja czy średnie są z zakresu od 1.0 do 6.0.
4. Weryfikacja czy numer składa się z 9 cyfr (wskazówka - len() i isdigit()).
"""

name = input("Proszę podaj imię: ")
last_name = input("Proszę podaj nazwisko: ")
age = int(input("Proszę podaj wiek: "))
subject = input("Proszę podaj kierunek studiów: ")
humane_average_grade = float(input("Proszę podaj średnią ocen z przedmiotów humanistycznych: "))
scientific_average_grade = float(input("Proszę podaj średnią ocen z przedmiotów ścisłych: "))
university = input("Proszę podaj nazwę uniwersytetu: ")
mobile = input("Proszę podaj numer telefonu: ")
average_grade = ((humane_average_grade + scientific_average_grade)/2)

if not name.isalpha():
    raise ValueError("Błąd. Imię posiada niedozwolone znaki.")

if not last_name.isalpha():
    raise ValueError("Błąd. Nazwisko posiada niedozwolone znaki.")

if not subject.isalpha():
    raise ValueError("Błąd. Kierunek studiów posiada niedozwolone znaki.")

if age <= 0:
    raise ValueError("Błąd. Wiek musi być większy od zera.")

if not 1.0 < humane_average_grade < 6.0:
    raise ValueError("Błąd. Średnia ocen powinna mieć watość od 1.0 do 6.0.")

if not 1.0 < scientific_average_grade < 6.0:
    raise ValueError("Błąd. Średnia ocen powinna mieć watość od 1.0 do 6.0.")

if len(mobile) != 9:
    raise ValueError("Błąd. Numer telefonu nie składa się z 9 cyfr.")

if not mobile.isdigit(): 
    raise ValueError("Błąd. Numer telefonu posiada błędne znaki.")

print("Imię:", name)
print("Nazwisko:", last_name)
print("Wiek:", age)
print("Kierunek studiów", subject)
print("Średnia ocen z przedmiotów humanistycznych", humane_average_grade)
print("Średnia ocen z przedmiotów ścisłych", scientific_average_grade)
print("Nazwa uniwersytetu:", university)
print("Numer telefonu:", mobile)
print("Średnia ocen:", average_grade)