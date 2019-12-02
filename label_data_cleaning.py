'''
  Label wise accuracy analysis
'''
import json
import pandas as pd

# Read file
with open("./clean_data.json") as json_file:
  data = (json.loads(json_file.read()))

labels = []
for i in data:
  for j in i[1]:
    labels.append(j['cans'])

labels_arr = list((set(labels)))
labels = {}
for i in labels_arr:
  labels[i] = {
    'skeleton':[],
    'avatar':[]
  }

for i in data:
  for j in i[1]:
    if j['file'].find('.fbx') == -1:
      # Skeleton
      labels[j['cans']]['skeleton'].append({
          'date': i[0], 
          'guess':j['guess'], 
          'time_taken':round(j['time_taken'],2), 
          'replays':j['num_replays'], 
          'pauses':j['pauses']  
        }) 
    else:
      # Avatar
      labels[j['cans']]['avatar'].append({
          'date': i[0], 
          'guess':j['guess'], 
          'time_taken':round(j['time_taken'],2), 
          'replays':j['num_replays'], 
          'pauses':j['pauses']  
        }) 

print (labels)
