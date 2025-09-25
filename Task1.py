num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

max_num = max(num1, num2, num3)
min_num = min(num1, num2, num3)

print(f"Наибольшее число: {max_num}")
print(f"Наименьшее число: {min_num}")

if num1 == num2 == num3:
    print("Все числа равны")
else:
    print("Не все числа равны")