from decimal import *
import math
getcontext().prec = 100
f=open("C-small-practice.in","r")
f2=open("output1.txt","w")
cases=int(f.readline()[:-1])
count=0
while (count<cases):
    n=int(f.readline()[:-1])
    sq=Decimal(math.sqrt(Decimal(5)))

    
    ans=((Decimal(3)+sq)**n)%1000
    print(Decimal(ans))
    number="{:03d}".format(int(ans))
    f2.write("Case #"+str(count+1)+": "+number[-3:]+"\n")
    count+=1

f.close()
f2.close()
