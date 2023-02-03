myFile = open("text.txt", "r")
sum = 0
listone = []
list_2 = []
while True:
    line = myFile.readline()
    fhalf, shalf = line.split(",")
    cison, cistw = fhalf.split("-")
    cisth, cisfh = shalf.split("-")
    cison = int(cison)
    cistw = int(cistw)
    cisth = int(cisth)
    cisfh = int(cisfh)
    range_1 = range(cison, cistw + 1)
    range_2 = range(cisth, cisfh + 1)
    list_1 = list(range_1)
    list_2 = list(range_2)
    if any(item in list_1 for item in list_2):
        sum+=1
        list_1 = []
        list_2 = []

    else:
        list_1 = []
        list_2 = []

print(sum)