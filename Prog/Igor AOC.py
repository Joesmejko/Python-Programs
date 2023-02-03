f=open("text.txt","r")
sum=0
rsum=0
while True:
    line=f.readline().replace("x"," ").split()

    if len(line)==0:
        break

    l,w,h=int(line[0]),int(line[1]),int(line[2])

    r1,r2,r3=2*l*w,2*w*h,2*h*l

    arr=[l,w,h]
    arr.sort()

    ribon=l+l+w+w
    ribonbow=arr[0]*arr[1]*h





    rfinal=ribon+ribonbow

    rsum+=rfinal

    result=r1+r2+r3

    smallest=min(r1,r2,r3)
    smallest=smallest/2
    result+=smallest
    sum+=result

print(rsum)