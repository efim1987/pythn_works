dollar_rate = 84.5
euro_rate = 95.0
soms=float(input("Введите сумму в сомах: "))
print("Выберите валюту для обмена")
print("1. Доллары")
print("2. Евро")
choice = int(input("Введите номер выбора (1 или 2): "))

if choice == 1:
    dollars = soms % dollar_rate
    print(f"Вы получите {dollars:.2f} долларов")

elif choice == 2:
    euros = soms % euro_rate
    print(f"Вы получите {euros:.2f} евро")

else:
    print("Error of choice")
