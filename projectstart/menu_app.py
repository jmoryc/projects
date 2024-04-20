while True:

    print("Opcje dostępne w aplikacji: ")
    print("1 - Start aplikacji")
    print("2 - Ustawienia")
    print("3 - Wyjdź z aplikacji")

    choice = int(input("Proszę wybierz opcję od 1 do 3: "))

    if choice == 1:
        print("Start aplikacji")
    elif choice == 2:
        print("Ustawienia aplikacji")
    elif choice ==3:
        print("Koniec aplikacji")
        break
    
    else:
        print("Wybrałeś opcję która nie stnieje")