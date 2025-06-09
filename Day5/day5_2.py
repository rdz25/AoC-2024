from collections import defaultdict
rules = defaultdict(list)

with open("rules.txt") as file:
    for line in file:
        dep, page = line.replace('\n','').split('|')
        rules[page].append(dep)

def badUpdate(updates,rules) -> (int, int):
    seen = set()
    updates_set = set(updates)
    index = 0
    for update in updates:
        #check for dependencies on update
        # print("update:" + update)
        for dependency in rules[update]:
            #if both update and dependency are present, then dependency needs to be previously printed/seen\
            # print("dependency:" + dependency)
            if dependency in updates_set and dependency not in seen:
                dependencyindex = updates.index(dependency)
                return (index,dependencyindex)
        #pass check, add to set, move to next update
        seen.add(update)
        index += 1
    return (-1,None)

# def fixUpdates(updates, rules):


total = 0
with open("updates.txt") as file:
    for line in file:
        updates = line.replace('\n','').split(',')
        badindex = badUpdate(updates,rules)
        #incorrect
        if badindex != (-1,None):
            #fix
            while badindex != (-1,None):
                #Potential improvements: move dependency before bad index instead of swap; check for badUpdate starting from badindex instead of anew each time
                updatesfix = updates
                updatesfix[badindex[0]], updatesfix[badindex[1]] = updatesfix[badindex[1]], updatesfix[badindex[0]]
                badindex = badUpdate(updatesfix, rules)
            total += int(updatesfix[len(updatesfix)//2])

print(total)