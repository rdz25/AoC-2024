from collections import defaultdict
import copy

class Puzzle:
    def __init__(self,filename):
        self.numrows = None
        self.numcols = None
        self.grid = []
        self.loadGrid(filename)

    def loadGrid(self, filename: str):
        with open(filename) as file:
            row = 0
            for line in file:
                array = []
                col = 0
                for char in line[:-1]: # skip newline
                    array.append(char)
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
    
    def printGrid(self, pos=None):
        grid_copy = copy.deepcopy(self.grid)
        if pos:
            print('Position: ' + str((pos[0],pos[1])))
            if a.insideGrid(pos):
                grid_copy[pos[0]][pos[1]] = 'O'
            else:
                print('Not inside grid!')            
        print('\n'.join([' '.join([str(cell) for cell in row]) for row in grid_copy]))
        print('\n')
    
    def recurseRegion(self, pos: tuple[int, int], crop_type, crop_dict) -> int:
        '''Builds a area and perimeter dictionary for given crop type. Returns value to indicate perimeter'''
        #inside grid, same crop
        if self.insideGrid(pos) and self.grid[pos[0]][pos[1]] == crop_type:
            if pos not in seen:
                seen.add(pos)
                #increment area and perimeter
                crop_dict['area'] += 1
                #branch out
                for direction in [(-1,0),(1,0),(0,-1),(0,1)]:
                    new_pos = (pos[0]+direction[0], pos[1]+direction[1])
                    edge = self.recurseRegion(new_pos, crop_type, crop_dict)
                    # if edge is None:
                    #     a.printGrid(pos)
                    #     print(new_pos, crop_type, crop_dict)
                    # dictionary of positions and their set of edge direction tuples (up to 4)
                    if edge:
                        crop_dict['edge'][pos].add(direction)
            # edge not found; either hit seen or on an intermediate path coming back up the stack
            return 0
        else:
            # if not inside or not same crop, then direction has hit edge
            return 1

    def recurseRegionEdge(self, pos: tuple[int, int], edge_direction, move_direction=None) -> int:
        '''Travel along region's single edge in both directions, setting seen_set. Once done the cell, direction tuple will no longer be counted.'''
        # part of region; already checked for seen/visited
        # need to check if the cell has same edge
        if pos in crop_dict['edge'] and edge_direction in crop_dict['edge'][pos]:
            #move along edge
            # if move_direction is None:
            #     print(f"\t {pos}, {edge_direction}")
            # if (pos, edge_direction) == ((1,0),(0,1)):  # never hits new movedirection
            #     print('badadd')
            #     print(f"\t {pos} {edge_direction} {move_direction}")
            seen_edge.add((pos, edge_direction))
            if edge_direction == (-1,0) or edge_direction == (1,0):
                #move horizontal, adjust colum
                if move_direction is None:  # bidirectional move
                    self.recurseRegionEdge((pos[0],pos[1]+1), edge_direction, 1)
                    self.recurseRegionEdge((pos[0],pos[1]-1), edge_direction, -1)
                else:
                    self.recurseRegionEdge((pos[0],pos[1]+move_direction), edge_direction, move_direction)
            elif edge_direction == (0,-1) or edge_direction == (0,1):
                #move vertical, adjust row
                if move_direction is None:  # bidirectional move
                    self.recurseRegionEdge((pos[0]+1,pos[1]), edge_direction, 1)
                    self.recurseRegionEdge((pos[0]-1,pos[1]), edge_direction, -1)
                else:
                    self.recurseRegionEdge((pos[0]+move_direction,pos[1]), edge_direction, move_direction)
        # 
        


a = Puzzle('testinput.txt')
a.printGrid()

#seen for whole grid, logically only needs to be seen per crop type region, but technically unecessary to reset
seen = set()
price_sum = 0

# dictionary of crop types
# could hold each region's area and perimeter?
# region_dict = {}

for i in range(a.numrows):
    for j in range(a.numcols):
        if (i,j) not in seen:
            crop = a.grid[i][j]
            crop_dict = {'area': 0, 'edge': defaultdict(set)}
            a.recurseRegion((i,j), crop, crop_dict)
            # reset with each region
            seen_edge = set()   # (pos, direction)
            sum_edge = 0
            # (1,0)
            for pos, directions in crop_dict['edge'].items():
                for direction in directions:
                    if (pos, direction) not in seen_edge:
                        # new edge
                        sum_edge += 1
                        # print(pos, direction)
                        a.recurseRegionEdge(pos, direction)
            # print(f"\t Edges: {sum_edge}")
            price_sum += crop_dict['area'] * sum_edge
print(f"The total price is: {price_sum}")