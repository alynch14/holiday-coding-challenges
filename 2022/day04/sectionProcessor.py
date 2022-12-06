
def main():
    totalOverlap = 0
    totalSections = 0
    with open('input.txt', 'r') as file:
        for line in file:
            elfList = line.replace('\n', '').split(',')
            elf1 = elfList[0].split('-')
            print(elf1)
            elf2 = elfList[1].split('-')
            print(elf2)
            totalSections += get_all_overlapping_sections(int(elf1[0]), int(elf2[0]), int(elf1[1]), int(elf2[1]))
            if int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1]):
                print('if')
                totalOverlap += 1
                print(totalOverlap)
            elif int(elf2[0]) <= int(elf1[0]) and int(elf2[1]) >= int(elf1[1]):
                print('elif')
                totalOverlap += 1
                print(totalOverlap)
    print(totalOverlap)
    print(totalSections)

def get_all_overlapping_sections(lowerBound1: int, lowerBound2: int, upperBound1: int, upperBound2: int):
    totalSections = 0
    if lowerBound1 <= upperBound2 and lowerBound1 >= lowerBound2:
        totalSections += 1
    elif upperBound1 <= upperBound2 and upperBound1 >= lowerBound2:
        totalSections += 1
    elif lowerBound2 <= upperBound1 and lowerBound2 >= lowerBound1:
        totalSections += 1
    elif upperBound2 <= upperBound1 and upperBound2 >= lowerBound1:
        totalSections += 1
    return totalSections
    
            

if __name__ == '__main__':
    main()