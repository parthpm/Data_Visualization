import seaborn as sns
import matplotlib.pyplot as plt

#Seaborn comes with built-in data sets!
tips = sns.load_dataset('tips')

#rugplot
#rugplots are actually a very simple concept,
# they just draw a dash mark for every point on a
#  univariate distribution.
#  They are the building block of a KDE plot:
sns.rugplot(tips['total_bill'])
plt.show()

#kdeplot
#kdeplots are Kernel Density Estimation plots.
#  These KDE plots replace every single observation with
#  a Gaussian (Normal)
#  distribution centered around that value.
sns.kdeplot(tips['total_bill'])
plt.show()