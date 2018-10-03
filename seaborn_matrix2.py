import seaborn as sns
import matplotlib.pyplot as plt

tips=sns.load_dataset('tips')
flights=sns.load_dataset('flights')
pt=flights.pivot_table(values='passengers',index='month',columns='year')


#cluster map
#The clustermap uses hierarchal clustering to produce a clustered
# version of the heatmap.grouping related data

sns.clustermap(pt)
plt.show()

sns.clustermap(pt,cmap='coolwarm',standard_scale=1)
plt.show()