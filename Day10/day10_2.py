from collections import defaultdict
import copy

class Puzzle:
    def __init__(self,filename):
        self.numrows = None
        self.numcols = None
        self.grid = []
        self.trailhead_coord = [] #list of tuples with zero indexed row, col coords
        self.loadGrid(filename)

    def loadGrid(self, filename: str):
        with open(filename) as file:
            row = 0
            for line in file:
                array = []
                col = 0
                for char in line[:-1]:
                    array.append(char)
                    if char == '0':
                        self.trailhead_coord.append((row,col))
                    col += 1
                self.grid.append(array)
                row += 1
        self.numrows = len(self.grid)
        self.numcols = len(self.grid[0])

    def insideGrid(self, coord: tuple[int, int]) -> bool:
        if 0 <= coord[0] < self.numrows and 0 <= coord[1] < self.numcols:
            return True
        else:
            return False
    
    def recurseToPeak(self, seen_grid: list[list[tuple[int, int]]], prev_height: int, pos: tuple[int, int]):
        # not inside grid
        if not self.insideGrid(pos):
            # print(1)
            return 0
        current_height = int(self.grid[pos[0]][pos[1]])
        # not viable gradient
        if current_height - prev_height != 1:
            # print(2)
            return 0
        # # previously seen path
        # if seen_grid[pos[0]][pos[1]] != '!':
        #     # print(3)
        #     return 0
        # found peak, increment score
        if current_height == 9:
            seen_grid[pos[0]][pos[1]] = current_height
            return 1
        # not at peak yet
        # set seen
        seen_grid[pos[0]][pos[1]] = current_height
        # all directions
        new_pos = []
        for direction in [(-1,0), (1,0), (0,-1), (0,1)]:
            new_pos.append((pos[0]+direction[0], pos[1]+direction[1]))
        # print(current_height, pos)
        # printGrid(seen_grid)
        return self.recurseToPeak(seen_grid, current_height, new_pos[0]) + self.recurseToPeak(seen_grid, current_height, new_pos[1]) + self.recurseToPeak(seen_grid, current_height, new_pos[2]) + self.recurseToPeak(seen_grid, current_height, new_pos[3])

def printGrid(grid):
    # print('Position: ' + str((pos[0],pos[1])))
    print('\n'.join([' '.join([str(cell) for cell in row]) for row in grid]))
    print('\n')

a = Puzzle('input.txt')
# a.printGrid()

scores = []

for trailhead in a.trailhead_coord:
    seen_grid = []
    for row in range(a.numrows):
        seen_grid.append(['!'] * a.numcols)
    current_height = int(a.grid[trailhead[0]][trailhead[1]])
    score = a.recurseToPeak(seen_grid, current_height-1,trailhead)
    scores.append(score)

print(scores)
print(sum(scores))

