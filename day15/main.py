import sys

sys.path.insert(0, "../")
from intcomp import IntComp

class RepairDroid:
    def __init__(self, program):
        self.comp = IntComp(program)
        self.x = 0
        self.y = 0
        self.steps = 0
    
    def pos(self):
        return (self.x, self.y)

    def move(self, dir):
        self.comp.add_input([dir])
        res = self.comp.run()
        if res != 0:
            match dir:
                case 1:
                    self.y += 1
                case 2:
                    self.y -= 1
                case 3:
                    self.x += 1
                case 4:
                    self.x -= 1
            self.steps += 1
        return res

    def copy(self):
        new_droid = RepairDroid([])
        new_droid.comp = self.comp.copy()
        new_droid.x = self.x
        new_droid.y = self.y
        new_droid.steps = self.steps
        return new_droid

def read_input(filename):
    with open(filename, 'r') as f:
        return [int(x.strip()) for x in f.read().split(',')]

def find_shortest_distance(droid):
    checked = set(droid.pos())
    queue = [droid]
    while queue:
        curr = queue.pop(0)
        for dir in [1, 2, 3, 4]:
            new_droid = curr.copy()
            res = new_droid.move(dir)
            if res == 2:
                return new_droid
            if res == 0:
                continue
            new_pos = new_droid.pos()
            if new_pos in checked:
                continue
            checked.add(new_pos)
            queue.append(new_droid)
    return None

def part1(program):
    droid = RepairDroid(program)
    final_droid = find_shortest_distance(droid)
    return final_droid

def fill_area(droid):
    checked = set(droid.pos())
    queue = [droid]
    while queue:
        curr = queue.pop(0)
        for dir in [1, 2, 3, 4]:
            new_droid = curr.copy()
            res = new_droid.move(dir)
            if res != 1:
                continue
            new_pos = new_droid.pos()
            if new_pos in checked:
                continue
            checked.add(new_pos)
            queue.append(new_droid)
    return curr.steps

def part2(droid):
    droid.steps = 0
    return fill_area(droid)

if __name__ == "__main__":
    program = read_input('input.txt')
    droid = part1(program)
    print(droid.steps)
    print(part2(droid))