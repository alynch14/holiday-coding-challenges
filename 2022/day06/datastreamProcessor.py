from collections import deque
#first 4 non-matching characters mark beginning of data packet
def get_start_of_packet():
    datastream = ''
    with open('input.txt', 'r') as file:
        datastream = str(file.readline())
    characterList = deque([])
    streamStart = 0
    for char in datastream:
        streamStart += 1
        if streamStart < 5:
            characterList.append(char)
        else:
            characterList.popleft()
            characterList.append(char)
        if len(characterList) == 4:
            print(characterList.count(char))
            uniqueCounter = 0
            for character in characterList:
                uniqueCounter += characterList.count(character)
            if uniqueCounter == 4:
                return streamStart

def get_start_of_message():
    datastream = ''
    with open('input.txt', 'r') as file:
        datastream = str(file.readline())
    characterList = deque([])
    streamStart = 0
    for char in datastream:
        streamStart += 1
        if streamStart < 15:
            characterList.append(char)
        else:
            characterList.popleft()
            characterList.append(char)
        if len(characterList) == 14:
            print(characterList.count(char))
            uniqueCounter = 0
            for character in characterList:
                uniqueCounter += characterList.count(character)
            if uniqueCounter == 14:
                return streamStart



if __name__ == '__main__':
    print(get_start_of_packet())
    print(get_start_of_message())