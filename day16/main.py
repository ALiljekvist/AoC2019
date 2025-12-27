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
        # print('---', i, '---')
        for j in range(i, len(numbers)):
            if (j - i) % (i+1) == 0 and j != i:
                pos = (pos+1) % len(pattern)
            # print(numbers[j], pattern[pos])
            part_sum += numbers[j] * pattern[pos]
        if part_sum < 0:
            part_sum = -part_sum
        numbers[i] = part_sum % 10
        # print(part_sum, numbers[i])
    return numbers

def part1(data, num_ffts=100):
    for i in range(num_ffts):
        # print(i, data)
        data = perform_fft(data)
    return data

if __name__ == '__main__':
    data = read_input('input.txt')
    # data = read_input('example.txt')
    print(''.join([str(x) for x in part1(data, num_ffts=100)[:8]]))
