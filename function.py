start = -5
end = 5
step = 0.5
print("Result y=x^2: ")
x = start
while x<=end:
    y = x**2
    print(f"x = {x:.1f}, y = {y:.2f}")
    x += step
