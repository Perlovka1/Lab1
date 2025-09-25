n = int(input("Введите число n: "))

print("Числа от 1 до n:")
for i in range(1, n + 1):
    print(i, end=" ")

print("\nКвадраты чисел от 1 до n:")
for i in range(1, n + 1):
    print(i ** 2, end=" ")

sum_numbers = 0
for i in range(1, n + 1):
    sum_numbers += i

print(f"\nСумма всех чисел от 1 до n: {sum_numbers}")