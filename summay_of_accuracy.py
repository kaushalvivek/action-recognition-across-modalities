'''
  Summary of accuracy data.
  Prepare accuracy_data.csv before running this script
'''
import pandas as pd

data = pd.read_csv('accuracy_data.csv')

skeleton_accuracy_mean = round(data['skeleton_accuracy'].mean(),2)
skeleton_accuracy_median = round(data['skeleton_accuracy'].median(),2)

avatar_accuracy_mean = round(data['avatar_accuracy'].mean(),2)
avatar_accuracy_median = round(data['avatar_accuracy'].median(),2)

skeleton_accuracy_variance = round(data['skeleton_accuracy'].var(),2)
avatar_accuracy_variance = round(data['avatar_accuracy'].var(),2)

print("Skeleton Accuracy Mean : " + str(skeleton_accuracy_mean))
print("Skeleton Accuracy Median : " + str(skeleton_accuracy_median))
print("Skeleton Accuracy Variance : " + str(skeleton_accuracy_variance))
print("Avatar Accuracy Mean : " + str(avatar_accuracy_mean))
print("Avatar Accuracy Median : " + str(avatar_accuracy_median))
print("Avatar Accuracy Variance : " + str(avatar_accuracy_variance))