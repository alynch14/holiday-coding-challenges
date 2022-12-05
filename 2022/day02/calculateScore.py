
def main():
    options = {'X': 1, 'Y': 2, 'Z': 3}
    total_score = 0
    with open('rockPaperScissorSheet.txt', 'r') as file:
        for line in file:
            outcomeList = line.split(" ")
            elfHand = str(outcomeList[0])
            myHand = str(outcomeList[1].replace('\n', ''))
            print(elfHand)
            print(myHand)
            total_score += int(options[myHand])
            if elfHand == 'A' and myHand == 'X':
                total_score += 3
            elif elfHand == 'A' and myHand == 'Y':
                total_score += 6
            elif elfHand == 'B' and myHand == 'Y':
                total_score += 3
            elif elfHand == 'B' and myHand == 'Z':
                total_score += 6
            elif elfHand == 'C' and myHand == 'X':
                total_score += 6
            elif elfHand == 'C' and myHand == 'Z':
                total_score += 3
    print(total_score)
    everyMatchIsDraw()
 
def everyMatchIsDraw():
    options = {'A': 1, 'B': 2, 'C': 3}
    total_score = 0
    with open('rockPaperScissorSheet.txt', 'r') as file:
        for line in file:
            outcomeList = line.split(" ")
            elfHand = str(outcomeList[0])
            myHand = str(outcomeList[1].replace('\n', ''))
            if myHand == 'X' and elfHand == 'A':
                total_score += options['C']
            elif myHand == 'X' and elfHand == 'B':
                total_score += options['A']
            elif myHand == 'X' and elfHand == 'C':
                total_score += options['B']
            elif myHand == 'Y':
                total_score += 3 + options[elfHand]
            elif myHand == 'Z' and elfHand == 'A':
                total_score += 6 + options['B']
            elif myHand == 'Z' and elfHand == 'B':
                total_score += 6 + options['C']
            elif myHand == 'Z' and elfHand == 'C':
                total_score += 6 + options['A']
    print(total_score)


if __name__ == "__main__":
    main()