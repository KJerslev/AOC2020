# Problem 5 - flight seats

def lower(x):
    length = len(x)
    return x[0:length//2]


def upper(x):
    length = len(x)
    return x[length//2:length]


with open('inputdata.txt', 'r') as fd:
    lines = [line.rstrip() for line in fd]

# Part 1
rows = list(range(0, 128))
cols = list(range(0, 8))
seatIDs = []

for bcard in lines:
    row = rows
    col = cols
    for char in bcard[0:-3]:
        if char == "B":
            row = upper(row)
        elif char == "F":
            row = lower(row)

    for char in bcard[-3:]:
        if char == "R":
            col = upper(col)
        elif char == "L":
            col = lower(col)

    row = row[0]
    col = col[0]
    seatIDs.append(8 * row + col)

print("Part 1: The maximum seatID is: " + str(max(seatIDs)))

# Part 2
sortedIDs = sorted(seatIDs)
print("Part 2: Missing seatID: " + str(list(set(range(min(sortedIDs), max(sortedIDs))) - set(sortedIDs))[0]))
