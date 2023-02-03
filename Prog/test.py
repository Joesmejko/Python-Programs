myFile = open("text.txt", "r")
sum = 0
last_sum = 0

while True:
    line = myFile.readline()
    if str(line) == "\n":
        sum = 0
    else:
        line = int(line)
        sum += line
        if sum > last_sum:
            last_sum = sum
        if str(line) == "\n":
            sum = 0
    print(last_sum)