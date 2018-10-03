#Grids are general types of plots that allow you to map plot types to rows
# and columns of a grid,
# this helps you create similar plots separated by features.

import seaborn as sns
import matplotlib.pyplot as plt

iris=sns.load_dataset('iris')
print(iris.head())

#PairGrid
#Pairgrid is a subplot grid for plotting pairwise relationships in a dataset.

#Creates empty grid
sns.PairGrid(iris)
plt.show()

# Then you map to the grid
g = sns.PairGrid(iris)
g.map(plt.scatter)
plt.show()

# Map to upper,lower, and diagonal
g = sns.PairGrid(iris)
g.map_diag(plt.hist)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)
plt.show()

#pair plot
sns.pairplot(iris)
plt.show()