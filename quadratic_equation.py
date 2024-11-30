import math

a = float(input("Enter the value:"))
b = float(input("Enter the value:"))
c = float(input("Enter the value:"))

if a == 0:
    print("Это не квадратное уравнение")
else:
    D = b**2 - 4*a*c
    print(f"Дискриминант: {D}")

    if D > 0:
        x1 = (-b + math.sqrt(D)) / 2*a
        x2 = (-b + math.sqrt(D)) / 2*a
        print(f"Уравнение имеет 2 корня: x1 = {x1}, x2 = {x2}")
    
    elif D == 0:

        x = -b/2*a
        print(f"Уравнение имеет 1 кореньЖ x1,2 = {x}")

    else:
        print(f"Уравнение не имеет корней")
