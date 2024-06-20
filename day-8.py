#print the duplicate elements in new row in matrix

'''
ip1:1 2 3 4 5 1 2 3 4 1 2 3

op1:
    [[1,2,3,4,5],[1,2,3,4],[1,2,3,]]

ip2: 2 3 1 3 4 2 3 2
op2:
    [[2,3,1,4],[3,2],[3]]
    

'''
'''
def check(n,ou):
    a=[]
    b=[]
    if len(n)==0:
        return ou
    else:
        for i in n: 
            if i not in b:
                b.append(i)
            else:
                a.append(i)     
    ou.append(b)
    return check(a,ou)
    
        

n=list(map(int,input().split()))
#o=[]
ou=[]
print(check(n,ou))

'''
'''

#check whether  all the alphabets are there in list

l=input()
h=0
m=l.replace(' ','')
s=[]
for i in range(len(m)):
    if m[i] not in s:
        s.append(m[i])
    #print(ord(i))
#print(s)
for i in range(len(s)):
    if (ord(s[i])>=65 and ord(s[i])<=90)or(ord(s[i])>=97 and ord(s[i])<=122):
        h=h+1
        #print(h)
    
if(h==26):
    print('yes')
else:
    print('no')
    
'''


#print the length of longest substring without repeating characters

'''
a=input()
d={}
s=''
m=0
i=0
while(i<len(a)-1):
    while(i<len(a)):
        if a[i] not in s:
            s=s+a[i]
            d[a[i]]=i
        else:
            if len(s)>m:
                m=len(s)

            s=''
            break
        i=i+1
    i=d[a[i]]+1
print(m)
           
'''

#check how many trees won't burn (island)

'''
ip:
    6
    0 1 1 1 0 1
    0 1 0 1 0 0
    1 0 1 1 0 0
    0 0 0 1 1 1
    1 1 0 0 0 1
    1 1 1 0 1 0

    4,6

op:
    8
'''

'''

def check(i,j):
    
    if i<0 or i>len(l)-1 or j<0 or j >len(l)-1:
        return
    if l[i][j]==0:
        return 
    else:
        #print('d')
        if l[i][j]==1:
            l[i][j]=0
        #print(l)
        check(i-1,j)#top
        check(i,j-1)#left
        check(i+1,j)#bottom
        check(i,j+1)#right
    return 
        
n=int(input())  
l=[]
for i in range(n):
    a=[]
    for j in range(n):
        a.append(int(input()))
    l.append(a)
r=int(input())
c=int(input())
check(r-1,c-1)
c=0
for i in range(len(l)):
    for j in range(len(l)):
        if l[i][j]==1:
            c=c+1
print(l)
print(c)

 '''

#check whether the given word is in the given matrix

def check(i,j,k,t):
    if(k==len(s)):
        return 1
    if( i<0 or j<0 or i>=len(s) or j >=len(s) or a[i][j]!=s[k]):
        return
    if(a[i][j]==s[k]):
        a[i][j]=0
        t=check(i-1,j,k+1)
        t=check(i,j-1,k+1)
        t=check(i+1,j,k+1)
        t=check(i,j+1,k+1)
        return t
    
n=int(input())
l=[]
for i in range(n):
    a=[]
    for j in range(n):
        a.append(input())
    l.append(a)
s=input()
for i in range(n):
    for j in range(n):
        if l[i][j]==s[0]:
           c=check(i,j,1,0)
           if(c==1):
               print('yes')
               break
if(c==0):
    print('no')
            
        
        

