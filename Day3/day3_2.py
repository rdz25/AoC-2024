import re
with open("input.txt") as file:
    text = file.read()

muls = re.finditer(r"mul\([0-9]+,[0-9]+\)", text)
dos = re.finditer(r"do\(\)", text)
donts = re.finditer(r"don\'t\(\)", text)

do_indices = []
for do in dos:
    do_index = do.start()
    do_indices.append(do_index)

dont_indices = []
for dont in donts:
    dont_index = dont.start()
    dont_indices.append(dont_index)


def prevdodont(mul_index: int, dodont: list[int]) -> int:
    '''iterate and find previous index of do/dont. Could be improved not to start from the beginning each time; using a queue/deque maybe'''
    prev = -1
    for i in dodont:
        if i < mul_index:
            prev = i
        else:
            #bigger (can't be equal)
            return prev
    return prev


total = 0
for mul in muls:
    do_index = prevdodont(mul.start(),do_indices)
    dont_index = prevdodont(mul.start(),dont_indices)
    if do_index >= dont_index:
        # print(mul.group(0))
        string = mul.group(0)[4:len(mul.group(0))-1]
        numbers = string.split(',')
        total += int(numbers[0]) * int(numbers[1])
        
print(f"The sum of all multiplications is: {total}")
