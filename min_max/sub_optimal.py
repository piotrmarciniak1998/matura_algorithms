from random import sample


def find_min(values):
    min_value = float("inf")
    for value in values:
        if value < min_value:
            min_value = value
    return min_value


def find_max(values):
    max_value = float("-inf")
    for value in values:
        if value > max_value:
            max_value = value
    return max_value


input_list = sample(range(100), 10)
result_min = find_min(input_list)
result_max = find_max(input_list)
print(f"W zbiorze {input_list} minimalna wartość to {result_min}, a maksymalna to {result_max}.")
