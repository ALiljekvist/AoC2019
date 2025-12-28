def read_input(filename):
    try:
        with open(filename, 'r') as f:
            data = [x.strip() for x in f.readlines() if x.strip()]
            return data
    except:
        return None

def parse_grid(data):
    grid = {}
    for r, row in enumerate(data):
        for c, ch in enumerate(row):
            if ch == '#':
                grid[(r,c)] = 1
    return grid

def print_grid(grid):
    for r in range(5):
        row = ''
        for c in range(5):
            if (r,c) in grid:
                row += '#'
            else:
                row += '.'
        print(row)

def biodiversity_rating(grid):
    tot = 0
    for r in range(5):
        for c in range(5):
            if (r,c) in grid:
                tot += 2**(r*5+c)
    return tot

def part1(curr):
    cache = set()
    i = 0
    while biodiversity_rating(curr) not in cache:
        cache.add(biodiversity_rating(curr))
        next = {}
        for r in range(5):
            for c in range(5):
                ns = sum([curr.get((r+dr, c+dc), 0) for dr, dc in [(1, 0), (-1,0), (0, 1), (0,-1)]])
                match ns:
                    case 1:
                        next[(r,c)] = 1
                    case 2:
                        if (r,c) not in curr:
                            next[(r,c)] = 1
        curr = next
        i += 1
    return curr

def get_inner(dim, dimensions, dir):
    if dim >= len(dimensions):
        return 0
    grid = dimensions[dim]
    tot = 0
    match dir:
        case (1, 0):
            for c in range(5):
                tot += grid.get((0, c), 0)
        case (-1, 0):
            for c in range(5):
                tot += grid.get((4, c), 0)
        case (0, 1):
            for r in range(5):
                tot += grid.get((r, 0), 0)
        case (0, -1):
            for r in range(5):
                tot += grid.get((r, 4), 0)
        case _:
            print("PANIC")
            return 5000
    return tot

def get_outer(dim, dimensions, dir):
    if dim < 0:
        return 0
    match dir:
        case (1, 0):
            return dimensions[dim].get((3, 2), 0)
        case (-1, 0):
            return dimensions[dim].get((1, 2), 0)
        case (0, 1):
            return dimensions[dim].get((2, 3), 0)
        case (0, -1):
            return dimensions[dim].get((2, 1), 0)
        case _:
            print("PANIC")
            return 5000

def update(dim, dimensions, t):
    updated = {}
    for r in range(5):
        for c in range(5):
            if r == 2 and c == 2:
                # Part of other dimension
                continue
            ns = 0
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                if r + dr == 2 and c + dc == 2:
                    ns += get_inner(dim+1, dimensions, (dr, dc))
                elif r + dr < 0 or r + dr >= 5 or c + dc < 0 or c + dc >= 5:
                    ns += get_outer(dim-1, dimensions, (dr, dc))
                else:
                    ns += dimensions[dim].get((r+dr, c+dc), 0)
            match ns:
                case 1:
                    updated[(r,c)] = 1
                case 2:
                    if (r,c) not in dimensions[dim]:
                        updated[(r,c)] = 1
    return updated

def part2(grid, period=200):
    # Since all other levels are empty, we cannot reach further
    # than the period dimensions up/down in under that time
    dimensions = [{} for i in range(2*period+1)]
    dimensions[period] = grid
    for t in range(period):
        updated_dimensions = [{} for i in range(2*period+1)]
        for d in range(len(dimensions)):
            updated_dimensions[d] = update(d, dimensions, t)
        dimensions = updated_dimensions
    return sum([sum([v for k, v in dim.items()]) for dim in dimensions])

if __name__ == '__main__':
    data = read_input('input.txt')
    # data = read_input('example.txt')
    grid = parse_grid(data)
    p1 = part1(grid.copy())
    print(biodiversity_rating(p1))
    # print(part2(grid, period=10))
    print(part2(grid))
