n = int(input("Введите число для вычисления факториала: "))

factorial = 1
if n < 0:
    print("Факториала не существует для отрицательных чисел.")
elif n == 0:
    print("Факториал 0 равен 1.")
else:
    for i in range(1, n + 1):
        factorial *= i
    print(f"Factorial of number {n} equals {factorial}")
