"""
1. Napisz program służący do zarządzania danymi pracownika. Program na wejściu
otrzyma imię, nazwisko, wiek, tytuł naukowy (puste, jeśli nie ma),
wysokość wynagrodzenia, staż pracy i nazwę stanowiska.

Każdy pracownik, którego staż pracy wynosi 2 lata lub więcej posiada
kartę multisport, informacja o tym fakcie, powinna również zostać
uwzględniona w programie.

Program powinien wyświetlić wszystkie informacje o pracowniku na ekranie. Każda z nich
powinna być wyświetlona w osobnej linijce.

2. Nasz program został zaprezentowany zamawiającemu. Po jego pokazie, klient stwierdził, że
potrzebuje, aby program przechowywał jeszcze połączone informacje dotyczące imienia,
nazwiska i tytułu naukowego pracownika.

Kolejna uwaga dotyczyła nazwy stanowiska, powinna zawsze zapisywana w całości dużymi
literami, niezależnie od tego co zostanie do programu wprowadzone.

Oprócz tego powinno pojawić się pole z informacją o rocznych zarobkach pracownika
uwzględniających premię, która co roku wynosi 5% wynagrodzenia rocznego.
Dodatkowo, należy zabezpieczyć pole związane ze stanowiskiem. W tej firmie nie
występują nazwy stanowisk dłuższe niż 12 znaków. Jeśli taka się pojawi program ma dalej
nie przetwarzać danych.

"""

name = input("Proszę podaj imię: ")
last_name = input("Proszę podaj nazwisko: ")
age = int(input("Proszę podaj wiek: "))
employee_title = input("Proszę podaj tytuł naukowy: ")
monthly_salary = float(input("Proszę podaj wynagrodzenie miesięczne: "))
years_of_work = int(input("Proszę podaj staż pracy: "))
position = input("Proszę podaj nazwę stanowiska: ")

if len(position) > 12:
    raise ValueError("Błąd. Wprowadzono błedną nazwę stanowiska.")

multisport = False 

employee_info = f"{name} {last_name} {employee_title}"
position = position.upper()
complete_yearly_salary = monthly_salary * 12 * 1.05

if years_of_work >= 2:
    multisport = True

print("Imię:", name)
print("Nazwisko:", last_name)
print("Wiek:", age)
print("Wysokośc wynagrodzenia miesiecznego:", monthly_salary)
print("Wysokośc wynagrodzenia rocznego wraz z premią:", complete_yearly_salary)
print("Staż pracy:", years_of_work)
print("Stanowisko:", position)
print("Tytuł:", employee_info)

if multisport == True:
    print("Pracownik posiada kartę multisport.")