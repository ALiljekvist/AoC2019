def read_input(filename):
    with open(filename, 'r') as f:
        return [int(x) for x in f.read().split(',')]

def run(program):
    ind = 0
    while program[ind] != 99:
        in1, in2, out = program[ind+1], program[ind+2], program[ind+3]
        match program[ind]:
            case 1:
                program[out] = program[in1] + program[in2]
            case 2:
                program[out] = program[in1] * program[in2]
            case _:
                return program
        ind += 4
    return program

def part1(program):
    program[1] = 12
    program[2] = 2
    result = run(program)
    return result[0]

def part2(program):
    for i in range(100):
        for j in range(100):
            test_program = program.copy()
            test_program[1] = i
            test_program[2] = j
            if run(test_program)[0] == 19690720:
                return 100*i + j
    return -1

if __name__ == '__main__':
    program = read_input('input.txt')
    print(part1(program.copy()))
    print(part2(program))
