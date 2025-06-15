with open('input.txt') as file:
    line = file.readline()
#build and move at same time?


# build/expand representation
build = []  # could presize list
id = 0
for i in range(len(line)):
    if i % 2 == 0: # file
        for j in range(int(line[i])):
            build.append(id)
            
        id += 1
    else: # gap
        for j in range(int(line[i])):
            build.append(None)

# move files
right = len(build) - 1  # assume last is a file
i = 0
while i < right:
    if build[i] is None:
        build[i] = build[right]
        build[right] = None
        #find next right file
        while build[right] is None: # and right > 0
            right -= 1
    i += 1

# calculate
sum = 0
for index, fileid in enumerate(build):
    if fileid is None:
        break
    sum += index * fileid

print(f"The checksum is {sum}")


