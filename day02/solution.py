# f = open('test.txt') 
f = open('input.txt')

lines = f.readlines()
games = [line.split() for line in lines]

score = 0

'''
A -> Rock       0 
B -> Paper      1
C -> Scissors   2

X -> Rock
Y -> Paper
Z -> Scissors
'''

values = {
    'A': 0,
    'B': 1,
    'C': 2,
    'X': 0,
    'Y': 1,
    'Z': 2
}

LOST = 0
DRAW = 3
WIN = 6

for game in games:
    move1 = game[0]
    move2 = game[1]

    diff = values[move1] - values[move2]
    score += values[move2] + 1
    if diff == 0:
        score += DRAW 
    elif diff == 1 or diff == -2:
        score += LOST
    else:
        score += WIN

print(score)

'''
X means you need to lose,
Y means you need to end the round in a draw,
Z means you need to win
'''

score = 0

for game in games:
    move = game[0]
    result = game[1]

    if result == 'X':
        my_move = (values[move] - 1)%3
        score += LOST + my_move + 1
    elif result == 'Y':
        my_move = values[move]
        score += DRAW + my_move + 1
    else:
        my_move = (values[move] + 1)%3
        score += WIN + my_move + 1

print(score)