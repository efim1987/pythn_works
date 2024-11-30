n = int(input("Enter the number: "))
months = {
    1: "January", 
    2: "February", 
    3: "March", 
    4: "April", 
    5: "May",
    6: "june",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}
if n >= 1 and n <= 12:
    print(months[n])
else:
    print("Error")
