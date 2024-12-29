import numpy as np
file = 'input.txt'

def readInput():
    return list(map(lambda x: int(x.replace('\n','')), open(file,'r').readlines()))

def recursiveFuel(weights):
    totalFuel = 0
    for i in range(len(weights)):
        newFuel = weights[i]//3 - 2
        totalFuel += newFuel
        while newFuel > 6:
            newFuel = newFuel//3 - 2
            totalFuel += newFuel
    return totalFuel

if __name__ == '__main__':
    weights = readInput()
    print('Fuel for weight only:',sum(list(map(lambda x: x//3 - 2, weights))))
    print('Total fuel needed:', recursiveFuel(weights))
