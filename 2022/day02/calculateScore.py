

class Rock():
    score = 1
    character = 'A'

class Paper():
    score = 2
    character = 'B'

class Scissor():
    score = 3
    character = 'C'


def main():
    options = {'A': 1, 'B': 2, 'C': 3}
    total_score = 0
    with open('rockPaperScissorsSheet.txt', 'r') as file:
        for line in file:
            


if __name__ == "__main__":
    main()