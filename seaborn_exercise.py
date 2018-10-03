import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style('whitegrid')
titanic = sns.load_dataset('titanic')

print(titanic.head())
sns.jointplot(x='fare',y='age',data=titanic)
plt.show()

sns.distplot(titanic['fare'],bins=20,kde=False,color='red')
plt.show()

sns.boxplot(x='class',y='age',data=titanic)
plt.show()

sns.swarmplot(x='class',y='age',data=titanic)
plt.show()

sns.countplot(x='sex',data=titanic)
plt.show()

sns.heatmap(titanic.corr(),cmap='coolwarm')
plt.title('titanic.corr')
plt.show()

sns.FacetGrid(data=titanic,col='sex').map(plt.hist,'age')
plt.show()

