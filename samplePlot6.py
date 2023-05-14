import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate some sample data
requests = np.array([10, 20, 30, 40, 50])
technique1_inconsistencies = np.array([3, 5, 7, 8, 10])
technique2_inconsistencies = np.array([2, 4, 6, 7, 8])
servers = np.array([1, 2, 3])

# Create a meshgrid of x, y, and z values
x, y, z = np.meshgrid(requests, servers, [0, 1])
technique1_data = np.array([technique1_inconsistencies, technique1_inconsistencies])
technique2_data = np.array([technique2_inconsistencies, technique2_inconsistencies])

# Create the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


# Plot the bars for Technique 1
ax.bar3d(x.ravel(), y.ravel(), z.ravel(), 0.5, 0.5, technique1_data.ravel(),
         color='blue', alpha=0.8, label='Technique 1')

'''
# Plot the bars for Technique 2
ax.bar3d(x.ravel()+0.5, y.ravel(), z.ravel(), 0.5, 0.5, technique2_data.ravel(),
         color='green', alpha=0.8, label='Technique 2')


# Set the labels and title
ax.set_xlabel('Amount of Requests')
ax.set_ylabel('Amount of Servers')
ax.set_zlabel('Amount of Inconsistencies')
ax.set_title('Comparison of Techniques')

# Add a legend
ax.legend()

# Show the plot
plt.show()
'''