#tc=int(input())
inp=input().split(" ")

numbers=["1111110","0110000","1101101","1111001","0110011","1011011","1011111","1110000","1111111","1111011"]

suggest=[]
for i in numbers:
     if(i[1]=='1' and i[4]=='0' and i[5]=='0' and i[6]=='0'):
          suggest.append(i)
