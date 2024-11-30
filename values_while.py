numbers = []
number = None

while number != 0:
    number = int(input("Type 0 for exit: "))
    if numbers != 0:
        numbers.append(number)

print("Entered numbers in reverse: ", numbers[::-1])
