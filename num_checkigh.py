n = int(input("Enter the number: "))
if n < 0:
    print("Negative")
elif n % 2 == 0:
    print("Even")
    if n % 5 == 0:
        print("Divided by 5")
else:
    print("Odd")
    if n % 3 == 0:
        print("Divided by 3")
