import sys

sys.path.insert(0, "../")
from intcomp import IntComp

class Computer:
    def __init__(self, program, address):
        self.comp = IntComp(program)
        self.addr = address
        self.buffer_out = []
        self.write = None
        self.booted = False
        self.receiving = False

    def add_input_func(self, input_func):
        def provide_input():
            if not self.booted:
                self.booted = True
                return self.addr
            val_in = input_func()
            if val_in == -1:
                self.receiving = True
            return val_in
        self.comp.input_func = provide_input

    def halted(self):
        return self.comp.halted

    def tick(self):
        self.comp.tick()
        if self.comp.out is None:
            return
        self.receiving = False
        out = self.comp.out
        self.comp.out = None
        self.buffer_out.append(out)
        if len(self.buffer_out) >= 3:
            if self.write is None:
                print(f"No write function given to {self.addr}")
                return
            to_addr = self.buffer_out.pop(0)
            x = self.buffer_out.pop(0)
            y = self.buffer_out.pop(0)
            # print("Comp", self.addr, f"sending ({x}, {y}) to", to_addr)
            self.write(self.addr, to_addr, x, y)

class Network:
    def __init__(self, program):
        self.comps = [Computer(program, i) for i in range(50)]
        self.queue = dict((i, []) for i in range(50))
        for i in range(50):
            self.comps[i].add_input_func(self.read_socket(i))
            self.comps[i].write = self.write_socket()
        self.nat = (-1, -1)
        self.nat_y_hist = []

    def read_socket(self, i):
        def give_input():
            if len(self.queue[i]) == 0:
                return -1
            return self.queue[i].pop(0)
        return give_input
    
    def write_socket(self):
        def send_message(from_addr, to_addr, x, y):
            if to_addr >= len(self.queue):
                if to_addr != 255:
                    print("Alert! Large address not pointing to NAT:", to_addr)
                    quit()
                if self.nat == (-1, -1) and len(self.nat_y_hist) == 0:
                    print(y)
                self.nat = (x, y)
                return
            if to_addr < 0:
                print("ALERT! Negative address received from", from_addr)
                return
            self.queue[to_addr].append(x)
            self.queue[to_addr].append(y)
        return send_message

    def run(self):
        while not all([c.halted() for c in self.comps]):
            for ci, comp in enumerate(self.comps):
                if comp.halted():
                    continue
                comp.tick()
            if all([c.receiving for c in self.comps]) and self.nat != (-1, -1):
                x, y = self.nat
                self.nat = (-1, -1)
                if y in self.nat_y_hist:
                    return y
                self.nat_y_hist.append(y)
                self.queue[0].append(x)
                self.queue[0].append(y)
        return -1


def read_input(filename):
    with open(filename, 'r') as f:
        return [int(x.strip()) for x in f.read().split(',')]

def part1(program):
    net = Network(program)
    return net.run()

if __name__ == "__main__":
    program = read_input('input.txt')
    print(part1(program))
