str_to_int = {"0": 0,
              "1": 1,
              "2": 2,
              "3": 3,
              "4": 4,
              "5": 5,
              "6": 6,
              "7": 7,
              "8": 8,
              "9": 9,
              "A": 10,
              "B": 11,
              "C": 12,
              "D": 13,
              "E": 14,
              "F": 15}

int_to_str = {0: "0",
              1: "1",
              2: "2",
              3: "3",
              4: "4",
              5: "5",
              6: "6",
              7: "7",
              8: "8",
              9: "9",
              10: "A",
              11: "B",
              12: "C",
              13: "D",
              14: "E",
              15: "F"}

input_base = int(input("Wprowadź system wejściowy: "))
output_base = int(input("Wprowadź system docelowy: "))
input_text = input("Wprowadź liczbę: ")

input_list = []
for letter in input_text:
    input_list.append(str_to_int[letter])

input_number = 0
curr_base = 1
for number in reversed(input_list):
    input_number += number * curr_base
    curr_base *= input_base

output_list = []
while input_number > 0:
    output_list.append(input_number % output_base)
    input_number //= output_base

output_text = ""
for number in reversed(output_list):
    output_text += int_to_str[number]

print(f"{input_text} w systemie {input_base} to inaczej {output_text} w systemie {output_base}.")
