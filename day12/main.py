import math

class Moon:
    def __init__(self, raw_pos: str):
        self.pos = [int(y.split('=')[1]) for y in raw_pos[1:-1].split(', ')]
        self.vel = [0 for _ in range(len(self.pos))]
    
    def apply_gravity(self, other):
        for i in range(len(self.pos)):
            to_add = 1
            if self.pos[i] > other.pos[i]:
                to_add = -1
            elif self.pos[i] == other.pos[i]:
                to_add = 0
            self.vel[i] += to_add
            other.vel[i] -= to_add
    
    def move(self):
        for i in range(len(self.pos)):
            self.pos[i] += self.vel[i]
    
    def energy(self):
        return sum([abs(p) for p in self.pos]) * sum([abs(v) for v in self.vel])

    def __repr__(self):
        return f"pos={self.pos}, vel={self.vel}"

def read_input(filename):
    try:
        with open(filename, 'r') as f:
            data = [Moon(x.strip()) for x in f.readlines() if x.strip()]
            return data
    except:
        return None

def search_for_period(x, win_size=100):
    period = None
    if len(x) < win_size+1:
        return None
    for i in range(win_size):
        if x[i] != x[len(x)-win_size+i]:
            return None
    return len(x)-win_size

def simulate(moons, timesteps):
    speed_hists = [[], [], []]
    periods = [None, None, None]
    for t in range(timesteps):
        for i in range(len(moons)):
            for j in range(i+1, len(moons)):
                moons[i].apply_gravity(moons[j])
        for i, m in enumerate(moons):
            m.move()
        for i in range(len(periods)):
            period = periods[i]
            if period is not None:
                continue
            if period is None:
                speed_hists[i].append(moons[0].pos[i])
                period = search_for_period(speed_hists[i])
            if period is not None:
                periods[i] = period
        if all([p is not None for p in periods]):
            break
    return moons, periods

def part1(data):
    moons, _ = simulate(data, 1000)
    return sum([m.energy() for m in moons])

def part2(data):
    _, periods = simulate(data, 10000000000)
    lcm = math.lcm(periods[0], periods[1])
    lcm = math.lcm(lcm, periods[2])
    return lcm

if __name__ == "__main__":
    data = read_input('input.txt')
    # data = read_input('example.txt')
    print(part1(data.copy()))
    print(part2(data))
