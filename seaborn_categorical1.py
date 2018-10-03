import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

tips=sns.load_dataset('tips')
#factorplot
# boxplot
# violinplot
# stripplot
# swarmplot
# barplot
# countplot

#bar plot
#barplot is a general plot that allows you to aggregate
# the categorical
# data based off some function, by default the mean:

sns.barplot(y='total_bill',x='sex',data=tips)
plt.show()
sns.barplot(y='total_bill',x='sex',data=tips,estimator=np.std)
plt.show()

#countplot
# This is essentially the same as barplot except the
# estimator is explicitly counting the number of occurrences.
# Which is why we only pass the x value:


sns.countplot(x='sex',data=tips)
plt.show()