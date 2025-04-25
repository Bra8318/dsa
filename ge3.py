class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CLL:
    def __init__(self):
        self.head = None
        self.tail = None

    #insert at begin.
    def iab(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head


    #insert at end.
    def iae(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
        
    #insert at position.
    def iap(self,data,x):
        new_node = Node(data)
        if x == 1:
            self.iab(data)
        else:
            temp = self.head
            for i in range(1,x-1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node


    #delete at begin.
    def dab(self):
        if self.head is None:
                print("Circular list does not exist.")
        else:
            if self.head == self.tail:
                self.tail = None
            else:
                temp = self.head   
                self.head = temp.next
                self.tail.next = self.head
                temp = None

    #delete at end.
    def dae(self):
        if self.head is None:
            print("Circular list does not exist.")
        else:
            if self.head == self.tail:
                self.tail = None
            else:
                temp = self.head
                while temp.next != self.tail:
                    temp = temp.next
                temp.next = self.head
                self.tail = None
                self.tail = temp

    #delete at position.
    def dap(self,x):
        if self.head is None:
            print("Circular list does not exist.")
        elif x == 1:
            self.dab()
        else:
            temp = self.head
            temp1 = self.head.next
            for i in range(1,x-1):
                temp = temp.next
                temp1 = temp1.next
            temp.next = temp1.next
            if temp1 == self.tail:
                self.tail = temp
            temp1 = None


    #searching .
    def search(self):
        item = int(input())
        count = 0
        flag = 0
        temp = self.head
        while temp != self.tail:
            if item == temp.data:
                flag = 1
                break
            temp = temp.next
            count += 1    
        else:
            if temp == temp.data:
               flag = 1
        if flag == 1:
            print(item,"item is found at position!",count+1)
            print(temp)
        else:
            print(item,"item is not found at any position!")
            
        
        
        
    def display(self):
        if self.head is None:
            print("Circular list does not exist.")
        else:
            temp = self.head
            print(temp.data,end='->')
            while temp.next != self.head:
                temp = temp.next
                print(temp.data,end='->')
            print(temp.next.data)
        



l = CLL()
n1 = Node(10)
l.head = n1
l.tail = n1
l.tail.next = l.head

n2 = Node(20)
n1.next = n2
l.tail = n2
l.tail.next = l.head

n3 = Node(30)
n2.next = n3
l.tail = n3
l.tail.next = l.head 

n4 = Node(40)
n3.next = n4
l.tail = n4
l.tail.next = l.head

#l.iab(5)
#l.iae(50)
#l.iae(60)
#l.iap(25,3)
#l.dae()
#l.dap(3)
l.search()

#l.display()
