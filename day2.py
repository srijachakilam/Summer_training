'''#sum of digits is prime or not
def sum(n):
    s=0
    while(n>0):
        x=n%10
        s=s+x
        n=n//10
    return s
def pnp(x):
    if(n in [2,3,5,7]):
        return m
    else:
        return m+1
n=int(input())
m=n

    
if(n<10):
    print(pnp(n))
else:
    while(1):
        n=sum(n)
        if(n<10):
            break
    print(pnp(n))


    

#recursion
def fun(x):
    if (x==3):
        return 200
    print(x)
    t=fun(x+1)
    print(x)
    return t
print(fun(1))

def fun(x):
    if(x==3):
        return
    print(x)
    fun(x+1)
    print(x)
fun(1)

def fun(x):
    if(x==3):
        return
    print(x)
    fun(x+1)
    print(x)
print(fun(1))

def fun(x,s):
    if(x==len(a)):
        return s
    s=s+a[x]
    return fun(x+1,s)
a=[6,7,2,5]
print(fun(0,0)) //receive 20

#
 ip:
     a=[3,8,5,4,3]
     b=[5,0,9,3,2]

op:
    (12,17)

def fun1(x,s):
    if(x==len(a)):
        return s
    if(a[x]%2==0):
        s=s+a[x]
    return fun1(x+1,s)
def fun2(z,s):
    if(z==len(a)):
        return s
    if(b[z]%2!=0):
        s=s+b[z]
    return fun2(z+1,s)
a=list(map(int,input().split()))
b=list(map(int,input().split()))
x=fun1(0,0)
y=fun2(0,0)
print(x,y)

#sum of even numbers in given number
def fun(x):
    if x==0:
        return 0
    return x+fun(x-2)
n=int(input())
if n%2==0:
    print(fun(n))
else:
    print(fun(n-1))


a=list(map(int,input().split()))
if len(a)%2==0:
    print('yes')
else:
    print('no')

#mmmfff check whether m or f
str=input()
c1=0
c2=0
for i in str:
    if(i=='m'):
        c1=c1+1
    elif(i=='f'):
        c2=c2+1
if c1==c2:
    print('0')
elif c1>c2:
    print('m')
else:
    print('f')


        
str=input()
c1=0
for i in str:
    if(i=='m'):
        c1=c1+1
    elif(i=='f'):
        c1=c1-1
if c1==0:
    print('0')
elif c1>0:
    print('m')
else:
    print('f')

#removing stars from string
str=input()
l=[]
for i in str:
    if(i!='*'):
        l.append(i)
    else:
        l.pop()
print(''.join(l))


sort array
s=input()
l=s.split()
k=[0]*len(l)
for i in l:
    k[int(i[-1])-1]=i[:-1]
print(' '.join(k))'''
    







































