'''
Annoying handling of floating point precision and exact integer solutions but is fast without using the Extended Euclidean Algorithm
'''
import numpy as np

claw_games = []
line = True
with open("input.txt") as f:
    while line != '':
        params = {}
        A = f.readline()
        B = f.readline()
        prize = f.readline()
        params['A'] = (int(A[A.index('X+')+2:A.index(',')]), int(A[A.index('Y+')+2:A.index('\n')]))
        params['B'] = (int(B[B.index('X+')+2:B.index(',')]), int(B[B.index('Y+')+2:B.index('\n')]))
        # Part 2: 10000000000000 +
        modifier = 10000000000000
        params['Prize'] = (modifier + int(prize[prize.index('X=')+2:prize.index(',')]), modifier + int(prize[prize.index('Y=')+2:prize.index('\n')]))
        claw_games.append(params)
        # dict['B': B.index(Y+)]
        line = f.readline()

# print(claw_games[0]['Prize'] == (10000000008400,10000000005400))

cost = 0
for game in claw_games:
    a = np.array([  [game['A'][0], game['B'][0]],
                    [game['A'][1], game['B'][1]]
                ])
    b = np.array(game['Prize'])
    solution = np.linalg.solve(a,b)
    solution_int = [int(round(x)) for x in solution]
    # print(abs(solution-solution_int))
    if np.isclose(solution, solution_int, rtol=0, atol=1e-3).all():
        if all(x >= 0 for x in solution_int):
            cost += solution[0]*3 + solution[1]

print(int(cost))
