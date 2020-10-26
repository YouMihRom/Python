#number = int(input("Введите целое положительное число"))

number = 9123845

max = 0
while number // 10 >= 0:
    var = number % 10
    if var > max:
        max = var
    if number // 10 == 0:
        break
    number = number // 10

print(f"{max:d}")

