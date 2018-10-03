import seaborn as sns
import matplotlib.pyplot as plt
#faceitgrid
#FacetGrid is the general way to create grids of plots
#  based off of a feature:
tips=sns.load_dataset('tips')
print(tips.head())

#create empty grid
g=sns.FacetGrid(data=tips,row='smoker',col='time')
g=g.map(plt.hist,'total_bill')
plt.show()
