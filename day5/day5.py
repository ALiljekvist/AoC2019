def read_input(filename):
    with open(filename, 'r') as f:
        return [int(x.strip()) for x in f.read().split(',')]

def read(program, ind, mode):
    if mode == 0:
        return program[program[ind]]
    return program[ind]

def run(program, input):
    ind = 0
    out = 0
    while ind < len(program) and program[ind] != 99:
        mode, val = program[ind] // 100, program[ind] % 100
        match val:
            case 1:
                # Addition
                program[program[ind+3]] = read(program, ind+1, mode%10) + read(program, ind+2, mode//10)
                ind += 4
            case 2:
                # Multiplication
                program[program[ind+3]] = read(program, ind+1, mode%10) * read(program, ind+2, mode//10)
                ind += 4
            case 3:
                # Input
                program[program[ind+1]] = input
                ind += 2
            case 4:
                # Output
                out = read(program, ind+1, mode%10)
                if out != 0:
                    return out
                ind += 2
            case _:
                break
    return out

def part1(program):
    return run(program, 1)

def part2(program):
    return -1

if __name__ == '__main__':
    program = read_input('input.txt')
    # program = read_input('example.txt')
    print(part1(program.copy()))
    print(part2(program))
