def change_making(sum_of_money, money_list):
    change = dict()
    for value in money_list:
        if sum_of_money < money_list[-1]:
            return change
        elif sum_of_money >= value:
            how_many = int(sum_of_money // value)
            change[value] = how_many
            sum_of_money -= value * how_many
            sum_of_money = round(sum_of_money, 2)
    return change


input_number = float(input("Wprowadź kwotę: "))
result = change_making(input_number, [200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01])
print(f"Reszta z {input_number} to: {result}.")
