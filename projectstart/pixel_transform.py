"""Twoja firma odpowiada za tworzenie aplikacji, zespół zajmujący się grafiką przekazuje
twojemu kolory pixeli. Potrzebują, aby twój zespół przetworzył te wartości i przekazał im
poszczególne składniki RGB zapisane w systemie dziesiętnym. Uzyskaj wartości R, G, B dla
podanego na wejściu koloru pixela. Podany on zostanie w formacie heksadecymalnym np.
0xFF21F2. Program powinien przetłumaczyć wartości z systemu szesnastkowego na
dziesiętny i wypisać na ekranie.

Przykładowe dane wejściowe: 0xFF2F1A
Oczekiwany wynik: Red: 255 Green: 47 Blue: 26
"""

hex_pixel = input("Proszę podaj wartośc pixela (hex): ")
pixel = int(hex_pixel, 16)
print(pixel)

# RRRR RRRR GGGG GGGG BBBB BBBB
# RRRR RRRR
red = pixel >> 16

# RRRR RRRR GGGG GGGG BBBB BBBB
# RRRR RRRR GGGG GGGG
#           GGGG GGGG
green = (pixel >> 8) & 0xFF

# RRRR RRRR GGGG GGGG BBBB BBBB
# RRRR RRRR GGGG GGGG BBBB BBBB
#                     BBBB BBBB    
blue = pixel & 0xFF

print("Red:", red)
print("Green:", green)
print("Blue:", blue)
