"""Zadania: dodawanie nowego zadania, czyszczenie listy zadań, wyświetlanie zadań."""

to_do_list = []

while True:
    print("Dostępne opcje:")
    print("1. Wyświetl listę")
    print("2. Dodaj nowe zadanie")
    print("3. Wyczyść listę")
    print("4. Wyjdź z programu")

    option = int(input("Proszę wybierz opcję (od 1 do 4): "))

    if option == 1:
        if to_do_list == []:
            print("Lista zadań jest pusta.")
        else:
            print("Lista zadań: ")
            print(to_do_list)
    elif option == 2:
        task = input("Wpisz zadanie do dodania: ")
        to_do_list.append(task)
        print("Zadanie zostało dodane do listy.")
    elif option == 3:
        print("Lista została wyczyszczona. ")
    elif option == 4:
        print("Koniec programu. Dziękujemy za współpracę.")
        break
    
    else:
        print("Nie istnieje taka opcja.")