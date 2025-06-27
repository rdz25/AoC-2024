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
        translate = {'#':'##','O':'[]','.':'..','@':'@.'}
        with open(grid_file) as file:
            row = 0
            for line in file:
                processed_line = line.replace('\n','')
                array = []
                col = 0
                for char in processed_line:
                    if char == '@':
                        self.robot = (row,col)
                    new_chars = translate[char]
                    for new_char in new_chars:
                        array.append(new_char)
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
        new_pos_char = self.grid[new_pos[0]][new_pos[1]]
        seen = set()
        if self.obstacleCheck(new_pos, direction,seen):
            # print(seen)
            # update grid by:
            # move obstacles
            self.updateGrid(seen,direction)
            # move robot
            self.grid[new_pos[0]][new_pos[1]] = '@'
            self.grid[pos[0]][pos[1]] = '.'
            # set new robot pos
            self.robot = new_pos

    def obstacleCheck(self, pos, direction, seen) -> bool:
        '''Check if legal move and build a set `seen` of box pos to move'''
        if pos in seen:
            return True
        
        pos_char = self.grid[pos[0]][pos[1]]
        if pos_char == '#':
            return False
        elif pos_char == '.':
            return True
        # elif pos_char in {'[',']'}:
        seen.add(pos) # set of box pos
        pos_pair = self.pairPos(pos)
        seen.add(pos_pair)
        new_pos = (pos[0] + direction[0], pos[1] + direction[1])
        new_pos_pair = (pos_pair[0] + direction[0], pos_pair[1] + direction[1])
        return self.obstacleCheck(new_pos, direction, seen) and self.obstacleCheck(new_pos_pair, direction, seen)

    def updateGrid(self, seen: set[tuple[int,int]], direction: tuple[int,int]):
        '''
        Will have to work on a grid copy or slice or the end of the tree (maybe?) to avoid overwriting in the wrong order
        Or could hold box char values in a dictionary
        Or could derive box values since they follow rules
        Copy entire array not performant.
        '''
        temp_grid = copy.deepcopy(self.grid)
        for pos in seen:
            #blank all box locations
            temp_grid[pos[0]][pos[1]] = '.'
        for pos in seen:
            char = self.grid[pos[0]][pos[1]]
            new_pos = (pos[0] + direction[0], pos[1] + direction[1])
            # set current + direction to box
            temp_grid[new_pos[0]][new_pos[1]] = char
        self.grid = copy.deepcopy(temp_grid)


    # def updateGrid(self, pos, direction, prev_char):
    #     # pos_char = self.grid[pos[0]][pos[1]]
    #     # if pos_char == '.':
    #     #     #update position with prev_char
    #     #     self.grid[pos[0]][pos[1]] = prev_char
    #     #     #end of chain
    #     # elif pos_char in {'[',']'}:
    #     #     #update position with prev_char
    #     #     self.grid[pos[0]][pos[1]] = prev_char
    #     #     #continue chain
    #     #     new_pos = (pos[0] + direction[0], pos[1] + direction[1])
    #     #     pos_pair = self.pairPos(new_pos)
    #     #     pos_pair_char = grid[pos_pair[0]][pos_pair[1]]
    #     #     new_pos_pair = (pos_pair[0] + direction[0], pos_pair[1] + direction[1])
    #     #     if new_pos == pos_pair:
                
    #     #     else:
    #     #         grid
    #     #         self.updateGrid(new_pos, direction, pos_char)
    #     #         self.updateGrid(new_pos_pair, direction, pos_pair_char)
    #     # else:
    #     #     #shouldn't hit walls
    #     #     raise ValueError(f'Update error: {pos}:{pos_char}')  

    # def boxStack(self,pos,direction):
    #     '''Create a set of box pos that are connected to a starting push (pos and direction)'''
    #     new_pos = (pos[0] + direction[0], pos[1] + direction[1])
    #     new_char = grid[pos[0]][pos[1]]
    #     if self.pairPos(new_pos) in boxes:
    #         boxStack


    def pairPos(self,pos) -> tuple[int,int]:
        '''Returns the paired coordinate for boxes, otherwise None'''
        if self.grid[pos[0]][pos[1]] == '[':
            return (pos[0], pos[1] + 1)
        elif self.grid[pos[0]][pos[1]] == ']':
            return (pos[0], pos[1] - 1)
        else:
            return None

    def printGrid(self):
        print('\n'.join([' '.join([str(cell) for cell in row]) for row in self.grid]))
        print('\n')

    def scoreGPS(self) -> int:
        score = 0
        for row,line in enumerate(self.grid):
            for col,cell in enumerate(line):
                if cell == '[':
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
# # dataset = {'grid':'test_grid2.txt', 'moves':'test_moves2.txt'}
# # dataset = {'grid':'input_grid.txt', 'moves':'input_moves.txt'}

# a = Puzzle(dataset['grid'])
# moves = loadMoves(dataset['moves'])
# a.grid[2][7], a.grid[2][8], a.grid[2][9] = '[',']','.'
# a.grid[2][5], a.grid[2][6] = '[',']'


# print('Initial State:')
# a.printGrid()
# print(a.robot)
# print(a.obstacleCheck((2,7),(-1,0),set())) #false
# print(a.obstacleCheck((2,8),(1,0),set())) #true
# print(a.obstacleCheck((2,7),(0,1),set())) #true

# a.moveRobot((0,1))

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
# a.allMoves(moves[:90])
print('End State:')
a.printGrid()
print(f'The sum is: {a.scoreGPS()}')