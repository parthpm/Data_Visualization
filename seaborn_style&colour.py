import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset('tips')


sns.countplot(data=tips,x='sex',palette='coolwarm')
plt.show()
sns.set_style(style='whitegrid')
sns.countplot(data=tips,x='sex',palette='coolwarm')
plt.show()

#remove spine
sns.despine()
plt.show()

#Size and Aspect¶

#You can use matplotlib's plt.figure(figsize=(width,height)
#  to change the size of most seaborn plots.

# You can control the size and aspect ratio of most seaborn
# grid plots by passing
# in parameters: size, and aspect. For example:



#NON GRID PLOT
plt.figure(figsize=(12,8))
sns.countplot(data=tips,x='sex')
plt.show()

#scale and context
sns.set_context('poster',font_scale=4)
sns.countplot(x='sex',data=tips,palette='coolwarm')
plt.show()
