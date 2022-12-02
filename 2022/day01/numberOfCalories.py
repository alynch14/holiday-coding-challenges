def main():
    most_calories()
    top_three_total_calories()

def most_calories():
    mostCalories = 0
    currentCalories = 0
    with open('elfCalorieList.txt', 'r') as calorieFile:
        for line in calorieFile:
            if line == "\n":
                if currentCalories > mostCalories:
                    mostCalories = currentCalories
                currentCalories = 0
            else:
                currentCalories += int(line)
    print(mostCalories)
    print("\n")

def top_three_total_calories():
    topOne = 0
    topTwo = 0
    topThree = 0
    currentCalories = 0
    with open('elfCalorieList.txt', 'r') as calorieFile:
        for line in calorieFile:
            if line == "\n":
                if currentCalories > topOne:
                    topThree = topTwo
                    topTwo = topOne
                    topOne = currentCalories
                elif currentCalories > topTwo:
                    topThree = topTwo
                    topTwo = currentCalories
                elif currentCalories > topThree:
                    topThree = currentCalories
                currentCalories = 0
            else:
                currentCalories += int(line)
    totalCalories = topOne + topTwo + topThree
    print(totalCalories)


if __name__ == "__main__":
    main()