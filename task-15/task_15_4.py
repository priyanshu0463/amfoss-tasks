'''num=int(input("Enter a number:"))
temp=num
rev=0
while(num&gt;0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")'''



t=int(input())
for i in range(t):
    n=int(input())
    if n > 101101 and n < 1000000 :
        for i in range(100,1000):
            for j in range(999,99,-1):
                
                num=i*j
                temp=num
                r=0
                while(num>0):
                    d=num%10
                    r=r*10+d
                    num//=10
                if(temp==r and temp<=n):
                    print(temp)
                    break
                    
            
            
