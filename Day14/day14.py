from collections import defaultdict
import copy

class Puzzle:
    def __init__(self, filename, tall, wide):
        self.numrows = tall
        self.numcols = wide
        self.grid = []
        for i in range(self.numrows):
            self.grid.append([0]*self.numcols)
        self.robots = []
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
                self.robots.append(robot)
    
    def moveRobot(self,robot) -> dict:
        pos = robot['pos']
        vel = robot['vel']
        pos = ((pos[0] + vel[0]) % (self.numcols), (pos[1] + vel[1]) % (self.numrows))
        return {'pos':pos,'vel':vel}

    def incrementTime(self):
        for i, robot in enumerate(self.robots):
            self.robots[i] = self.moveRobot(robot)
    
    def quadrantCheck(self):
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

    def quadrantRobot(self, robot):
        xquad = (self.numcols // 2) + 1
        yquad = (self.numrows // 2) + 1
        
        pos = robot['pos']
        print(self.numcols,self.numrows)
        print(xquad,yquad)
        # not in middle
        if pos[0] != xquad - 1 and pos[1] != yquad - 1:
            print(pos, end=': ')
            quad = (pos[0] // xquad, pos[1] // yquad)
            print(quad)

#######
#######

# a = Puzzle('testinput2.txt', 7, 11)

# print(a.robots[0])
# out = a.robots[0]
# for i in range(5):
#     out = a.moveRobot(out)
# print(out)


#######
#######
# a = Puzzle('testinput2.txt', 7, 11)

# for i in range(5):
#     a.incrementTime()

# print(a.robots)
# a.quadrantCheck()   #lands in mid
# print(a.quadrant_counts)
# # robot = a.robots[0]
# # a.quadrantRobot(robot)

#######
#######
# a = Puzzle('testinput.txt', 7, 11)

# for i in range(100):
#     a.incrementTime()

# a.quadrantCheck()
# test_output = {(0, 0): 1, (1, 0): 3, (0, 1): 4, (1, 1): 1}
# print(a.quadrant_counts)
# print(a.quadrant_counts == test_output)

# product = 1
# for value in a.quadrant_counts.values():
#     product *= value
# print(f"The safety value is: {product}")

#######
#######
a = Puzzle('input.txt', tall=103, wide=101)
for i in range(10000):
    a.incrementTime()

a.quadrantCheck()
product = 1
for value in a.quadrant_counts.values():
    product *= value
print(f"The safety value is: {product}")