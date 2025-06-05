import pandas as pd

list1 = []
list2 = []
a = pd.read_table('input.txt', sep = '   ', header = None, engine = 'python')

list1 = sorted(a[0].to_list())
list2 = sorted(a[1].to_list())

distance = 0
for i in range(len(list1)):
    diff = list2[i] - list1[i] 
    # if distance < 0:
    #     print(i)
    distance += abs(diff)

print("The total distance is " + str(distance))

counter = {}

for num in list2:
    if num in counter:
        counter[num] += 1
    else:
        counter[num] = 1

similarity = 0
for num in list1:
    if num in counter:
        similarity += num * counter[num]

print("The total similarity is " + str(similarity))