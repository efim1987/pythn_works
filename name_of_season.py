number = int(input("Enter the number"))

seasons = {
    1: "Summer",
    2: "Spring",
    3: "Autumn",
    4: "Winter"
}

if number in seasons:
    print(seasons[number])
else:
    print("Error")
