import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rel_position(self, other):
        return Point(other.x-self.x, other.y-self.y)

    def scale(self, n: int):
        return Point(self.x*n, self.y*n)
    
    def magnitude(self):
        return self.x**2 + self.y**2

    def dist_sq(self, other):
        return (self.x-other.x)**2 + (self.y-other.y)**2

    def angle(self):
        # The angle is defined starting at 0 if pointing straight up
        # and going around clockwise
        angle = math.atan2(self.x, -self.y)
        if angle < 0:
            angle += 2 * math.pi
        return angle

    def blocks(self, other, eps=0.0000000001):
        return (self.angle() - other.angle())**2 < eps

    def __lt__(self, other):
        return self.magnitude() < other.magnitude()
    
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"({self.x},{self.y})"

def read_input(filename):
    with open(filename, 'r') as f:
        data = [x.strip() for x in f.readlines() if x.strip()]
    asteroids = []
    for y in range(len(data)):
        asteroids.extend([Point(x,y) for x in range(len(data[y])) if data[y][x] == '#'])
    return asteroids

def count_vissible(asteroids: list[Point], i: int):
    a = asteroids[i]
    # Sort them by distance, so we only have to check in one direction when comparing
    rel_points = sorted([a.rel_position(b) for j, b in enumerate(asteroids) if j != i])
    not_visible = []
    for j in range(len(rel_points)):
        if j in not_visible:
            continue
        for k in range(j+1, len(rel_points)):
            if rel_points[j].blocks(rel_points[k]):
                not_visible.append(k)
    not_visible.sort(reverse=True)
    for j in not_visible:
        rel_points.pop(j)
    return rel_points

def part1(data):
    visible = sorted([(count_vissible(data, i), data[i]) for i in range(len(data))], key= lambda x: len(x[0]), reverse=True)
    return visible[0]

def part2(visible_asteroids, o):
    visible_asteroids = sorted(visible_asteroids, key=lambda p: (p.angle(), p.magnitude()))
    chosen = visible_asteroids[200-1]
    return o.x + chosen.x, o.y + chosen.y

if __name__ == "__main__":
    data = read_input('input.txt')
    # data = read_input('example.txt')
    visible_asteroids, location = part1(data)
    print(len(visible_asteroids))
    x, y = part2(visible_asteroids, location)
    print(x*100 + y)