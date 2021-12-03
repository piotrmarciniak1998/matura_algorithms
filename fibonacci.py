def fibonacci_iter(n):
    f_n = 0
    f_n_1 = 1
    for i in range(n):
        temp = f_n
        f_n += f_n_1
        f_n_1 = temp
    return f_n


def fibonacci_recur(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recur(n - 1) + fibonacci_recur(n - 2)


number = int(input("Wprowadź wyraz ciągu Fibonacciego: "))
result_recur = fibonacci_recur(number)
result_iter = fibonacci_iter(number)
print(f"{number} wyraz ciągu Fibonacciego wynosi {result_recur}. -> recur")
print(f"{number} wyraz ciągu Fibonacciego wynosi {result_iter}. -> iter")
