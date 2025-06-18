with open('input.txt') as file:
    stones = file.readline().split(' ')

print(stones)

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

cache = {}

def countStones(stone: str, blinks_remaining: int):
    # print(f"\t Blinks remaining: {blinks_remaining}")
    if blinks_remaining == 0:
        return 1
    else:
        if (stone, blinks_remaining) in cache:
            # use cached number
            return cache[(stone,blinks_remaining)]
        else:
            new_stones = transformStone(stone)
            # count for the original stone
            stone_count = 0
            for new_stone in new_stones:
                stone_count += countStones(new_stone, blinks_remaining - 1)
            cache[stone,blinks_remaining] = stone_count
            return stone_count

sum = 0
for stone in stones:
    # print(f"Stone: {stone}")
    sum += countStones(stone, 75)
print(f"The number of stones is: {sum}")
print(f"Cache size: {len(cache)}")