## Declaration of variables
filerows = []
triangles = []
vTriangles = []
countValid = 0
a = []
b = []
c = []
vCounter = 0

file_obj = open('d3_input.txt', 'r')
filerows = file_obj.readlines()

for row in filerows:
    if row != "":
        l1 = int(str(row[0:3]).strip())
        l2 = int(str(row[4:8]).strip())
        l3 = int(str(row[9:]).strip())
        triangles.append([l1, l2, l3])

for row in filerows:
    # take three rows at a time
    if row != "" and vCounter < 3:
        a.append(int(str(row[0:3]).strip()))
        b.append(int(str(row[4:8]).strip()))
        c.append(int(str(row[9:]).strip()))
    vCounter = vCounter +1
    if vCounter == 3:
        vTriangles.append([a[0],a[1],a[2]])
        vTriangles.append([b[0],b[1],b[2]])
        vTriangles.append([c[0],c[1],c[2]])
        vCounter = 0
        a = []
        b = []
        c = []

for triangle in triangles:
    triangle.sort()
    if (triangle[0] + triangle[1]) > triangle[2]:
        countValid = countValid+1

print("Number of valid horizontal triangles is: " + str(countValid))

countValid = 0
for vTriangle in vTriangles:
    vTriangle.sort()
    if (vTriangle[0] + vTriangle[1]) > vTriangle[2]:
        countValid = countValid+1

print("Number of valid vertical triangles is: " + str(countValid))
