# Advent of code - 2016 day 1
# url: http://adventofcode.com/2016/day/1
# solution by Anton Sabah Ryberg 2017-10-10

# Declare variables
directions = ['N','E','S','W','N']
instructions = []  # ex. R2, L3, R5, R1, R1
myTravel = []

# Initial position
curHeading = 'N'
curPosX = 0
curPosY = 0
myTravel.append([curPosX, curPosY])

# Read input.txt
file_obj = open('d1_input.txt','r')
rawinput = file_obj.read()

instructions = rawinput.strip().split(', ')

for instruction in instructions:
    turn = instruction[0]
    steps = instruction[1:]

    # Update new heading
    if turn == 'R':
        a = directions.index(curHeading)
        a = a+1
        curHeading = directions[a]
    elif turn == 'L':
        a = directions.index(curHeading)
        if a == 0:
            a = 4
        a = a-1
        curHeading = directions[a]
    else:
        print("Something went wrong!")

    for s in range(int(steps)):
        if curHeading == 'W':
            curPosX = curPosX-1
        elif curHeading == 'E':
            curPosX = curPosX+1
        elif curHeading == 'N':
            curPosY = curPosY+1
        elif curHeading == 'S':
            curPosY = curPosY-1
        myTravel.append([curPosX, curPosY])

# Part One
finPosX = myTravel[len(myTravel)-1][0]
finPosY = myTravel[len(myTravel)-1][1]
pX = finPosX
pY = finPosY
if finPosX < 0:
    pX = finPosX * -1
if finPosY < 0:
    pY = finPosY * -1
part_one_answer = pX + pY
print("The final position is X: " + str(finPosX) + " Y: " + str(finPosY) + " and the answer to part one is: " + str(part_one_answer))

# Part Two
a_counter = 0
lookup = [0, 0]
result_found = 0
while int(a_counter) < len(myTravel) and result_found == 0:
    lookup = myTravel[a_counter]
    result = myTravel.index(lookup)
    if result < a_counter:
        result_found = 1
    a_counter = a_counter + 1
finPosX = myTravel[result][0]
finPosY = myTravel[result][1]
pX = finPosX
pY = finPosY
if finPosX < 0:
    pX = finPosX * -1
if finPosY < 0:
    pY = finPosY * -1
part_two_answer = pX + pY
print("The final position is X: " + str(finPosX) + " Y: " + str(finPosY) + " and the answer to part two is: " + str(part_two_answer))
