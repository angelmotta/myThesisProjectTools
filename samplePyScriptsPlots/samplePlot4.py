import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = np.linspace(0, 10**6, 10000)
y1 = np.sin(x)
y2 = np.cos(x)

# Create the plot with a logarithmic y-axis
fig, ax = plt.subplots()
ax.plot(x, y1, label='Line 1')
ax.plot(x, y2, label='Line 2')
ax.set_yscale('log')

# Set the axis labels and legend
ax.set_xlabel('X-axis values')
ax.set_ylabel('Y-axis values')
ax.legend()

# Show the plot
plt.show()
