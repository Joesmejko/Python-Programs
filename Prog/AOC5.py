list_1 = ["F", "T", "C", "L", "R", "P", "G", "Q"]
list_2 = ["N", "Q", "H", "W", "R", "F", "S", "J"]
list_3 = ["F", "B", "H", "W", "P", "M", "Q"]
list_4 = ["V", "S", "T", "D", "F"]
list_5 = ["Q", "L", "D", "W", "V", "F", "Z"]
list_6 = ["Z", "C", "L", "S"]
list_7 = ["Z", "B", "M", "V", "D", "F"]
list_8 = ["T", "J", "B"]
list_9 = ["Q", "N", "B", "G", "L", "S", "P", "H"]

dic = {
    1: list_1,
    2: list_2,
    3: list_3,
    4: list_4,
    5: list_5,
    6: list_6,
    7: list_7,
    8: list_8,
    9: list_9
}

myFile = open("text.txt", "r")
while True:
    line = myFile.readline()
    one, two, thr, fou, fiv, six = line.split(" ")
    two = int(two)
    fou = int(fou)
    six = int(six)
    for i in range(two):
        dic[six].append(dic[fou][-two])
        dic[fou].pop(-two)
        two -= 1