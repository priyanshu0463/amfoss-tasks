t=int(input())
for i in range (t):
    lst1=[]
    lst=[]
    m=0
    s=0
    
    n=int(input())
    
    lst=list(map(int,input().strip().split()))[:n]
    for k in  lst:
        s=s+k
    l=len(lst)
    if n>1 and t>0 and s>0 and s <=(2*(10**5)):
        for i in range (l-1):
            while (lst[i]>0 and lst[i]<=(10**9)):
                for j in range(i,l):
                    if lst[j]==0:
                        lst[j]=lst[j]+1
                        lst[i]=lst[i]-1
                        m=m+1
                        break
                    elif j==l-1:
                        lst[l-1]=lst[l-1]+1
                        lst[i]=lst[i]-1
                        m=m+1
                        break
                    
    if s <=(2*(10**5)):
            print(m)
