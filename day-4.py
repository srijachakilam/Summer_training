#oops
'''
class qwer:
    def __init__(self,v,u):
        self.a=u
        self.b=v
    def asd(self):
        print('hello',self.a)
        x.aaa
    def aaa(self):
        print('hi',self.b)
x=qwer(20,40)
y=qwer(50,10)
y=asd()
'''
#inheritance


'''


'''
#linkedlist
#we can create more than one linkedlist in a single program

class node:
    def __init__(self,d):
        self.data = d
        self.next = None

class sll:
    def __init__(self):
        self.head=None
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end='->')
            t=t.next

    def add_end(self,x):
        if(self.head==None):
            self.head=node(x)
        else:
            t=self.head
            while(t.next!=None):
                t=t.next
            t.next=node(x)

    def add_begin(self,x):
        t=self.head
        t1=node(x)
        t1.next=t
        self.head=t1
        
    #sum of all nodes
    def sum_nodes(self):
        t=self.head
        s=0
        while(t!=None):
            s=s+t.data
            t=t.next
        print('sum:',s)

    #search the key and print if found
    def search(self,k):
        t=self.head
        f=0
        while(t.next!=None):
            if(t.data==k):
                f=1
                break
            t=t.next
        if(f==1):
            print('Found')
        else:
            print('Not found')
            
    #find the sum of all even nodes in linked list
    def sum_even(self):
        t=self.head
        s=0
        while(t!=None):
            if(t.data%2==0):
                s=s+t.data
            t=t.next
        print('sum_of_even:',s)
                
    #find the middle element of the linked list
    def middle(self):
        slow=self.head
        fast=self.head
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
        print('middle_element:',slow.data)

    
    #check whether the length is even or odd    
    def even_odd(self):
        slow=self.head
        fast=self.head
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
        if (fast==None):
            print('even length')
        else:
            print('odd length')
            
    #find the possible pairs of the linked list
    def pairs(self):
        t1=self.head
        t2=self.head.next
        while(t1.next!=None):
            t2=t1.next
            while(t2!=None):
                print(t1.data,t2.data)
                t2=t2.next
            t1=t1.next
            
        
            
    #length of substring
    def los(self):
        t=self.head
        c=1
        max_c=0
        while(t.next!=None):
            if(t.data == (t.next.data)-1):
                c+=1
                if(max_c<c):
                    max_c=c
            else:
                
                c=1
            t=t.next
        
        print('maximum_count:',max_c)

    #selection sort
    #8 4 3 9 6 1
    def selection(self):
        c=0
        t1 = self.head
        while(t1.next!=None):
            f=0
            t2=t1.next
            while(t2!=None):
                if(t1.data>t2.data):
                    f=1
                    t=node(t1.data)
                    t1.data=t2.data
                    t2.data=t.data
                t2=t2.next
                c+=1
            t1=t1.next
            if(f==0):       #used to reduce the iterations
                break
            
        self.display()
        print(c)

    #bubble sort
        #8 4 3 9 6 1
    def bubble(self):
        t1=self.head
        c=0
        while(t1.next!=None):
            f=0
            t2=self.head
            while(t2.next!=None):
                if(t2.data>t2.next.data):
                    f=1
                    t=node(t2.data)
                    t2.data=t2.next.data
                    t2.next.data=t.data
                c+=1
                t2=t2.next
            if(f==0):       #reduce the no of iterations
                break

            t1=t1.next
        self.display()
        print(c)
    #reverse the linked list using 2 pointers

    '''def reverse(self):
        a=self.head
        b=a.next
        a.next=None
        c=b.next
        while(c.next!=None):
            #c=b.next
            b.next=a
            a=b
            b=c
            c=c.next
        self.head=b
        self.display()
        '''
        

            
l1=sll()
l2=sll()
l3=sll()
'''l1.head=node(10)'''
l3.add_begin(2)
l3.add_end(3)
l3.add_begin(1)
l3.add_end(4)
l3.add_end(7)
l3.add_end(8)
l3.add_end(9)
l3.display()
print()
l3.los()
print()


l1.add_end(10)
l1.add_end(20)
l1.add_end(30)
l1.add_end(40)
l1.add_begin(100)
print()
l1.sum_nodes()
print()
l1.search(10)
l1.search(110)

l2.add_begin(2)
l2.add_end(3)
l2.add_begin(9)
l2.add_end(8)
l2.add_end(1)
l2.add_end(7)
l2.add_end(6)
l2.add_end(5)

l1.add_end(50)
print()
l1.display()
print()
print()
l2.display()
print()
print()
l1.middle()
print()
l1.sum_even()
print()
l1.even_odd()
print()
l3.pairs()
print()

l2.selection()
l2.bubble()
l2.reverse()
