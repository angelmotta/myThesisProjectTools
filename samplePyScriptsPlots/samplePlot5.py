import matplotlib.pyplot as plt
import numpy as np

# Generate some sample data
requests = np.array([10, 20, 30, 40, 50])
technique1_inconsistencies = np.array([3, 5, 7, 8, 10])
technique2_inconsistencies = np.array([2, 4, 6, 7, 8])

# Set the width of each bar
bar_width = 0.35

# Set the x positions of the bars
r1 = np.arange(len(requests))
print(r1)
r2 = [x + bar_width for x in r1]

# Create the plot
plt.bar(r1, technique1_inconsistencies, color='blue', width=bar_width, edgecolor='white', label='Technique 1')
plt.bar(r2, technique2_inconsistencies, color='green', width=bar_width, edgecolor='white', label='Technique 2')

# Add text labels on top of each bar
for i, v1, v2 in zip(r1, technique1_inconsistencies, technique2_inconsistencies):
    plt.text(i, v1+0.1, str(v1), ha='center')
    plt.text(i+bar_width, v2+0.1, str(v2), ha='center')

# Add xticks on the middle of the group bars
plt.xlabel('Amount of Requests')
plt.ylabel('Amount of Inconsistencies')
plt.xticks([r + bar_width / 2 for r in range(len(requests))], requests)

# Add a legend
plt.legend()

# Show the plot
plt.show()
