class Bird:
    def __init__(self, bird_type, rate, wing):
        self.type = bird_type
        self.rate = rate
        self.wing = wing

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BSTree:
    
    def __init__(self):
        self.root = None
# f1:
    def insert(self, input_data):
        birds_data = input_data.split(' ')
        for bird_data in birds_data:
            bird_info = bird_data.strip('()').split(',')
            xType, xRate, xWing = bird_info[0], int(bird_info[1]), int(bird_info[2])
            if xType[0] == 'B' or xRate > 10:
                return  
            new_bird = Bird(xType, xRate, xWing)
            if self.root is None:
                self.root = Node(new_bird)
            else:
                self._insert_recursive(self.root, new_bird)
    def _insert_recursive(self, current_node, bird):
        if bird.rate <= current_node.data.rate:
            if current_node.left is None:
                current_node.left = Node(bird)
            else:
                self._insert_recursive(current_node.left, bird)
        else:
            if current_node.right is None:
                current_node.right = Node(bird)
            else:
                self._insert_recursive(current_node.right, bird)
            
# breath first search for f1 output:
    def bread_first(self,root):
        h = self.height(root)
        for i in range(1, h+1):
            self.p_bread_first(root, i)

    def p_bread_first(self,root, level):
        lst = []
        if root is None:
            return
        if level == 1:
            print((f"({root.data.type},{root.data.rate},{root.data.wing})"),end = " ")
        elif level > 1:
            self.p_bread_first(root.left, level-1)
            self.p_bread_first(root.right, level-1)

    def height(self,node):
        if node is None:
            return 0
        else:
            lheight = self.height(node.left)
            rheight = self.height(node.right)
            return max(rheight+1, lheight +1)

# f2:
    def pre_order(self,node):
        lst = [4,5,6,7,8,9]
        if node is None:
            return
        if node.data.wing in lst:
            print((f"({node.data.type},{node.data.rate},{node.data.wing})"),end = " ")
 
        self.pre_order(node.left)
 
        self.pre_order(node.right)
#f3:
    global lst
    lst = [] # list for check odd position
    def f3(self,root):
        h = self.height(root)
        for i in range(1, h+1):
            self.bread_first_f3(root,i)
            
    def bread_first_f3(self,root, level):
        if root is None:
            return
        if level == 1:
            lst.append(root)
            if lst.index(root)%2 == 0:
                print((f"({root.data.type},{root.data.rate},{root.data.wing})"),end = " ")

        elif level > 1:
            self.bread_first_f3(root.left, level-1)
            self.bread_first_f3(root.right, level-1)

#f4:
    def Postorder(self, root):
        if root == None:
            return
 
        self.Postorder(root.left)
 
        self.Postorder(root.right)
        if root.data.wing <=4 and root.data.rate >6:
            print((f"({root.data.type},{root.data.rate},{root.data.wing})"),end = " ")
#f5:
    def Inorder(self,root):
        if root:
            self.Inorder(root.left)
            if root.data.type[0] in ['A','C']:
                print((f"({root.data.type},{root.data.rate},{root.data.wing})"),end = " ")
         
            self.Inorder(root.right)
    global lst2
    lst2 = []

#f6:
    def Inorder6(self,root):
        if root:
            self.Inorder6(root.left)
            print((f"({root.data.type},{root.data.rate},{root.data.wing})"),end = " ")
            self.Inorder6(root.right)
    def Inorder_3th(self,root): # return 3th node when perform inorder 
        if root:
            self.Inorder_3th(root.left)
            lst2.append(root)
            self.Inorder_3th(root.right)
        return lst2
    def get_father(self,tree): # find father of 3-th node
        for node in tree.Inorder_3th(tree.root):
            if node.left is tree.Inorder_3th(tree.root)[2] or node.right is tree.Inorder_3th(tree.root)[2]:
                return node.data.rate
            
    def getLeftMostNode(self, node):
        temp = node
        while temp.left is not None:
            temp = temp.left
        return temp
    
    def deleteNode(self, root,k):
        if root is None:
            return root
        if k < root.data.rate:
            root.left = self.deleteNode(root.left, k)
        
        elif k > root.data.rate:
            root.right = self.deleteNode(root.right, k)
        
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            
            temp = self.getLeftMostNode(root.right)
            
            root.data.rate = temp.data.rate
            
            root.right = self.deleteNode(root.right, temp.data.rate)
        return root
    
#f7:
    global lst3
    lst3 = []
    def Postorder7(self, root):
        if root == None:
            return
 
        self.Postorder7(root.left)
        self.Postorder7(root.right)
        print(f"({root.data.type},{root.data.rate},{root.data.wing})",end = " ")
    def get_6th(self, root):
        if root:
            self.get_6th(root.left)
            self.get_6th(root.right)
            lst3.append(root.data.rate)
        return lst3
#f8:
    global lst4
    lst4 = []
    def pre_order8(self,root):
        if root is None:
            return
        print((f"({root.data.type},{root.data.rate},{root.data.wing})"),end = " ")
 
        self.pre_order8(root.left)
 
        self.pre_order8(root.right)
    def get_f8(self, root):
        if root is None:
            return
        lst4.append(root) 
        self.pre_order8(root.left)
        self.pre_order8(root.right)
        
    
    
        
def main():
    while True:
        choice = input("\nEnter your choice 1-11: ")

        if choice == '1':
            tree = BSTree()
            f1_input = input('enter f1 input: ')
            print('f1 input:', f1_input)
            tree.insert(f1_input)
            print('f1 output:', end = ' ')
            tree.bread_first(tree.root)
        elif choice == '2':
            tree2 = BSTree()
            f2_input = input('\nenter f2 input: ')
            print('f2 input:', f2_input)
            tree2.insert(f2_input)
            print('f2 output:', end = ' ')
            tree2.pre_order(tree2.root)
        elif choice == '3':
            tree3 = BSTree()
            f3_input = input('\nenter f3 input: ')
            print('f3 input:', f3_input)
            tree3.insert(f3_input)
            print('f3 output:', end = ' ')
            tree3.f3(tree3.root)
        elif choice == '4':
            tree4 = BSTree()
            f4_input = input('\nenter f4 input: ')
            print('f4 input:', f4_input)
            tree4.insert(f4_input)
            print('f4 output:', end = ' ')
            tree4.Postorder(tree4.root)
        elif choice == '5':
            tree5 = BSTree()
            f5_input = input('\nenter f5 input: ')
            print('f5 input:', f5_input)
            tree5.insert(f5_input)
            print('f5 output:', end = ' ')
            tree5.Inorder(tree5.root)
        elif choice == '6':
            tree6 = BSTree()
            f6_input = input('\nenter f6 input: ')
            tree6.insert(f6_input)
            print('f6 input:',end = ' ' )
            tree6.Inorder6(tree6.root)
            print('\nf6 output:', end = ' ')
            tree6.Inorder6(tree6.deleteNode(tree6.root,tree6.get_father(tree6)))

if __name__ == "__main__":
    main()

    
    

        
    
    
    