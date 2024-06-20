'''
class Node:
    def __init__(self,n):
        self.data=n
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
        
    def add(self,n):
        if self.root==None:
            self.data=Node(n)
            print('added')
            return
        else:
            if self.data<n:
                print('l')
                self.left.add(n)
            
            else:
                print('r')
                self.right.add(n)

    def inorder(self):
        if(self.data==None):
            return
        else:
            print(self.root)
            self.left.inorder()
            self.right.inorder()
    
t1=BST()
t1.add(10)
t1.add(20)
t1.add(30)
t1.add(9)
t1.add(8)
#t1.inorder()
'''


'''
class node:
    def __init__(self,d):
        self.data=d
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def create(self,root,d):
        if root ==None:
            return node(d)
        elif(root.data>d):
            #print(root.data)
            root.left=self.create(root.left,d)
        else:
            #print(root.data)
            root.right=self.create(root.right,d)
        return root
    def preorder(self,root):
        if root:
            print(root.data,end='->')
            self.preorder(root.left)
            self.preorder(root.right)
    def inorder(self,root):
        if root:
            
            self.inorder(root.left)
            print(root.data,end='->')
            self.inorder(root.right)

    def postorder(self,root):
        
            if(root!=None):
                self.postorder(root.left)
                self.postorder(root.right)
                print(root.data,end='->')

            
            

t1=BST()
t1.root=node(11)
t1.create(t1.root,10)
t1.create(t1.root,5)
t1.create(t1.root,20)
t1.create(t1.root,1)
t1.create(t1.root,6)
print()
print('pre')
t1.preorder(t1.root)
print()
print('post')
t1.postorder(t1.root)
print()
print('in')
t1.inorder(t1.root)
        



----OR----
'''

class node:
  def __init__(self,n):
    self.data=n
    self.left=None
    self.right=None
