import numpy as np
x = np.arange(0,100)
y = x*2
z = x**2
import matplotlib.pyplot as plt

figure=plt.figure()
ax=figure.add_axes([0.1,0.1,0.9,0.9])
ax.plot(x,y)
figure.show()

fig=plt.figure()
ax1=figure.add_axes([0,0,1,1])
ax2=figure.add_axes([0.2,0.5,.2,.2])
ax1.plot(x,y)
ax2.plot(x,y)
fig.show()

f,a=plt.subplots(nrows=1,ncols=2,figsize=(18,6))
a[0].plot(x,y,'b--')
a[1].plot(x,z,color='red',lw=10)
f.show()
