#add all the even odd and float number separetly in the list
'''
input = 5 3.8 7 5.6 4 2 3
output = 15 6 9.4

n1= input().split()
E,O,D=0,0,0
for i in n1:
    if '.' in i:
        D= D+i
        
    else:
        i=int(i)
        if i%2 == 0:
            E=E+i
        else:
            O=O+i
            
print('E -',E,'O-',O,'D-',D)


'''
#count the numbers divisible by 7 between 300 and 400
'''
#input:300,400
n1 =400
n2= 300
c=(n1//7)-(n2//7)
print(c)


'''



#check whether the number is prime, if prime keep it the same otherwise print the next prime


'''
def prime(n):
    c=0
    for i in range(1,n//2):
        if n%i==0:
            c=c+1
    if c==1:
        return n
    else:
        return prime(n+1)


n=int(input())
s=prime(n)
print(s)


-----------------OR-----------------


n=int(input())
while(1):
    c=0
    for i in range(2,(n//2)+1):
        if(n%i==0):
            c=c+1
            break
    if(c==0):
        print(n)
        break
    else:
        n=n+1
'''

#count of prime digits in given number
'''

n=int(input())
c=0
count=0
while(n):
    if(n%10 in [2,3,5,7]):
        c=c+1
    n=n//10
print(c)

'''

'''
n = input()
count=0
l,u,d,s=0,0,0,0
    
for i in n:
    if i.isupper():
        u=1
    elif i.islower():
        l=1
    elif i.isdigit():
        d=1
    else:
        s=1
m=4-(l+u+d+s)
if(len(n)+m)<8:
    print(8-len(n))
elif (len(n)+m)==8:
    print(m)
else:
    print('-1')
    
'''

#convert all the vowels into uppercase
'''
input:placements
output:plAcEmEnts


n1 = input()
v=['a','e','i','o','u','A','E','I','O','U']
n2=''
for i in n1:
    if i in v:
        i=i.upper()
        n2 = n2+ i
    else:
        n2=n2+i
print(n2)

'''

#count and print the required
'''
a=input()
uv,uc,lv,lc,d,s=0,0,0,0,0,0
for i in a:
    if(i.isupper()):
        if(i in 'AEIOU'):
            uv=uv+1
        else:
            uc=uc+1
    elif(i.islower()):
        if(i in 'aeiou'):
            lv=lv+1
        else:
            lc=lc+1
    elif(i.isdigit()):
        d=d+1
    else:
        s=s+1
print("uv-",uv)
print("uc-",uc)
print("lv-",lv)
print("lc-",lc)
print("d-",d)
print("s-",s)


'''
#dupicate with order
'''
n1 = list(map(int,input().split()))
n2=[]
for i in n1:
    if i not in n2:
        n2.append(i)
for i in n2:
    print(i,'-',n1.count(i))

'''

#sliding window technique
'''
n1=input()
i=0
m=''
c=1
for i in range(len(n1)-1):
    if(n1[i] == n1[i+1]):
        c=c+1
    else:
        m=m+n1[i] + str(c)
        c=1
m =m+n1[-1] +str(c)
print(m)
'''



    








    
