import seaborn as sns
import matplotlib.pyplot as plt

#Seaborn comes with built-in data sets!
tips = sns.load_dataset('tips')

# box plot (or box-and-whisker plot) shows the distribution of
# quantitative data in a way that facilitates comparisons between
#  variables or across levels of a categorical variable. The box
# shows the quartiles of the dataset while the whiskers extend to
# show the rest of the distribution, except for points that are
# determined to be “outliers”
# using a method that is a function of the inter-quartile range.

print(tips.head())
sns.boxplot(x='day',y='tip',data=tips,hue='sex')
plt.show()
sns.boxplot(x='day',y='total_bill',hue='smoker',data=tips,palette='rainbow')
plt.show()

## Can do entire dataframe with orient='h'
sns.boxplot(data=tips,palette='rainbow',orient='h')
plt.show()
