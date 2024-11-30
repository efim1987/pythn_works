n = int(input("Enter the number: "))
start_fibonachi = [0, 1]
for i in range(2, n):
    start_fibonachi.append(start_fibonachi[i-1]+start_fibonachi[i-2])
    print("Числа Фибоначчи:", start_fibonachi[:n])

