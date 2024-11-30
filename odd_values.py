start = int(input("Enter the number: "))
end = int(input("Enter  the number: "))
for i in range(start, end+1):
    if i % 2 != 0:
        print(i, end = ' ')
