age = int(input("Enter age of child: "))

age_to_name = {
    5: "Оля",
    6: "Миша",
    7: "Серёжа",
    8: "Костя"
}

if age in age_to_name:
    print(f"Имя ребёнка: {age_to_name[age]}")
else:
    print("Error")
