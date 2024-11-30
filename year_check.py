year = int(input("Enter the year"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} является високосным")
else:
    print(f"{year} не является високосным")
