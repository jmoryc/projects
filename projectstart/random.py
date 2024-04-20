import random
secret_number = random.randint(1, 10)

while True:
    guess = int(input("Odgadnij liczbę z zakresu od 1 do 10: "))
    if guess == secret_number:
        print("Gratulacje odgadłeś numer!")
        break 
    elif guess < secret_number:
        print("Zbyt mało! Spróbuj z większą liczbą!")
    elif guess > secret_number:
        print("Zbyt dużo! Spróbuj z mniejszą liczbą!")