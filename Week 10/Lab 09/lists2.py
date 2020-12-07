def main():
    input_nums = input("Enter numbers separated by commas: ")
    input_search = input("Enter a number to look for: ")

    collectNums(input_nums, input_search)


def collectNums(nums, search):
    input_nums = nums.split(",")

    counter = 0
    for item in input_nums:
        if item == search:
            counter += 1

    return print("Appeared {} times.\nConstitutes {:.0%} of this data set."
                 .format(counter, (counter / len(input_nums))))


main()
