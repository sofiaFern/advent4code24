import csv


def isIncreasing(firstVal, secondVal):

    return firstVal < secondVal

def isWithinRange(firstVal, secondVal):

    return abs(secondVal - firstVal) <= 3

with open('challenge_inputs/day2_input.csv', 'r') as file:
    reader = csv.reader(file)

    # 1. cleaning data
    levels = [[int(x) for x in row[0].split(' ')] for row in reader]

## Part 1 ##
def levelIsSafe(level):
    # foundation for each level
    increaseBool = isIncreasing(level[0], level[1])

    for i in range(len(level) - 1):
        if  level[i]!= level[i+1] and isWithinRange(level[i], level[i+1]) and increaseBool == isIncreasing(level[i], level[i+1]):
            continue
    
        return False

    return True

def removeOneLevel(level):
    for i in range(len(level)):
        new_level = level[:i] + level[i+1:]
        if levelIsSafe(new_level):
            return True
    # print(f'Didnt pass {level}')
    return False

safeCount = 0
for level in levels:
    # print(f'starting level: {level}')
    
    if levelIsSafe(level):
        safeCount += 1 
        # print('Original level is safe')
    elif removeOneLevel(level): # Part 2 included here
        safeCount += 1
        # print('Removing one works')
    
print(f'safeCount: {safeCount}')
