myFile = open("input.txt", "r")
line = myFile.readline()
xx = 0
yy = 0
x = 0
y = 0
a = 2
i = 0
sada = set()
for f in range(len(line)):
    zoz = list(line[i:a])
    if zoz[0] == "v":
        y += 1
        sada.add((x, y))
    if zoz[0] == "^":
        y -= 1
        sada.add((x, y))
    if zoz[0] == ">":
        x += 1
        sada.add((x, y))
    if zoz[0] == "<":
        x -= 1
        sada.add((x, y))
        print(len(line))
    if zoz[1] == "v":
        yy += 1
        sada.add((xx, yy))
    if zoz[1] == "^":
        yy -= 1
        sada.add((xx, yy))
    if zoz[1] == ">":
        xx += 1
        sada.add((xx, yy))
    if zoz[1] == "<":
        xx -= 1
        sada.add((xx, yy))
    a += 2
    i += 2




print(len(sada))