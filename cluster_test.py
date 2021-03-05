import numpy as np

my_cluster_contant = 20 # if 20 values are closest to each other its a cluster

arr = np.random.randint(2,20,360) # assuming laser scan data 

cluster_list = [] # just to store 

for i in arr:
    if i >= 8 and i <= 12:
        cluster_list.append(i)
print(len(cluster_list))

if len(cluster_list) => my_cluster_contant:  # if laser scan has more then my_cluster_constant is a decent object
    print("object detected")
else:
    print("Keep going")
