import sys

sys.path.insert(0, "../")
from intcomp import IntComp

def create_combinations(size):
    if size == 1:
        return [[1], [0]]
    combinations = []
    sub_combs = create_combinations(size-1)
    for comb in sub_combs:
        new_comb = comb.copy()
        new_comb.append(1)
        comb.append(0)
        combinations.append(new_comb)
        combinations.append(comb)
    return combinations

class SmallDroid:
    def __init__(self, program):
        self.comp = IntComp(program)
        self.inputs = []
    
    def run(self):
        out = ''
        while not self.comp.halted:
            new_out = self.comp.run()
            try:
                out += chr(new_out)
            except:
                print(new_out)
            if out.endswith('Command?'):
                break
        return out

    def add_input(self, new_input):
        if new_input[-1] != '\n':
            new_input += '\n'
        self.inputs.extend([ord(c) for c in new_input])
    
    def give_input(self):
        return self.inputs.pop(0)

    def try_all_combinations(self):
        self.add_input('inv')
        output = self.run()
        items = [x[2:] for x in output.split('\n') if '-' in x]
        combinations = create_combinations(len(items))
        output = 'heavier'
        for comb in combinations:
            # Drop any item that should not be held in this attempt
            to_remove = [items[i] for i, keep in enumerate(comb) if not keep]
            for item in to_remove:
                self.drop(item)
            # Try to go through the identification
            self.add_input('west')
            output = self.run()
            if 'Alert!' not in output:
                # Seems like this was succesful, break
                break
            # Pick up the items again
            for item in to_remove:
                self.pickup(item)
        return output

    def drop(self, item):
        self.add_input(f"drop {item}")
        self.run()

    def pickup(self, item):
        self.add_input(f"take {item}")
        self.run()

def read_input(filename):
    with open(filename, 'r') as f:
        return [int(x.strip()) for x in f.read().split(',')]

def part1(program):
    droid = SmallDroid(program)
    droid.comp.input_func = droid.give_input
    while not droid.comp.halted:
        output = droid.run()
        print(output)
        new_input = input()
        if new_input == 'try all':
            output = droid.try_all_combinations()
            return output
        droid.add_input(new_input)

if __name__ == "__main__":
    program = read_input('input.txt')
    print(part1(program))
