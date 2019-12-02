import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('accuracy_data.csv')

data['skeleton_accuracy'] = data['skeleton_accuracy'].round(decimals=1)
data['avatar_accuracy'] = data['avatar_accuracy'].round(decimals=1)

skeleton = data['skeleton_accuracy']
avatar = data['avatar_accuracy']

# seaborn histogram
a= sns.distplot(skeleton, hist = False, kde = True,
                 kde_kws = {'linewidth': 3},
                 label = 'skeleton')

a= sns.distplot(avatar, hist = False, kde = True,
                 kde_kws = {'linewidth': 3},
                 label = 'avatar')
a.set(ylim=(0, None))
a.set(xlim=(0, 100))

# Add labels
plt.title('Frequency Distribution of Accuracy')
plt.xlabel('percentage accuracy')
plt.ylabel('frequency')

plt.savefig('accuracy_frequency.png')