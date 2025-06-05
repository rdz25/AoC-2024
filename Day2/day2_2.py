def unsafeReport(report):
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
        elif i == 1:
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
    return i-1 if not safe else -1

safereport = 0
with open("input.txt") as f:
    for line in f:
        report = line.split()
        #if still safe, increment safe report counter  
        index = unsafeReport(report)
        if index == -1:  
            safereport += 1
        #unsafe, remove element and check
        #only need the index once, so it's inelegant to have a variable for the flag and the index each
        else:
            unsafe = index
            while unsafe != -1 and index >= 0:
                #check a copy while removing candidate
                copy = report[:index] + report[index + 1:]
                unsafe = unsafeReport(copy)
                index -= 1
            if unsafe == -1:
                safereport += 1


print(f"The number of safe reports is: {safereport}")