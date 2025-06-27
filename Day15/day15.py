from collections import defaultdict
import copy

class Puzzle:
    def __init__(self, grid_file):
        self.numrows = None
        self.numcols = None
        self.grid = []
        # robot position
        self.robot = None
        # build grid
        self.loadGrid(grid_file)
        # Consider holding dict of box positions

    def loadGrid(self, grid_file: str):
        with open(grid_file) as file:
            row = 0
            for line in file:
                processed_line = line.replace('\n','')
                array = []
                col = 0
                for char in processed_line:
                    if char == '@':
                        self.robot = (row,col)
                    array.append(char)
                    col += 1
                self.grid.append(array)
                row += 1
        self.numrows = len(self.grid)
        self.numcols = len(self.grid[0])

    def allMoves(self, moves):
        for move in moves:
            self.moveRobot(move)
            # print(move)
            # self.printGrid()

    
    def moveRobot(self, direction) -> tuple[int,int]:
        pos = self.robot
        new_pos = (pos[0] + direction[0], pos[1] + direction[1])
        # check if moveable
        if self.obstacleCheck(new_pos, direction):
            # update grid (moving robot and obstacles)
            self.updateGrid(new_pos, direction, '@')
            self.grid[pos[0]][pos[1]] = '.'
            # set new robot pos
            self.robot = new_pos

    def updateGrid(self, pos, direction, prev_char):
        pos_char = self.grid[pos[0]][pos[1]]
        if pos_char == '.':
            #update position with prev_char
            # Refactor if statement?
            self.grid[pos[0]][pos[1]] = prev_char
            #end of chain
        elif pos_char == 'O':
            #update position with prev_char
            self.grid[pos[0]][pos[1]] = prev_char
            #continue chain
            new_pos = (pos[0] + direction[0], pos[1] + direction[1])
            self.updateGrid(new_pos, direction, pos_char)
        else:
            #shouldn't hit walls
            raise ValueError(f'Update error: {pos}:{pos_char}')

    def obstacleCheck(self, pos, direction) -> bool:
        pos_char = self.grid[pos[0]][pos[1]]
        if pos_char == '#':
            return False
        elif pos_char == 'O':
            new_pos = (pos[0] + direction[0], pos[1] + direction[1])
            return self.obstacleCheck(new_pos, direction)
        elif pos_char == '.':
            return True
        else:
            raise ValueError(f'Obstacle error: {pos}:{pos_char}')

    def printGrid(self):
        print('\n'.join([' '.join([str(cell) for cell in row]) for row in self.grid]))
        print('\n')

    def scoreGPS(self) -> int:
        score = 0
        for row,line in enumerate(self.grid):
            for col,cell in enumerate(line):
                if cell == 'O':
                    score += 100 * row + col
        return score
            
def loadMoves(moves_file: str) -> list:
    moves_list = []
    translation = {'<':(0,-1),'^':(-1,0),'>':(0,1),'v':(1,0)}
    with open(moves_file) as file:
        for line in file:
            processed_line = line.replace('\n','')
            for char in processed_line:
                moves_list.append(translation.get(char))
    return moves_list

#######
#######
# dataset = {'grid':'test_grid.txt', 'moves':'test_moves.txt'}
# dataset = {'grid':'test_grid2.txt', 'moves':'test_moves2.txt'}
dataset = {'grid':'input_grid.txt', 'moves':'input_moves.txt'}

a = Puzzle(dataset['grid'])
moves = loadMoves(dataset['moves'])
print('Initial State:')
a.printGrid()
a.allMoves(moves)
print('End State:')
a.printGrid()
print(f'The sum is: {a.scoreGPS()}')