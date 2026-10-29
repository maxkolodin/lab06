input_str = input("Введите целые числа: ")
numbers = []
for part in input_str.split():
    numbers.append(int(part))
e = []
for number in numbers:
    if number % 2 == 0:
        e.append(number)
count = len(e)
total_sum = sum(e)
sorted_e = sorted(e)
print(f"Выборка: {e}")
print(f"Количество: {count}")
print(f"Сумма: {total_sum}")
print(f"Отсортированная копия: {sorted_e}")
