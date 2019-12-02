import pandas as pd
from scipy.stats import wilcoxon, ttest_ind, normaltest, shapiro

data = pd.read_csv('accuracy_data.csv')

middle_school = data.loc[data['user_age_group']=='middle_school']
high_school = data.loc[data['user_age_group']=='high_school']
college = data.loc[data['user_age_group']=='college']

print (middle_school.count())
print (high_school.count())
print (college.count())

print("----------------- MIDDLE SCHOOL -----------------\n")
print("Skeleton Accuracy Mean  : " + str(round(middle_school['skeleton_accuracy'].mean(),2)) + '%')
print("Skeleton Accuracy Median: " + str(round(middle_school['skeleton_accuracy'].median(),2)) + '%\n')
print("Avatar Accuracy Mean  : " + str(round(middle_school['avatar_accuracy'].mean(),2)) + '%')
print("Avatar Accuracy Median: " + str(round(middle_school['avatar_accuracy'].median(),2)) + '%\n')
print("----------------- HIGH SCHOOL -----------------\n")
print("Skeleton Accuracy Mean  : " + str(round(high_school['skeleton_accuracy'].mean(),2)) + '%')
print("Skeleton Accuracy Median: " + str(round(high_school['skeleton_accuracy'].median(),2)) + '%\n')
print("Avatar Accuracy Mean  : " + str(round(high_school['avatar_accuracy'].mean(),2)) + '%')
print("Avatar Accuracy Median: " + str(round(high_school['avatar_accuracy'].median(),2)) + '%\n')
print("----------------- COLLEGE -----------------\n")
print("Skeleton Accuracy Mean  : " + str(round(college['skeleton_accuracy'].mean(),2)) + '%')
print("Skeleton Accuracy Median: " + str(round(college['skeleton_accuracy'].median(),2)) + '%\n')
print("Avatar Accuracy Mean  : " + str(round(college['avatar_accuracy'].mean(),2)) + '%')
print("Avatar Accuracy Median: " + str(round(college['avatar_accuracy'].median(),2)) + '%\n')

ms = middle_school['skeleton_accuracy']
ma = middle_school['avatar_accuracy']

hs = high_school['skeleton_accuracy']
ha = high_school['avatar_accuracy']

cs = college['skeleton_accuracy']
ca = college['avatar_accuracy']

print ("Wilcox ms vs hs : ")
print((wilcoxon(ms, hs).pvalue))

print ("Wilcox ms vs cs : ")
print((wilcoxon(ms, cs).pvalue))

print ("Wilcox hs vs cs : ")
print((wilcoxon(hs, cs).pvalue))

