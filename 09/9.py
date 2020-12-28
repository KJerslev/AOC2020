# Problem 9 - Encoding error
# Part 1: Find the first number is a series of numbers that is not the sum of two previous numbers.

from itertools import combinations

with open('input.dat', 'r') as fd:
    numbers = [int(line.rstrip()) for line in fd]

preamble = 25        # How many numbers to be ignored
FirstInvalid = 0
FirstInvalidPos = 0


def check_number(pos):
    global FirstInvalid, FirstInvalidPos
    startpos = pos - preamble
    combs = [lst for lst in combinations(numbers[startpos:pos], 2)]     # Create list of unique combinations of numbers
    sums = [sum(i) for i in combs]
    if numbers[pos] in sums:
        check_number(pos + 1)
    else:
        FirstInvalid = numbers[pos]
        FirstInvalidPos = pos
        print("Part 1: " + str(numbers[pos]) + " is the first number not equal to a sum")


check_number(preamble)

# Part 2

ListOfNumbers = numbers[:FirstInvalidPos]


def get_contiguous_lst():
    for i in range(0, FirstInvalidPos):
        for j in range(i, FirstInvalidPos):
            contiguousList = numbers[i:j]
            if sum(contiguousList) == FirstInvalid:
                return contiguousList


Part2Lst = get_contiguous_lst()

print("Part 2: The minimum value in the contiguous list is: " + str(min(Part2Lst)))
print("Part 2: The maximum value in the contiguous list is: " + str(max(Part2Lst)))
print("Part 2: Their sum is: " + str(min(Part2Lst) + max(Part2Lst)))
