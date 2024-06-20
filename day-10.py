#sum of largest prime numbers between 2 numbers in list
'''
ip:
 4,8,14,22,36,68
 
op: sum of largest prime numbers between 2 numbers in list
    [7,13,19,31,67]
    137
'''
'''
def isprime(n):
    c=0
    for i in range(2,n//2+1):
        if n%i==0:
            c+=1
    if c==0:
        return True
    else:
        return False
            
n=list(map(int,input().split()))
a=0
l=[]
for i in range(len(n)-1):
    j=i+1
    for k in range(n[j]-1,n[i],-1):
        x=isprime(k)
        if x:
            l.append(k)
            break
print(sum(l))

'''


'''
ip:
    4 9 8 2 14 3 15 6

   1-[4 8 9 2 14 3 15 6]
   2-[4 2 8 9 14 3 15 6]
   3-[4 2 8 9 14 3 15 6]
   4-[4 2 8 3 9 14 15 6]
   5-[4 2 8 3 9 14 15 6]
   6-[4 2 8 3 9 6 14 15]

'''
'''
n=list(map(int,input().split()))
for i in range(len(n)):
    j=i+2
    m=n.index(min(n[i:j+1]))
    t=n[m]
    n[m]=n[i]
    n[i]=t
    j+=1
print(n)

'''
'''
ip:
    "hello:5438,car:214,book:8799,apple:2187"

op:
find len of word and if it is there in corresponding number print that index otherwise print the next lowest index if not available print 'x'

    oaxp
'''
'''
s=input()
j=0
l=[]
oot=''
for i in range(len(s)):
    if s[i]==':' or s[i]==',': 
        l.append(s[j:i])
        j=i+1
    if i==len(s)-1:
        l.append(s[j:i+1])

print(l)
for i in range(0,len(l),2):
    j=i+1
    x=len(l[i])
    if str(x) in l[j]:
        
        oot=oot+(l[i][x-1])
    else:
        for k in range(x-1,0,-1):
            if str(k) in l[j]:
                oot=oot+(l[i][k-1])
                break
        else:
            oot=oot+'x' 
print(oot)
    
'''  
    
