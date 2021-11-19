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
print("NWD liczby A i B wynosi:", euclidean_recur(number_a, number_b))
