import numpy as np
import matplotlib.pyplot as plt

# Generate some sample data
requests = np.array([10, 20, 30, 40, 50])
technique1_inconsistencies = np.array([3, 5, 7, 8, 10])
technique2_inconsistencies = np.array([2, 4, 6, 7, 8])

# Set the width of each bar
width = 0.35

# Create the figure and axes objects
fig, ax = plt.subplots()

# Create the bars for Technique 1
ax.bar(requests - width/2, technique1_inconsistencies, width, color='blue', alpha=0.8, label='Technique 1')

# Create the bars for Technique 2
ax.bar(requests + width/2, technique2_inconsistencies, width, color='green', alpha=0.8, label='Technique 2')

# Add text labels on top of each bar
for x1, y1, y2 in zip(requests, technique1_inconsistencies, technique2_inconsistencies):
    ax.text(x1 - width/2, y1 + 0.1, str(y1), ha='center', fontsize=8)
    ax.text(x1 + width/2, y2 + 0.1, str(y2), ha='center', fontsize=8)

# Set the labels and title
ax.set_xlabel('Amount of Requests')
ax.set_ylabel('Amount of Inconsistencies')
ax.set_title('Comparison of Techniques')

# Add a legend
ax.legend()

# Show the plot
plt.show()
