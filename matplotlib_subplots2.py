import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,5,11)
y=x**2

## Use similar to plt.figure() except use tuple unpacking to grab fig and axes
fig,axes=plt.subplots(nrows=1,ncols=2)

##since axes is iterable we can iterate

for ax in axes:
    ax.plot(x,y,'b')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
plt.tight_layout()
fig.show()
