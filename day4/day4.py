input = '359282-820401'

def checkrules(number:str):
    check1 = False
    check2 = True
    check3 = False
    combos = []
    counter = 1
    for i in range(1,len(number)):
        if number[i] == number[i-1]:
            counter += 1
        else:
            combos.append(counter)
            counter = 1
        if number[i] < number[i-1]:
            check2 = False
    if counter > 1:
        combos.append(counter)
    for combo in combos:
        if combo >= 2:
            check1 = True
        if combo == 2:
            check3 = True
    return check1 and check2, check2 and check3

if __name__ == '__main__':
    low, high = list(map(lambda x: int(x), input.split('-')))
    totalavailable1 = 0
    totalavailable2 = 0
    for number in range(low, high+1):
        test1, test2 = checkrules(str(number))
        if test1:
            totalavailable1 += 1
        if test2:
            totalavailable2 += 1
    print('Number allowed passwords for first part:', totalavailable1)
    print('Number allowed passwords for second part', totalavailable2)
