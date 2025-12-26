import sys
import time

sys.path.insert(0, "../")
from intcomp import IntComp

def read_input(filename):
    with open(filename, 'r') as f:
        return [int(x.strip()) for x in f.read().split(',')]

class Game:
    def __init__(self, program):
        self.comp = IntComp(program)
        self.comp.program[0] = 2
        self.grid = [[0 for x in range(40)] for y in range(25)]
        self.score = 0
        self.ball = (0, 0)
        self.board = (0, 0)

    def run(self):
        self.run_iter()
        while all(all([v != 2] for v in row) for row in self.grid) and not self.comp.halted:
            self.run_iter()
        return self.score

    def run_iter(self, debug=False):
        x, y, val = self.read_next()
        while (x != -1 or y != 0) and not self.comp.halted:
            if debug:
                print(x, y, val)
            if val == 4:
                self.ball = (x, y)
            elif val == 3:
                self.board = (x, y)
            self.grid[y][x] = val
            x, y, val = self.read_next()
        if val > self.score:
            # Apparently the program ends with setting the score to 0
            self.score = val

    def read_next(self):
        x = self.comp.run()
        y = self.comp.run()
        val = self.comp.run()
        return x, y, val

    def print_grid(self):
        rows = []
        for y in range(25):
            row = ''
            for x in range(40):
                val = self.grid[y][x]
                draw = '.'
                if val == 1:
                    draw = 'I'
                elif val == 2:
                    draw = '#'
                elif val == 3:
                    draw = '_'
                elif val == 4:
                    draw = 'O'
                row += draw
            rows.append(row)
        print('\n'.join(rows), flush=True)

def part1(program):
    comp = IntComp(program)
    tot_blocks = 0
    while not comp.halted:
        _ = comp.run()
        _ = comp.run()
        t_id = comp.run()
        if t_id == 2:
            tot_blocks += 1
    return tot_blocks

def part2(program, show=False):
    game = Game(program)
    def add_input():
        if show:
            game.print_grid()
            time.sleep(0.25)
        val = 0
        if game.ball[0] < game.board[0]:
            val = -1
        if game.ball[0] > game.board[0]:
            val = 1
        return val
    game.comp.input_func = add_input
    return game.run()

if __name__ == "__main__":
    program = read_input('input.txt')
    print(part1(program))
    print(part2(program))