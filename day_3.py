#print the alphabets according to the given number
'''
input: khoor
         3
output: hello

input: bvec
        4
output: xray

input: bcdmnwc
        9
output: student


s= input()
n=int(input())
new = ''
for i in s:
    s1 = ord(i)- n
    while(s1<97):
        s1 = 97 - s1
        s1 = 122 -(s1-1)
    new = new + chr(s1)
print(new)


----OR----

s=input()
n=int(input())
c=n%26
new =''
for i in s:
    if((ord(i)-c)>=97):
        new = new + chr(ord(i)-c)
    else:
        new = new +chr(ord(i)-c+26)

print(new)       
'''


#print the len of longest substring

'''
input: xyzabcdefklmnopqefgh
output: 7


s=input()
count=1
ma=0
for i in range(len(s)-1):
    if(ord(s[i+1]) == (ord(s[i])+1)):
        count +=1
        if(ma<count):
            ma =count
    else:
        count=1

print(ma)
'''


#check whether the string is correct or not with repeating


'''
input:
        3
        xyz
        pqr
        abc
        "yraxpazr"
output:
        yes

input:
        4
        abcd
        xyze
        pqrw
        stuv
        "cyptdzsayq" //the element should be from each row in order otherwize the string is wrong
        
output:
        No
        



n=int(input())
m=[]
for i in range(n):
    a=[]
    for j in range(n):
        a.append(input())
    m.append(a)
str = input()
index=0
flag=0
for i in str:
    if i in m[index]:
        index+=1
        if(index==n):
            index=0
    else:
        flag=1
        break
if(flag==1):
    print('no')
else:
    print('yes')
    
----OR----

n=int(input())
m=[]
for i in range(n):
    m.append(input())
str=input()
for i in range(len(str)):
    if i not in m[i%n]:
        print('no')
        break
else:
    print('yes')
    

'''

#check whether the string is correct or not without repeating

'''
input:
        3
        x x x
        a b c
        p q r
        "xaqxbr"
output:yes

input:
        3
        xyz
        abx
        pqr
        "xapybqzxr"'
output:yes


n=int(input())
m=[]
for i in range(n):
        m.append(list(input()))
str=input()
f=0
for i in range(len(str)):
    if(str[i] not in m[i%n]):
        print('no')
        f=1
        break
        
    else:
        m[i].remove(str[i])
if(f==0):
    print('yes')

        
'''
 #set doesnt allow sets,dict,lists inside it



#check whether the given number is palindrome without converting into string and use recursion


'''
input:12321
output:yes

def reverse(n,re):
    if(n>0):
        x=n%10
        re=(re*10)+x
        return reverse(n//10,re)
    else:
        return re
n=int(input())
r=reverse(n,0)
if(r==n):
    print('palindrome')
else:
    print('not a palindrome')

'''


#find the maximum profit
'''
input:15 3 2 7 8 4

n=list(map(int,input().split()))
m=0
for i in range(len(n)-1):
    for j in range(i+1,len(n)):
        if(n[i]<n[j] and n[j]-n[i]>m):
            m=n[j]-n[i]
print(m)

----OR----



n=int(input())
b=n[0]
pr=0
for i in range(len(n)):
    if b>n[i]:
        b=i
    else:
        if(pr
        pr=b-i
        
    
'''


#patterns
#1
'''
input: 5
output:
    * * * * *
    * 1 2 3 *
    * 4 5 6 *
    * 7 8 9 *
    * * * * *


n=int(input())
k=1
for i in range(n):
    for j in range(n):
        if(i==0 or i==(n-1) or j==0 or j==(n-1)):
            print('*',end=' ')
        else:
            print(k,end=' ')
            k+=1
    print()
            
'''
#2
'''
input : 4
output:
     _ _ _ _ a _ _ _ _
     _ _ _ a b a _ _ _
     _ _ a b c b a _ _
     _ a b c d c b a _
     
'''

n=int(input())
for i in range(n):
    for j in range(n-i):
        print('_',end=' ')
    for k in range((2*i+1)//2):
        print(chr(c),end=' ')
        c+=1
    for k in range((2*i+1)//2):
        print(chr(c),end=' ')
        c=c-1
    c=97
    for l in range(n-i):
        print('_',end=' ')
    print()
        

    
