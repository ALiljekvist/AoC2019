class IntComp:
    def __init__(self, program, inputs=None, input_func=None):
        self.program = program[:]
        self.ind = 0
        self.memory = {}
        self.inputs = inputs if inputs is not None else []
        self.halted = False
        self.relative_base = 0
        self.input_func = input_func if input_func is not None else self.default_input

    def copy(self):
        new_comp = IntComp(self.program[:])
        new_comp.ind = self.ind
        new_comp.memory = self.memory.copy()
        new_comp.inputs = self.inputs.copy()
        new_comp.halted = self.halted
        new_comp.relative_base = self.relative_base
        return new_comp

    def add_input(self, new_inputs):
        self.inputs += new_inputs

    def default_input(self):
        return self.inputs.pop(0)

    def read(self, ind, mode):
        addr = self.program[ind]
        if mode == 1:
            # Immediate mode, return the value directly
            return addr
        if mode == 2:
            # Relative mode, add the base to the value
            addr += self.relative_base
        # Choose the correct part of the memory to read from
        if addr < len(self.program):
            return self.program[addr]
        return self.memory.get(addr, 0)

    def write(self, ind, val, mode):
        if mode == 2:
            ind += self.relative_base
        # Choose the correct part of the memory to write to
        if ind < len(self.program):
            self.program[ind] = val
            return
        self.memory[ind] = val

    def run_until_halted(self):
        out = -1
        while not self.halted:
            new_out = self.run()
            if not self.halted:
                out = new_out
        return out

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
                    self.write(out, a + b, (mode//100)%10)
                    self.ind += 4
                case 2:
                    # Multiplication
                    a = self.read(ind+1, mode%10)
                    b = self.read(ind+2, (mode//10)%10)
                    out = self.program[ind+3]
                    self.write(out, a * b, (mode//100)%10)
                    self.ind += 4
                case 3:
                    # Input
                    inp = self.input_func()
                    out = self.program[ind+1]
                    self.write(out, inp, mode%10)
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
                    self.write(out, val, (mode//100)%10)
                    self.ind += 4
                case 8:
                    # Equals
                    a = self.read(ind+1, mode%10)
                    b = self.read(ind+2, (mode//10)%10)
                    out = self.program[ind+3]
                    val = 0
                    if a == b:
                        val = 1
                    self.write(out, val, (mode//100)%10)
                    self.ind += 4
                case 9:
                    # Update relative base
                    val = self.read(ind+1, mode%10)
                    self.relative_base += val
                    self.ind += 2
                case 99:
                    self.halted = True
                    break
                case _:
                    print(f"INVALID OP CODE {op}")
                    print(ind)
                    quit()
        return out
