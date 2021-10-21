
# Read input to lines-array
lines = []
# fileObj = open('d7_example.txt', 'r')
# fileObj = open('d7_example2.txt', 'r')
fileObj = open('d7_input.txt', 'r')
for line in fileObj:
    if line != "\n":
        lines.append(line.strip())
fileObj.close()


# Returns an array of parts
def getParts(row):
    stuff = []
    row = row.replace('[', '|[')
    row = row.replace(']', ']|')
    stuff = row.split('|')
    return stuff


# Returns an array of parts separated from brackets, [0, 'text'].
# The first part if flagged if the text was surronded by brackets or not; 0 = no brackets, 1 = brackets
def sortBrackets(parts):
    stuff = []
    for part in parts:
        if part[0] == '[':
            brackets = 1
            part = part.strip('[]')
        else:
            brackets = 0
        stuff.append([brackets, part])
    stuff.sort(reverse=True)
    return stuff


# Check if the four characters is TLS, ex. abba
# (any four-character sequence which consists of a pair of two different characters
# followed by the reverse of that pair, such as xyyx or abba.)
def isTLS(fourChar):
    result = False
    if len(fourChar) == 4:
        c1 = fourChar[0:1]
        c2 = fourChar[1:2]
        c3 = fourChar[2:3]
        c4 = fourChar[3:4]
        if c1 == c4 and c2 == c3:
            if c1 != c2:
                result = True
    return result


# Check if the three characters is BAB, ex. bab
def isBAB(threeChar):
    result = False
    if len(threeChar) == 3:
        c1 = threeChar[0:1]
        c2 = threeChar[1:2]
        c3 = threeChar[2:3]
        if c1 == c3 and c1 != c2:
            result = True
    return result


# Takes three chars and invert them, ex. bab -> aba
def getABA(bab):
    aba = " - Error in getABA() - "
    if len(bab) == 3:
        aba = bab[1:2]
        aba = aba + bab[0:1]
        aba = aba + bab[1:2]
    return aba


print(' --- Part one ---')

countTLS = 0

for l in lines:
    parts = getParts(l)
    sParts = sortBrackets(parts)
    lineValid = True
    validTLSFound = False

    sI = 0
    for sPart in sParts:
        sPartValid = False
        sLen = len(sPart[1])
        if sLen > 3:
            while sI+3 < sLen:
                sSubPart = sPart[1][sI:sI+4]
                isValidTLS = isTLS(sSubPart)
#                print "The subpart: " + str(sSubPart) + " -- TLS: " + str(isValidTLS)

                # Invalidates the line if TLS was found inside brackets
                if sPart[0] == 1 and isValidTLS == 1:
                    # print "TLS was inside brackets, line is invalid! Line: " + str(l)
                    lineValid = False

                # Flag the sub part that a valid TLS was found in combination without brackets
                if sPart[0] == 0 and isValidTLS == 1:
                    # print "TLS is valid and no brackets found, part: " + str(sPart) + " is valid!"
                    validTLSFound = True
                    sPartValid = True

                sI = sI +1
            sI = 0
#        print "   Debug: sPart: " + str(sPart)
#    print "   Debug: Line: " + str(l) + " Valid: " + str(lineValid)

    # Invalidates the line if no sub parts was TLS
    if validTLSFound == 0:
        lineValid = False

    # Count number of IPs that support TLS
    if lineValid:
        countTLS = countTLS +1

print('Number of IPs that supports TLS: ' + str(countTLS))
print('\n --- Part two ---')

countSSL = 0

for l in lines:
    parts = getParts(l)
    sParts = sortBrackets(parts)

    lineSSL = False

    partIndex = 0
    for sPart in sParts:

        # Start with the brackets
        BABinBrackets = False
        if sPart[0] == 1:
            bracketLen = len(sPart[1])
            if bracketLen > 2:
                sI = 0
                while sI+3 < bracketLen+1:
                    bab = sPart[1][sI:sI+3]

                    # Find [bab] inside brackets
                    if isBAB(bab):
                        BABinBrackets = True
                        babIndex = partIndex

                        # get 'aba' from '[bab]'
                        aba = getABA(bab)

                        # Look for reverse-[aba] (bab) in other parts
                        pIndex = 0
                        for p in sParts:
                            if pIndex != babIndex:
                                if p[1].find(aba) != -1 and p[0] == 0:
                                    # print " Line: " + str(l) + " - BAB: " + str(bab) + " - ABA found: " + str(p[1])
                                    lineSSL = True
                            pIndex = pIndex+1
                    sI = sI+1
        partIndex = partIndex + 1

    if lineSSL:
        countSSL = countSSL + 1

print('Number of IPs that supports SSL: ' + str(countSSL))
