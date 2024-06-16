# Drawing a graph of function

import matplotlib.pyplot as plt
import numpy as np

# Define the function
def f(x):
    return 2 * x + 3

# Generate x values
x = np.linspace(-10, 10, 400)
y = f(x)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='y = 2x + 3', color='blue')
plt.scatter(0, 3, color='red') # y-intercept
plt.scatter(1, 5, color='green') # Another point on the line
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.title('Graph of y = 2x + 3')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
