# Declare variables
output = ""
# filename = 'd9_example.txt'
filename = 'd9_input.txt'


def isinstruction(inst):
    isinstr = False
    instarr = []
    if inst.find('x') > 0:
        instarr = inst.split('x')
        # a = int(instarr[0])
        # b = int(instarr[1])
        # print("a: " + str(a) + " b: " + str(b))
        isinstr = True
    # print(" I AM HERE AND I AM : " + str(isinstr) + " inst is: " + str(inst) +
    # "   and instarr : " + str(instarr) + "  and the result of find x is: " + str(inst.find('x')))
    return isinstr


# Read file
fileObj = open(filename, 'r')
for line in fileObj:
    if line != '\n':
        row = line
fileObj.close()

rowLen = len(row.strip())
print(' --- Part one ---')
print("The compressed input length is: " + str(rowLen))

# print row

paraFound = False
instruction = ""
numChars = 0
numReps = 0
charsRep = ""

for char in row:

    # As long we do not have to take care of any repetition
    if (numChars == 0) and (numReps == 0):
        charsRep = ""

        # When the first parentheses is found set the flag = True
        if (not paraFound) and (char == '('):
            paraFound = True

        # If the first parentheses is found record the instruction as long as no more parentheses is found
        elif paraFound and (char != ")") and (char != "("):
            instruction = instruction + char

        # If the last parentheses is found stop record the instruction and check it out!
        elif paraFound and (char == ")"):
            # print("                     analyze this as a instruction: " + instruction)

            if isinstruction(instruction):
                numChars = int((instruction.split('x'))[0])
                numReps = int((instruction.split('x'))[1])
                # print("Will take this number of subsequent chars: "
                # + str(numChars) + " and repeat them this many times: " + str(numReps))

            elif not isinstruction(instruction):
                output = output + "(" + instruction + ")"

            paraFound = False
            instruction = ""

        # As long as no parentheses is found, append the output..
        elif not paraFound:
            output = output + char

        # No idea if there are other scenarios at this moment.
        else:
            print(" this needs to be considered! ")

    else:
        # print("now we have something to do...")
        if numChars > 0:
            charsRep = charsRep + char
            numChars = numChars - 1
        # print("adding chars to repeat: " + str(charsRep) + "    numChars is now: " + str(numChars))

        if numChars == 0:
            cnr = 0
            while cnr < numReps:
                # print("adding the repeated chars : " + charsRep + "
                # and repeat them : " + str(numReps) + " times... counting: " + str(cnr))
                output = output + charsRep
                cnr = cnr + 1
                if cnr == numReps:
                    numReps = 0

        # return to normal
        paraFound = False
        instruction = ""

    # Return result

# print output
print("The total length of the output is: " + str(len(output.strip())))
print(" --- Part two ---")


def count_chars(input_string):
    paraFound = False
    instruction = ""
    numChars = 0
    numReps = 0
    charsRep = ""
    decompressed_size = 0

    for char in input_string:

        # As long we do not have to take care of any repetition
        if (numChars == 0) and (numReps == 0):
            charsRep = ""

            # When the first parentheses is found set the flag = True
            if (not paraFound) and (char == '('):
                paraFound = True

            # If the first parentheses is found record the instruction as long as no more parentheses is found
            elif paraFound and (char != ")") and (char != "("):
                instruction = instruction + char

            # If the last parentheses is found stop record the instruction and check it out!
            elif paraFound and (char == ")"):
                if isinstruction(instruction):
                    numChars = int((instruction.split('x'))[0])
                    numReps = int((instruction.split('x'))[1])
                elif not isinstruction(instruction):
                    decompressed_size += len(str("(" + instruction + ")"))
                paraFound = False
                instruction = ""

            # As long as no parentheses is found, add +1 to decompressed_size..
            elif not paraFound:
                decompressed_size += 1
        else:
            if numChars > 0:
                charsRep = charsRep + char
                numChars = numChars - 1
            if numChars == 0:
                # 2017-10-26 - Send _charsRep_ to a function counting chars here - ex. '(3x5)ICQ(9x5)IYUPTHPKX'
                # take the returned number of chars from the counting function and multiply it with _numReps_
                # then skip the while loop below because no _output_ will be saved, set _numReps_ = 0
                decompressed_size += numReps * count_chars(charsRep)
                numReps = 0
            # return to normal
            paraFound = False
            instruction = ""
    return decompressed_size


# print output
print("The total length of the output is: " + str(count_chars(row) - 1))
