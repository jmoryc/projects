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

3. Klient jest zadowolony z funkcjonalności programu, ale oczekuje jeszcze zabezpieczenia
programu przed błędami użytkowników. W szczególności zależy mu na:
    1. Sprawdzeniu czy użytkownik podał imię, nazwisko.
    2. Sprawdzeniu czy podany wiek jest większy od zera i czy staż pracy oraz mięsięczne
    wynagrodzenie są większe bądź równe zeru.
    3. Sprawdzeniu czy imię i nazwisko składają się zawsze jedynie z liter.

Ostatnim wymaganiem związanym z naszym produktem jest zapewnienie persystencji dla
danych. W trakcie działania programu są one zbierane, ale nigdzie nie są przechowywane.
W tym celu należy wykorzystać bazę danych SQLite.
Dodaj do obecnie istniejącego kodu obsługę zapisywania danych do bazy
"""

import sqlite3

connection = sqlite3.connect("employees.db")

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                    id INTEGER PRIMARY KEY,
                    employee_info TEXT,
                    age INTEGER,
                    monthly_salary REAL,
                    complete_yearly_salary REAL,
                    years_of_work INTEGER,
                    position TEXT,
                    multisport INTEGER
                )''')

name = input("Proszę podaj imię: ")
last_name = input("Proszę podaj nazwisko: ")
age = int(input("Proszę podaj wiek: "))
employee_title = input("Proszę podaj tytuł naukowy: ")
monthly_salary = float(input("Proszę podaj wynagrodzenie miesięczne: "))
years_of_work = int(input("Proszę podaj staż pracy: "))
position = input("Proszę podaj nazwę stanowiska: ")

if name == "" or last_name == "":
    raise ValueError("Błąd. Brakujące imię lub nazwisko.")

if age <= 0:
    raise ValueError("Błąd. Podany wiek jest mniejszy od 0.")

if years_of_work < 0:
    raise ValueError("Błąd. Podany staż pracy jest mniejszy od 0.")

if monthly_salary < 0:
    raise ValueError("Błąd. Podane wynagrodzenie jest mniejsze od 0.")

if not name.isalpha():
    raise ValueError("Błąd. Imię posiada niedozwolone znaki.")

if not last_name.isalpha():
    raise ValueError("Błąd. Nazwisko posiada niedozwolone znaki.")

if len(position) > 12:
    raise ValueError("Błąd. Wprowadzono błedną nazwę stanowiska.")

multisport = False 

employee_info = f"{name} {last_name} {employee_title}"
position = position.upper()
complete_yearly_salary = monthly_salary * 12 * 1.05

if years_of_work >= 2:
    multisport = True

cursor.execute("INSERT INTO employees (employee_info, age, monthly_salary, complete_yearly_salary, years_of_work, position, multisport) \
               VALUES (?, ?, ?, ?, ?, ?, ?)", (employee_info, age, monthly_salary, complete_yearly_salary, years_of_work, position, multisport))

connection.commit()

cursor.execute("SELECT * FROM employees")
employees = cursor.fetchall()
print("Pracownicy w bazie danych:", employees)

cursor.close()
connection.close()

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