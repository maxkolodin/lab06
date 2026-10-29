numbers = []
for part in input("Целые числа через пробел: ").split():
    numbers.append(int(part))
transformed = numbers.copy()
for i in range(len(transformed)):
    if transformed[i] < 0:
        transformed[i] = -transformed[i]
print(f"Исходный список: {numbers}")
print(f"Новый список: {transformed}")
