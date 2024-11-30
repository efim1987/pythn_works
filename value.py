def value(a):
    if a%2 == 0 and a%3 == 0 and a%5 == 0:
        return a**2
    else:
        return a
input_a=int(input())
result=value(input_a)
print(result)
