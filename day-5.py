#leetcode questions

'''key='hello world'
key=key.replace(' ','')
print(key)
s=''
for i in key:
    if i not in s:
        s=s+i
asc=97
for i in range(len(s)):
    
    s[i]=chr(asc)
    asc+=1
print(s)



s1=''
asc=97
for i in range(26):
    s1=s1+chr(asc) 
print(s1)
'''

#3120 question leetcode
'''
word='AabBCc'
s=''
for i in word:
    if i not in s:
        s=s+i
c=0
for i in s:
    if (i.upper() in s) and  (i.lower() in s):
        c+=1
print(c//2)



word='ASD'
if word.isupper():
    print('dg')


word1='Hello'


word='AaaAB'
s=''
for i in word:
    if i.upper() and i.lower() in word:
        s=s+i
print(s)
'''


#linked list


class node:
    def __init__(self,d):
        self.data=d
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def add_back(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            t=node(x)
            self.tail.next=t
            t.prev=self.tail
            self.tail=self.tail.next
    def add_front(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            t=node(x)
            t.next=self.head
            t.prev=None
            self.head.prev=t
            self.head=t
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end='->')
            t=t.next
        print()

    def rev_display(self):
        t=self.tail
        while(t!=None):
            print(t.data,end='->')
            t=t.prev
        print()

    def search(self,k):
        t1=self.head
        t2=self.tail
        f=0
        while(t1 != t2 and t1!=t2.next): #for even length and odd length
            if(t1.data==k or t2.data==k):
                f=1
                break
            t1=t1.next
            t2=t2.prev
        if(t1.data==k):     #to check the middle element of odd length list
            f=1
        if(f==0):
            print('not found')
        else:
            print('found')

    def even_odd_length(self):
        t1=self.head
        t2=self.tail
        f=1
        while(t1!=t2 and t1!=t2.next):
            t1=t1.next
            t2=t2.prev
        if(t1==t2):
            print('odd')
        else:
            print('even')

    def palindrome(self):
        t1=self.head
        t2=self.tail
        f=1
        while(t1!=t2 and t1 !=t2.next):
            if(t1.data == t2.data):
                f=0
            else:
                f=1
                break
            t1=t1.next
            t2=t2.prev
        if(f==0):
            print('palindrome')
        else:
            print('not palindrome')

    def half(self):  #only possible for even length
        #method-1
        '''t1=self.head
        t2=self.tail
        while(t1.next!=t2):
            t1=t1.next
            t2=t2.prev
        t1=self.head
        #print(t2.data)
        while(t2!=None):
            temp=node(t1.data)
            t1.data=t2.data
            t2.data=temp.data
            t1=t1.next
            t2=t2.next'''

        '''------OR-----'''
        #method-2
        slow=self.head
        fast=self.head
        while(fast!=None):
            fast=fast.next.next
            slow=slow.next
        self.tail.next=self.head
        self.head.prev=self.tail
        t1=slow.prev
        t1.next=None
        slow.prev=None
        self.head=slow
        self.tail=t1
            
        
            
        
                
        
l1=dll()
l1.add_front(15)
l1.add_front(12)
l1.add_front(10)
l1.add_front(9)
l1.add_front(8)
l1.add_front(7)
l1.add_front(5)
l1.add_front(3)
l1.display()
l1.rev_display()
l1.search(10)
l1.search(990)
l1.even_odd_length()
l1.palindrome()
l1.display()
l1.half()
l1.display()
















