#print all the possible 3 pairs in a list
'''
ip:
    3 2 5 4 1 6 8

op:
    325 324 321 326 328 354 351 356 358 341 346 348
    316 318 368 254 251 256 258  241 246 .....



l=list(map(int,input().split()))
for i in range(len(l)):
    for j in range(i+1,len(l)+1):
        for k in range(j+1,len(l)):
            print(l[i],l[j],l[k],end='\n')


#using recursion

def combination(l,k):
    def pairs(curr,start):
        if (len(curr)==k):
            print(curr)
            return
        for i in range(start,len(l)):
            pairs(curr+[l[i]],i+1)
        return
    pairs([],0)
a=list(map(int,input().split()))
k=3
combination(a,k)


#fibbonacci

def fun(x):
    if(x==1):
        return 1
    if(x==2):
        return 2
    return fun(x-1) + fun(x-2)
fun(3)
'''


#subsequence anagram rotations
'''
ip:
    school
    3
    L 2
    R 3
    L 1

op:
    yes
'''

'''

s=input()
l=[]
n=int(input())
x=''
for i in range(n):
    l.append(input())
    l.append(int(input()))
print(l)
for j in range(0,len(l),2):
    if l[j]=='L':
        #print(s[l[j+1]])
        x=x+s[l[j+1]]
    elif l[j]=='R':
        x=x+s[-(l[j+1])]
print(x)
x=list(x)
x.sort()
s1=[]
for i in range(len(s)-(n-1)):
    t=list(s[i:n+i])
    t.sort()
    s1.append(t)
print(s1)
for i in s1:
    if i==x:
        print('yes')
        break
else:
    print('no')
    
'''    

#check whether a given number can be formed by adding to prime numbers

'''
ip:
    12
op:
    yes

possible cases:
    1 11
    2 10
    3 9
    4 8
    5 7
    6 6
'''
'''
def isprime(x):
    if(x==1):
        return 1
    if(x==2):
        return 1
    for i in range(2,(x//2)+1):
        if(x%i==0):
            return 0
    return 1
a=int(input())
for i in range(1,(a//2)+1):
    if(isprime(i) and isprime(a-i)):
        print('yes')
        break
else:
    print('no')
'''


#laxographical order
'''
ip:
    2
    polikujmnhytgbvfredcxswqaz
    abcd
    qwryupcsfoghjkldezxvbintma
    ativedoc

op:
    bdca
    codevita


'''
'''
n=int(input()) 
for i in range(n):
    a=input()
    b=input()
    for j in a:
        if j in b:
            x=b.count(j)
            print(x*j,end='')
                
'''

#recursion

#13 9 4 10 5 7
#13 10 9 7 5 4

def fun(l):
    if(len(l)==0):
        return 0
    if(len(l)==1):
        return l[0]
    if(len(l)==2):
        return max(l)
    le=l[0]+fun(l[2:])
    ri=l[1]+fun(l[3:])
    return max(le,ri)
    
l=list(map(int,input().split()))
print(fun(l))







