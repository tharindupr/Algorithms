
def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a%b
    return a

def cal(p,q,c,i):

    
    if(p>=q):
        
        if(c==0 and rational(p,q)):
            print("Case #"+str(i)+": 1")
        elif(rational(p,q)):
            print("Case #"+str(i)+": "+str(c))
        else:
            print("Case #"+str(i)+": impossible")
    else:
        c+=1
        cal(p*2,q,c,i)
        

    
def rational(p,q):
    from fractions import Fraction
    gc=gcd(p,q)
    if(p==q):
        return(True)
    else:
        st=str(p/q)
        
        a=str(Fraction(st))
        b=a.split("/")
        if(p//gc==int(b[0]) and q//gc==int(b[1])):
            return(True)
        else:
            return(False)

f=open("A-large.in","r")
cases=int(f.readline()[:-1])
for i in range(1,cases+1):
    pq=(f.readline()[:-1]).split("/")
    p=int(pq[0])
    q=int(pq[1])
    cal(p,q,0,i)
    
