def read_input(filename):
    try:
        with open(filename, 'r') as f:
            data = [x.strip() for x in f.readlines() if x.strip()]
            return data
    except:
        return None

def new_stack(deck):
    return list(reversed(deck))

def deal(deck, increment):
    new_deck = [0 for x in range(len(deck))]
    ind = 0
    while deck:
        new_deck[ind] = deck.pop(0)
        ind = (ind+increment) % len(new_deck)
    return new_deck

def cut(deck, at):
    if at < 0:
        at += len(deck)
    return deck[at:] + deck[:at]

def shuffle(operations, deck_size=10007):
    deck = list(range(deck_size))
    for op in operations:
        things = op.split(' ')
        if things[0] == 'cut':
            deck = cut(deck, int(things[-1]))
        if things[0] == 'deal':
            try:
                increment = int(things[-1])
                deck = deal(deck, increment)
            except:
                deck = new_stack(deck)
    return deck

def run_tests():
    tests = [(["deal with increment 7",
              "deal into new stack",
              "deal into new stack"],
              [0, 3, 6, 9, 2, 5, 8, 1, 4, 7]),
              (["cut 6",
              "deal with increment 7",
              "deal into new stack"],
              [3, 0, 7, 4, 1, 8, 5, 2, 9, 6]),
              (["deal with increment 7",
              "deal with increment 9",
              "cut -2"],
              [6, 3, 0, 7, 4, 1, 8, 5, 2, 9]),
              (["deal into new stack",
              "cut -2",
              "deal with increment 7",
              "cut 8",
              "cut -4",
              "deal with increment 7",
              "cut 3",
              "deal with increment 9",
              "deal with increment 3",
              "cut -1",],
              [9, 2, 5, 8, 1, 4, 7, 0, 3, 6]),]
    for i, (ops, res) in enumerate(tests):
        out = shuffle(ops, deck_size=10)
        if len(out) != len(res):
            print("Test", i+1, "output len mismatch", len(out), len(res))
            continue
        matching = True
        for j in range(len(out)):
            if out[j] != res[j]:
                matching = False
        if not matching:
            print("Fail", i+1, out, res)

if __name__ == '__main__':
    data = read_input('input.txt')
    run_tests()
    out = shuffle(data)
    print(out.index(2019))
