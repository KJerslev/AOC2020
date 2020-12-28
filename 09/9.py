# Problem 9 - Encoding error
# Part 1: Find the first number is a series of numbers that is not the sum of two previous numbers.

from itertools import combinations

with open('input.dat', 'r') as fd:
    numbers = [int(line.rstrip()) for line in fd]

preamble = 25        # How many numbers to be ignored

# Part 1


def check_number(pos):
    global numbers
    startpos = pos - preamble
    combs = [lst for lst in combinations(numbers[startpos:pos], 2)]     # Create list of unique combinations of numbers
    sums = [sum(i) for i in combs]
    if numbers[pos] in sums:
        check_number(pos + 1)
    else:
        print("Part 1: " + str(numbers[pos]) + " is the first number not equal to a sum")
    return [numbers[pos], pos]


FirstInvalidLst = check_number(preamble)

# # Part 2
#
# FirstInvalid = FirstInvalidLst[0]
# FirstInvalidPosition = FirstInvalidLst[1]
# ListOfNumbers = numbers[:FirstInvalidPosition]
#
# def check_sum(length):
#     for i in range(2,FirstInvalidPosition):
#         combs2 = [lst for lst in combinations(ListOfNumbers, i)]
#