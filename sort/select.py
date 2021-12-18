from random import sample


def swap(idx_a, idx_b, input_list):
    c = input_list[idx_a]
    input_list[idx_a] = input_list[idx_b]
    input_list[idx_b] = c


def select_sort(input_list):
    # number_of_swaps = 0
    # number_of_iterations = 0
    for i in range(len(input_list) - 1):
        idx = i
        for j in range(i + 1, len(input_list)):
            # number_of_iterations += 1
            if input_list[j] < input_list[idx]:
                idx = j
        # number_of_swaps += 1
        swap(i, idx, input_list)
    # print(number_of_iterations, number_of_swaps)
    return input_list


random_list = sample(range(100), 20)

# random_list is sorted, so to display difference between input and output, we use .copy()
result = select_sort(random_list.copy())

print(f"Zbiór {random_list} uporządkowany przy pomocy sortowania przez wybór ma postać {result}.")
