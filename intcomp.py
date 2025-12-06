
def read(program, ind, mode):
    if mode == 0:
        return program[program[ind]]
    return program[ind]

def run(program, input=0, continue_on_zero=False):
    ind = 0
    out = 0
    while ind < len(program):
        mode, val = program[ind] // 100, program[ind] % 100
        match val:
            case 1:
                # Addition
                a = read(program, ind+1, mode%10)
                b = read(program, ind+2, (mode//10)%10)
                out = program[ind+3]
                program[out] = a + b
                ind += 4
            case 2:
                # Multiplication
                a = read(program, ind+1, mode%10)
                b = read(program, ind+2, (mode//10)%10)
                out = program[ind+3]
                program[out] = a * b
                ind += 4
            case 3:
                # Input
                program[program[ind+1]] = input
                ind += 2
            case 4:
                # Output
                out = read(program, ind+1, mode%10)
                if not continue_on_zero:
                    return out
                ind += 2
            case 5:
                # Jump if true
                a = read(program, ind+1, mode%10)
                b = read(program, ind+2, (mode//10)%10)
                if a != 0:
                    ind = b
                else:
                    ind += 3
            case 6:
                # Jump if false
                a = read(program, ind+1, mode%10)
                b = read(program, ind+2, (mode//10)%10)
                if a == 0:
                    ind = b
                else:
                    ind += 3
            case 7:
                # Less than
                a = read(program, ind+1, mode%10)
                b = read(program, ind+2, (mode//10)%10)
                out = program[ind+3]
                val = 0
                if a < b:
                    val = 1
                program[out] = val
                ind += 4
            case 8:
                # Equals
                a = read(program, ind+1, mode%10)
                b = read(program, ind+2, (mode//10)%10)
                out = program[ind+3]
                val = 0
                if a == b:
                    val = 1
                program[out] = val
                ind += 4
            case 99:
                break
            case _:
                print(f"INVALID OP CODE {val}")
                quit()
    return out
