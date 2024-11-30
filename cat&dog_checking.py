animals = ["cat", "dog"]
print("Take choice: cat or dog")
choice = input()
if choice == "cat":
    print("There are 3 kinds of cat: 1, 2, 3")
    kind_cat = input()
    if kind_cat == "1":
        print("White")
    elif kind_cat == "2":
        print("Gray")
    elif kind_cat == "3":
        print("Black")
    else:
        print("Error of choice of cat kinds")
elif choice == "dog":
    print("There are 3 kinds of dog: 1, 2, 3")
    kind_dog = input()
    if kind_dog == "1":
        print("White")
    elif kind_dog == "2":
        print("Gray")
    elif kind_dog == "3":
        print("Black")
    else:
        print("Error of choice of dog kinds")
else:
    print("Error of choice")
