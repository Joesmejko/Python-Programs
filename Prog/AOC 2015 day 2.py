def dimensions(l, w, h):
    if l*l*2 < w and (2*l*w) < h :
        smallest = 
    elif w < h :
        smallest = w
    else :
        smallest = h
    area = ((2*l*w) + (2*w*h) + (2*h*l) + smallest)
    return area

suma = 0

myFile = open("text.txt", "r")
while True:
    line = myFile.readline()
    if line == "":
        break
    l, w, h = line.split("x")
    l = int(l)
    w = int(w)
    h = int(h)
    suma += dimensions(l,w,h)
print(suma)
    

