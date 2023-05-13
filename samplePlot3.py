import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = np.random.normal(size=10000)
y = np.random.normal(size=10000)

# Create a histogram
fig, ax = plt.subplots()
ax.hist(y, bins=50)
ax.set_xlabel('Y-axis values')
ax.set_ylabel('Frequency')

# Create a heatmap
fig, ax = plt.subplots()
heatmap, xedges, yedges = np.histogram2d(x, y, bins=50)
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
ax.imshow(heatmap.T, extent=extent, origin='lower', cmap='plasma')
ax.set_xlabel('X-axis values')
ax.set_ylabel('Y-axis values')

# Create subplots
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(8, 8))
axs[0, 0].scatter(x, y, s=1)
axs[0, 0].set_xlabel('X-axis values')
axs[0, 0].set_ylabel('Y-axis values')

axs[0, 1].hist(x, bins=50, orientation='horizontal')
axs[0, 1].set_xlabel('Frequency')
axs[0, 1].set_ylabel('X-axis values')

axs[1, 0].hist(y, bins=50)
axs[1, 0].set_xlabel('Y-axis values')
axs[1, 0].set_ylabel('Frequency')

axs[1, 1].hist2d(x, y, bins=50, cmap='plasma')
axs[1, 1].set_xlabel('X-axis values')
axs[1, 1].set_ylabel('Y-axis values')

# Adjust spacing between subplots
plt.tight_layout()

# Show the plots
plt.show()
