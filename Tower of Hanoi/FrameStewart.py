from math import sqrt

n, m = map(int, raw_input().split())

def FrameStewart(n):
     
    if n == 1:
        return n
    else:
        i = round(sqrt((2 * n) + 1)) - 1
        return (2*FrameStewart(n-i) + 2**i - 1)


ans = FrameStewart(n)
if ans <= m:
    print "YES"
else: print "NO"
