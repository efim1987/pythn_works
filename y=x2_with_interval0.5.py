import numpy as np
import mathlotlib.pyplot as plt

x = np.arange(0, 5.5, 0.5)
y = x**2

for xi, yi in zip(x, y):
    print(f"x: {xi: .lf}, y: {yi: .if}")

plt.plot(x, y, marker='0')
plt.title("Graphic")
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.xlim(0, 5)
plt.y.lim(0, 26)
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')

plt.show()
