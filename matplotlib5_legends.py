import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,5,11)
y=x**2

fig=plt.figure()
axis=fig.add_axes([0.1,0.1,0.8,0.8])
axis.plot(x,x**2,label='X squared')
axis.plot(x,x**3,label='X cubed')
fig.legend(loc=2) #for loaction of legend
#ax.legend(loc=0) # let matplotlib decide the optimal location
fig.show()
