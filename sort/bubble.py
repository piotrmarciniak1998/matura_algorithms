from random import sample


def swap(idx_a, idx_b, input_list):
    c = input_list[idx_a]
    input_list[idx_a] = input_list[idx_b]
    input_list[idx_b] = c


def bubble_sort(input_list):
    # number_of_swaps = 0
    # number_of_iterations = 0
    for i in range(len(input_list)):
        for j in range(len(input_list) - (i + 1)):
            # number_of_iterations += 1
            if input_list[j] > input_list[j + 1]:
                # number_of_swaps += 1
                swap(j, j + 1, input_list)
    # print(number_of_iterations, number_of_swaps)
    return input_list


random_list = sample(range(100), 20)

# random_list is sorted, so to display difference between input and output, we use .copy()
result = bubble_sort(random_list.copy())

print(f"Zbiór {random_list} uporządkowany przy pomocy sortowania bąbelkowego ma postać {result}.")
