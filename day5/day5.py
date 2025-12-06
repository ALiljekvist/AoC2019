import sys

sys.path.insert(0, "../")
from intcomp import run

def read_input(filename):
    with open(filename, 'r') as f:
        return [int(x.strip()) for x in f.read().split(',')]

def part1(program):
    return run(program, 1, continue_on_zero=True)

def part2(program):
    return run(program, 5)

if __name__ == '__main__':
    program = read_input('input.txt')
    print(part1(program.copy()))
    # ex = [3,9,8,9,10,9,4,9,99,-1,8]
    # print(run(ex, 8) == 1)
    # print(run(ex, 0) == 0)
    # ex = [3,9,7,9,10,9,4,9,99,-1,8]
    # print(run(ex, 7) == 1)
    # print(run(ex, 8) == 0)
    # ex = [3,3,1108,-1,8,3,4,3,99]
    # print(run(ex, 8) == 1)
    # print(run(ex, 0) == 0)
    # ex = [3,3,1107,-1,8,3,4,3,99]
    # print(run(ex, 7) == 1)
    # print(run(ex, 8) == 0)
    # ex = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
    # print(run(ex, 0) == 1)
    # print(run(ex, 8) == 0)
    # ex = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
    # print(run(ex, 0) == 1)
    # print(run(ex, 8) == 0)
    print(part2(program))
