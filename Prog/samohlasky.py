counter = 0
f = 0
samo = "aäeiyouáéíýóú"
veta = input("Zadaj slová... ")
while f != len(veta):
    if veta[f] in samo:
        counter += 1
    f += 1
print("Počet samohlások je... " + str(counter))