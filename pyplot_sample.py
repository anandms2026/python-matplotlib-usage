import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([0,6,6,8,11,10])
ypoints = np.array([0, 250,100,150,200,250])
plt.plot(ypoints, linestyle='dashed', marker='o', color='b')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.bar(x,y)
plt.show()