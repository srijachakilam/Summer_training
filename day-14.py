#trapping rain water
'''
n=[0,1,0,2,1,0,1,3,2,1,2,1]
left=n.copy()
right=n.copy()
j=1
for i in range(len(left)-1):
    if left[i]>left[j]:
        left[j]=left[i]
    j=j+1
  
for i in range(len(n)-1,-1,-1):
    if right[i]>right[i-1]:
        right[i-1]=right[i]
s=0
print(left)
print(right)
for i in range(len(n)):
    s=s+(abs(min(left[i],right[i])-n[i]))
print(s)
'''

'''
class Solution:
    def trap(self, height: List[int]) -> int:
        l=[0]*len(height)
        r=[0]*len(height)
        m=0#max left
        for i in range(len(height)):
            if(height[i]>m):
                m=height[i]
            l[i]=m
        m1=0 #max right
        for i in range(len(height)-1,-1,-1):
            if(height[i]>m1):
                m1=height[i]
            r[i]=m1
        s=0 #no.of water getting trap
        for i in range(len(height)):
            s=s+(abs(min(l[i],r[i]))-height[i])#in case if it is negative
        return s
'''

#coin change
'''
ip:
    [1,3,4,7]
    15
op:
    4
'''

'''
def fun():
    l1=[-1]*(n+1)
    l1[0]=0
    for i in l:
        for j in range(1,n+1):
            if (j>=i):
                if(l1[j-i]!=-1):
                    if(l1[j]!=-1):
                        l1[j]=min(l1[j],l1[j-i]+1)
                    else:
                        l1[j]=l1[j-i]+1
    print(l1[-1])
l=[1,3,4,5]
n=17
fun()
'''


# find the number of possible paths from first to last in a matrix

'''
ip:
    4X3

    - - -
    - - -
    - - -
    - - -

op:
    
'''
'''
def check(i,j,c):
    if i<0 or i>=n or j<0 or j >=m:
        return c
    if i==n-1 and j==m-1:
        c=c+1
        return c
    vi.append((i,j))
    if ((i-1,j) not in vi):
        c=check(i-1,j,c)#top
    if ((i,j-1) not in vi):   
        c=check(i,j-1,c)#left
    if ((i+1,j) not in vi):
        c=check(i+1,j,c)#bottom
    if ((i,j+1) not in vi):
        c=check(i,j+1,c)#right
    vi.pop()
    
    return c
                
n=int(input())
m=int(input())
vi=[]
print(check(0,0,0))


'''

 # find the number of possible paths from first to last in a matrix with obstacle

'''
ip:
    4X3

    - - -
    - - -
    - - -
    - - -

op:
    
'''
'''
def check(i,j,c):
    if i<0 or i>=n or j<0 or j >=m or (i==k and j==l):
        return c
    if i==n-1 and j==m-1:
        c=c+1
        return c
    vi.append((i,j))
    if ((i-1,j) not in vi):
        c=check(i-1,j,c)#top
    if ((i,j-1) not in vi):   
        c=check(i,j-1,c)#left
    if ((i+1,j) not in vi):
        c=check(i+1,j,c)#bottom
    if ((i,j+1) not in vi):
        c=check(i,j+1,c)#right
    vi.pop()
    
    return c
                
n=int(input())
m=int(input())
k=int(input())
l=int(input())
vi=[]
print(check(0,0,0))
'''

#n-queens with rook
'''
ip:
    
'''
'''
def queen(r):
    if r==n:
        return
    if r!=a:
        for c in range(n):
            if check(r,c):
                m[r][c]='q'
                break
        return queen(r+1)
    else:
        queen(r+1)

def check(i,j):
    if j==b:
        return 0
    r=i
    c=j
    for i in range(r+1):
        if m[i][j]=='q':
            return 0
    i=r
    while(i>=0 and j>=0):
        if m[i][j]=='q':
            return 0
        i=i-1
        j=j-1
    while(r>=0 and c<n):
        if m[i][j]=='q':
            return 0
        r=r-1
        c=c+1
    return 1
n=int(input())
a=int(input())#rook position
b=int(input())
m=[]
for i in range(n):
    m.append([0]*n)

queen(0)
print(m)
'''

#sunlight problem
#print the building numbers on which the sunlight falls
'''
ip:
    3,5,9,6,8,10
    
op:
    left:3,5,9,10
    right:10

'''
'''
l=list(map(int,input().split()))
left=l.copy()
right=l.copy()
for i in range(len(left)-1):
    if left[i]>left[i+1]:
        left[i+1]=left[i]
        
for i in range(len(right)-1,-1,-1):
    if right[i]>right[i-1]:
        right[i-1]=right[i]

print(list(set(left)))
print(list(set(right)))
        
'''

#coins
'''
ip:
    2 3 5 6
    8
op:
    yes
'''

#loops
'''
n=list(map(int,input().split()))
x=int(input())
s=0
f=0
for i in range(len(n)):
    for j in range(1,len(n)):
        s=sum(n[i:j+1])
        #print(s)
        if s==x:
            #print(s)
            f=1
            break
if f==1:
    print('yes')
else:
    print('no')
'''

#dp above question

'''
n=list(map(int,input().split()))
m=int(input())
matrix=[]
for i in range(len(n)+1):
    matrix.append(0*(m+1))
for i in range(1,len(matrix)):
    for j in range(m):
    
        if j==0 or j==n[i]:
            matrix[i][j]=1
        elif j<n[i]:
            matrix[i][j]=matrix[i-1][j]
        else:
            x=j-n[i]
            matrix[i][j]=matrix[i-1][x]
print(matrix)
'''

#print the longest even number from 2 strings
'''
n=input()
m=input()
l=[]
for i in n:
    if i.isdigit():
        l.append(i)
for i in m:
    if i.isdigit():
        l.append(i)        

a=[]
for i in l:
    if i not in a:
        a.append(i)
a.sort(reverse=True)#sorted(a,reverse=True)

if (int(a[-1])%2==0):
    print(''.join(a))
else:
    for i in range(len(a)-2,-1,-1):
        if (int(a[i])%2==0):
            a.append(a.pop(i))
            print(''.join(a))
            break
    else:
        print(-1)
  '''
#check palindrome if not print the next palindrome

'''
ip1:
    122 24  7654    76583   1234
op2:
    131 33  7667    76667   1331
'''
'''
def check(n,m):
    rev=0
    while(n):
        x=n%10
        rev=(rev*10)+x
        n=n//10
        
    if rev==m:
        return rev
    else:
        return check(m+1,m+1)
        
n=int(input())
print(check(n,n))
'''

n=input()
x=''
if len(n)%2==0:
    x=n[:len(n)//2]
    if (x+x[::-1])>n:
        print(x)
    else:
        y=int(x)+1
        print()
    
    
    
