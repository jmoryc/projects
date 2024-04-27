"""Firma z branży transportowej zajmuje się tymczasowym magazynowaniem
przewiezionego towaru. Niestety, często dochodzi do sytuacji, w której
dostępne magazyny są przepełnione. Dostaliśmy zlecenie na napisanie
programu, który będzie określał czy przy zamówieniu danej ilości sztuk towaru
magazyny zostaną przepełnione.

Sztuka towaru może być zakwalifikowana jako mała (zajmie 1 m2), średnia
(zajmie 2 m2) i duża (zajmie 3 m2). Wysokością towaru się nie przejmujemy.
Każdy magazyn jest takiej samej wielkości i może pomieścić 100 m2 towaru.

Program na wejściu otrzymuje ilość sztuk towaru każdej wielkości i ilość
dostępnych magazynów, ma poinformować użytkownika czy towar się
zmieści i z jak wielu magazynów będzie musiał skorzystać (ilość magazynów
ma być liczbą całkowitą).
"""
cargo_small = int(input("Proszę podaj ilość małych sztuk: "))
cargo_medium = int(input("Proszę podaj ilość średnich sztuk: "))
cargo_big = int(input("Proszę podaj ilość dużych sztuk: "))

free_storage = int(input("Proszę podaj ilość dostępnych magazynów: "))
whole_cargo = 1 * cargo_small + 2 * cargo_medium + 3 * cargo_big

required_storage = whole_cargo / 100
required_whole_storage = whole_cargo // 100

if required_storage % 1 != 0:
    required_whole_storage = required_whole_storage + 1

if free_storage < required_whole_storage:
    print("Dojdzie do przepełnienia!")

print("Ilość dostępnych magazynów:", free_storage)
print("Ilość wymaganych magazynów: ", required_whole_storage)

