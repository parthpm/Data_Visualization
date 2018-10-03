import seaborn as sns
import matplotlib.pyplot as plt

#Seaborn comes with built-in data sets!
tips = sns.load_dataset('tips')

#Combinig Data plots

sns.violinplot(x='tip',y='day',data=tips)
sns.swarmplot(x='tip',y='day',color='black',data=tips)
plt.show()

#factorplot
# factorplot is the most general form of a categorical plot.
# It can take in a kind parameter to adjust the plot type:

sns.factorplot(x='day',y='tip',data=tips,kind='bar')
plt.show()