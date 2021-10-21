hInp = []
password = ""

file_obj = open('d6_input.txt', 'r')
# file_obj = open('d6_example.txt', 'r')

# Read horizontal lines from input
for line in file_obj:
    if line != "\n":
        n = 0
        for c in line:
            if c != "\n":
                hInp.append([n,c])
                n = n+1
file_obj.close()

# Get the password length
hInp.sort(reverse=True)
pwdLen = hInp[0][0]

posCnt = 0
while posCnt < pwdLen+1:
    pos = ""
    uniq = []

    for p in hInp:
        if p[0] == posCnt:
            pos = pos + p[1]
            if uniq.count(p[1]) == 0:
                uniq.append(p[1])
#    print "Position: " + str(pos)
#    print "Unique chars: " + str(uniq)

    letters = []
    for u in uniq:
        letters.append([pos.count(u), str(u)])
    letters.sort(reverse=True)
    password = password + letters[0][1]
#    print "New char: " + str(letters[0][1])
    posCnt = posCnt + 1

print(' --- Part one ---')
print('The password is: ' + password)
print(' --- Part two ---')

password = ""
posCnt = 0
while posCnt < pwdLen+1:
    pos = ""
    uniq = []
    for p in hInp:
        if p[0] == posCnt:
            pos = pos + p[1]
            if uniq.count(p[1]) == 0:
                uniq.append(p[1])
    letters = []
    for u in uniq:
        letters.append([pos.count(u), str(u)])
    letters.sort()
    password = password + letters[0][1]
    posCnt = posCnt + 1

print('The password is: ' + password)
