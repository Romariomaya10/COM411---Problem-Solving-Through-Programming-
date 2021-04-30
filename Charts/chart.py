import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7]
y = [10,15.5,18.2,20,25,36,40]

plt.xlabel("Age")
plt.ylabel("Score")

plt.bar(x,y, color = ["m", "g", "r", "b"])
plt.plot(x,y)

plt.show()