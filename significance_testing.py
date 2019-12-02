import pandas as pd
from scipy.stats import wilcoxon, ttest_ind, normaltest, shapiro

data = pd.read_csv('accuracy_data.csv')

skeleton = data.iloc[:,2]
avatar = data.iloc[:,4]

print("\Skeleton Normalcy: ")
print(normaltest(skeleton).pvalue)

print("\Avatar Normalcy: ")
print(normaltest(avatar).pvalue)

print("\nWilcoxon p-value: ")
print((wilcoxon(skeleton, avatar).pvalue))

print("\nT-test p-value: ")
print(ttest_ind(skeleton, avatar,equal_var=False).pvalue)