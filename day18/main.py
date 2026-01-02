def read_input(filename):
    try:
        with open(filename, 'r') as f:
            data = [x.strip() for x in f.readlines() if x.strip()]
            return data
    except:
        return None

def parse_grid(data):
    grid = dict()
    starts = []
    for r, row in enumerate(data):
        for c, val in enumerate(row):
            if val == '#':
                continue
            if val == '@':
                starts.append((r,c))
            grid[(r, c)] = val
    return grid, starts

def map_grid(grid):
    starts = [pos for pos, v in grid.items() if v != '.']
    mappings = {}
    # Walk to all neighbors from each position
    for pos in starts:
        neighbors = {}
        queue = [(0, pos)]
        cache = set([pos])
        while queue:
            steps, (x, y) = queue.pop(0)
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                new_pos = (x+dx, y+dy)
                if new_pos in cache or new_pos not in grid:
                    continue
                cache.add(new_pos)
                if grid[new_pos] != '.':
                    neighbors[new_pos] = steps + 1
                    continue
                queue.append((steps + 1, new_pos))
        mappings[pos] = neighbors
    return mappings

def put_in_queue(state, queue):
    i = 0
    while i < len(queue) and queue[i][0] < state[0]:
        i += 1
    queue.insert(i, state)

def get_next(at, hist, mappings, grid):
    keys = set([grid[x].lower() for x in hist if grid[x].isalpha()])
    next_options = []
    considered = set()
    explore = [(0, at)]
    while explore:
        steps, curr = explore.pop(0)
        if curr in considered:
            continue
        considered.add(curr)
        if curr in hist:
            for pos, new_steps in mappings[curr].items():
                if pos in considered:
                    continue
                put_in_queue((steps+new_steps, pos), explore)
            continue
        val = grid[curr]
        if val.isalpha() and val.upper() == val:
            if val.lower() not in keys:
                continue
        next_options.append((steps, curr))
    return next_options

def to_hash(hist, grid):
    pos = hist[-1]
    return f"({pos[0]},{pos[1]})"+''.join(sorted([grid[x] for x in hist]))

def find_shortest_dfs(hist, mappings, grid, all_keys, cache):
    keys = set([grid[x].lower() for x in hist if grid[x].isalpha()])
    if len(keys) >= all_keys:
        return 0
    hashed = to_hash(hist, grid)
    if hashed in cache:
        return cache[hashed]
    min_steps = 100000000
    for (new_steps, pos) in get_next(hist[-1], hist, mappings, grid):
        hist.append(pos)
        steps = new_steps + find_shortest_dfs(hist, mappings, grid, all_keys, cache)
        hist.pop()
        if steps < min_steps:
            min_steps = steps
    cache[hashed] = min_steps
    return min_steps

def part1(start, mappings, grid):
    all_keys = len(set([grid[x].lower() for x in mappings.keys() if grid[x].isalpha()]))
    return find_shortest_dfs([start], mappings, grid, all_keys, {})

def to_hash_p2(positions, keys):
    return ''.join([f'({p[0]},{p[1]})' for p in positions]) + ''.join(sorted(list(keys)))

def find_shortest_dfs_p2(positions, hist, mappings, grid, all_keys, cache):
    keys = set([grid[x].lower() for x in hist if grid[x].isalpha()])
    if len(keys) >= all_keys:
        return 0
    hashed = to_hash_p2(positions, keys)
    if hashed in cache:
        return cache[hashed]
    min_steps = 100000000
    for i in range(len(positions)):
        pos = positions[i]
        for (new_steps, new_pos) in get_next(pos, hist, mappings, grid):
            hist.append(new_pos)
            positions[i] = new_pos
            steps = new_steps + find_shortest_dfs_p2(positions, hist, mappings, grid, all_keys, cache)
            positions[i] = pos
            hist.pop()
            if steps < min_steps:
                min_steps = steps
    cache[hashed] = min_steps
    return min_steps

def part2(positions, mappings, grid):
    all_keys = len(set([grid[x].lower() for x in mappings.keys() if grid[x].isalpha()]))
    return find_shortest_dfs_p2(positions, positions.copy(), mappings, grid, all_keys, {})

if __name__ == '__main__':
    data = read_input('input.txt')
    # data = read_input('example.txt')
    grid, positions = parse_grid(data)
    start = positions[0]
    mappings = map_grid(grid)
    print(part1(start, mappings, grid))
    data[start[0]-1] = data[start[0]-1][:start[1]-1] + '@#@' + data[start[0]-1][start[1]+2:]
    data[start[0]] = data[start[0]][:start[1]-1] + '###' + data[start[0]][start[1]+2:]
    data[start[0]+1] = data[start[0]+1][:start[1]-1] + '@#@' + data[start[0]+1][start[1]+2:]
    grid, positions = parse_grid(data)
    mappings = map_grid(grid)
    print(part2(positions, mappings, grid))
