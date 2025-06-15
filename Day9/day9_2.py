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

def chunkIndices(start_index, starting_side, values):
    '''Return inclusive'''
    find = values[start_index]
    end_index = start_index
    if starting_side == 'right':
        while start_index > 0 and values[end_index] == find:
            end_index -= 1
        return (end_index + 1, start_index)
    elif starting_side == 'left':
        while end_index < len(build) and values[end_index] == find:
            end_index += 1
        return (start_index, end_index - 1)
    # else:
        #problem
    


# move files
j = len(build) - 1  # right file end index
i = int(line[0]) # left gap start index
i_reset = i # used to reset
while i < j:
    #find gap chunk
    gap_chunk = chunkIndices(i, 'left', build)
    gap_len = gap_chunk[1] - gap_chunk[0] + 1
    # find file chunk
    file_chunk = chunkIndices(j, 'right', build)
    file_len = file_chunk[1] - file_chunk[0] + 1
    #keep trying to find next gap chunk that fits, moving i
    while j > i and gap_len <  file_len:
        # print(build)
        # print(f'filelen: {file_len}')
        # print(build[file_chunk[0]:file_chunk[1]+1])
        # print(gap_chunk)
        # print('\n')
        #find next gap
        i = gap_chunk[1] + 1
        while build[i] is not None:
            i += 1
        gap_chunk = chunkIndices(i, 'left', build)
        gap_len = gap_chunk[1] - gap_chunk[0] + 1
    #suitable gap found
    if gap_len >=  file_len and gap_chunk[0] < file_chunk[0]:
        # swap chunk
        # print(build)
        # print(gap_chunk, file_chunk)
        # print(gap_len, file_len)
        build[gap_chunk[0]:gap_chunk[0]+file_len], build[file_chunk[0]:file_chunk[1]+1] = build[file_chunk[0]:file_chunk[1]+1], build[gap_chunk[0]:gap_chunk[0]+file_len]

    # i needs to be on leftmost gap; j moves to next file chunk
    i = int(line[0])
    while build[i] is not None:
        i += 1

    j -= file_len 
    while j > i and build[j] is None:
        j -= 1



# calculate
sum = 0
for index, fileid in enumerate(build):
    if fileid is not None:
        sum += index * fileid

print(f"The checksum is {sum}")


