import hashlib

print(' --- Part One ---')

password = ""
pwdLen = 8
input = b"ugkcyxxp"

counter = 0
while pwdLen >0:
    foundFiveZero = False
    while foundFiveZero == False:
        test = str(input) + str(counter)
        m = hashlib.md5()
        m.update(test)
        md5Hex = m.hexdigest()
        if md5Hex[:5] == "00000":
            password = password + md5Hex[5:6]
#            print "Found five zeros here: " + md5Hex
            foundFiveZero = True
        counter = counter +1
    pwdLen = pwdLen - 1

#print "This was the hash input: " + test
print('The password is: ' + password)

print(' --- Part Two ---')

password = ""
pwdChars = [[0,'_'],[1,'_'],[2,'_'],[3,'_'],[4,'_'],[5,'_'],[6,'_'],[7,'_']]
pwdLen = 8
digitFound = 0
input = b"ugkcyxxp"

counter = 0
while pwdLen > digitFound:
    foundFiveZero = False
    while foundFiveZero == False:
        test = input + str(counter)
        m = hashlib.md5()
        m.update(test)
        md5Hex = m.hexdigest()
        if md5Hex[:5] == "00000":
            position = md5Hex[5:6]
            if position in str(range(8)):
                pos = int(position)
                if pwdChars[pos][1] == '_':
                    pwdChars[pos][1] = str(md5Hex[6:7])
                    print(pwdChars)
                    digitFound = digitFound +1
            foundFiveZero = True
        counter = counter +1

for i in pwdChars:
    password = password + str(i[1])

print('The password is: ' + password)
