#The plt.subplots() object will act as a more automatic axis manager.

import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,5,11)
y=x**2

## Use similar to plt.figure() except use tuple unpacking to grab fig and axes
fig,axes=plt.subplots(nrows=1,ncols=2)
print(axes)
fig.show()
# fig is canvas as stated earlier
#axes is numpy array of axes in subplots
## Now use the axes object to add stuff to plot
axes[0].plot(x,y,'r')
axes[1].plot(y,x,'b')

fig.show()





