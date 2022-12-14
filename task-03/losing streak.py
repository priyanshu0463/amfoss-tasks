lst=list(map(int,input().strip().split()))[:2]
n=lst[0]
m=lst[1]
c=0
while(m>n):
    if m%2==0:
        
        m=m/2
        c=c+1
    
    if m!=n:
        
    
        m=m/3
        c=c+1
        
if m==n :
    print(c)
else:
    print(-1)
    
