import matplotlib.pyplot as plt
x = [7, 8, 9, 10, 10, 12, 12, 12, 13, 14, 14, 15, 16, 16, 17, 18, 18, 19, 20, 20,
     21, 22, 23, 24, 25, 25, 26, 28, 30, 32, 35, 36, 38, 40, 42, 44, 48, 50]
plt.hist(x,bins=10,color='red')
plt.title("Histogram")
plt.xlabel('Total Bill')
plt.ylabel('Frequency')
plt.show()