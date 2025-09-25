import random

numbers = [random.randint(1, 100) for _ in range(10)]

print("Список чисел:", numbers)

max_value = max(numbers)
min_value = min(numbers)
sum_numbers = sum(numbers)

print("Максимальное значение:", max_value)
print("Минимальное значение:", min_value)
print("Сумма всех элементов:", sum_numbers)

sorted_numbers = sorted(numbers)
print("Отсортированный список по возрастанию:", sorted_numbers)