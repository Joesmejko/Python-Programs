myFile = open("text.txt", "r")
suma = 0
i = 0
cisla = []
for i in range(22):
    line = myFile.readline().split()
    if all(x in line for x in ("$", "cd")) or "dir" in line or all(x in line for x in ("$", "ls")):
        cisla.append(suma)
        suma = 0
    else:
        suma+=int(line[0])

cisla.append(suma)
filtered_numbers = [n for n in cisla if n < 100000]
result = sum(filtered_numbers)
    
print(result)