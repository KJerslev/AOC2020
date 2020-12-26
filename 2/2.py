# Problem 2 - Valid passwords

with open('inputdata.txt', 'r') as fd:
    lines = [line.rstrip().replace(":","").split() for line in fd]

# Part 1
validPasswords = 0
invalidPasswords = 0
for line in lines:
    reps = line[-1].count(line[-2])
    limits = line[0].split("-")
    if (reps >= int(limits[0]) and reps <= int(limits[-1])):
        validPasswords = validPasswords + 1
    else:
        invalidPasswords = invalidPasswords + 1

print("Part 1: The number of valid passwords is: " + str(validPasswords))

# Part 2
validPasswords = 0
invalidPasswords = 0
for line in lines:
    positions = [int(i) for i in line[0].split("-")]
    if (line[-1][positions[0]-1] != line[-1][positions[1]-1]) and ((line[-1][positions[0]-1] == line[-2]) or (line[-1][positions[1]-1] == line[-2])):
        validPasswords = validPasswords + 1
    else:
        invalidPasswords = invalidPasswords + 1

print("Part 2: The number of valid passwords is: " + str(validPasswords))