from random import sample


def find_min_max(values):
    min_values = []
    max_values = []

    for i in range(len(values) // 2):
        a = values[i * 2]
        b = values[i * 2 + 1]
        if a > b:
            min_values.append(b)
            max_values.append(a)
        else:
            min_values.append(a)
            max_values.append(b)

    if len(values) % 2 == 1:
        min_values.append(values[-1])
        max_values.append(values[-1])

    min_value = float("inf")
    for value in min_values:
        if value < min_value:
            min_value = value

    max_value = float("-inf")
    for value in max_values:
        if value > max_value:
            max_value = value

    return min_value, max_value


input_list = sample(range(100), 11)
result_min, result_max = find_min_max(input_list)
print(f"W zbiorze {input_list} minimalna wartość to {result_min}, a maksymalna to {result_max}.")
