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

#direction as y, x
direction = (-1,0)
row, col = start[0], start[1]
unique = 0
while 0 <= col < totalcolumns and 0 <= row < totalrows:
    #check position for blockage
    if grid[row][col] == '#':
        #reset position
        row, col = prevrow, prevcol
        #change direction; Note: transformation different because it's not a Cartesian graph
        direction = (direction[1], -direction[0])
    #check if position is visited
    elif grid[row][col] != 'X':
        unique += 1
        #set visited
        grid[row][col] = 'X'
    #move
    prevrow, prevcol = row, col
    row += direction[0]
    col += direction[1]
print(unique)
# print(grid)