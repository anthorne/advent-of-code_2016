import sys
import time

# Declare variables
display = ['..................................................',
           '..................................................',
           '..................................................',
           '..................................................',
           '..................................................',
           '..................................................']
instructions = []


# Read instructions from file
def readInput():
    # fileObj = open('d8_example.txt', 'r')
    fileObj = open('d8_input.txt', 'r')
    for line in fileObj:
        if line != '\n':
            instructions.append(line.strip())


# Print text on specific position
def print_there(x, y, text):
     sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
     sys.stdout.flush()


# Prints the current display
def getDisplay():
    header = "==[ Easter Bunny HQ ]=============================\n"
    print_there(4, 5, header)
    cr=5
    for row in display:
        print_there(cr,5,row)
        cr=cr+1
    print_there(11,5, "==================================================")

# Turn on a single pixel at x:y - b; 1: On, 0: Off
def pix(x, y, b):
    row = display[y]
    cx=0
    updatedRow = ""
#    print "updating x: " + str(x) + "  y: " + str(y) + "  setting pixel on: " + str(b)
    while cx-1 < x:
        if cx == x:
            if b == 1:
                updatedRow = updatedRow + "#" + str(row[cx+1:])
            elif b == 0:
                updatedRow = updatedRow + "." + str(row[cx+1:])
            else:
                updatedRow = updatedRow + str(row[cx:cx+1]) + str(row[cx+1:])
        else:
            updatedRow = updatedRow + row[cx:cx+1]
        cx=cx+1
    display[y] = updatedRow


# Create a small rectangle. Param ex. 3x2
def rect(param):
    param = param.split('x')
    x = int(param[0])
    y = int(param[1])
    cx=0
    cy=0
    while cy < y:
#        print " y : " + str(cy)
        while cx < x:
#            print "  x : " + str(cx)
            # Turn on a pixel at position cx:cy
            pix(cx, cy, 1)
            cx=cx+1
        cx=0
        cy=cy+1

# Returns the state of a pixel; 0 = off, 1 = on
def getPix(x, y):
    state = 0
    row = display[y]
    cx=0
    pix = ""
#    print "updating x: " + str(x) + "  y: " + str(y) + "  setting pixel on: " + str(b)
    while cx-1 < x:
        if cx == x:
            pix = str(row[cx:cx+1])
        cx=cx+1
    if pix == "#":
        state = 1
    elif pix == ".":
        state = 0
    else:
        print(' - error in getPix()-function -')
    return state


# Rotates the array input by (step) number of steps
def rotateArray(arr, step):
    arrIn = arr
    arrLen = len(arr)
    cs = 0
    ca = 0
    # Iterate number of steps to shift
    while cs < step:
        result = []
        # Iterate number of array positions
        while ca < arrLen:
            # If the first array position - take the last one
            if ca == 0:
                result.append(arrIn[arrLen-1])
            else:
                result.append(arrIn[ca-1])
            ca=ca+1
        ca=0
        arrIn = result
        cs=cs+1
    return result


# Rotates the column (x) down by (p) pixels
def rotateCol(x, p):
    # Get column
    col = []
    cr=0
    for row in display:
        col.append(getPix(x,cr))
        cr=cr+1
    # Shift column-array
    col = rotateArray(col,p)
    # Update display with new array
    colLen = len(col)
    cl=0
    while cl < colLen:
        pix(x,cl,col[cl])
        cl=cl+1


# Rotates the row (y) by (p) pixels
def rotateRow(y, p):
    # Get row
    row = []
    rowLen = len(display[y])
    cl=0
    while cl < rowLen:
        row.append(getPix(cl,y))
        cl=cl+1
    # Shift row-array
    row = rotateArray(row,p)
    # Update display with new array
    cl=0
    while cl < rowLen:
        pix(cl,y,row[cl])
        cl=cl+1


# Main program

readInput()
for instr in instructions:
    iSplit = instr.split(' ')
    if iSplit[0] == 'rect':
        rect(iSplit[1])
    elif iSplit[0] == 'rotate' and iSplit[1] == 'column':
        x = int(iSplit[2].split('=')[1])
        p = int(iSplit[4])
        rotateCol(x, p)
    elif iSplit[0] == 'rotate' and iSplit[1] == 'row':
        y = int(iSplit[2].split('=')[1])
        p = int(iSplit[4])
        rotateRow(y, p)

    getDisplay()
    time.sleep(0.05)


# Count lit pixels
litPixels = 0
rc = 20
for row in display:
    litPixels = litPixels + int(str(row).count('#'))
#    text = str(row) + " --- pixels on: " + str(litPixels)
#    print_there(rc,5,text)
    rc += 1

text = "Pixels lit: " + str(litPixels)
print_there(12, 5, text)
