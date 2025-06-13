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
    def antinodeFinder(self, start_coords: tuple[int, int], distance_r: int, distance_c: int, direction: int) -> list[tuple[int, int]]:
        n = 0
        antinodes = []
        antinode = start_coords[0] + direction * n * distance_r, start_coords[1] + direction * n * distance_c
        while self.insideGrid(antinode):
            # inside, add
            antinodes.append(antinode)
            # calculate next antinode
            antinode = start_coords[0] + direction * n * distance_r, start_coords[1] + direction * n * distance_c
            n += 1
        return antinodes


a = Puzzle('input.txt')

antinodes = set()
for key, coords in a.node_coord.items():
    for i in range(len(coords)):
        for j in range(i + 1,len(coords)):
            distance_r, distance_c = coords[j][0] - coords[i][0], coords[j][1] - coords[i][1]
            antinodes = antinodes.union(a.antinodeFinder(coords[i],distance_r,distance_c,-1))
            antinodes = antinodes.union(a.antinodeFinder(coords[j],distance_r,distance_c,1))
                    
print(len(antinodes))
