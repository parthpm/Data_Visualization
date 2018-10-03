import seaborn as sns
import matplotlib.pyplot as plt

#Seaborn comes with built-in data sets!
tips = sns.load_dataset('tips')
#pairplot
#pairplot will plot pairwise relationships across an entire
# dataframe (for the numerical columns)
#and supports a color hue argument (for categorical columns).

sns.pairplot(tips)
sns.pairplot(data=tips,hue='sex',palette='coolwarm')
plt.show()