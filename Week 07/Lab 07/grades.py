# This program prompts the user for five scores.
# It then shows the letter grade equivalent of each entered score.
# Finally, it prints the average of all five scores, as well as the letter grade equivalent of the average score.

# Main is the "main" function of the program - it calls all other functions.
# It is the only function called outside of the scope of another function, at the bottom.
# main() does not require any arguments.
def main():
    score1 = float(input("Enter test score 1: "))
    score2 = float(input("Enter test score 2: "))
    score3 = float(input("Enter test score 3: "))
    score4 = float(input("Enter test score 4: "))
    score5 = float(input("Enter test score 5: "))

    showScores(score1)
    showScores(score2)
    showScores(score3)
    showScores(score4)
    showScores(score5)

    calcAverage(score1, score2, score3, score4, score5)

# showScores() prints the score passed as an argument as well as its letter grade equivalent,
# by calling printLetterGrade() in the print statement.
# showScores() expects one score as an argument.
def showScores(score):
    # The showScores() outputs in the instructions have no trailing zeros - a behavior of ints and specifically formatted floats.
    # Since it's not specified if that's intentional or not, I'll convert
    # score to an int for visual consistency.
    # Number accuracy is not lost doing this, so I imagine it's fine.
    print("{} is {}". format(int(score), printLetterGrade(score)))

# printLetterGrade() finds the letter grade equivalent for any score between 0 and 100.
# It returns the letter grade equivalent, rather than printing it, which allows the letter grade equivalent
# to be included in a print statement elsewhere.
# printLetterGrade expects one score as an argument.
def printLetterGrade(score):
    letterGrade = "A"
    if score < 60:
        letterGrade = "F"
    elif score < 70:
        letterGrade = "D"
    elif score < 80:
        letterGrade = "C"
    elif score < 90:
        letterGrade = "B"
    return letterGrade

# calcAverage() determines the average of all five scores, as well as the equivalent letter grade, and prints both.
# calcAverage() expects five scores as arguments.
def calcAverage(score1, score2, score3, score4, score5):
    average = (score1 + score2 + score3 + score4 + score5) / 5
    print("The average is: {} which is {}".format(average, printLetterGrade(average)))

main()
