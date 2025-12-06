
class IntComp:
    def __init__(self, program, inputs):
        self.program = program[:]
        self.inputs = inputs
        self.halted = False
        self.ind = 0

    def add_input(self, new_inputs):
        self.inputs += new_inputs

    def read(self, ind, mode):
        val = self.program[ind]
        if mode == 1:
            return val
        return self.program[val]

    def write(self, ind, val):
        self.program[ind] = val

    def run(self, continue_on_zero=False):
        out = 0
        while self.ind < len(self.program):
            ind = self.ind
            mode, op = self.program[ind] // 100, self.program[ind] % 100
            match op:
                case 1:
                    # Addition
                    a = self.read(ind+1, mode%10)
                    b = self.read(ind+2, (mode//10)%10)
                    out = self.program[ind+3]
                    self.write(out, a + b)
                    self.ind += 4
                case 2:
                    # Multiplication
                    a = self.read(ind+1, mode%10)
                    b = self.read(ind+2, (mode//10)%10)
                    out = self.program[ind+3]
                    self.write(out, a * b)
                    self.ind += 4
                case 3:
                    # Input
                    inp = self.inputs.pop(0)
                    out = self.program[ind+1]
                    self.write(out, inp)
                    self.ind += 2
                case 4:
                    # Output
                    out = self.read(ind+1, mode%10)
                    self.ind += 2
                    if not continue_on_zero:
                        return out
                case 5:
                    # Jump if true
                    a = self.read(ind+1, mode%10)
                    b = self.read(ind+2, (mode//10)%10)
                    if a != 0:
                        self.ind = b
                    else:
                        self.ind += 3
                case 6:
                    # Jump if false
                    a = self.read(ind+1, mode%10)
                    b = self.read(ind+2, (mode//10)%10)
                    if a == 0:
                        self.ind = b
                    else:
                        self.ind += 3
                case 7:
                    # Less than
                    a = self.read(ind+1, mode%10)
                    b = self.read(ind+2, (mode//10)%10)
                    out = self.program[ind+3]
                    val = 0
                    if a < b:
                        val = 1
                    self.write(out, val)
                    self.ind += 4
                case 8:
                    # Equals
                    a = self.read(ind+1, mode%10)
                    b = self.read(ind+2, (mode//10)%10)
                    out = self.program[ind+3]
                    val = 0
                    if a == b:
                        val = 1
                    self.write(out, val)
                    self.ind += 4
                case 99:
                    self.halted = True
                    break
                case _:
                    print(f"INVALID OP CODE {op}")
                    print(ind)
                    quit()
        return out
