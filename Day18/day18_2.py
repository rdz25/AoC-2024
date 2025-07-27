import heapq as hq

class Puzzle:
    def __init__(self, file, xmax, ymax, num_bytes):
        self.ymax = ymax
        self.xmax = xmax
        self.grid = []
        # start position
        self.start = (0,0)
        # end position
        self.end = (xmax,ymax)
        # build grid
        self.obstacles = set()
        self.loadObstacles(file, num_bytes)

    def loadObstacles(self, file: str, num_bytes: int):
        with open(file) as file:
            for i in range(num_bytes):
                line = file.readline()
                processed_line = line.replace('\n','')
                x, y = [int(x) for x in processed_line.split(',')]
                self.obstacles.add((x,y))
    
    def validPos(self, pos):
        x, y = pos
        if 0 <= x <= self.xmax and 0 <= y <= self.ymax and pos not in self.obstacles:
            return True
        else:
            return False

    def pathDjikstra(self):
        pos = self.start
        heap = []
        hq.heappush(heap, (0, pos))
        seen = set(pos)
        while heap:
            score, pos = hq.heappop(heap)
            # print(pos, len(heap))            
            if pos == self.end:
                return score
            # move
            for direction in {(1,0),(-1,0),(0,1),(0,-1)}:
                new_pos = (pos[0] + direction[0], pos[1] + direction[1])
                if self.validPos(new_pos) and new_pos not in seen:
                    seen.add(new_pos)
                    hq.heappush(heap,(score + 1, new_pos)) 


input = {'file':'input.txt','xmax':70,'ymax':70,'num_bytes':1024}
testinput = {'file':'testinput.txt','xmax':6,'ymax':6,'num_bytes':25}
a = Puzzle(**testinput)
# print(a.obstacles)
# TODO solves but there are more optimal way to iterate num_bytes; could binary search num_bytes range; could also run a connection/pathing algo on the obstacles
for i in range(1025,3450):
    input = {'file':'input.txt','xmax':70,'ymax':70,'num_bytes':i}
    a = Puzzle(**input)
    if a.pathDjikstra() is None:
        print(i)
        break
