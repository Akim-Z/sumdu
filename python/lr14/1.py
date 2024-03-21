import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


x = np.linspace(-5, 5, 1000)
y = (1 / x) * np.sin(5 * x)

plt.plot(x, y, linestyle='-', color='blue', linewidth=2, label='Y(x) = (1/x) * sin(5*x)')
plt.xlabel('x')
plt.ylabel('Y(x)')
plt.title('Графік функції Y(x) = (1/x) * sin(5*x)')
plt.legend()
plt.grid(True)
plt.show()
