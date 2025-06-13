from collections import defaultdict

class Puzzle:
    def __init__(self,filename):
        self.numrows = None
        self.numcols = None
        self.grid = []
        self.node_coord = defaultdict(list) #list of tuples with zero indexed row, col coords
        self.loadGrid(filename)

    def loadGrid(self, filename: str):
        with open(filename) as file:
            row = 0
            for line in file:
                array = []
                col = 0
                for char in line[:-1]:
                    array.append(char)
                    if char != '.':
                        self.node_coord[char].append((row,col))
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



a = Puzzle('input.txt')
# def antinodeFinder(coords)
antinodes = set()
for key, coords in a.node_coord.items():
    for i in range(len(coords)):
        for j in range(i + 1,len(coords)):
            distance_r, distance_c = coords[j][0] - coords[i][0], coords[j][1] - coords[i][1]
            antinode1 = coords[i][0] - distance_r, coords[i][1] - distance_c
            antinode2 = coords[j][0] + distance_r, coords[j][1] + distance_c
            if a.insideGrid(antinode1):
                antinodes.add(antinode1)
            if a.insideGrid(antinode2):
                antinodes.add(antinode2)
print(len(antinodes))

