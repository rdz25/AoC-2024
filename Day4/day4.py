grid = []
with open("input.txt") as file:
    for line in file:
        array = []
        for char in line[:-1]:
            array.append(char)
        grid.append(array)

class Puzzle:
    def __init__(self,grid):
        self.numrows = len(grid)
        self.numcols = len(grid[0])
        self.found = 0
        self.word = 'XMAS'

    def wordSearch(self,row, column, searchindex,direction):
        if searchindex >= len(self.word):
            self.found += 1
            return

        if not(0 <= row < self.numrows and 0 <= column < self.numcols):  #not inside grid
            return
        
        if self.word[searchindex] == grid[row][column]:    #match found
            #no turning/zigzags allowed
            i = direction[0]
            j = direction[1]    
            self.wordSearch(row + i, column + j, searchindex + 1,direction)



    def wordCount(self):
        for row in range(self.numrows):
            for column in range(self.numcols):
                if self.word[0] == grid[row][column]:  #char match
                    #no turning/zigzags allowed after this
                    for i in range(-1,2):
                        for j in range(-1,2):
                            if (i,j) != (0,0):
                                self.wordSearch(row + i, column + j, 1,(i,j))

        print(f"{''.join(self.word)} count: {self.found}")
a = Puzzle(grid)
a.wordCount()
