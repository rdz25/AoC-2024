with open('input.txt') as file:
    stones = file.readline().split(' ')

def transformStone(stone: str) -> list[str]:
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


for i in range(25):
    print(f"Step {i+1}")
    blink_build = []
    for stone in stones:
        new_stones = transformStone(stone)
        for new_stone in new_stones:
            blink_build.append(new_stone)
    stones = blink_build

print(len(stones))