# Declaration of variables
instructions = []

# Read input
file_obj = open('d2_input.txt', 'r')
for line in file_obj:
    instructions.append(line.strip())
file_obj.close()

# Part one

#  1 2 3
#  4 5 6
#  7 8 9

keypad = [[7, 8, 9],
          [4, 5, 6],
          [1, 2, 3]]

#  y 2
#  y 1 +
#  y 0 1 2
#    x x x

curPosX = 1
curPosY = 1

# Part two

#      1
#    2 3 4
#  5 6 7 8 9
#    A B C
#      D

p2keypad = [['x', 'x', 'D', 'x', 'x'],
            ['x', 'A', 'B', 'C', 'x'],
            [5, 6, 7, 8, 9],
            ['x', 2, 3, 4, 'x'],
            ['x', 'x', 1, 'x', 'x']]

#  y 4
#  y 3
#  y 2   +
#  y 1
#  y 0 1 2 3 4
#    x x x x x

p2curPosX = 2
p2curPosY = 2

code = ""
p2code = ""

for instruction in instructions:
    if instruction != "":
        for char in instruction:

            # Part one
            if (char.lower() == 'u' and curPosY < 2):
                curPosY = curPosY +1
            elif (char.lower() == 'd' and curPosY > 0):
                curPosY = curPosY -1
            elif (char.lower() == 'l' and curPosX > 0):
                curPosX = curPosX -1
            elif (char.lower() == 'r' and curPosX < 2):
                curPosX = curPosX +1

            # Part two
            if (char.lower() == 'u' and p2curPosY < 4 and p2keypad[p2curPosY+1][p2curPosX] != 'x'):
                p2curPosY = p2curPosY +1
            elif (char.lower() == 'd' and p2curPosY > 0 and p2keypad[p2curPosY-1][p2curPosX] != 'x'):
                p2curPosY = p2curPosY -1
            elif (char.lower() == 'r' and p2curPosX < 4 and p2keypad[p2curPosY][p2curPosX+1] != 'x'):
                p2curPosX = p2curPosX +1
            elif (char.lower() == 'l' and p2curPosX > 0 and p2keypad[p2curPosY][p2curPosX-1] != 'x'):
                p2curPosX = p2curPosX -1

        code = code + str(keypad[curPosY][curPosX])
        p2code = p2code + str(p2keypad[p2curPosY][p2curPosX])
print("The code for part one is: " + code)
print("The code for part two is: " + p2code)
