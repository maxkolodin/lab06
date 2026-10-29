numbers = [int(x) for x in input().split()]
if not numbers:
    print("Нет данных")
else:
    count = len(numbers)
    total = sum(numbers)
    minimum = numbers[0]
    maximum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
        if number > maximum:
            maximum = number
    average = total / count
    print(f"Количество: {count}, Сумма: {total}, Минимум: {minimum}, Максимум: {maximum}, Среднее: {average:.2f}")
