class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,root,key):
        if root is None:
            return Node(key)
        if root.data>key:
            root.left = self.insert(root.left,key)
        elif root.data < key:
            root.right = self.insert(root.right,key)
        return root

    def inorder(self,root):
        if root is not None:
            self.inorder(root.left)
            print(root.data,end=' ')
            self.inorder(root.right)
            
    def postorder(self,root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=' ')
            
    def preorder(self,root):
        if root is not None:
            print(root.data,end = ' ')
            self.preorder(root.left)
            self.preorder(root.right)

    def search(self,root,key):
        if root is None:
            print("key not found! ")
            return None
        if root.data == key:
            print("key is found! ")
            return root
        elif root.data < key:
            return self.search(root.right,key)
        else:
            return self.search(root.left,key)
       

    def delete(self,root,key):
        if root is None:
            print("Key not found! ")
            return root
        if root.data < key:
            root.right = self.delete(root.right,key)
        elif root.data > key:
            root.left = self.delete(root.left,key)
        else:
            #if no child.
            if root.left is None and root.right is None:
                return None
            #if one child.
            elif root.left is None:
                return root.right
                
            elif root.right is None:
                return root.left
                
        #if two children.    
            temp = self.min_value(root.right)
            root.data = temp.data
            root.right = self.delete(root.right,temp.data)
        return root


    def min_value(self,root):
        current = root
        while current.left is not None:
            current = current.left
        return current
    
bst = BST()

print("This is Binary search tree implementation")
while True:
    operation = input("\n enter your operations \n 1.Insert \n 2.Search \n 3.Delete \n 4.exit \n")

    if operation == "insert":
        data = input("enter your keys or data using space: ")
        key = list(map(int,data.split()))
        for k in key:
            #data = int(input("enter your keys or data"))
            bst.root = bst.insert(bst.root,k)
        
    elif operation == "search":
        x = int(input("enter your key for find in BST: "))
        bst.search(bst.root,x)
        
    elif operation == "delete":
        x = int(input("enter your key for delete in BST: "))
        bst.root = bst.delete(bst.root,x)
        
    else:
         break

    order = input("Enter your order type :")
    if order == "inorder":
        bst.inorder(bst.root)
    elif order == "postorder":
        bst.postorder(bst.root)
    elif order == "preorder":
        bst.preorder(bst.root)
    else:
        None



