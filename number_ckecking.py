n = int(input("Enter the number: "))

if n < 0:
    print("Отрицательное")
if n % 2 == 0:
    print("Кратно 2")
    if n % 6 == 0:
        print("Кратно 6")
else:
    print("Error")
