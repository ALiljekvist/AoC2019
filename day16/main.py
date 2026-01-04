def read_input(filename):
    try:
        with open(filename, 'r') as f:
            data = [int(x) for x in f.read().strip()]
            return data
    except:
        return None

pattern = [1, 0, -1, 0]

def perform_fft(numbers):
    for i in range(len(numbers)):
        part_sum = 0
        pos = 0
        for j in range(i, len(numbers)):
            if (j - i) % (i+1) == 0 and j != i:
                pos = (pos+1) % len(pattern)
            part_sum += numbers[j] * pattern[pos]
        if part_sum < 0:
            part_sum = -part_sum
        numbers[i] = part_sum % 10
    return numbers

def part1(data, num_ffts=100):
    for i in range(num_ffts):
        data = perform_fft(data)
    return ''.join([str(x) for x in data[:8]])

def part2(data):
    offset = sum([int(v) * 10**i for i, v in enumerate(reversed(data[:7]))])
    new_data = data * 10000
    new_data = new_data[offset:]
    # By printing the length of the real input signal and the offset, I quickly
    # realized that the pattern was the same for all the remaining numbers
    # after the offset and that I could compute a running summation
    # backwards instead.
    for _ in range(100):
        rem = 0
        for i in reversed(range(len(new_data))):
            rem += new_data[i]
            rem = rem % 10
            new_data[i] = rem
    return ''.join([str(s) for s in new_data[:8]])

if __name__ == '__main__':
    data = read_input('input.txt')
    # data = read_input('example.txt')
    print(part1(data.copy()))
    print(part2(data))
