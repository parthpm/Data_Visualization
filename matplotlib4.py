#Figure size, aspect ratio and DPI
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,5,11)
y=x**2
# #Matplotlib allows the aspect ratio, DPI and figure size to be specified
#  when the Figure object is created.
# You can use the figsize and dpi keyword arguments.
#
# figsize is a tuple of the width and height of the figure in inches
# dpi is the dots-per-inch (pixel per inch).

fig=plt.figure(figsize=(10,4),dpi=100)
ax=fig.add_axes([0.1,0.1,0.8,0.8])
ax.set_xlabel('x')
ax.plot(x,y)

fig.show()

fig1, axes1 = plt.subplots(figsize=(12,6),nrows=2,ncols=1)
for axes in axes1:
    axes.plot(x, y, 'r')
    axes.set_xlabel('x')
    axes.set_ylabel('y')
    axes.set_title('title')
fig1.show()