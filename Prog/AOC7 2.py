f=open("text.txt", "r")
arr=[]
suma = 0
while True:
    line=f.readline().split()
    if len(line) == 0:
        break
    if all(x in line for x in ("$", "cd")) or "dir" in line or all(x in line for x in ("$", "ls")):
        suma = 0
    else:
        arr.append(int(line[0]))

print(arr)
novy = sum(arr)


filtered_numbers= [n for n in arr if n<100000]
result=sum(filtered_numbers)


print(novy-result)