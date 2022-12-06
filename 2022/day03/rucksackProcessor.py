
from ctypes import sizeof


numberKeyDict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
    'A': 27,
    'B': 28,
    'C': 29,
    'D': 30,
    'E': 31,
    'F': 32,
    'G': 33,
    'H': 34,
    'I': 35,
    'J': 36,
    'K': 37,
    'L': 38,
    'M': 39,
    'N': 40,
    'O': 41,
    'P': 42,
    'Q': 43,
    'R': 44,
    'S': 45,
    'T': 46,
    'U': 47,
    'V': 48,
    'W': 49,
    'X': 50,
    'Y': 51,
    'Z': 52
}

def main():
    totalWeight = 0
    with open('input.txt', 'r') as file:
        for line in file:
            # print(len(line)/2)
            line = line.replace('\n', '')
            # print (len(line))
            totalWeight += search_string(line[:len(line)//2], line[len(line)//2:])
    print(totalWeight)
    totalBadgePriority()

def search_string(firstString: str, secondString: str):
    for char in firstString: 
        print(char)
        if secondString.__contains__(char):
            print(numberKeyDict[char])
            return numberKeyDict[char]
            
def totalBadgePriority():
    totalWeight = 0
    with open('input.txt', 'r') as file:
        lineList = []
        counter = 0
        for line in file:
            counter += 1
            lineList.append(line.replace('\n', ''))
            if counter % 3 == 0:
                str1 = str(lineList.pop())
                print(str1)
                str2 = str(lineList.pop())
                print(str2)
                str3 = str(lineList.pop())
                print(str3)
                totalWeight += get_shared_badge_weight(str1, str2, str3)
    print(totalWeight)

def get_shared_badge_weight(one: str, two: str, three: str):
    for char in one:
        if two.__contains__(char) and three.__contains__(char):
            print(char)
            return numberKeyDict[char]


if __name__ == '__main__':
    main()