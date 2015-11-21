file=open("C-small-attempt0.in","r")
cases=int(file.readline()[:-1])

for k in range(cases):
    line=file.readline()[:-1].split(" ")
    r=int(line[0])
    c=int(line[1])
    bombs=int(line[2])

    squares=[1,4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,289,324,361,400,441,484]
    target=(r*c)-bombs

    if target in squares:
        #print(k+1)
        print(str(target)+" " +str(k+1))

    
