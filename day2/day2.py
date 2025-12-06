import sys

sys.path.insert(0, "../")
from intcomp import run

def read_input(filename):
    with open(filename, 'r') as f:
        return [int(x) for x in f.read().split(',')]

def part1(program):
    program[1] = 12
    program[2] = 2
    run(program)
    return program[0]

def part2(program):
    for i in range(100):
        for j in range(100):
            test_program = program.copy()
            test_program[1] = i
            test_program[2] = j
            run(test_program)
            if test_program[0] == 19690720:
                return 100*i + j
    return -1

if __name__ == '__main__':
    program = read_input('input.txt')
    print(part1(program.copy()))
    print(part2(program))
