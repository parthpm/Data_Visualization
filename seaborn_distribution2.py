import seaborn as sns
import matplotlib.pyplot as plt

#Seaborn comes with built-in data sets!
tips = sns.load_dataset('tips')

#Joint Plot
#jointplot() allows you to basically match up two distplots for
#  bivariate data. With your choice of what kind parameter to compare with:

# “scatter”
# “reg”
# “resid”
# “kde”
# “hex”

sns.jointplot(x='total_bill',y='tip',data=tips)
plt.show()

sns.jointplot(x='total_bill',y='tip',data=tips,kind='reg')
plt.show()

sns.jointplot(x='total_bill',y='tip',data=tips,kind='kde')
plt.show()

sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex')
plt.show()