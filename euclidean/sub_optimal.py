def euclidean_iter(a, b):
    while a != b:
        if a > b:
            a -= b
        elif b > a:
            b -= a
    return a


def euclidean_recur(a, b):
    if a > b:
        return euclidean_recur(a - b, b)
    elif b > a:
        return euclidean_recur(a, b - a)
    return a


number_a = int(input("Wprowadź liczbę A: "))
number_b = int(input("Wprowadź liczbę B: "))
result_recur = euclidean_recur(number_a, number_b)
result_iter = euclidean_iter(number_a, number_b)
print(f"NWD liczby {number_a} i {number_b} wynosi {result_recur}. -> recur")
print(f"NWD liczby {number_a} i {number_b} wynosi {result_iter}. -> iter")
