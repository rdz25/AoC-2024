grid = []
with open("input.txt") as file:
    for line in file:
        array = []
        for char in line[:-1]:
            array.append(char)
        grid.append(array)

numrows = len(grid)
numcols = len(grid[0])
found = 0
word = 'MAS'

#find center letter A
#can't be in first/last row and column
for row in range(1,numrows-1):
    for column in range(1,numcols-1):
        if 'A' == grid[row][column]:  #char match
            #search cross
            if ((grid[row - 1][column - 1] == 'S' and grid[row + 1][column + 1] == 'M') 
                or (grid[row - 1][column - 1] == 'M' and grid[row + 1][column + 1] == 'S')) \
                and ((grid[row - 1][column + 1] == 'S' and grid[row + 1][column - 1] == 'M') \
                or (grid[row - 1][column + 1] == 'M' and grid[row + 1][column - 1] == 'S')):
                found += 1

print(f"X-MAS count: {found}")
