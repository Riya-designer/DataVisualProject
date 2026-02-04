import matplotlib.pyplot as plt

x = ["Thurs","Fri","Sat","Sun"]
y = [170,120,250,190]

plt.bar(x,y)
plt.title("Bar Chart")
plt.xlabel('Day')
plt.ylabel('Total Bill')
plt.show()