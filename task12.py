first_number, second_number = int(input("Сумма чисел: ")), int(input("Произведение чисел: "))
for i in range(1, first_number+1):
    for j in range(1, first_number+1):
        if i + j == first_number and i * j == second_number:
            print(f"Задуманные Петей Числа {first_number} {second_number} -> {i} {j}")