def mi(st):
    original=""
    pre=""
    for y in range(0,len(st)):
        
        
        if(st[y-1]==st[y] and y>0):
             continue
        else:
            original+=st[y]
             
        return(original)
        
