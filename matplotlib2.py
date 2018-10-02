#object oriented method
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,5,11)
y=x**2

# This means we will instantiate figure objects and then call
# methods or attributes from that object.

## Create Figure (empty canvas)
fig=plt.figure()

# Add set of axes to figure
axes=fig.add_axes([0.1,0.1,0.8,0.8]) # # left, bottom, width, height (range 0 to 1)

# Plot on that set of axes
axes.plot(x,y)
axes.set_xlabel('X label')
axes.set_ylabel('Y Label')
axes.set_title('Title')
fig.show()


