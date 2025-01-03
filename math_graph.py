import matplotlib.pyplot as plt

x=[1,2,3,4]
y=[9,7,8,2]
z=[2,3,4,5]


plt.plot(x,y,z, label="plane")
plt.title("Simple plane")
plt.legend()
plt.show()