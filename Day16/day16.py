import heapq as hq

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
    
    def getChar(self, pos):
        return self.grid[pos[0]][pos[1]]

def pathDjikstra(puzzle):
    pos = puzzle.start
    facing = (0,1)
    heap = []
    # starting position; doesn't check backwards, which could apply at the start
    hq.heappush(heap, (0,pos,facing))
    seen = set()
    while heap:
        score, pos, facing = hq.heappop(heap)        
        if puzzle.getChar(pos) == 'E':
            return score
        # valid position
        elif puzzle.getChar(pos) != '#' and pos not in seen:
            # print(score, pos, facing)
            # puzzle.grid[pos[0]][pos[1]] = 'X'
            seen.add(pos)
            # check same direction and left and right
            for direction in {facing, (facing[1], -facing[0]), (-facing[1], facing[0])}:
                if direction == facing:
                    cost = 1    # 1 step
                else:
                    cost = 1001 # turn and 1 step
                new_pos = (pos[0] + direction[0], pos[1] + direction[1])
                hq.heappush(heap, (score + cost, new_pos, direction))


a = Puzzle('input.txt')
a.printGrid()
score = pathDjikstra(a)
print(f"The score is: {score}")