import numpy as np
import time

class State:
    def __init__(self, pos, die, visited, N):
        self.pos = pos
        self.die = die
        self.visited = visited
        self.neighbours = self._get_neighbour_positions()
        self.S = grid[self.pos]
        self.N = N

    def visit(self):
        self.visited[self.pos] = True

    def make_state_for_neighbour(self, npos):
        direction = (
            npos[0] - self.pos[0],
            npos[1] - self.pos[1]
        )
        next_die = self.tip(direction)
        next_visited = self.visited.copy();
        next_visited[npos] = True
        return State(npos, next_die, next_visited, self.N + 1)

    def tip(self, direction):
        res = self.die.copy()
        if direction == (0, -1):
            self._swap(res, left, bottom)
            self._swap(res, face, left)
            self._swap(res, face, right)
        elif direction == (0, 1):
            self._swap(res, right, bottom)
            self._swap(res, face, right)
            self._swap(res, face, left)
        elif direction == (-1, 0):
            self._swap(res, up, bottom)
            self._swap(res, face, up)
            self._swap(res, face, down)
        elif direction == (1,0):
            self._swap(res, down, bottom)
            self._swap(res, face, down)
            self._swap(res, face, up)
        return res

    def _get_neighbour_positions(self):
        return [
            (x,y)
            for x,y in [ # neighbours
                (self.pos[0] - 1, self.pos[1]    ),
                (self.pos[0] + 1, self.pos[1]    ),
                (self.pos[0],     self.pos[1] - 1),
                (self.pos[0],     self.pos[1] + 1)
            ]
            if 0 <= x <= 5
            and 0 <= y <= 5
        ]

    def _swap(self, die, x, y):
        die[x], die[y] = die[y], die[x]

    def __repr__(self):
        # slow but pretty
        nvalues = [grid[pos] for pos in self.neighbours]
        view = f'''
        pos={self.pos}, S={self.S}, N={self.N}, neighbours={nvalues}
        ------------------------------------
        {self.visited[0,:].tolist()} | {self.die[0,:].tolist()}
        {self.visited[1,:].tolist()} | {self.die[1,:].tolist()}
        {self.visited[2,:].tolist()} | {self.die[2,:].tolist()}
        {self.visited[3,:].tolist()} | 
        {self.visited[4,:].tolist()} | 
        {self.visited[5,:].tolist()} | 
        '''
        view = '\n'.join(map(str.strip, view.split('\n')))
        return view



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
pos = (5,0)
target = 732
N = 0
S = 0

visited = grid.copy()
visited.fill(False)

current = State(pos, die, visited, N)
to_visit = [current] # stack of states

counter = 0
while grid[current.pos] != target:
    current = to_visit[-1]
    current.visit()

    print('-'*50)
    print(f'to_visit = {[s.S for s in to_visit]}')
    print(f'counter = {counter}'); counter += 1
    print(current)
    time.sleep(.5)

    if len(current.neighbours) == 0:
        _ = to_visit.pop()
        continue

    while len(current.neighbours) > 0:
        neighbour = current.neighbours.pop()
        nstate = current.make_state_for_neighbour(neighbour)
        if not current.visited[neighbour]:
            face_value = (nstate.S - current.S) / nstate.N
            if face_value % 1 != 0:
                continue
            else:
                face_value = str(face_value).split('.')[0]
            if not nstate.die[face] in die_vars:
                value = nstate.die[face]
                if value != face_value: continue
            else:
                nstate.die[face] = face_value
            to_visit.append(nstate)





