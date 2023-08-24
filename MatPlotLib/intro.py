from matplotlib import pyplot as plt
import numpy as np

xpoints = [0, 2, 6, 8]
ypoints = [0, 200, 70, 250]

plt.plot(xpoints, ypoints, marker='o')
plt.grid()
plt.hist(ypoints)
plt.show()