import math
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def isthere(lis):
     primes=[0]
     for i in lis:
          if(is_prime(int(i))):
               primes.append(int(i))
     return(max(primes))
def factors(n):
    result = []

    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)

    return result

def spli(a):
     d=factors(a)
     if(len(d)%2==0):
          return(max(d[(len(d)/2)-1:(len(d)/2)+1]))
     else:
          return(d[(len(d)//2)+1])
     

a=int(input())
b=input().strip().split(" ")
c=input().strip().split(" ")

total=0
for i in c:
     total+=int(i)

area=int(b[0])*int(b[1])



if(total>area or total<area):
     print("no")
else:
     k=isthere(c)
    
     if(k!=0):
          c.remove(str(k))
          if(int(b[0])>=k or int(b[1])>=k):
     
               if(int(b[0])>=spli(int(max(c))) or int(b[1])>=spli(int(max(c))) ):
                    print("yes")
               else:
                    print("no")
          else:
               print("no")
          
