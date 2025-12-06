import sys

sys.path.insert(0, "../")
from intcomp import IntComp

def read_input(filename):
    with open(filename, 'r') as f:
        return [int(x.strip()) for x in f.read().split(',')]

if __name__ == "__main__":
    program = read_input('input.txt')
    print(IntComp(program, inputs=[1]).run_until_halted())
    print(IntComp(program, inputs=[2]).run_until_halted())