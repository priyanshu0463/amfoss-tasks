t=int(input())
for i in range (t):
    lst1=[]
    lst=[]
    c=0
    z=0
    
    n=int(input())
    
    lst1=list(map(int,input().strip().split()))[:n] 

    lst=sorted(lst1,reverse = True)
    
    l=len(lst)
    for j in range(l-1):
        
        if lst[j]==lst[j+1]:
            
            lst[j]=0
            lst=sorted(lst,reverse = True)
            
    for k in lst:
        
        if k == 0:
            z=z+1 
        
    for m in range (l+1-z):
        
        
        lst[0]=lst[0]-lst[1]
        lst=sorted(lst,reverse = True)
        
        
            
        
    for o in lst:
        if o == 0:
            c=c+1
    if l-c>1 :
        print("NO")
    else:
        print("YES")
        
        
