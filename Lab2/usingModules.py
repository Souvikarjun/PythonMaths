from matplotlib import pyplot as plt
import numpy as np


x = np.linspace(-10,10,400)
y1 = (6-3*x) / 2
y2 = x-4

plt.plot(x,y1,lable="3x+2y=6")
plt.plot(x,y2,lable="x-y=4")
plt.axhline(0,color="black",linewidth=0.5)
plt.axvline(0,color="black",linewidth=0.5)
plt.grid(color="gray", linestyle="--",linewidth=0.5)

plt.legend()
plt.show()