#sum of even number in list1 and odd numbers in list2
'''
ip:
    6 3 2 9 4 7
    8 7 5 3 6 9

op:
    
    [13, 11, 9, 15, 9, 7, 5, 11, 11, 9, 7, 13]

'''

'''
def che1(n1,n2,i,j,l):
    if i==len(n1):
        return l
    #print(l)
    def check(n1,n2,i,j,l):
        if j==len(n2):
            return l
        if n1[i]%2==0:
            if n2[j]%2!=0:
                x=n1[i]+n2[j]
                l.append(x)
        j+=1
        #print(l)
        l=check(n1,n2,i,j,l)
        return l
    l=check(n1,n2,i,j,l)
    l=che1(n1,n2,i+1,j,l)
    return l

n1=list(map(int,input().split()))
n2=list(map(int,input().split()))
l=[]
print(che1(n1,n2,0,0,l))
'''


#sum of all the possible sum from even number from list1 to odd in list2

'''
ip:
    6 3 2 9 4 7
    8 7 5 3 6 9

op:

        
    [13, 11, 9, 15, 9, 7, 5, 11, 11, 9, 7, 13]
    [48,32,40]

'''

'''
def che1(n1,n2,i,j,l,a):
    if i==len(n1):
        return a
    #print(l)
    def check(n1,n2,i,j,l,a):
        if j==len(n2):
            return a
        if n1[i]%2==0:
            if n2[j]%2!=0:
                x=n1[i]+n2[j]
                l.append(x)
        j+=1
        #print(l)
        a=check(n1,n2,i,j,l,a)
        return a
    a.append(sum(l))
    
    #print(a)
    a=check(n1,n2,i,j,l,a)

    a=che1(n1,n2,i+1,j,l,a)
    return a

n1=list(map(int,input().split()))
n2=list(map(int,input().split()))
print(che1(n1,n2,0,0,[],[]))
'''

