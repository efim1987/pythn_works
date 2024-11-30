numbers = list(range(1, 15))
filtered_numbers = []

for num in numbers:
    if num % 3 == 0:
        continue
    filtered_numbers.append(num)

for num in filtered_numbers:
    if num >= 7:
        break
    print(num)

print(filtered_numbers)
