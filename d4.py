# Todo: Fix broken solution for part two
import string

rooms = []
realRooms = []
sectorSum = 0

file_obj = open('d4_input.txt', 'r')
rooms = file_obj.readlines()

for room in rooms:
    if room.find('['):
        i = []
        i = room.strip().split('-')

        sector = i[len(i)-1].split('[')[0]
        checksum = i[len(i)-1].split('[')[1].replace("]", "")
        name = ""
        cnt = 0
        for cnt in range(len(i)-1):
            name = name + i[cnt]

        # Order the letters and count them
        nameArray = []
        for char in name:
            nameArray.append(char)
        nameArray.sort()

        # Get all unique letters
        uniqChar = []
        for c in nameArray:
            if uniqChar.count(c) == 0:
                uniqChar.append(c)

        # Count unique letters
        numPerChar = []
        for uc in uniqChar:
            numPerChar.append([nameArray.count(uc),uc])
        numPerChar.sort(reverse=True)

        # Find out the max num of occurance for the most common letter
        maxNum = 0
        for n in numPerChar:
            if maxNum < int(n[0]):
                maxNum = int(n[0])
#        print "max num: " + str(maxNum)

        # Group the letters on number of occurances
        charsgrp = []
        while maxNum > 0:
            charsmax = []
            for c in numPerChar:
                if c[0] == maxNum:
                    charsmax.append(c[1])
            charsmax.sort()
            charsgrp.append(charsmax)
            maxNum = maxNum-1
#        print "charsgrp:     " + str(charsgrp)

        # Get the five most common chars
        verifyChecksum = ""
        for chars in charsgrp:
            for char in chars:
                verifyChecksum = verifyChecksum + char
        verifyChecksum = verifyChecksum[0:5]

        # debug stuff
#        print "num per char:  " + str(numPerChar)
#        print "name:          " + str(name)
#        print "sector:        " + str(sector)
#        print "checksum:      " + str(checksum)
#        print "verifysum:     " + str(verifyChecksum)

        if checksum == verifyChecksum:
            # print "This room is real!"
            realRooms.append(room)
            sectorSum = sectorSum + int(sector)

print(" --- Part one ---\nThe sum of the sector IDs of the real rooms is: " + str(sectorSum))
print(" --- Part two ---")

decryptedNames = []

for room in rooms:
    if room.find('['):
        i = []
        i = room.strip().split('-')

        sector = i[len(i)-1].split('[')[0]
        checksum = i[len(i)-1].split('[')[1].replace("]", "")

        name = room.split('[')[0]
        name = name[:len(name)-len(sector)-1]

        # Rotate letters
        indx = ""
        tempname = ""
        for n in range(int(sector)):
            cnt = 0
            for c in name:
                if c == "-":
                    tempname = tempname + "-"
                elif c == "z":
                    tempname = tempname + "a"
                else:
                    indx = c.index()
                    tempname = tempname + string.lowercase[indx + 1]
                cnt = cnt+1
            name = tempname
            tempname = ""
        decryptedNames.append([name, sector])

# Print all decrypted names
decryptedNames.sort()
for dname in decryptedNames:
    print("Sector: " + str(dname[1]) + "\tName: " + str(dname[0]))

print(" \n Northpole objects is found in sector: 482")
