'''n=int(input())
c=n
for i in range(1,n):
    if n%i==0:
        for j in range(2,i):
            if i%j!=0:
                c=i
print(c)'''
            
        
c=0
lst=[]
t = int(input())
if t>=1 and t<=10:
    
    for a0 in range(t):
        a=int(input())
        if a>=10 and a<=(10**12):
            lst=lst + [a]
        else:
            continue
    for k in lst:
        c=k
        lst1=[]
        for i in range(2,int(k//2)+1):
                
            if k%i==0:
                lst1=lst1 + [i]
                    
                for j in lst1:
                    for z in range(2,int(j**(1/2))+1):
                        if j%z==0:
                            
                            lst1.remove(j)    
                            break           
        lst1.reverse()             
        if len(lst1)==0:
            print(c)
        else :
            print(lst1[0])
