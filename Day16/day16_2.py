import heapq as hq
import copy
from collections import defaultdict

class Puzzle:
    def __init__(self, grid_file):
        self.numrows = None
        self.numcols = None
        self.grid = []
        # start position
        self.start = None
        # end position
        self.end = None
        # build grid
        self.loadGrid(grid_file)
        # # parent lookup for tracking path
        # self.parent = {}

    def loadGrid(self, grid_file: str):
        with open(grid_file) as file:
            row = 0
            for line in file:
                processed_line = line.replace('\n','')
                array = []
                col = 0
                for char in processed_line:
                    if char == 'S':
                        self.start = (row,col)
                    elif char == 'E':
                        self.end = (row,col)
                    array.append(char)
                    col += 1
                self.grid.append(array)
                row += 1
        self.numrows = len(self.grid)
        self.numcols = len(self.grid[0])

    def printGrid(self):
        print('\n'.join([' '.join([str(cell) for cell in row]) for row in self.grid]))
        print('\n')

    def markPaths(self, distances):
        '''Copy grid and mark all paths with X, overwriting Start and End'''
        grid_copy = copy.deepcopy(self.grid)
        stack = [self.end]
        # iterate backwards from end
        seen = set()
        count = 0
        while stack:
            pos = stack.pop()
            grid_copy[pos[0]][pos[1]] = 'X'
            count += 1
            seen.add(pos)
            for direction in {(1,0),(-1,0),(0,1),(0,-1)}:
                new_pos = (pos[0] + direction[0], pos[1] + direction[1])
                # recurse back to lower distances values
                check_distance = distances.get(new_pos, float('inf'))
                if new_pos not in seen and check_distance < distances.get(pos):
                    stack.append(new_pos)   
            
        print('\n'.join([' '.join([str(cell) for cell in row]) for row in grid_copy]))
        print('\n')

        return count

    
    def getChar(self, pos):
        return self.grid[pos[0]][pos[1]]

def pathDjikstra(puzzle) -> dict[tuple[int,int], int]:
    '''Need to build the distance map: a dictionary of position and facing tuples with their distance score'''
    pos = puzzle.start
    facing = (0,1)
    heap = []
    # starting position; doesn't check backwards, which could apply at the start
    hq.heappush(heap, (0,pos,facing))
    seen = set()
    # TODO modify distance map to keep score for each STATE (position and facing) and return other lowest distance states rather than the first
    dist = {}
    while heap:
        score, pos, facing = hq.heappop(heap)
        dist[pos] = score
        if puzzle.getChar(pos) == 'E':
            return dist
        # prior valid check; add position to visited
        seen.add(pos)
        # check same direction and left and right
        for direction in {facing, (facing[1], -facing[0]), (-facing[1], facing[0])}:
            if direction == facing:
                cost = 1    # 1 step
            else:
                cost = 1001 # turn and 1 step
            # only move to valid positions
            new_pos = (pos[0] + direction[0], pos[1] + direction[1])
            if puzzle.getChar(new_pos) != '#' and new_pos not in seen:
                hq.heappush(heap, (score + cost, new_pos, direction))


a = Puzzle('testinput.txt')
a.printGrid()
distance = pathDjikstra(a)
score = distance.get(a.end)
# print(distance.get((7,5)))
# print(distance.get((7,4)))
print(distance.get((9,3)))
print(distance.get((10,3)))
print(distance.get((11,3)))

print(f"The score is: {score}")
print(f"The number of tiles in path are: {a.markPaths(distance)}")