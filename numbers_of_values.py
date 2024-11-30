number = input("Enter the number: ")
digits = [int(digit) for digit in number]
sum_of_digits = sum(digits)
product_of_digits = 1
for digit in digits:
    product_of_digits *= digit

print(f"Cумма цифр: {sum_of_digits}")
print(f"Произведение цифр: {product_of_digits}")
