import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

tips=sns.load_dataset('tips')

# #violinplot
# A violin plot plays a similar role as a box and whisker plot. It shows the
# distribution of quantitative data across several levels of one (or more)
# categorical variables such that those distributions can be compared. Unlike
# a box plot, in which all of the plot components correspond to actual
# datapoints, the violin plot
# features a kernel density estimation of the underlying distribution.

sns.violinplot(y='total_bill',x='day',data=tips)
plt.show()


sns.violinplot(y='tip',x='day',data=tips,hue='sex')
plt.show()

sns.violinplot(y='tip',x='day',data=tips,hue='sex',split=True)
plt.show()