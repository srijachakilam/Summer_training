'''
ip:
    7
1 school
1 world
1 word
1 scholar
2 word
True -->op
2 wood
False -->op
3 sch
True -->op


op:

'''
'''
n=int(input())
l=[]
c=0
for i in range(n):
    a=int(input())
    b=input()
    if a==1:
        if b not in l:
        #l.append(a)
            l.append(b)
    elif a==2:
        if b in l:
            print(True)
        else:
            print(False)
    elif a==3:
        for i in range(len(l)):
            #if i.startswith(b)- to check prefix
            #if i.endswith(b)-to check suffix
            if b in l[i]:
                c=c+1  
        print(c)
    elif a==4:
        for b in l:
            l.remove(b)
        print(l)
'''

#tries
'''
class node:
    def __init__(self):
        self.d={}
        self.flag=0
        self.c={}
class tries:
    def __init__(self):
        self.root=node()

    def insert(self,s):
        t=self.root
        for i in s:
            if i not in t.d:
                t.d[i]=node()
            t=t.d[i]
        t.flag=1
        #print(t.flag)
        #print(t.d)
    def search(self,a):
        t=self.root
        for i in a:
            if i not in t.d:
                return False
            t=t.d[i]
        if t.flag==1:
            return True
        else:
            return False

    def prefix(self,a):
        t=self.root
        for i in a:
            if i not in t.d:
                return False
            t=t.d[i]
        #print(t.c[i])
        return True

    def print_prefix(self,a):#print all the words with given prefix
        def fun(t,s):
            if t.flag==1:
                print(s)
            for i in t.d:
                fun(t.d[i],s+i)
        t=self.root
        s=''
        for i in a:
            if i in t.d:
                s=s+i
                t=t.d[i]
            else:
               print('False')
               return 
        fun(t,s)

    
t1=tries()
n=int(input())
for i in range(n):
    a,s=input().split()
    if a=='1':
        t1.insert(s)
    elif a=='2':
        print(t1.search(s))
    elif a=='3':
        print(t1.prefix(s))
    else:
        t1.print_prefix(s)
''' 
#print the longest prefix based on given list of prefix list



class node:
    def __init__(self):
        self.d={}
        self.flag=0
        self.c={}
class tries:
    def __init__(self):
        self.root=node()

    def insert(self,s):
        t=self.root
        for i in s:
            if i not in t.d:
                t.d[i]=node()
            t=t.d[i]
        t.flag=1
        #print(t.flag)
        #print(t.d)
    def long_prefix(self,a):#print all the words with given prefix
        def fun1(t,s,m):
            if t.flag==1:
                if len(s)>m:
                    m=len(s)
            for i in t.d:
                fun1(t.d[i],s+i,m)
            return m
        t=self.root
        s=''
        m=0
        for i in a:
            if i in t.d:
                s=s+i
                t=t.d[i]
            else:
               return 
        fun1(t,s,m)
        print(l)
        return m
t1=tries()
t1.insert('words')
t1.insert('word')
t1.insert('apple')
t1.insert('apricot')
t1.insert('worlds')
x=list(map(str,input().split()))
l=[]
for i in x:
    b=t1.long_prefix(i)
        
