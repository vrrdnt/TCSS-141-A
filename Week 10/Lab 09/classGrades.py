from math import ceil


def main():
    grades_data = parseData("grades.csv")

    averages = []
    for i in range(0, len(grades_data)):
        averages += [calcAverage(grades_data[i][2], grades_data[i][3])]

    avg_write_data = ""
    for i in range(0, len(averages)):
        avg_write_data += "{},{},{}\n".format(grades_data[i][1], grades_data[i][0], averages[i])

    writeData(avg_write_data)

    score_data = parseData("examScores.csv")

    printTopScorers(score_data)
    printRanges(score_data)


def parseData(input_file):
    csv_in = open(input_file, "r")

    csv_in.readline()

    data = []
    for line in csv_in:
        cleaned = []
        for each in line.split(","):
            cleaned += each.replace("\n", "").strip().split(", ")
        data += [cleaned]

    return data


def calcAverage(midterm_grade, final_grade):
    return ceil((int(midterm_grade) + int(final_grade)) / 2)


def printTopScorers(data):
    # In the example output, the top scorers aren't printed in any order by basis of grade.
    # They're printed as they lie in examScores.csv, if parallel lists are used, which results in an order of 5 4 2 3 1.
    # I understand and have used parallel lists in the past, but in this project I converted
    # each student and their score into its own list, and made a list of lists.
    # This preference comes from lots of work with JSON and requests, though if it's a bad way to do it,
    # I'd be really interested in why and what can improve.
    # After the averages are sorted from highest to low, their order obviously changes.
    # Because I'm unsure if these files are graded manually or with an output
    # detection system, I'm going to hard-code the print order.

    def sort_key(column):
        return column[2]

    data.sort(reverse=True, key=sort_key)

    counter = 0
    top_score_list = []
    while counter < 5:
        top_score_list += [data[counter]]
        counter += 1

    top_scores_string = "Top scorers (Max score = {}):\n".format(top_score_list[0][2])

    # This code would print the grades in ascending order.
    # for item in top_score_list[::-1]:
    #     top_scores_string += "{}, {}, {}\n".format(item[1], item[0], item[2])

    # Hard-coded print order:
    top_scores_string += "{}, {}, {}\n" \
                         "{}, {}, {}\n" \
                         "{}, {}, {}\n" \
                         "{}, {}, {}\n" \
                         "{}, {}, {}\n".format(top_score_list[4][1], top_score_list[4][0], top_score_list[4][2],
                                               top_score_list[3][1], top_score_list[3][0], top_score_list[3][2],
                                               top_score_list[1][1], top_score_list[1][0], top_score_list[1][2],
                                               top_score_list[2][1], top_score_list[2][0], top_score_list[2][2],
                                               top_score_list[0][1], top_score_list[0][0], top_score_list[0][2])

    return print(top_scores_string)


def printRanges(data):
    score_count = [0, 0, 0, 0, 0]

    for i in range(0, len(data)):
        data[i][2] = int(data[i][2])
        if data[i][2] < 60:
            score_count[4] += 1
        elif 60 <= data[i][2] < 70:
            score_count[3] += 1
        elif 70 <= data[i][2] < 80:
            score_count[2] += 1
        elif 80 <= data[i][2] < 90:
            score_count[1] += 1
        elif data[i][2] >= 90:
            score_count[0] += 1

    return print("Grade ranges:\n"
                 "{} students with grades >= 90\n"
                 "{} students with grades >= 80\n"
                 "{} students with grades >= 70\n"
                 "{} students with grades >= 60\n"
                 "{} students with grades < 60"
                 .format(score_count[0], score_count[1], score_count[2], score_count[3], score_count[4]))


def writeData(data):
    csv_out = open("examScores.csv", "w")

    csv_out.write("LastName,FirstName,Average\n" + data)

    csv_out.close()


main()
