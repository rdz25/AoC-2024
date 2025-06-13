def backtrackOperations(left,equation):
    if left == test and len(equation) == 0:
        return True
    elif left > test or len(equation) == 0:    # cannot equal test value
        return False
    else:   # left < test and len(equation) > 0:
        # newleft = eval(str(left) + op + str(equation[0]))
        return backtrackOperations(left + equation[0],equation[1:]) or backtrackOperations(left * equation[0],equation[1:]) or backtrackOperations(int(str(left) + str(equation[0])),equation[1:])
  
sum = 0
with open("input.txt") as file:
    for line in file:
        line = line.replace('\n','')
        test, equation = line.split(': ')
        test = int(test)
        equation_str = equation.split(' ')
        equation = []
        for number in equation_str:
            equation.append(int(number))
        if backtrackOperations(equation[0],equation[1:]):
            sum += test

print(f"Test sum is: {sum}")
