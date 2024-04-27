students_in_group = {"Jan Bednarek", "SaraKostek", "EmiliaFrejzer", "RyszardMasternak", "Krzysztof Pluta"}

homework_done = set()

program_active = True

while program_active:
    print("""
    Co chcesz zrobić?
    1 - Wprowadzić identyfikator studenta, który wykonał zadanie
    2 - Wyświetlić listę wszystkich studentów w grupie
    3 - Wyświetlić listę studentów, którzy jeszcze nie oddali zadania
    4 - Wyświetlić listę studentów, którzy już oddali zadanie
    5 - Wyjść z programu
""")
    
    option = int(input("Proszę wybierz opcję (od 1 do 5): "))

    if option == 1:
        id = input("Proszę wprowadź identyfikator: ")
        if id in students_in_group:
            if id not in homework_done:
                homework_done.add(id)
            else: 
                print("Ten student oddał już swoje zadanie!")
        else:
            print("Taki student nie istnieje w tej grupie!")
        
    elif option == 2:
        print(students_in_group)
    elif option == 3:
        print(students_in_group.difference(homework_done))
    elif option == 4:
        if len(homework_done) == 0:
            print("Nikt jeszcze nie oddał zadania.")
        else:
            print(homework_done)
    elif option == 5:
        print("Koniec programu")
        program_active = False
    else:
        print("Opcja poza zakresem dozwolonym!")

    