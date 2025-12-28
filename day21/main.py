import sys

sys.path.insert(0, "../")
from intcomp import IntComp

class SpringDroid:
    def __init__(self, program):
        self.comp = IntComp(program)

    def survey(self):
        instructions = []
        instructions.append("NOT A J")
        instructions.append("NOT B T")
        instructions.append("OR T J")
        instructions.append("NOT C T")
        instructions.append("OR T J")
        instructions.append("AND D J")
        instructions.append("WALK\n")
        inputs = [ord(ch) for ch in '\n'.join(instructions)]
        self.comp.add_input(inputs)
        dmg = 0
        while not self.comp.halted:
            out = self.comp.run()
            if out == 0:
                break
            dmg = out
        return dmg

    def run(self):
        instructions = []
        instructions.append("NOT B J")
        instructions.append("NOT C T")
        instructions.append("OR T J")
        instructions.append("NOT D T")
        instructions.append("OR T J")
        instructions.append("NOT E T")
        instructions.append("OR T J")
        instructions.append("NOT F T")
        instructions.append("OR T J")
        instructions.append("NOT G T")
        instructions.append("OR T J")
        instructions.append("NOT H T")
        instructions.append("OR T J")
        instructions.append("AND I J")
        instructions.append("RUN\n")
        inputs = [ord(ch) for ch in '\n'.join(instructions)]
        self.comp.add_input(inputs)
        dmg = 0
        while not self.comp.halted:
            out = self.comp.run()
            if out == 0:
                break
            dmg = out
        return dmg

def read_input(filename):
    with open(filename, 'r') as f:
        return [int(x.strip()) for x in f.read().split(',')]

def part1(program):
    droid = SpringDroid(program)
    return droid.survey()

def part2(program):
    droid = SpringDroid(program)
    return droid.run()

if __name__ == "__main__":
    program = read_input('input.txt')
    print(part1(program))
    print(part2(program))
