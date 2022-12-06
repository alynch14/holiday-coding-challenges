
#This one's a dooosey
def main():
    tempStacks = [
        ['V', 'C', 'D', 'R', 'Z', 'G', 'B', 'W'],
        ['G', 'W', 'F', 'C', 'B', 'S', 'T', 'V'],
        ['C', 'B', 'S', 'N', 'W'],
        ['Q', 'G', 'M', 'N', 'J', 'V', 'C', 'P'],
        ['T', 'S', 'L', 'F', 'D', 'H', 'B'],
        ['J', 'V', 'T', 'W', 'M', 'N'],
        ['P', 'F', 'L', 'C', 'S', 'T', 'G'],
        ['B', 'D', 'Z'],
        ['M', 'N', 'Z', 'W']
    ]

    with open('input.txt', 'r') as file:
        for line in file:
            instruction = line.replace('\n', '').split(' ')
            numberToMove = int(instruction[1])
            print(numberToMove)
            fromStack = int(instruction[3])-1
            print(fromStack)
            toStack = int(instruction[5])-1
            print(toStack)
            counter = 0
            while counter < numberToMove:
                counter += 1
                tempStacks[toStack].append(tempStacks[fromStack].pop())
    for value in tempStacks:
        print(value.pop())

def multiple_crates_at_once():
    tempStacks = [
        ['V', 'C', 'D', 'R', 'Z', 'G', 'B', 'W'],
        ['G', 'W', 'F', 'C', 'B', 'S', 'T', 'V'],
        ['C', 'B', 'S', 'N', 'W'],
        ['Q', 'G', 'M', 'N', 'J', 'V', 'C', 'P'],
        ['T', 'S', 'L', 'F', 'D', 'H', 'B'],
        ['J', 'V', 'T', 'W', 'M', 'N'],
        ['P', 'F', 'L', 'C', 'S', 'T', 'G'],
        ['B', 'D', 'Z'],
        ['M', 'N', 'Z', 'W']
    ]

    with open('input.txt', 'r') as file:
        for line in file:
            instruction = line.replace('\n', '').split(' ')
            numberToMove = int(instruction[1])
            print(numberToMove)
            fromStack = int(instruction[3])-1
            print(fromStack)
            toStack = int(instruction[5])-1
            print(toStack)
            print(tempStacks[fromStack].__len__())
            index = tempStacks[fromStack].__len__() - numberToMove
            print(index)
            counter = 0
            while counter < numberToMove:
                counter += 1
                tempStacks[toStack].append(tempStacks[fromStack].pop(index))
    for value in tempStacks:
        print(value.pop())

if __name__ == '__main__':
    main()
    multiple_crates_at_once()