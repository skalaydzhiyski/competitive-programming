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

def get_all_adjacent_to(current_position):
    directions = [
        (current_position[0] - 1, current_position[1]    ),
        (current_position[0] + 1, current_position[1]    ),
        (current_position[0],     current_position[1] - 1),
        (current_position[0],     current_position[1] + 1)
    ]
    return [
        (x,y)
        for x,y in directions
        if 0 <= x <= 5
        and 0 <= y <= 5
    ]

def get_valid_moves_from(current_move):
    current_position, die, N, S = current_move
    adjacent = get_all_adjacent_to(current_position)
    valid = []
    for next_position in adjacent:
        direction = (
            next_position[0] - current_position[0],
            next_position[1] - current_position[1]
        )
        next_die_state = tip(die, direction)

        face_value = (grid[next_position] - S) / (N+1)
        if face_value % 1 != 0: # assume integers only
            continue

        face_value = str(int(face_value))
        if next_die_state[face] in unassigned_die_sides:
            next_die_state[face] = face_value
        if next_die_state[face] != face_value:
            continue

        valid.append(
            (next_position, next_die_state, N+1, grid[next_position])
        )
    return valid

def render(move, path):
    pos, die, N, S = move
    view = f'''
    pos={pos}, S={S}, N={N}
    ------------------------------------
    {die[0,:].tolist()}
    {die[1,:].tolist()}
    {die[2,:].tolist()}
    ------------------------------------
    {path[0,:].tolist()}
    {path[1,:].tolist()}
    {path[2,:].tolist()}
    {path[3,:].tolist()}
    {path[4,:].tolist()}
    {path[5,:].tolist()}
    ------------------------------------
    '''
    print(view)
    path[path == marker] = visited_marker


grid = np.array([
    [57,33,132,268,492,732],
    [81,123,240,443,353,508],
    [186,42,195,704,452,228],
    [-7,2,357,452,317,395],
    [5,23,-4,592,445,620],
    [0,77,32,403,337,452]
])
die = np.array([
    ['c','d','-'],
    ['e','a','f'],
    ['-','b','-'],
], dtype='<U3')
face, bottom = (1,1), (0,0)
left, right, up, down = (1,0), (1,2), (0,1), (2,1)
unassigned_die_sides = 'abcdef'

# only used for viz
path = grid.copy().astype(str)
marker, visited_marker = 'X', 'x'

N = S = 0
target = 732
current_position = (5,0)
to_visit = [(current_position, die, N, S)]

store = []

if __name__ == '__main__':
    while True:
        current_move = to_visit.pop()
        old_N = N
        current_position, die, N, S = current_move
        path = grid.copy().astype(str)
        for pos,n,_ ,_ in store:
            path[pos] = visited_marker
        path[current_position] = marker
        render(current_move, path)

        store.append((current_position, N, die, grid[current_position]))

        if old_N >= N:
            store = [s for s in store if s[1] <= N]
            to_remove = []
            for x in range(len(store)-1):
                if store[x][1] == store[x+1][1]:
                    to_remove.append(x)
            store = [s for i, s in enumerate(store) if i not in to_remove]

        if grid[current_position] == target:
            break

        valid_moves = get_valid_moves_from(current_move)
        if len(valid_moves) == 0:
            continue

        to_visit += valid_moves
        time.sleep(.1)

    non_visited = path[
        (path != marker) &
        (path != visited_marker)
    ].astype(int)
    result = non_visited.sum()
    print(result, non_visited)

    

