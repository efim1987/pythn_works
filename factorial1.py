def factorial (number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)

a = int(input("Enter the number: "))
print(f"factorial of {a} is {factorial(a)}")
