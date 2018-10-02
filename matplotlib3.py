# 2 plots in same figure
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,5,11)
y=x**2

# Create Figure (empty canvas)
fig1=plt.figure()

axes1=fig1.add_axes([0.1,0.1,0.8,0.8])
axes2=fig1.add_axes([0.2,0.5,0.4,0.3])

# the larger axis figure
axes1.plot(x,y,'r')
axes1.set_xlabel('X label Big')
axes1.set_ylabel('Y label big')
axes1.set_title('Big title')

#smaller sxis figure

axes2.plot(y,x,'b')
axes2.set_xlabel('X label Small')
axes2.set_ylabel('Y label Small')
axes2.set_title('Small title')

plt.show()
