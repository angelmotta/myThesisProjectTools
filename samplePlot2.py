import matplotlib.pyplot as plt
import numpy as np

# Generate some sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)
print("y values:")
print(y)

# Plot the data
fig, ax = plt.subplots()
ax.plot(x, y)

# Reduce the number of values on the y-axis
yticks = np.linspace(np.floor(np.min(y)), np.ceil(np.max(y)), 5)
ax.set_yticks(yticks)

# Show the plot
plt.show()
