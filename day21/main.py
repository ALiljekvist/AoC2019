import sys

sys.path.insert(0, "../")
from intcomp import IntComp

class SpringDroid:
    def __init__(self, program):
        self.comp = IntComp(program)

    def run(self, instructions):
        inputs = [ord(ch) for ch in '\n'.join(instructions)]
        self.comp.add_input(inputs)
        dmg = 0
        hist = []
        while not self.comp.halted:
            out = self.comp.run()
            if out is None:
                break
            hist.append(out)
            dmg = out
        if dmg == 10:
            print(''.join([chr(out) for out in hist[:-1]]))
        return dmg

def read_input(filename):
    with open(filename, 'r') as f:
        return [int(x.strip()) for x in f.read().split(',')]

def part1(program):
    instructions = []
    instructions.append("NOT A J")
    instructions.append("NOT B T")
    instructions.append("OR T J")
    instructions.append("NOT C T")
    instructions.append("OR T J")
    instructions.append("AND D J")
    instructions.append("WALK\n")
    droid = SpringDroid(program)
    return droid.run(instructions)

def part2(program):
    droid = SpringDroid(program)
    instructions = []
    instructions.append("NOT A J")
    instructions.append("NOT B T")
    instructions.append("OR T J")
    instructions.append("NOT C T")
    instructions.append("OR T J")
    instructions.append("AND D J")
    instructions.append("NOT E T")
    instructions.append("AND E T")
    instructions.append("OR E T")
    instructions.append("OR H T")
    instructions.append("AND T J")
    instructions.append("RUN\n")
    return droid.run(instructions)

if __name__ == "__main__":
    program = read_input('input.txt')
    print(part1(program))
    print(part2(program))
