from collections import defaultdict
import copy

class Puzzle:
    def __init__(self, filename, tall, wide):
        self.numrows = tall
        self.numcols = wide
        self.grid = []
        for i in range(self.numrows):
            self.grid.append(['.']*self.numcols)
        self.robots_start = []
        self.robots = None  #repurposing to generate positions after X gens
        #build list of robot positions and velocities
        self.loadGrid(filename)
        #only set at the end, otherwise write code to reset/update through movement
        self.quadrant_counts = {(0,0):0,(0,1):0,(1,0):0,(1,1):0}

    def loadGrid(self, filename: str):
        with open(filename) as file:
            for line in file:
                robot = {}
                line = line.replace('\n','')
                pos = line[line.index('p=')+2:line.index(' v')]
                vel = line[line.index('v=')+2:]
                #coordinates are x, y (not row, col); origin in top left; zero indexed
                robot['pos'] = tuple([int(i) for i in pos.split(',')])
                robot['vel'] = tuple([int(i) for i in vel.split(',')])
                self.robots_start.append(robot)
        self.robots = [None] * len(self.robots_start)
    
    def moveRobot(self,robot,n_gen) -> dict:
        '''Given robot, calculate the end position after n_gen generations and return robot'''

        pos = robot['pos']
        vel = robot['vel']
        pos = ((pos[0] + n_gen* vel[0]) % (self.numcols), (pos[1] + n_gen * vel[1]) % (self.numrows))
        return {'pos':pos,'vel':vel}

    def incrementTime(self,n_gen):
        '''Reconfigured to use as setTime, generating positions from robots_start '''
        self.robots = [None] * len(self.robots_start)
        self.quadrant_counts = {(0,0):0,(0,1):0,(1,0):0,(1,1):0}
        for i, robot in enumerate(self.robots_start):
            self.robots[i] = self.moveRobot(robot,n_gen)
            
            # set quadrant after move
            xquad = (self.numcols // 2) + 1
            yquad = (self.numrows // 2) + 1
            pos = self.robots[i]['pos']
            # not in middle
            if pos[0] != xquad - 1 and pos[1] != yquad - 1:
                # print(pos, end=': ')
                quad = (pos[0] // xquad, pos[1] // yquad)
                self.quadrant_counts[quad] += 1
                # print(quad)
    
    def quadrantCheck(self):
        '''Force a reset and recount of current quadrant state'''
        # reset qc
        self.quadrant_counts = {(0,0):0,(0,1):0,(1,0):0,(1,1):0}

        xquad = (self.numcols // 2) + 1
        yquad = (self.numrows // 2) + 1
        
        for robot in self.robots:
            pos = robot['pos']
            # not in middle
            if pos[0] != xquad - 1 and pos[1] != yquad - 1:
                # print(pos, end=': ')
                quad = (pos[0] // xquad, pos[1] // yquad)
                self.quadrant_counts[quad] += 1
                # print(quad)

    def safetyScore(self) -> int:
        product = 1
        for value in a.quadrant_counts.values():
            product *= value
        return product

    def printGrid(self):
        grid_copy = copy.deepcopy(self.grid)
        for robot in self.robots:
            pos = robot['pos']
            grid_copy[pos[1]][pos[0]] = 'X'
        print('\n'.join([' '.join([str(cell) for cell in row]) for row in grid_copy]))
        print('\n')


testinput = {'filename':'testinput.txt','tall':7,'wide':11}
fullinput = {'filename':'input.txt','tall':103,'wide':101}

#######
#######

a = Puzzle(**fullinput)
a.incrementTime(6587)

# a.quadrantCheck()
a.printGrid()
product = a.safetyScore()
print(f"The safety value is: {product}")

#######
#######
# import matplotlib.pyplot as plt
# import numpy as np

# a = Puzzle(**fullinput)
# line_plot = []
# x = []
# for i in range(1000,10000):
#     x.append(i)
#     a.incrementTime(i)
#     line_plot.append(a.safetyScore())

# line_plot = np.array(line_plot)
# plt.plot(x, line_plot, linestyle = 'dotted')
# plt.savefig('safety_plot.png')
# plt.show()

# with open("values.txt", "w") as f:
#     f.write("")

# for i,val in enumerate(line_plot):
#     if val < 1.2e8:
#         with open("values.txt", "a") as f:
#             f.write(f"{x[i]}:\t {val}\n")
#             print(f"{x[i]}:\t {val}")
