"""4. Napisz program, który będzie na wejściu otrzymywał hasło od użytkownika. Program
powinien prosić użytkownika o hasło, dopóki nie wpisze on poprawnego. Jeżeli
użytkownik wpisze tekst quit, program powinien zakończyć działanie. Poprawne hasło to:
KursPythona123!"""

while True:
    password = input("Proszę podaj hasło: ")
    if password == "KursPythona123!":
        print("Dostęp przyznany!")
        break
    elif password == "quit":
        print("Kończę działanie programu!")
        break
    else:
        print("Podałeś niepoprawne hasło. Spróbuj ponownie!")