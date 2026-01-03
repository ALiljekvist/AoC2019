def read_input(filename):
    try:
        with open(filename, 'r') as f:
            data = [x.strip() for x in f.readlines() if x.strip()]
            return data
    except:
        return None

def shuffle(operations, a, b, N):
    for op in operations:
        things = op.split(' ')
        if things[0] == 'cut':
            fa, fb = 1, -int(things[-1])
        if things[0] == 'deal':
            try:
                # deal with increment
                fa, fb, = int(things[-1]), 0
            except:
                # deal into new stack
                fa, fb = -1, -1
        # Since these can be written as linear functions, we can write the
        # mappings as a F(a) on the unit (1) and an offset F(b).
        # Each new mapping then becomes:
        # F(a) * (a * x + b) + F(b) = F(a)*a*x + F(a)*b + F(b)
        # Since this in turn is linear, the x can be multiplied later
        # Use the modulo operator to not have the numbers go off far.
        # Since the final answer is also mod N, this will not affect any
        # intermediate answer or the final answer.
        a = (fa * a) % N
        b = (fa * b + fb) % N
    return a, b

def part1(data):
    N = 10007
    # Represent the number c as c = (a * x + b), and the function in modular form will become
    # F(c) mod N = (F(a) * x + F(b)) mod N
    a, b = shuffle(data, 1, 0, N)
    return (a * 2019 + b) % N

# This uses Fermat's little theorem to calculate a modular inverse
# of a mod N (this is given that N is a prime number)
def inv(a, N):
    return pow(a, N-2, N)

def part2(data):
    N = 119315717514047
    M = 101741582076661
    a, b = shuffle(data, 1, 0, N)
    # The shuffle is now to be performed M times, where the entire shuffle can be written as it's own linear function:
    # a' = F(a) * a'
    # b' = F(a) * b + F(b)
    # The F(a) is now 'a' and F(b) is 'b', and we start from a = 1 and b = 0 again.
    # This done M times can be simplified to become:
    # F(a) = a^M mod N = a^M, mod N
    # F(b) = (a * b + F(b))^M, mod N
    #      = b * (a^M + a^(M-1) + ... + a^2 + a + 1), mod N
    #      = b * (a^M - 1) * inv(a-1), mod N
    a_M = pow(a, M, N)
    b_M = b * (a_M - 1) * inv(a-1, N)

    # The final answer can then be found through the linear fucntion as in part 1.
    # However, we now want to find the original position so we have to solve for x:
    # F(c) = F(a)*x + F(b) mod N  =>
    # x = (F(c) - F(b)) * inv(F(a)) mod N
    return ((2020 - b_M) * inv(a_M, N)) % N

if __name__ == '__main__':
    data = read_input('input.txt')
    print(part1(data))
    print(part2(data))
