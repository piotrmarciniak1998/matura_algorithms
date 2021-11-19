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
print("NWD liczby A i B wynosi:", euclidean_recur(number_a, number_b))