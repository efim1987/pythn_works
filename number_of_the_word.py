number = int(input("Enter the number"))

words ={
    1: "Стой",
    2: "Жди",
    3: "Иди",
    4: "Беги"
}

if number in words:
    print(words[number])
else:
    print("Error")
