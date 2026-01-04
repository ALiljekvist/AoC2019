import sys

sys.path.insert(0, "../")
from intcomp import IntComp

TURNS = {0: [(0,1), (0,-1)], 1: [(1,0), (-1,0)], 2: [(0,-1), (0,1)], 3: [(-1,0), (1,0)]}
NEXT = [(-1,0), (0,1), (1,0), (0,-1)]

class ScaffoldingRobot:
    def __init__(self, pos, dir, program):
        self.comp = IntComp(program)
        self.start = pos
        self.r = pos[0]
        self.c = pos[1]
        self.dir = dir

    def pos(self):
        return (self.r, self.c)

    def wake_up(self):
        self.comp.program[0] = 2
    
    def run(self, instructions):
        for instr in instructions:
            self.comp.add_input([ord(s) for s in instr])
        output = []
        out = self.comp.run()
        while out is not None and not self.comp.halted:
            output.append(out)
            out = self.comp.run()
        return output

    def walk(self, grid):
        walked = 0
        dr, dc = NEXT[self.dir]
        while (self.r+dr, self.c+dc) in grid:
            self.r += dr
            self.c += dc
            walked += 1
        return str(walked)

    def turn(self, grid):
        turns = TURNS[self.dir]
        if (self.r + turns[0][0], self.c+turns[0][1]) in grid:
            # print("Right:", self.dir, (self.dir + 1) % 4)
            self.dir = (self.dir + 1) % 4
            return 'R'
        if (self.r + turns[1][0], self.c+turns[1][1]) in grid:
            # print("Left:", self.dir, (self.dir - 1) % 4)
            self.dir = (self.dir - 1) % 4
            return 'L'
        return None

    def find_way(self, grid):
        # By printing the grid, it seemed as if there was a way
        # to only turn when you need to.
        moves = []
        walked = self.walk(grid)
        if walked != '0':
            moves.append(walked)
        turn = self.turn(grid)
        while turn is not None:
            moves.append(turn)
            walked = self.walk(grid)
            moves.append(walked)
            turn = self.turn(grid)
        return moves

def read_input(filename):
    with open(filename, 'r') as f:
        return [int(x.strip()) for x in f.read().split(',')]

def read_grid(comp):
    grid = []
    row = []
    while not comp.halted:
        out = comp.run()
        if out is None:
            continue
        match out:
            case 10:
                grid.append(row)
                row = []
            case _:
                row.append(chr(out))
    return grid

def transform_grid(grid, program):
    spots = {}
    droid = None
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            match val:
                case '#':
                    spots[(r,c)] = 1
                case '^':
                    droid = ScaffoldingRobot((r,c), 0, program)
                    spots[(r,c)] = 1
                case '>':
                    droid = ScaffoldingRobot((r,c), 1, program)
                    spots[(r,c)] = 1
                case 'v':
                    droid = ScaffoldingRobot((r,c), 2, program)
                    spots[(r,c)] = 1
                case '<':
                    droid = ScaffoldingRobot((r,c), 3, program)
                    spots[(r,c)] = 1
    return spots, droid

def part1(program):
    comp = IntComp(program)
    grid = read_grid(comp)
    grid, droid = transform_grid(grid, program)
    alignment = 0
    for (r, c) in grid.keys():
        if sum([1 if (r+dr, c+dc) in grid else 0 for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]]) == 4:
            alignment += r * c
    return grid, droid, alignment

def print_grid(grid, droid):
    for r in range(max([ri for (ri, _) in grid.keys()])+1):
        row = ''
        for c in range(max([ci for (_, ci) in grid.keys()])+1):
            if (r,c) in grid:
                if (r,c) == droid.pos():
                    row += ['^', '>', 'v', '<'][droid.dir]
                    continue
                row += '#'
                continue
            row += '.'
        print(row)

def split_into_parts(path, parts):
    if len(parts) > 3:
        return False
    if len(path) == 0:
        return True
    l = 2
    while len(','.join(path[:l])) <= 20 and l < len(path):
        mod_path = path.copy()
        window = mod_path[:l]
        i = 0
        while i < len(mod_path) - l + 1:
            matches = True
            for j in range(l):
                if mod_path[i+j] != window[j]:
                    matches = False
                    break
            if matches:
                for _ in range(l):
                    mod_path.pop(i)
            else:
                i += 1
        parts.append(window)
        if split_into_parts(mod_path, parts):
            return True
        parts.pop()
        l += 1
    return False

def find_order(path, parts):
    order = []
    joined_path = ''.join(path)
    joined_parts = [''.join(p) for p in parts]
    while joined_path:
        for i, p in enumerate(joined_parts):
            if joined_path.startswith(p):
                match i:
                    case 0:
                        order.append('A')
                    case 1:
                        order.append('B')
                    case 2:
                        order.append('C')
                joined_path = joined_path[len(p):]
                break
    return order

def part2(grid, droid: ScaffoldingRobot):
    droid.wake_up()
    path = droid.find_way(grid)
    # Split the path into sub-parts
    parts = []
    if not split_into_parts(path, parts):
        return "FAILED to split into parts"
    # Figure out the order of the parts
    order = find_order(path, parts)
    instructions = []
    instructions.append(','.join(order)+'\n')
    for part in parts:
        instructions.append(','.join(part)+'\n')
    instructions.append("n\n")
    return droid.run(instructions)

if __name__ == "__main__":
    program = read_input('input.txt')
    grid, droid, p1 = part1(program)
    print(p1)
    p2 = part2(grid, droid)
    debug = False
    if len(p2) > 1 and debug:
        grid = ''.join([chr(p) for p in p2])
        print(grid[:-1])
    print(p2[-1])

