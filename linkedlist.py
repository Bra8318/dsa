class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self,data):
        new_node = Node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def at_position(self,data,pos):
        new_node = Node(data)
        temp = self.head
        for i in range(pos-1):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
       
        

    def remove_first(self):
        temp = self.head
        self.head = temp.next
        temp.next = None

    def remove_end(self):
        prev = self.head
        temp = self.head.next
        while temp.next is not None:
            temp = temp.next
            prev = prev.next
        prev.next = None

    def remove_at_position(self,pos):
        prev = self.head
        temp = self.head.next
        for i in range(1,pos-1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next
        

    def display(self):
        if self.head is None:
            print("Linked List is not existed")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data,end = "->")
                temp = temp.next

            print("none")


l = LinkedList()
node1 = Node(10)
l.head = node1
node2 = Node(20)
node1.next = node2
node3 = Node(30)
node2.next = node3
node4 = Node(40)
node3.next = node4
node5 = Node(50)
node4.next = node5


#function calling
l.insert_begin(5)
l.insert_end(60)
l.at_position(25,3)
l.at_position(50,0)
l.remove_at_position(3)
l.remove_first()
l.remove_end()
l.display()
