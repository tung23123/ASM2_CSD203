import math
from Bird import *
from Node import *
from MyQueue import *
class BSTree:
    def __init__(self):
        self.root = None
    # end def
    def clear(self):
        self.root = None
    def isEmpty(a):
        return a.root == None
    #end def
    def visit(a,p):
        if p==None:
            return
        print(f"{p.data}",end =" ")
    #end def
    def preOrder(a,p):
        if p==None:
            return
        a.visit(p)
        a.preOrder(p.left)
        a.preOrder(p.right)
    #end def
    def preVisit(a):
        a.preOrder(a.root)
        print("")
    #end def
    def postOrder(a,p):
        if p==None:
            return
        a.postOrder(p.left)
        a.postOrder(p.right)
        a.visit(p)
    #end def
    def postVisit(a):
        a.postOrder(a.root)
        print("")
    #end def
    def inOrder(a,p):
        if p==None:
            return
        a.inOrder(p.left)
        a.visit(p)
        a.inOrder(p.right)        
    #end def
    def inVisit(a):
        a.inOrder(a.root)
        print("")
    #end def
    def breadth_first(a):
        if a.isEmpty():
            return
        my = MyQueue()
        my.EnQueue(a.root)
        while not my.isEmpty():
            p = my.DeQueue()
            a.visit(p)
            if p.left!=None:
                my.EnQueue(p.left)
            if p.right!=None:
                my.EnQueue(p.right)
        print("")        
    #end def
    def insert(a,type, rate, wing):        
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 1 ========

        newNode = Node(data = Bird(type, rate,wing))
        if type[-1] == "B" or  rate > 10:
            return
        if a.root is None:
            a.root = newNode
        else:
            current = a.root
            while current:
                if rate < current.data.Rate:
                    if current.left:
                        current = current.left
                    else:
                        current.left = newNode
                    
                        break
                elif rate > current.data.Rate:
                    if current.right:
                        current = current.right
                    else:
                        current.right = newNode
                        
                        break
                else:
                     break

        pass 
    def f2(self):        
       # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 2========
        self.preOrder2(self.root)
        print("")
    def preOrder2(a,p):
        if p==None:
            return
        if p.data.Wing in [4,5,6,7,8,9,10]:
            a.visit(p)
        a.preOrder2(p.left)
        a.preOrder2(p.right)
        pass
    
    
    def f3(self):
    # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 3========

        self.breadth_first3()
        
    def breadth_first3(a):
        if a.isEmpty():
            return
        dic = {}
        my = MyQueue()
        my.EnQueue(a.root)
        count = 1
        dic.update({a.root:count})
        while not my.isEmpty():
            p = my.DeQueue()
            if dic[p]%2 == 1:
                a.visit(p)
            if p.left!=None:
                my.EnQueue(p.left)
                count += 1
                dic.update({p.left:count})
            if p.right!=None:
                my.EnQueue(p.right)
                count += 1
                dic.update({p.right:count})
        print("") 

    def f4(a,p):
        if p==None:
            return
        a.f4(p.left)
        a.f4(p.right)
        if p.data.Wing <= 4 and p.data.Rate > 6:
            a.visit(p)
    
    def f5(a,p):
        if p==None:
            return
        a.f5(p.left)
        if p.data.Type[0] == 'A' or p.data.Type[0] == 'C':
            a.visit(p)
        a.f5(p.right)
    def f7(self):
        self.postOrder7(self.root)
    
    def postOrder7(a,p):
        count = 0
        if p==None:
            return
        a.postOrder7(p.left)
        a.postOrder7(p.right)
        if count != 6:
            count += 1
        if count == 6:
            return p
    def delByCopyLeft(self,p):
        if not p:
            return
        rightmost = p.left
        parent = None
        while rightmost.right:
            parent = rightmost
            rightmost = rightmost.right
        p.data = rightmost.data
        if parent:
            parent.right = rightmost.left
        else:
            p.left = rightmost.left
        return
    
    
    def _find_parent(self, root, node):
        if not root:
            return None
        if root.left == node or root.right == node:             
            return root
        if node.data.Rate < root.data.Rate: 
            return self._find_parent(root.left, node)
        else:
            return self._find_parent(root.right, node)
    def insert_right_subtree(self, left_subtree, right_subtree):
        if left_subtree is None:
            return
        current = left_subtree
        while current.right:
            current = current.right
        current.right = right_subtree

        pass
    def delByMergingLeft(self, node):
        parent = self._find_parent(self.root,node)

        if parent is None:
            self.root = node.left  
            self.insert_right_subtree(node.left, node.right)
        else:
            if parent.left == node:
                parent.left = node.left  
                self.insert_right_subtree(node.left, node.right)
            else:
                parent.right = node.left  
                self.insert_right_subtree(node.left, node.right)   
    def f6(a,p):
        count = 0 
        if p==None:
            return
        a.f6(p.left)
        if count < 3:
            count += 1
        if count == 3:
            return self.delByMergingLeft(p)
        a.f6(p.right)
        
    


# end class
