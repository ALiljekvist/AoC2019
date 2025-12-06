import sys

sys.path.insert(0, "../")
from intcomp import IntComp

def read_input(filename):
    with open(filename, 'r') as f:
        return [int(x.strip()) for x in f.read().split(',')]

def create_combinations(num_thrusters, curr, combs):
    if len(curr) == num_thrusters:
        combs.append(curr.copy())
        return
    for i in range(5):
        if i in curr:
            continue
        curr.append(i)
        create_combinations(num_thrusters, curr, combs)
        curr.pop()

def part1(program, combs):
    max_out = 0
    for inps in combs:
        amps = [IntComp(program, [inps[i]]) for i in range(len("ABCDE"))]
        out = 0
        for amp in amps:
            amp.add_input([out])
            new_out = amp.run()
            if amp.halted:
                break
            out = new_out
        max_out = max(out, max_out)
    return max_out

def part2(program, combs):
    max_out = 0
    for inps in combs:
        amps = [IntComp(program, [inps[i]]) for i in range(len("ABCDE"))]
        out = 0
        while all([not amp.halted for amp in amps]):
            for amp in amps:
                amp.add_input([out])
                new_out = amp.run()
                if not amp.halted:
                    out = new_out
        max_out = max(out, max_out)
    return max_out

if __name__ == "__main__":
    program = read_input('input.txt')
    combs = []
    create_combinations(len("ABCDE"), [], combs)
    print(part1(program, combs))
    # Bump the phase shifters into the new register
    combs = [[x+5 for x in comb] for comb in combs]
    # print(part2([3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5], [[9,8,7,6,5]]))
    print(part2(program, combs))
