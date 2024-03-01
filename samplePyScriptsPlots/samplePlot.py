import matplotlib.pyplot as plt

# Sample throughput data
throughput = [10, 20, 30, 40, 50]
time = [1, 2, 3, 4, 5]

# Create plot
plt.plot(time, throughput)
plt.xlabel('Time')
plt.ylabel('Throughput')
plt.title('Throughput over Time')

# Show plot
plt.show()