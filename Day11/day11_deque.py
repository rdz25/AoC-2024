from collections import deque

BLINKS = 75
FILENAME = 'testinput.txt'

with open(FILENAME) as file:
    stones = file.readline().split(' ')

stones = deque(stones)
stones.append('EOF')

def transformStone(stone: str) -> list[str]:
    '''Contains rules for transforming or splitting a stone at each step'''
    if stone == '0':
        return ['1']
    elif len(stone) % 2 == 0:
        halfway = len(stone)//2
        left = stone[0:halfway]
        right = stone[halfway:].lstrip('0')
        if right == '':
            right = '0'
        return [left, right]
    else:
        return [str(int(stone) * 2024)]

# (stone, blink) : num_stones
cache = {}

for i in range(1,1+BLINKS):
    stone = stones.popleft()
    while stone != 'EOF':
        values = transformStone(stone)
        for value in values:
            stones.append(value)
        stone = stones.popleft()
    #append the EOF back to the end
    stones.append(stone)
    print(f'Step {i}')
    print(len(stones)-1)
