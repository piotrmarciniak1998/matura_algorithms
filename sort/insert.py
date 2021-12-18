from random import sample


def insert_sort(input_list):
    # number_of_swaps = 0
    # number_of_iterations = 0
    for i in range(1, len(input_list)):
        val = input_list[i]
        j = i - 1
        while j >= 0 and val < input_list[j]:
            # number_of_iterations += 1
            input_list[j + 1] = input_list[j]
            j -= 1
        # number_of_swaps += 1
        input_list[j + 1] = val
    # print(number_of_iterations, number_of_swaps)
    return input_list


random_list = sample(range(100), 20)

# random_list is sorted, so to display difference between input and output, we use .copy()
result = insert_sort(random_list.copy())

print(f"Zbiór {random_list} uporządkowany przy pomocy sortowania przez wstawianie ma postać {result}.")
