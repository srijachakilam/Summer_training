#print the element which has occurance more than length of list

'''l=list(map(int,input().split()))
h=len(l)//2
for i in l:
    c=l.count(i)
    if(c>h):
        f=i
    else:
        f='invalid input'
print(f)

----OR----


l=list(map(int,input().split()))
w=l[0]
c=1
for i in range(1,len(l)):
    if l[i]!=w:
        c=c-1
        if(c==0):
            c=1
            w=l[i]
    else:
        c+=1
        
    
print(w)



n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))

s=n*(n+1)//2
su=0
for i in l:
    su=su+i
print(s-su)
'''
#find the largest kth
'''
n=int(input())
m=int(input())
a=[]
for i in range(1,n+1):
    if(n%i==0):
        a.append(i)
print(a[-m])
        
'''


#find whether 2 numbers are co primes
'''
import math
a=int(input())
b=int(input())
if(math.gcd(a,b)==1):
    print('yes')
else:
    print('no')
'''



#balance parantheses

n=input()
l1=[]
f=0
for i in n:
    if i=='{' or i=='[' or i=='(':
        l1.append(i)
    else:
        if not l1:
            f=0
        
        if i ==']' and l1[-1]=='[':
            l1.pop()
        elif i=='}' and l1[-1]=='{':
            l1.pop()
        elif i==')' and l1[-1]=='(':
            l1.pop()
    if  not l1:
        f=1
    else:
        f=0
if f==0:
    print('no')
else:
    print('yes')
        
            
        

    

    




             
    
