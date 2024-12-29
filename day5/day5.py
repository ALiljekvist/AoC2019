def readInput():
    data = open('input.txt', 'r').read()
    program = list(map(lambda x: int(x), data.split(',')))
    return program

def intcodeComputer(program, mode=0):
    if mode == 0:
        ind = 0
        while ind < len(program):
            if program[ind] == 99:
                return program
            if program[ind] == 1:
                program[program[ind+3]] = program[program[ind+1]] + program[program[ind+2]]
                ind += 4
            elif program[ind] == 2:
                program[program[ind+3]] = program[program[ind+1]] * program[program[ind+2]]
                ind += 4
            elif program[ind] == 3:
                program[program[ind+1]] = 0 # change 0 for some input given
                print('Not fully implemented')
                ind += 2
            elif program[ind] == 4:
                output = program[ind+1]
                ind += 2
            else:
                print('Faulty command, exiting...')
                break
        return program
    elif mode == 1:
        print('not implemented')
        return program
    else:
        print('invalid mode')
        return program


if __name__ == '__main__':
    program = readInput()

