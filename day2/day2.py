def readInput():
    data = open('input.txt', 'r').read()
    program = list(map(lambda x: int(x), data.split(',')))
    return program

def intcodeComputer(program):
    ind = 0
    while program[ind] != 99:
        if program[ind] != 1 and program[ind] != 2:
            return program
        in1, in2, out = program[ind+1], program[ind+2], program[ind+3]
        if program[ind] == 1:
            program[out] = program[in1] + program[in2]
        elif program[ind] == 2:
            program[out] = program[in1] * program[in2]
        ind += 4
    return program

def setProgram(program, noun, verb):
    newprogram = program.copy()
    newprogram[1] = noun
    newprogram[2] = verb
    return newprogram

if __name__ == '__main__':
    program = readInput()
    for i in range(100):
        for j in range(100):
            newprogram = setProgram(program, i, j)
            newprogram = intcodeComputer(newprogram)
            if i == 12 and j == 2:
                print('Answer for part 1:', newprogram[0])
            if newprogram[0] == 19690720:
                print('Answer for part 2:', 100*i + j)