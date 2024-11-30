start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))
divisor = int(input("Введите число, которому должны быть кратны числа: "))
print(f"Числа в диапазоне от {start} до {end}, кратные {divisor}:")
for i in range(start, end + 1):
    if i % divisor == 0:
        print(i, end= ' ')
