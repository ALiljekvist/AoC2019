import sys

sys.path.insert(0, "../")
from intcomp import IntComp

class ScaffoldingRobot:
    def __init__(self):
        return

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
            case 35:
                row.append(1)
            case 46:
                row.append(0)
            case 10:
                grid.append(row)
                row = []
            case _:
                match chr(out):
                    case '^':
                        row.append(2)
                    case '>':
                        row.append(3)
                    case 'v':
                        row.append(4)
                    case '<':
                        row.append(5)
    return grid

def part1(program):
    comp = IntComp(program)
    grid = read_grid(comp)
    alignment = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                continue
            part_sum = 0
            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                try:
                    part_sum += 1 if grid[i+di][j+dj] == 1 else 0
                except:
                    pass
            if part_sum == 4:
                alignment += i * j
    return grid, alignment

def print_grid(grid):
    for row in grid:
        chrs = []
        for c in row:
            match c:
                case 1:
                    chrs.append('#')
                case 0:
                    chrs.append('.')
                case 2:
                    chrs.append('^')
                case 3:
                    chrs.append('>')
                case 4:
                    chrs.append('v')
                case 5:
                    chrs.append('<')
        print(''.join(chrs))

def part2(program, grid):
    program[0] = 2
    comp = IntComp(program)
    print_grid(grid)
    return

if __name__ == "__main__":
    program = read_input('input.txt')
    grid, p1 = part1(program)
    print(p1)
    part2(program, grid)