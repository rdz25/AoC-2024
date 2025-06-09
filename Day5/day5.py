from collections import defaultdict
rules = defaultdict(list)

with open("rules.txt") as file:
    for line in file:
        dep, page = line.replace('\n','').split('|')
        rules[page].append(dep)

def validUpdates(updates,rules):
    seen = set()
    updates_set = set(updates)
    for update in updates:
        #check for dependencies on update
        # print("update:" + update)
        for dependency in rules[update]:
            #if both update and dependency are present, then dependency needs to be previously printed/seen\
            # print("dependency:" + dependency)
            if dependency in updates_set and dependency not in seen:
                return False
        #pass check, add to set, move to next update
        seen.add(update)
    return True

total = 0
with open("updates.txt") as file:
    for line in file:
        updates = line.replace('\n','').split(',')
        if validUpdates(updates,rules):
            total += int(updates[len(updates)//2])

print(total)