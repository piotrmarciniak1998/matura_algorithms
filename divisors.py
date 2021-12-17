def divisors(number):
    divisor = 2
    output_list = []
    while number > 1:
        while number % divisor == 0:
            output_list.append(divisor)
            number /= divisor
        divisor += 1
    return output_list


input_number = int(input("Wprowadź liczbę: "))
result = divisors(input_number)
print(f"Dzielniki {input_number} to: {result}.")
