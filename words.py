number=int(input("Enter the number"))

numbers = {
    1: "Один",
    2: "Два",
    3: "Три",
    4: "Четыре",
    5: "Пять"
}

if 1 <= number <= 5:
    print(f"Number: {numbers[number]}")
else:
    print("Underfined, try again")
