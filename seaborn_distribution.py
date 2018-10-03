import seaborn as sns
import matplotlib.pyplot as plt

# distplot
# jointplot
# pairplot
# rugplot
# kdeplot

#Seaborn comes with built-in data sets!
tips = sns.load_dataset('tips')

print(tips.head())
#distplot
#The distplot shows the distribution of a univariate set of observations.
sns.distplot(tips['total_bill'])
plt.show()

sns.distplot(tips['total_bill'],bins=1,kde=False,)
plt.show()