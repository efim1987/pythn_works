base = float(input("Введите число, которое нужно возвести в степень: "))
limit = int(input("Введите ограничение для степени: "))

for degree in range(1, limit + 1):
    result = base**degree
    print(f"{base} ^ {degree} = {result}")
