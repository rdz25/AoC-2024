safereport = 0
with open("input.txt") as f:
    for line in f:
        report = line.split()

        #each line is a report with levels as elements
        prevlevel = None
        prevdirection = None
        safe = True
        i = 0
        while safe and i < len(report):
            level = int(report[i])
            #check for direction and diff starting at i = 2
            if i >= 2:
                diff = level - prevlevel
                if 1 <= abs(diff) <= 3 and prevdirection ^ diff >= 0:
                    #still safe
                    prevlevel = level
                    prevdirection = diff
                else:
                    safe = False
            #check for diff starting at i = 1
            if i == 1:
                diff = level - prevlevel
                if 1 <= abs(diff) <= 3:
                    #still safe
                    prevdirection = diff
                    prevlevel = level
                else:
                    safe = False
            #first report
            else:
                prevlevel = int(report[i])
            i += 1
        #if still safe, increment safe report counter  
        if safe:  
            safereport += 1

print(f"The number of safe reports is: {safereport}")