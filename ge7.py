class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    def __init__(self):
        self.root = None

    def height(self,node):
        if not node:
            return 0
        return node.height

#right right rotation.
    def RR(self,y):
        x = y.left
        t = x.right

        x.right = y
        y.left = t

        y.height = 1 + max(self.height(y.left),self.height(y.right))
        x.height = 1 + max(self.height(x.left),self.height(x.right))

        return x

# left left rotation.
    def LL(self,x):
        y = x.right
        t = y.left

        y.left = x
        x.right = t

        x.height = 1 + max(self.height(x.left),self.height(x.right))
        y.height = 1 + max(self.height(y.left),self.height(y.right))

        return y


    
    def balance(self,node):
        bf = self.height(node.left) - self.height(node.right)
        if not node:
            return 0
        return bf


    def insert(self,root,key):
        if not root:
            return Node(key)

        if root.data < key:
            root.right = self.insert(root.right,key)
        elif root.data > key:
            root.left = self.insert(root.left,key)
        else:
            return root

        root.height = 1 + max(self.height(root.left),self.height(root.right))
        b = self.balance(root)

        #LL case.
        if b > 1 and key < root.left.data:
            return self.RR(root)

        #RR case.
        if b < -1 and key > root.right.data:
            return self.LL(root)

        #LR case.
        if b > 1 and key > root.left.data:
            root.left = self.LL(root.left)
            return self.RR(root)

        #RL case.
        if b < -1 and key < root.right.data:
            root.right = self.RR(root.right)
            return self.LL(root)
        return root


    def preorder(self,root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end=' ')
            self.inorder(root.right)

    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=' ')

    def search(self,root,key):
        if not root:
            print("key not found! ")
            return None
        if root.data == key:
            print("key is found! ")
            return root
        elif root.data < key:
            return self.search(root.right,key)
        else:
            return self.search(root.left,key)

    def min_value(self,root):
        current = root
        while current.left is not None:
            current = current.left
        return current
    
    def delete(self,root,key):
        if not root:
            return None
        if root.data < key:
            root.right =  self.delete(root.right,key)
        elif root.data > key:
            root.left = self.delete(root.left,key)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = min_value(root)
            root.data = temp.data
            root.right = self.delete(root.right,temp.data)

            root.height = 1 + max(self.height(root.left),self.height(root.right))
            b = balance(root)

            #LL case.
            if b > 1 and key < root.left.data:
                return self.RR(root)
            #RR case.
            elif b < -1 and key > root.right.data:
                return self.LL(root)
            #LR case.
            elif b > 1 and key > root.left.data:
                root.left = self.LL(self.left)
                return self.RR(root)
            elif b < -1 and key < root.right.data:
                root.right = self.RR(root.right)
                return self.LL(root)
        return root


a = AVL()
while True:
    print("\nAVL tree implementation")
    operation = input("\n Enter your operation \n1.Insert \n2.Search \n3.Delete \n4.Exit \n")
    if operation == "insert" or operation == "1":
        data = input("enter your keys or data using space: ")
        key = list(map(int,data.split()))
        for k in key:
            a.root = a.insert(a.root,k)
        print("Data submitted successfully.")

    elif operation == "search" or operation == "2":
        x = int(input("Enter the key for search! "))
        a.search(a.root,x)

    elif operation == "delete" or operation == "3":
        x = int(input("Enter the key for delete! "))
        a.root = a.delete(a.root,x)

    else:
        break
    #a.root = a.preorder(a.root)
    order = input("\n Enter your operations \n1.Preorder \n2.Inorder \n3.Postorder \n4.Exit \n")
    if order == "1" or order == "preorder":
        a.preorder(a.root)
        
    elif order == "2" or order == "inorder":
        a.inorder(a.root)
        
    elif order == "3" or order == "postorder":
        a.postorder(a.root)
        
    else:
        break



