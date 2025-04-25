class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        
    #insert at the begin.
    def iab(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    #insert at position.
    def iap(self,data,x):
        new_node = Node(data)
        temp = self.head
        for i in range(x-1):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    #insert at end.
    def iae(self,data):
        new_node = Node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
       

    #delete at the begin.
    def dab(self):
        temp = self.head
        self.head = temp.next
        temp.next = None

    #delete at position.
    def dap(self,x):
        temp = self.head
        temp1 = self.head.next
        for i in range(1,x-1):
            temp = temp.next
            temp1 = temp1.next
        temp.next = temp1.next
        temp1.next = None

    #delete at end.
    def dae(self):
        temp = self.head
        temp1 = self.head.next
        while temp1.next is not None:
            temp = temp.next
            temp1 = temp1.next
        temp.next = None


    #searching.
    def search(self):
        item = int(input("Enter item for search.\n"))
        flag = 0
        count = 0
        temp = self.head
        while temp.next is not None:
            if item == temp.data:
                flag = 1
                break
            temp = temp.next
            count += 1
        else:
            if item == temp.data:
                flag = 1
        if flag == 1:
            print(item,"item is found at position",count+1)
            print(temp)
        else:
            print(item,"item is not found at any position")

            
    def display(self):
        if self.head is None:
            print("Linked list is not exist")
        else:
            temp = self.head 
            while temp is not None:
                print(temp.data,end = '->')
                temp = temp.next


l = SLL()
n1 = Node(10)
l.head = n1

n2 = Node(20)
n1.next = n2

n3 = Node(30)
n2.next = n3

#l.iab(5)
#l.iab(2)
#l.iap(25,3)
#l.dab()
#l.dap(2)
#l.iae(40)
#l.iae(50)
#l.dae()
l.search()
    

#l.display()
