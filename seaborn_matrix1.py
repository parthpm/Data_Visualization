#Matrix Plots
#Matrix plots allow you to plot data as color-encoded matrices and can
# also be used to indicate clusters within the data

#Heat Maps


import seaborn as sns
import matplotlib.pyplot as plt

tips=sns.load_dataset('tips')
flights=sns.load_dataset('flights')

print(flights.head())


# Matrix form for correlation data
t=tips.corr()
print(t)

sns.heatmap(t)
plt.show()
sns.heatmap(t,cmap='coolwarm',annot=True)
plt.show()
# using a pivot table
pt=flights.pivot_table(values='passengers',index='month',columns='year')

print(pt)
sns.heatmap(pt,linecolor='white',linewidths=1)
plt.show()

