start = -3
end = 8
step = 1.5
print("Result y=x^3")
x = start
while x <= end:
    y = x**3
    print(f"x = {x:.1f}, y = {y:.2f}")
    x += step
