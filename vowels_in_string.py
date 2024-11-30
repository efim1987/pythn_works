text = input("Enter the string: ")
vowels = 'aoeuIAEOU'
count = sum(1 for char in text if char in vowels)
print('Quantity: ', count)
