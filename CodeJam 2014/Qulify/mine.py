file=open("magic.txt","r")
m = int(file.readline().strip())
w=[]
b=[]
c=1
while m>=1:
    w.append(file.readline().strip())

    b=w[0].split()
    w.pop()

    R=int(b[0])
    C=int(b[1])
    M=int(b[2])

    print("Case #",end='')
    print(c,end=': ')
    print()
    if C==1 and R-M > 1:
        a=R-M-1
        print('c')
        print('.\n'*a,end='')
        print('*'*M)
    elif R==1 and C-M > 1:
        a=C-M-1
        print('c',end='')
        print('.'*a,end='')
        print('*'*M)
       
    elif R>1 and C>1 and (R*C)-M>3:
        
        b=(R*C)-M-1
        if b-2<=C-1:
            pb=b-2
            print('c',end='')
            print('.'*pb,end='')
            b=b-pb
            if C>pb:
                r=C-pb-1
                print('*'*r)
                print('.'*2,end='')
                b=b-2
                if b==0:
                    print()
              
                if C>2:
                        print('*'*(C-2))
            pb=pb+1
            for i in range(2,R):
                for j in range(0,C):
                    print('*',end='')
                print()
        elif b-2+1>C:
            r=C
   
            b=b-r+1
            print('c',end='')
            print('.'*(r-1))
            print('.'*2,end='')
            b=b-2
            
            if b>=C-2:
                print('.'*(C-2))
                b=b-(C-2)
                
            elif b<C-2:
                print('.'*b,end='')
                print('*'*(C-b-2))
            for i in range(2,R):
                
                if b>=C:
                    
                    print('.'*C)
                    b=b-C
                    
                elif b<C:
                      
                    print('.'*b,end='')
          
                    print('*'*(C-b))
                    b=0
                
               
               
                        
                
                
    else:
        print("Impossible")
            
        



    m=m-1
    c=c+1
