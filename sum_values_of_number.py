number = int(input("Enter the number: "))
sum_digits = 0
number = abs(number)
while number > 0:
    sum_digits += number % 10
    number //= 10
print(sum_digits)
