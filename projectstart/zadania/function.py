"""Napisz program, który będzie wyliczał sumę i średnią nieparzystych elementów zawartych
w liście. Przykłady list: [1, 2, 3], [5, 312, 2, -12], [-2, -5, -2, -10], [0, 0, 0], [1, 1, 1]. Program
powinien wykorzystywać funkcję i wypisać wyniki na ekranie."""

test_list_1 = [1, 2, 3]
test_list_2 = [5, 312, 2, -12]
test_list_3 = [-2, -5, -2, -10]
test_list_4 = [0, 0, 0]
test_list_5 = [1, 1, 1]

def sum_and_avg(test_list):
    list_sum = 0
    list_count = 0 

    for elem in test_list_1:
        if elem % 2 == 0:
            list_sum += elem
            list_count += 1

    list_awg = list_sum / list_count

    if list_count != 0:
        list_avg = list_sum / list_count
        print("suma parzystych elementów listy:", list_sum)
        print("średnia parzystych elementów listy:", list_avg)
    else:
        print("nie ma parzystych liczb")

sum_and_avg(test_list_1)