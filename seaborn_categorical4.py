import seaborn as sns
import matplotlib.pyplot as plt

#Seaborn comes with built-in data sets!
tips = sns.load_dataset('tips')

#stripplot
#The stripplot will draw a scatterplot where one variable is categorical.
#  A strip plot can be drawn on its own, but it is also a good complement
#  to a box or violin plot in cases where you want to show all observations
# along with some representation of the underlying distribution.

#SwarmPlot
#The swarmplot is similar to stripplot(), but the points are adjusted
# (only along the categorical axis) so that they don’t overlap. This
#  gives a better representation of the distribution of values, although
#  it does not scale as well to large numbers of observations (both in
#  terms of the ability to show all
#  the points and in terms of the computation needed to arrange them).

sns.stripplot(x='day',y='total_bill',data=tips,hue='sex',split=True)
plt.show()

#for not allowing the overlapping of points
sns.stripplot(x='day',y='total_bill',data=tips,jitter=True)
plt.show()

sns.swarmplot(x='day',y='total_bill',data=tips)
plt.show()

sns.swarmplot(x='day',y='total_bill',data=tips,hue='sex',palette='rainbow')
plt.show()

