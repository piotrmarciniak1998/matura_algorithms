from math import sqrt


def is_perfect_number(number):
    result = 1
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            result += i + number / i
    if result == number:
        return True
    else:
        return False


input_number = int(input("Wprowadź liczbę: "))
if is_perfect_number(input_number):
    print("Wprowadzona liczba jest liczbą doskonałą.")
else:
    print("Wprowadzona liczba nie jest liczbą doskonałą.")
