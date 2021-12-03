from math import sqrt


def decompose(number):
    denom = 2
    sqrt_number = sqrt(number)
    output_list = []
    while number > 1 and denom <= sqrt_number:
        while number % denom == 0:
            output_list.append(denom)
            number /= denom
        denom += 1
    return output_list


input_number = int(input("Wprowadź liczbę: "))
result = decompose(input_number)
print(f"Dzielniki {input_number} to: {result}.")
