number = input("Enter the number: ")
even_count = 0
odd_count = 0

for digit in number:
    digit = int(digit)
    if digit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Количество чётных цифр: {even_count}")
print(f"Количество нечётных цифр: {odd_count}")
