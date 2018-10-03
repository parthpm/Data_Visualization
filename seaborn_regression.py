#Regression Plots

#lmplot allows you to display linear models, but it also
# conveniently allows you to split up those plots based off
# of features,
# as well as coloring the hue based off of features.

import seaborn as sns
import matplotlib.pyplot as plt

tips=sns.load_dataset('tips')
print(tips.head())

sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',aspect=0.5,size=5)
plt.show()

#using grids
sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',col='day',row='smoker')
plt.show()

#aspect and size parameter
sns.lmplot(x='total_bill',y='tip',data=tips,col='day',hue='sex',palette='coolwarm',
          aspect=0.6,size=8)
plt.show()

