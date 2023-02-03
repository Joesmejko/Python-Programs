import numpy as np

grid = np.genfromtxt("text.txt", dtype=int)

row = 0
colum = 0
sada = set()
a = 1
f = 98

for i in range(99):
    biggest = grid[row, 0]
    sada.add((row, 0))
    sada.add((row, 98))
    for a in range(98):
        if grid[row, a] > biggest:
            sada.add((row, a))
            biggest = grid[row, a]
    last_biggest = biggest
    biggest = grid[row, f]
    f -= 1
    while biggest < last_biggest:
        if grid[row, f] > biggest:
            biggest = grid[row, f]
            sada.add((row, f))
        f -= 1
    row += 1
    f = 98
    a = 1

for i in range(99):
    biggest = grid[0, colum]
    sada.add((0, colum))
    sada.add((98, colum))
    for a in range(98):
        if grid[a, colum] > biggest:
            sada.add((a, colum))
            biggest = grid[a, colum]
    last_biggest = biggest
    biggest = grid[f, colum]
    f -= 1
    while biggest < last_biggest:
        if grid[f, colum] > biggest:
            biggest = grid[f, colum]
            sada.add((f, colum))
        f -= 1
    colum += 1
    f = 98
    a = 1


print(len(sada))