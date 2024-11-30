number = int(input("Enter the number"))
             
alphabet = "abcdefgh"

if 1<= number <= 8:
    print(f"Буква под номером {number}: {alphabet[number -1]}")
else:
    print("Error")
