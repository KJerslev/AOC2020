# Problem 8 - boot loader

with open('input.dat', 'r') as f:
    input = [line.rstrip() for line in f]

position = 0
accumulator = 0
positions = []


def nop():
    global position
    position += 1
    read_command(position)


def acc(value):
    global accumulator
    accumulator += value
    nop()


def jmp(value):
    global position
    position += value
    read_command(position)


def read_command(Position):
    global input, positions
    command = input[Position]
    action = command[0:3]
    value = int(command[3:])
    if Position in positions:
        return
    else:
        positions.append(Position)
    if action == "nop":
        nop()
    elif action == "acc":
        acc(value)
    else:
        jmp(value)


read_command(0)
print("Part 1: The value of the accumulator just before a command is executed a second time: " + str(accumulator))
