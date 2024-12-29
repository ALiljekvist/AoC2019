import numpy as np
import matplotlib.pyplot as plt

def readInput():
    data = open('input.txt', 'r').readlines()
    path1 = data[0].replace('\n','').split(',')
    path2 = data[1].replace('\n','').split(',')
    return path1, path2

def createPath(path):
    pos = [0,0]
    totalSteps = 0
    horizontal = []
    vertical = []
    coords = [[0],[0]]
    for move in path:
        letter, number = move[0], int(move[1:])
        if letter == 'R':
            horizontal.append((pos[1], pos[0], pos[0] + number, totalSteps))
            pos[0] += number
            totalSteps += number
            coords[0].append(pos[0])
            coords[1].append(pos[1])
        elif letter == 'U':
            vertical.append((pos[0], pos[1], pos[1] + number, totalSteps))
            pos[1] += number
            totalSteps += number
            coords[0].append(pos[0])
            coords[1].append(pos[1])
        elif letter == 'D':
            vertical.append((pos[0], pos[1], pos[1] - number, totalSteps))
            pos[1] -= number
            totalSteps += number
            coords[0].append(pos[0])
            coords[1].append(pos[1])
        elif letter == 'L':
            horizontal.append((pos[1], pos[0], pos[0] - number, totalSteps))
            pos[0] -= number
            totalSteps += number
            coords[0].append(pos[0])
            coords[1].append(pos[1])
    return horizontal, vertical, coords

def checkCrossings(path, horizontal, vertical):
    crossingsdistances = []
    pos = [0,0]
    newsteps = 0
    for move in path:
        letter, number = move[0], int(move[1:])
        if letter == 'R':
            newx = pos[0] + number
            for tx, y1, y2, steps in vertical:
                if y1 > y2:
                    y1, y2 = y2, y1
                if pos[0] < tx < newx and y1 < pos[1] < y2:
                    totalsteps = steps + newsteps + abs(tx - pos[0]) + abs(pos[1] - y1)
                    crossingsdistances.append((abs(tx) + abs(pos[1]), totalsteps))
            pos[0] = newx
            newsteps += number
        elif letter == 'U':
            newy = pos[1] + number
            for ty, x1, x2, steps in horizontal:
                if x1 > x2:
                    x1, x2 = x2, x1
                if pos[1] < ty < newy and x1 < pos[0] < x2:
                    totalsteps = steps + newsteps + abs(pos[0] - x1) + abs(ty - pos[1])
                    crossingsdistances.append((abs(ty) + abs(pos[0]), totalsteps))
            pos[1] = newy
            newsteps += number
        elif letter == 'D':
            newy = pos[1] - number
            for ty, x1, x2, steps in horizontal:
                if x1 > x2:
                    x1, x2 = x2, x1
                if newy < ty < pos[1] and x1 < pos[0] < x2:
                    totalsteps = steps + newsteps + abs(pos[0] - x1) + abs(ty - pos[1])
                    crossingsdistances.append((abs(ty) + abs(pos[0]), totalsteps))
            pos[1] = newy
            newsteps += number
        elif letter == 'L':
            newx = pos[0] - number
            for tx, y1, y2, steps in vertical:
                if y1 > y2:
                    y1, y2 = y2, y1
                if newx < tx < pos[0] and y1 < pos[1] < y2:
                    totalsteps = steps + newsteps + abs(tx - pos[0]) + abs(pos[1] - y1)
                    crossingsdistances.append((abs(tx) + abs(pos[1]), totalsteps))
            pos[0] = newx
            newsteps += number
    return crossingsdistances

def plotPaths(coords1, coords2):
    x1 = np.array(coords1[0])
    x2 = np.array(coords2[0])
    y1 = np.array(coords1[1])
    y2 = np.array(coords2[1])
    plt.plot(x1,y1,'b')
    plt.plot(x2,y2,'r')
    plt.show()

if __name__ == '__main__':
    path1, path2 = readInput()
    horizontal, vertical, coords = createPath(path1)
    horizontal2, vertical2, coords2 = createPath(path2)
    distances = checkCrossings(path2, horizontal, vertical)
    mindist = distances[0][0]
    minsteps = distances[0][1]
    print(distances)
    for i in range(1, len(distances)):
        if distances[i][0] < mindist:
            mindist = distances[i][0]
        if distances[i][1] < minsteps:
            minsteps = distances[i][1]
    plotPaths(coords, coords2)
    print('Closest intersection at:', mindist)
    print('Minimum steps to an intersection:', minsteps)