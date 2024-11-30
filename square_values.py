def print_squares(a, b):
    start = min(a, b)
    end = max(a, b)
    for num in range(a, b):
        print(f"{num}^2 = {num**2}")

a = int(input("Enter first number"))
b = int(input("Enter second number"))

print_squares(a, b)
