num1 = float(input("First number: "))
num2 = float(input("Second number: "))
num3 = float(input("Third number: "))
numbers=[num1, num2, num3]
unique_numbers = set(numbers)
same_count = 3-len(unique_numbers)
if same_count == 0:
    print("Все числа разные")
elif same_count == 1:
    print("Два числа одинаковые")
else:
    print("Все числа одинаковые")
