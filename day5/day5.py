import sys

sys.path.insert(0, "../")
from intcomp import IntComp

def read_input(filename):
    with open(filename, 'r') as f:
        return [int(x.strip()) for x in f.read().split(',')]

def part1(program):
    comp = IntComp(program, [1])
    return comp.run(continue_on_zero=True)

def part2(program):
    comp = IntComp(program, [5])
    return comp.run()

if __name__ == '__main__':
    program = read_input('input.txt')
    print(part1(program.copy()))
    print(part2(program))
