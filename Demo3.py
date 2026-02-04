import matplotlib.pyplot as plt

cars = ['AUDI','BMW','FORD','TESLA','WAGON']
data = [23,10,35,15,12]

plt.pie(data,labels=cars)
plt.title('Pie Chart')
plt.show()