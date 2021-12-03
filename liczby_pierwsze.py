from math import sqrt


def is_prime_number(number):
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


input_number = int(input("Wprowadź liczbę: "))
if is_prime_number(input_number):
    print(f"{input_number} jest liczbą pierwszą.")
else:
    print(f"{input_number} nie jest liczbą pierwszą.")