from decimal import *
getcontext().prec = 60
f = open('C-small-practice.in')
C = int(f.readline())
for c in range(C):
    n = int(f.readline())
    a = Decimal(3)
    b = Decimal(5)
    print(a)
    print(b)
    print(b.sqrt())
    a = ((a + b.sqrt())**n)%1000
    print(a)
    print("Case #{:d}: {:03d}\n\n".format(c+1, int(a)))
