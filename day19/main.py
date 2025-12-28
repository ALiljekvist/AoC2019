import sys

sys.path.insert(0, "../")
from intcomp import IntComp

def read_input(filename):
    with open(filename, 'r') as f:
        return [int(x.strip()) for x in f.read().split(',')]

def calc_grid(program, size=50):
    grid = []
    for y in range(size):
        row = []
        for x in range(size):
            comp = IntComp(program)
            comp.add_input([x, y])
            row.append(comp.run())
        grid.append(row)
    return grid

def part1(program):
    return calc_grid(program)

def print_grid(grid):
    for row in grid:
        print(''.join(['#' if c == 1 else '.' for c in row]))

def walk_line_until_square(program, x, y):
    res = 1
    while True:
        if res == 1:
            x += 1
        else:
            y += 1
        res = IntComp(program, inputs=([x, y])).run()
        if res == 1:
            dx = x-99
            if dx < 0:
                continue
            dy = y+99
            if IntComp(program, inputs=([dx, dy])).run() == 1:
                return dx, y

def part2(program, grid):
    y = len(grid)-1
    x = max([i for i, x in enumerate(grid[y]) if x == 1])
    lx, ly = walk_line_until_square(program, x, y)
    return lx * 10000 + ly

if __name__ == "__main__":
    program = read_input('input.txt')
    grid = part1(program)
    print(sum([sum(row) for row in grid]))
    print(part2(program, grid))

