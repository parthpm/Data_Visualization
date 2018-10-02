import numpy as np
x = np.arange(0,100)
y = x*2
z = x**2
import matplotlib.pyplot as plt

fig,axes=plt.subplots(1,3,figsize=(12,4))
axes[0].plot(x,x**2,x**3)
axes[0].set_title("Default axes range")

axes[1].plot(x,x**2,x**3)
axes[1].set_ylim([0,60])
axes[1].set_title('X limit set')
axes[2].plot(x,x**2,x**3)
axes[2].set_ylim([0,60])
axes[2].set_xlim([2,5])

fig.show()
