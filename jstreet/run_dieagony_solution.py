import numpy as np
import time

def swap(die, x, y):
    die[x], die[y] = die[y], die[x]

def tip(die, direction):
    res = die.copy()
    if direction == (0, -1):
        swap(res, left, bottom)
        swap(res, face, left)
        swap(res, face, right)
    elif direction == (0, 1):
        swap(res, right, bottom)
        swap(res, face, right)
        swap(res, face, left)
    elif direction == (-1, 0):
        swap(res, up, bottom)
        swap(res, face, up)
        swap(res, face, down)
    elif direction == (1,0):
        swap(res, down, bottom)
        swap(res, face, down)
        swap(res, face, up)
    return res

def get_adjacent(pos):
    directions = [
        (pos[0] - 1, pos[1]    ),
        (pos[0] + 1, pos[1]    ),
        (pos[0],     pos[1] - 1),
        (pos[0],     pos[1] + 1)
    ]
    return [
        (x,y)
        for x,y in directions
        if 0 <= x <= 5
        and 0 <= y <= 5
    ]

def is_valid_next_step(next_position, next_die_state, N, S):
    face_value = (grid[next_position] - S) / (N+1)
    if face_value % 1 != 0:
        return False
    face_value = str(int(face_value))
    return next_die_state[face] in die_vars\
        or next_die_state[face] == face_value

def get_valid_moves_from(current_pos, die, N, S):
    adjacent = get_adjacent(current_pos)
    valid = []
    for next_position in adjacent:
        direction = (next_position[0] - current_pos[0], next_position[1] - current_pos[1])
        next_die_state = tip(die, direction)
        if not is_valid_next_step(next_position, next_die_state, N, S):
            continue
        valid.append(
            (next_position, next_die_state, grid[next_position], N+1)
        )
    return valid


move_mapping = {
    'u': (-1,0),
    'd': (1,0),
    'l': (0,-1),
    'r': (1,1),
}

die_vars = 'abcdef'
die = np.array([
    ['c','d','-'],
    ['e','a','f'],
    ['-','b','-'],
], dtype='<U3')
face, bottom          = (1,1), (0,0)
left, right, up, down = (1,0), (1,2), (0,1), (2,1)

grid = np.array([
    [57,33,132,268,492,732],
    [81,123,240,443,353,508],
    [186,42,195,704,452,228],
    [-7,2,357,452,317,395],
    [5,23,-4,592,445,620],
    [0,77,32,403,337,452]
])
path = grid.copy().astype(str) # only used for visualisation
current_pos = (5,0)
target = 732
N = 0
S = grid[current_pos]
to_visit = [(current_pos, die, N, S)]

while grid[current_pos] != target:
    #print(current_pos, S, N)
    #print(die)
    #print(path)
    #print(grid[current_pos])
    current_move = to_visit.pop()
    valid_moves = get_valid_moves_from(*current_move)

    if len(valid_moves) == 0:
        # continue
        pass
    elif len(valid_moves) == 1:
        # make the move
        pass
    else: # more than one valid move
        # push all to the stack
        print('something')
        pass

  

