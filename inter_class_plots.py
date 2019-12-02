import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('accuracy_data.csv')

middle_school = data.loc[data['user_age_group']=='middle_school']
high_school = data.loc[data['user_age_group']=='high_school']
college = data.loc[data['user_age_group']=='college']

# seaborn histogram
a= sns.distplot(middle_school['avatar_accuracy'], hist = False, kde = True,
                 kde_kws = {'linewidth': 3},
                 label = 'middle_school')

a= sns.distplot(high_school['avatar_accuracy'], hist = False, kde = True,
                 kde_kws = {'linewidth': 3},
                 label = 'high_school')

a= sns.distplot(college['avatar_accuracy'], hist = False, kde = True,
                 kde_kws = {'linewidth': 3},
                 label = 'college')

a.set(ylim=(0, None))
a.set(xlim=(0, 100))

# Add labels
plt.title('Frequency Distribution of Accuracy for Avatar')
plt.xlabel('percentage accuracy')
plt.ylabel('frequency')

plt.savefig('inter_class_avatar_accuracy_frequency.png')