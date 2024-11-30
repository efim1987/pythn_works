price = int(input("Enter the price: 2500, 5000, 500: "))

price_to_items = {
    2500: "Стол",
    5000: "Кровать",
    500: "Табурет"
}

if price in price_to_items:
    name_of_items = price_to_items[price]
    print(f"Назване предмета: {name_of_items}")
else:
    print("Error")
