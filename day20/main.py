def read_input(filename):
    try:
        with open(filename, 'r') as f:
            data = [x.replace('\n', '') for x in f.readlines() if x]
            return data
    except:
        return None

def parse_grid(data):
    grid = {}
    for r, row in enumerate(data):
        for c, val in enumerate(row):
            if val == ' ' or val == '#':
                continue
            grid[(r,c)] = val
    return grid

def get4neighbs(p, grid):
    neighbs = []
    for dr in [-1, 1]:
        if (p[0]+dr,p[1]) in grid:
            neighbs.append((p[0]+dr, p[1]))
    for dc in [-1, 1]:
        if (p[0], p[1]+dc) in grid:
            neighbs.append((p[0], p[1]+dc))
    return neighbs

def solidate_portals(grid):
    to_remove = set()
    to_add = []
    for p, val in grid.items():
        if val == '.':
            continue
        if p in to_remove:
            continue
        to_remove.add(p)
        neighbs = get4neighbs(p, grid)
        if len(neighbs) == 1:
            anchor = neighbs[0]
            other = neighbs[0]
        else:
            for n in neighbs:
                if grid[n] != '.':
                    anchor = p
                    other = n
        to_remove.add(other)
        dr, dc = p[0]-other[0], p[1]-other[1]
        order = [grid[p], grid[other]]
        if dr > 0 or dc > 0:
            order = reversed(order)
        to_add.append((anchor, ''.join(order)))
    for p in to_remove:
        grid.pop(p)
    for pos, name in to_add:
        grid[pos] = name
    return grid

def dist(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

def connect_portals(grid, midpoint):
    pairs = {}
    for p, item in grid.items():
        if item == '.':
            continue
        pairs[item] = pairs.get(item, [])
        pairs[item].append(p)
    portals = {}
    start = end = None
    for name, pair in pairs.items():
        if name == 'AA':
            start = pair[0]
            continue
        if name == 'ZZ':
            end = pair[0]
            continue
        # Figure out which portal is the inner and outer one
        p1, p2 = pair[0], pair[1]
        if dist(p1, midpoint) < dist(p2, midpoint):
            p1, p2 = p2, p1
        portals[p1] = (p2, -1)
        portals[p2] = (p1, 1)
    return portals, start, end

def find_shortest_path(start, end, grid, portals):
    cache = set([start])
    queue = [(-1, start)]
    while queue:
        steps, curr = queue.pop(0)
        for n in get4neighbs(curr, grid):
            if n in cache:
                continue
            if n == end:
                return steps
            match grid[n]:
                case '.':
                    queue.append((steps+1, n))
                    cache.add(n)
                case 'ZZ':
                    return steps
                case _:
                    new_n, _ = portals[n]
                    queue.append((steps, new_n))
                    cache.add(n)
                    cache.add(new_n)
    return -2

def part1(start, end, grid, portals):
    return find_shortest_path(start, end, grid, portals)

def find_shortest_path_with_levels(start, end, grid, portals):
    cache = set([start])
    queue = [(-1, 0, start)]
    while queue:
        steps, level, curr = queue.pop(0)
        # print(steps, level, curr)
        for n in get4neighbs(curr, grid):
            if (n, level) in cache:
                continue
            if n == end:
                if level != 0:
                    continue
                return steps
            match grid[n]:
                case '.':
                    queue.append((steps+1, level, n))
                    cache.add((n, level))
                case 'AA' | 'ZZ':
                    continue
                case _:
                    new_n, delta = portals[n]
                    new_level = level + delta
                    if new_level < 0:
                        continue
                    queue.append((steps, new_level, new_n))
                    cache.add((n, level))
                    cache.add((new_n, new_level))
    return -2

def part2(start, end, grid, portals):
    return find_shortest_path_with_levels(start, end, grid, portals)

if __name__ == '__main__':
    data = read_input('input.txt')
    midpoint = (len(data)//2, len(data[0])//2)
    grid = parse_grid(data)
    grid = solidate_portals(grid)
    portals, start, end = connect_portals(grid, midpoint)
    print(part1(start, end, grid, portals))
    print(part2(start, end, grid, portals))
