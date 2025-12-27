class Recipe:
    def __init__(self, name, val):
        self.name = name
        self.val = val
        self.ingredients = dict()

    def add_ingredient(self, name, val):
        self.ingredients[name] = self.ingredients.get(name, 0) + val

    def create(self, num_needed, recipes, stock):
        if num_needed == 0:
            return
        if stock.get(self.name, 0) >= num_needed:
            stock[self.name] = stock.get(self.name, 0) - num_needed
            return
        scale = (num_needed - stock.get(self.name, 0)) // self.val
        if (num_needed - stock.get(self.name, 0)) % self.val != 0:
            scale += 1
        # Remove the number of needed items
        if scale == 0:
            # No need to create any more of these items
            return
        # Create the needed values of any ingredients
        for name, num in self.ingredients.items():
            if name == 'ORE':
                # Special handling of ORE
                stock['ORE'] = stock.get('ORE', 0) + scale * num
                continue
            sub_recipe = recipes[name]
            sub_recipe.create(scale*num, recipes, stock)
        # Add the number of created items into the stock and remove the used ones
        stock[self.name] = stock.get(self.name, 0) + self.val * scale
        stock[self.name] -= num_needed
        if stock[self.name] < 0:
            print(self.name, "is now negative", stock[self.name], f"({self.val * scale}, {num_needed})")

    def __repr__(self):
        return ' + '.join([f'{v} {k}' for k, v in self.ingredients.items()]) + f' = {self.val} {self.name}'

def read_input(filename):
    try:
        with open(filename, 'r') as f:
            data = [x.strip() for x in f.readlines() if x.strip()]
            return parse_recipes(data)
    except:
        return None

def parse_recipes(raw_recipes):
    recipes = dict()
    for raw_recipe in raw_recipes:
        stuff = raw_recipe.split(' => ')
        out = stuff[1].split(' ')
        recipe = Recipe(out[1], int(out[0]))
        for raw_in in stuff[0].split(', '):
            ing = raw_in.split(' ')
            recipe.add_ingredient(ing[1], int(ing[0]))
        recipes[out[1]] = recipe
    return recipes

def get_num_ore_for_fuel_count(recipes, count):
    root_recipe = recipes['FUEL']
    stock = dict()
    root_recipe.create(count, recipes, stock)
    return stock.get('ORE', 0)

def part1(recipes):
    return get_num_ore_for_fuel_count(recipes, 1)

def part2(recipes, starting_value, threshold):
    # Perform binary search on number of fuels we can create 
    # until we find the ORE count just below threshold
    low = starting_value
    # Assume you can not double the number of fuels created by the ORE count for one
    high = starting_value*2
    while high - low > 1:
        # print(low, high)
        mid = (low+high)//2
        count = get_num_ore_for_fuel_count(recipes, mid)
        if count > threshold:
            high = mid
        else:
            low = mid
    return low

if __name__ == '__main__':
    data = read_input('input.txt')
    # data = read_input('example.txt')
    p1 = part1(data)
    print(p1)
    ore_deposit = 1000000000000
    print(part2(data, ore_deposit//p1, ore_deposit))