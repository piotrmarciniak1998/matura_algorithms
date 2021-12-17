def euclidean_iter(a, b):
    while b != 0:
        c = a
        a = b
        b = c % b
    return a


def euclidean_recur(a, b):
    """
    if b != 0:
        c = a
        a = b
        b = c % b
        return euclidean_recur(a, b)
    """
    if b != 0:
        return euclidean_recur(b, a % b)
    else:
        return a


number_a = int(input("Wprowadź liczbę A: "))
number_b = int(input("Wprowadź liczbę B: "))
result_recur = euclidean_recur(number_a, number_b)
result_iter = euclidean_iter(number_a, number_b)
print(f"NWD liczby {number_a} i {number_b} wynosi {result_recur}. -> recur")
print(f"NWD liczby {number_a} i {number_b} wynosi {result_iter}. -> iter")