class tree:
    def __init__(self):
        self.root=None
    def creat(self,root,x):
        if self.root==None:
            self.root=node(x)
            return self.root
        if root==None:
            return node(x)
        elif(root.data>x):
            root.left=self.creat(root.left,x)
        else:
            root.right=self.creat(root.right,x)
        return root
    def preorder(self,root):
        if root:
            print(root.data,end='->')
            self.preorder(root.left)
            self.preorder(root.right)
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end='->')
            self.inorder(root.right)
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end='->')

    def sum_nodes(self,root,s):
        if root:
            s=s+root.data+self.sum_nodes(root.left,s)+self.sum_nodes(root.right,s)
        return s
    def even(self,root,es):
        if root:
            if root.data%2==0:
                es=es+root.data+self.even(root.left,es)+self.even(root.right,es)
            else:
                es=es+self.even(root.left,es)+self.even(root.right,es)
        return es

    def odd(self,root,os):
        if root:
            if root.data%2!=0:
                os=os+root.data+self.odd(root.left,os)+self.odd(root.right,os)
            else:
                os=os+self.odd(root.left,os)+self.odd(root.right,os)
        return os
    def abs_diff(self,root):
        x=self.even(self.root,0)
        y=self.odd(self.root,0)
        return (x-y)
    def abs_dif(self,root):
        if root:
            if root.data%2!=0:
                return root.data+self.abs_dif(root.left)+self.abs_dif(root.right)
            else:
                return self.abs_dif(root.left)+self.abs_dif(root.right)-root.data
        else:
            return 0
            '''if root.data%2==0:
                es=es+root.data+self.even(root.left,es)+self.even(root.right,es)
            else:
                es=es+self.even(root.left,es)+self.even(root.right,es)
                '''
    def height(self,root):
        if root==None:
            return -1
        return max(self.height(root.left),self.height(root.right))+1
    
    def balanced(self,root):
        return abs(self.height(root.left)-self.height(root.right))

    def no_of_leaf(self,root,s):
        if root==None:
            return s
        '''if root.left==None and root.right==None:
            return 1
        return (self.no_of_leaf(root.left,s)+self.no_of_leaf(root.right,s))
        '''
        if root.left==None and root.right==None:
            s=s+1

        s=self.no_of_leaf(root.left,s)
        s=self.no_of_leaf(root.right,s)
        return s
    def sum_leaf(self,root,s):
        ''' if root==None:
            return 0
        if root.left==None and root.right==None:
            return root.data+self.sum_leaf(root.left)+self.sum_leaf(root.right)
        return self.sum_leaf(root.left)+self.sum_leaf(root.right)  
        '''
        if root==None:
            return s
        if root.left==None and root.right==None:
            s=s+root.data
        s=self.sum_leaf(root.left,s)
        s=self.sum_leaf(root.right,s)
        return s
    def search(self,root,k):
        if root:
            if root.data==k:
                return True
            elif root.data>k:
                return self.search(root.left,k)
            else:
                return self.search(root.right,k)
        else:
            return False
        return False
    def depth(self,root,y,c):
        if root==None:
            return -1
        if root.data==y:
            return c
        elif root.data>y:
            return self.depth(root.left,y,c+1)
        else:
            return self.depth(root.right,y,c+1)

    def topv(self,root):
      if root==None:
        return 
      d={}
      q=[(root,0)]
      while(q):
        root=q[0][0]
        if root.left!=None:
          q.append((root.left,q[0][1]-1))
        if root.right!=None:
          q.append((root.right,q[0][1]+1))
        if(q[0][1] not in d):
          d[q[0][1]]=root.data
        q.pop(0)
       
      for i in sorted(d):
        print(d[i],end=" ")
        
      
        
      
        
    def botv(self,root):
        pass
      
    def leftv(self,root,c,l):#left view
      if root==None:
        return
      if c not in l:
        l.append(c)
        print(root.data)
      self.leftv(root.left,c+1,l)
      self.leftv(root.right,c+1,l)

    def rightv(self,root,c,l):#right view
      if root==None:
        return
      if c not in l:
        l.append(c)
        print(root.data)
      self.rightv(root.right,c+1,l)
      self.rightv(root.left,c+1,l)
        
t1=tree()
t1.creat(t1.root,10)
t1.creat(t1.root,5)
t1.creat(t1.root,2)
t1.creat(t1.root,7)
t1.creat(t1.root,15)
t1.creat(t1.root,11)
t1.creat(t1.root,20)
t1.creat(t1.root,21)
t1.creat(t1.root,22)
#t1.creat(t1.root,20)
print()
print('pre')
t1.preorder(t1.root)
print()
print('in')
t1.inorder(t1.root)
print()
print('post')
t1.postorder(t1.root)
print()
print('sum')
print(t1.sum_nodes(t1.root,0))
print()
print('difference b/w sum of left and sum of right subtree')
print(t1.sum_nodes(t1.root.left,0)-t1.sum_nodes(t1.root.right,0))
print()
print('even sum')
print(t1.even(t1.root,0))
print('odd sum')
print(t1.odd(t1.root,0))
print()
print('absolute diff')
print(t1.abs_diff(t1.root))
print()
print('method-2 abs dif')
print(abs(t1.abs_dif(t1.root)))
print()
print('height')
print(t1.height(t1.root))
print()
print('balanced')
if t1.balanced(t1.root):
    print('yes')
else:
    print('no')
print()
print('no of leaf nodes')
print(t1.no_of_leaf(t1.root,0))
print()
print('sum of leaf nodes')
print(t1.sum_leaf(t1.root,0))
print()
'''print('search')
k=int(input())
print(t1.search(t1.root,k))
print()
print('depth')
y=int(input())
print(t1.depth(t1.root,y,0))
print()
'''
print('leftview')
t1.leftv(t1.root,0,[])
print()
print('rightview')
t1.rightv(t1.root,0,[])
print()
print('topview')
print(t1.topv(t1.root))
