a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(f"Numbers cube {a} to {b}")
for i in range(a, b+1):
    print((f"{i}^3 = {i**3}"))
