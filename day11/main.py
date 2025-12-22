import sys

sys.path.insert(0, "../")
from intcomp import IntComp

def read_input(filename):
    with open(filename, 'r') as f:
        return [int(x.strip()) for x in f.read().split(',')]

class HullPainter:
    def __init__(self, program: list[int], starting_color=0):
        self.comp = IntComp(program)
        self.hull = {(0,0): starting_color}
        self.x, self.y = 0, 0
        self.dir = 0
    
    def run(self):
        while not self.comp.halted:
            self.paint_and_move()

    def paint_and_move(self):
        pos = (self.x, self.y)
        self.comp.add_input([self.hull.get(pos, 0)])
        paint_as_color = self.comp.run()
        turn = self.comp.run()
        self.hull[pos] = paint_as_color
        self.turn_and_move(turn)

    def turn_and_move(self, turn):
        if turn == 0:
            self.dir = (self.dir-1 + 4) % 4
        else:
            self.dir = (self.dir + 1) % 4
        self.move()

    def move(self):
        if self.dir == 0:
            self.y -= 1
        elif self.dir == 1:
            self.x += 1
        elif self.dir == 2:
            self.y += 1
        else:
            self.x -= 1

    def visualize_hull(self):
        xs = [p[0] for p in robot.hull.keys()]
        ys = [p[1] for p in robot.hull.keys()]
        for y in range(min(ys), max(ys)+1):
            row = []
            for x in range(min(xs), max(xs) + 1):
                row.append(robot.hull.get((x, y), 0))
            print(''.join(['#' if c == 1 else " " for c in row]))

if __name__ == "__main__":
    program = read_input('input.txt')
    robot = HullPainter(program)
    robot.run()
    print(len(robot.hull.keys()))
    # Part 2, start on a white panel instead
    robot = HullPainter(program, starting_color=1)
    robot.run()
    robot.visualize_hull()