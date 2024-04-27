"""3. Napisz program, który będzie wypisywał na ekranie kolejne litery tekstu wpisanego
przez użytkownika. Jeżeli litera będzie spółgłoską, program ma nas o tym
poinformować. Nie bierzemy pod uwagę polskich znaków. Przykłady tekstów do
przetestowania: "python", "charlie" """

text = input("Proszę podaj tekst: ")
vowels = ["a", "e", "i", "o", "u", "y"]

for letter in text:
    if letter in vowels:
        print(letter, "Litera jest samogłoską!")
    else:
        print(letter)