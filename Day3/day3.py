import re
with open("input.txt") as file:
    text = file.read()

muls = re.findall(r"mul\([0-9]+,[0-9]+\)", text)
total = 0
for mul in muls:
    string = mul[4:len(mul)-1]
    numbers = string.split(',')
    total += int(numbers[0]) * int(numbers[1])

print(f"The sum of all multiplications is: {total}")
