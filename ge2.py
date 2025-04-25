class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None

    #insert at begin.
    def iab(self,data):
        new_node = Node(data)
        temp = self.head
        new_node.next = temp
        temp.prev = new_node
        self.head = new_node

    #insert at end.
    def iae(self,data):
        new_node = Node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    #insert at position.
    def iap(self,data,x):
        new_node = Node(data)
        temp = self.head
        for i in range(1,x-1):
            temp = temp.next
        new_node.prev = temp
        new_node.next = temp.next
        temp.next.prev = new_node
        temp.next = new_node
        
        
    #delete at begin.
    def dab(self):
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.head.prev = None

    #delete at end.
    def dae(self):
        temp = self.head
        temp1 = self.head.next
        while temp1.next is not None:
            temp = temp.next
            temp1 = temp1.next
        temp.next = None
        temp1.prev = None
        
    #delete at position.
    def dap(self,x):
        temp = self.head
        temp1 = self.head.next
        for i in range(1,x-1):
            temp = temp.next
            temp1 = temp1.next
        temp.next = temp1.next
        temp.next.prev = temp
        
    def display(self):
        if self.head is None:
            print("Doubly linked list is not exist")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data,end='->')
                temp = temp.next


l = DLL()
n1 = Node(10)
l.head = n1

n2 = Node(20)
n2.prev = n1
n1.next = n2

n3 = Node(30)
n3.prev = n2
n2.next = n3

n4 = Node(40)
n4.prev = n3
n3.next = n4


#l.iab(5)
#l.iae(50)
#l.iap(60,5)
#l.iap(70,3)
#l.dab()
#l.dae()
l.dap(1)
l.display()
        
