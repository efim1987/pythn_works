N = int(input("Сколько чисел Фибоначчи вывести"))
a, b = 0, 1
print(a, b, end='')
for _ in range(N-2):
    a, b = b, a + b
    print(b, end='')
