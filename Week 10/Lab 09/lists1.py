list1 = [4, 1, 2, 3, 4]
list2 = [1, 3, 5, 7]


# set up a variable called odds and calculate the number of odd numbers in
# a list. If you calculate odds for list1, 2 should be printed;
# if on list 2, 4 should be printed

# List 2
odds = 0
for item in list2:
    if item % 2 == 1:
        odds += 1

print(odds)


# set up a variable called newList that contains original list elements
# rotated to the right (you should probably use some of the Python built-in
# list methods - check Python docs)
# for list1 the new list should result in [4, 4, 1, 2, 3]
# for list2 the new list should result in [7, 1, 3, 5]

# List 2
newList = [list2[-1]] + list2[:-1]

print(newList)


# set up a variable called anotherList that contains original list elements
# multiplied by a number entered by a user, except when the original list number
# is already a multiple of the number entered by the user, for example
# for list1 and a value 3,
# anotherList should contain [12, 3, 6, 3, 12]

anotherList = []
multiplier = int(input("Enter a multiplier: "))
for item in list1:
    if item % multiplier != 0:
        anotherList += [item * multiplier]
    else:
        anotherList += [item]


print(anotherList)


# check whether the first or the last value in a list is larger and replace
# all original values in a list with the larger of the two, for example,
# the new version of list1, called changedList and will contain [4, 4, 4, 4, 4]

changedList = []
if list1[0] > list1[-1]:
    for i in range(len(list1)):
        changedList += [list1[0]]
else:
    for i in range(len(list1)):
        changedList += [list1[-1]]

print(changedList)
