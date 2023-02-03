myFile = open("text.txt", "r")
line = myFile.readline()
i = 0
floor = 1
first = 0
while True:
    if line[i] == " ":
        break
    if line[i] == "(":
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        first = i
        break
    i+=1
print(floor)
print(first)