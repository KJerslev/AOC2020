with open('inputdata.txt','r') as fd:
    numbers = [int(line.rstrip()) for line in fd]

# Part 1
for number in numbers:
    SumList = [number + x for x in numbers]
    index = numbers.index(number)
    # print(SumList)
    if 2020 in SumList:
        index2k = SumList.index(2020)
        print("Part 1: The two numbers that add to 2020 are: " + str(numbers[index]) + " and " + str(numbers[index2k]))
        print("Part 1: Product of the two numbers that add to 2020: " + str(int(numbers[index] * numbers[index2k])))
        break


# Part 2
numbersList = []
for number in numbers:
    SumList2 = [[number + x + y for x in numbers] for y in numbers]
    index1 = numbers.index(number)
    LocateList = [2020 in lst for lst in SumList2]
    if True in LocateList:
        index2 = LocateList.index(True)
        index3 = LocateList.index(True, index2+1)
        break

print("Part 2: The three numbers that add to 2020 are: " + str(numbers[index1]) + ", " + str(numbers[index2]) + " and " + str(numbers[index3]))
print("Part 2: Product of the three numbers that add to 2020 is: " + str(numbers[index1]*numbers[index2]*numbers[index3]))