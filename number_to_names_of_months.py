num_of_month = int(input("Enter the number"))
if num_of_month==12 or num_of_month==1 or num_of_month==2:
    season="Winter"
if num_of_month==3 or num_of_month==4 or num_of_month==5:
    season="Spring"
if num_of_month==6 or num_of_month==7 or num_of_month==8:
    season="Summer"
if num_of_month==9 or num_of_month==10 or num_of_month==11:
    season="Autumn"
else:
    print("No season")
print(f"Season: {season}")
