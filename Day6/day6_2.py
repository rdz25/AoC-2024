import copy

grid = []
row = 0
with open("input.txt") as file:
    for line in file:
        array = []
        column = 0
        #ignore newline char
        for char in line[:-1]:
            array.append(char)
            if char == "^":
                start = (row,column)
            column += 1
        grid.append(array)
        row += 1
totalrows, totalcolumns = len(grid),len(grid[0])

def printGrid(pos,pgrid):
    #current position
    pgrid[pos[0]][pos[1]] = 'X'
    print('Position: ' + str((pos[0],pos[1])))
    print('\n'.join([' '.join([str(cell) for cell in row]) for row in pgrid]))
    print('\n')

#def to run pathing
def oneStep(pos, prevpos,direction):
    row, col = pos[0], pos[1]
    #check position for blockage
    if grid[row][col] == '#':
        #reset position
        row, col = prevpos[0], prevpos[1]
        #change direction; Note: transformation different because it's not a Cartesian graph
        direction = (direction[1], -direction[0])
    # #check if position is visited
    # elif grid[row][col] != 'X':
    #     #set visited
    #     grid[row][col] = 'X'
    #move
    prevpos = pos
    row += direction[0]
    col += direction[1]
    #new pos
    return {'pos':(row, col),'prevpos':prevpos,'direction':direction}
'''
Test for a single insertion
'''
# counter = 0
# locations = []
# i, j = 1, 7
# grid[i][j] = 'O'
# # print((i,j))
# #run pathing
# guard = {'pos':start,'prevpos':start,'direction':(-1,0)}
# looper = dict(guard)
# while 0 <= guard['pos'][1] < totalcolumns and 0 <= guard['pos'][0] < totalrows and 0 <= looper['pos'][1] < totalcolumns and 0 <= looper['pos'][0] < totalrows:
#     printGrid(guard['pos'],copy.deepcopy(grid))
#     #dictionary unpacking
#     guard = oneStep(**guard)
#     #twostep
#     looper = oneStep(**looper)
#     #only take second step if within grid
#     if 0 <= looper['pos'][1] < totalcolumns and 0 <= looper['pos'][0] < totalrows:
#         looper = oneStep(**looper)
#     else:
#         break
#     #loop found
#     if looper['pos'] == guard['pos'] and looper['direction'] == guard['direction']:
#         counter += 1
#         locations.append((i,j))
#         #reset inserted obstacle
#         grid[i][j] = '.'
#         break
# #reset inserted obstacle
# grid[i][j] = '.'


counter = 0
locations = []
#iterate with single obstruction inserted
for i in range(totalrows):
    for j in range(totalcolumns):
        if (i, j) != start and grid[i][j] != '#':
            grid[i][j] = '#'
            # print((i,j))
            #run pathing
            guard = {'pos':start,'prevpos':start,'direction':(-1,0)}
            looper = dict(guard)
            while 0 <= guard['pos'][1] < totalcolumns and 0 <= guard['pos'][0] < totalrows and 0 <= looper['pos'][1] < totalcolumns and 0 <= looper['pos'][0] < totalrows:
                # printGrid(guard['pos'],grid)
                #dictionary unpacking
                guard = oneStep(**guard)
                #twostep
                looper = oneStep(**looper)
                #only take second step if within grid
                if 0 <= looper['pos'][1] < totalcolumns and 0 <= looper['pos'][0] < totalrows:
                    looper = oneStep(**looper)
                else:
                    break
                #loop found
                if looper['pos'] == guard['pos'] and looper['direction'] == guard['direction']:
                    counter += 1
                    locations.append((i,j))
                    #reset inserted obstacle
                    grid[i][j] = '.'
                    break
            #reset inserted obstacle
            grid[i][j] = '.'

# print('\n'.join([' '.join([str(cell) for cell in row]) for row in grid]))
# for location in locations:
#     printGrid(location,copy.deepcopy(grid))

print(f"Possible obstacle positions: {counter}")