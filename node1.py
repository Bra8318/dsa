class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None

    #insert the value

    def atBegin(self,data):
        new_node = Node(data)
        temp = self.head
        temp.prev = new_node
        new_node.next = temp
        self.head = new_node

    def atEnd(self,data):
        new_node = Node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def atPosition(self,data,pos):
        new_node = Node(data)
        temp = self.head
        for i in range(pos-1):
            temp = temp.next
        new_node.prev = temp
        new_node.next = temp.next
        temp.next.prev = new_node
        temp.next = new_node

    #deletion of the value
    def removeAtBegin(self):
            temp = self.head
            self.head = temp.next
            temp.prev = None

    def removeAtEnd(self):
        temp = self.head
        temp1 = self.head.next
        while temp1.next is not None:
            temp1 = temp1.next
            temp = temp.next
        temp.next = None

    def removeAtPosition(self,pos):
        temp = self.head
        temp1 = self.head.next
        for i in range(1,pos-1):
            temp = temp.next
            temp1 = temp1.next
        temp.next = temp1.next

    
        
        

    def display(self):
        if self.head is None:
            print("Double linked list not exist")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data,end = "--><--")
                temp = temp.next
               



l = DLL()
n1 = Node(10)
l.head = n1
n2 = Node(20)
n1.next = n2
n2.prev = n1
n3 = Node(30)
n2.next = n3
n3.prev = n2
n4 = Node(40)
n3.next = n4
n4.prev = n3
l.atBegin(5)
l.atEnd(50)
l.atPosition(25,3)
l.removeAtBegin()
l.removeAtEnd()
l.removeAtPosition(3)
l.display()
