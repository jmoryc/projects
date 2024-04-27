"""1. Napisz program, który będzie wyliczał średnią wszystkich elementów zawartych w
liście. Przykłady list do przetestowania: [1, 2, 3], [5, 312, 2, -12], [-2, -5, -2, -10], [0, 0,
0], [1, 1, 1]

2. Napisz program, który będzie wyliczał sumę i średnią nieparzystych elementów
zawartych w liście. Przykłady list do przetestowania: [1, 2, 3], [5, 312, 2, -12], [-2, -5,
-2, -10], [0, 0, 0], [1, 1, 1]

3. Napisz program, który będzie wypisywał na ekranie kolejne litery tekstu wpisanego
przez użytkownika. Jeżeli litera będzie spółgłoską, program ma nas o tym
poinformować. Nie bierzemy pod uwagę polskich znaków. Przykłady tekstów do
przetestowania: "python", "charlie"""

test_list_1 = [1, 2, 3]
test_list_2 = [5, 312, 2, -12]
test_list_3 = [-2, -5, -2, -10]
test_list_4 = [0, 0, 0]
test_list_5 = [1, 1, 1]

list_sum = 0

for elem in test_list_5:
    list_sum += elem

print("Suma elementów listy: ", list_sum)
