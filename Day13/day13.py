'''
Too slow to loop for anything big; would need to implement Extended Euclidean Algorithm for that
'''
claw_games = []
line = True
with open("testinput.txt") as f:
    while line != '':
        params = {}
        A = f.readline()
        B = f.readline()
        prize = f.readline()
        params['A'] = (int(A[A.index('X+')+2:A.index(',')]), int(A[A.index('Y+')+2:A.index('\n')]))
        params['B'] = (int(B[B.index('X+')+2:B.index(',')]), int(B[B.index('Y+')+2:B.index('\n')]))
        params['Prize'] = (int(prize[prize.index('X=')+2:prize.index(',')]), int(prize[prize.index('Y=')+2:prize.index('\n')]))
        claw_games.append(params)
        # dict['B': B.index(Y+)]
        line = f.readline()

def solveSystem(A: tuple[int, int], B: tuple[int, int], T: tuple[int, int]) -> list[tuple[int, int]]:
    soln_list = []
    for a in range(0,T[0] // A[0] + 1):
        # a*Ax + b*Bx = Tx; b = (Tx - a*Ax) / Bx
        if B[0] == 0:
            continue
        b = (T[0] - a * A[0]) / B[0]
        #b is integer and soln works for Y
        if b.is_integer() and a*A[1] + b*B[1] == T[1]:
            soln_list.append((a,int(b)))
    return soln_list
            
def minPrice(soln_list) -> int:
    if not soln_list:   # empty
        return 0
    curr_min = float('inf')
    for soln in soln_list:
        curr_min = min(3*soln[0] + soln[1], curr_min)
    return curr_min

cost = 0
for game in claw_games:
    # print(game['Prize'][0] // game['A'][0])
    soln_list = solveSystem(game['A'],game['B'],game['Prize'])
    if len(soln_list)>1:
        print(soln_list)
    cost += minPrice(soln_list)

print(cost)




