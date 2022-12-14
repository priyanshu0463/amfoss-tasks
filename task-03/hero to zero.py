t=int(input())
for i in range (t):
    lst1=[]
    lst=[]
    c=0
    
    n=int(input())
    
    lst1=list(map(int,input().strip().split()))[:n] 

    lst=sorted(lst1)
    
    l=len(lst)
    for k in lst:
        if k==0:
            c=c+1

    
    if c>0:
        print(l-c)
    else:
        
        q=0
        z=0
        
        for f in range (l-1):
            if lst[f]==lst[f+1]:
                lst[f]=0
                q=q+1
                sorted(lst)
            
            
        for w in lst:
            if w==0:
                z=z+1
        if z>0:
            print(l-z+q)
        else:
            print(l+1)
