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

def simulate(moons, timesteps, original_positions=None):
    for t in range(timesteps):
        for i in range(len(moons)):
            for j in range(i+1, len(moons)):
                moons[i].apply_gravity(moons[j])
        for i, m in enumerate(moons):
            m.move()
            if original_positions is None:
                continue
            if all([m.pos[j] == original_positions[i][j] for j in range(len(m.pos))]):
                print(f"Moon {i+1} repeated position after {t} steps")
        print(t, moons[0])
    return moons

def part1(data):
    moons = simulate(data, 1000)
    return sum([m.energy() for m in moons])

def part2(data):
    original_positions = [m.pos[:] for m in data]
    moons = simulate(data, 1000000, original_positions)
    return moons

if __name__ == "__main__":
    data = read_input('input.txt')
    # data = read_input('example.txt')
    print(part1(data))
    print(part2(data))
