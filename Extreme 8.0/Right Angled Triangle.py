import math
num=int(input())

for d in range(0,num):
    t=True
    leg=input().strip().split()
    leg=[int(i) for i in leg]
    x=leg[0]
    y=leg[1]
    for j in range (1,x):
        if(math.sqrt(x*x-j*j).is_integer()):
            ang=180-math.asin(j/x)-90
            saba=(j/x)*y
            #print(saba)
            if saba.is_integer():
                print("TRUE")
                t=False
                break
    if t:
        print("FALSE")
