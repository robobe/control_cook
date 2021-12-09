import matplotlib.pyplot as plt
import numpy as np

xstart = 0
xstop = 2*np.pi
increment = 0.1

x = np.arange(xstart,xstop,increment)
y = np.sin(x)
z = np.cos(x)

plt.subplot(2,1,1)
plt.plot(x , y)
plt.title("sin")
plt.axis([0, 10, -1, 1])
plt.grid()
plt.xlabel("x")
plt.ylabel("y")


plt.subplot(2,1,2)
plt.plot(x , z)
plt.plot(x, y)
plt.title("cos")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["cos", "sin"])
plt.show()