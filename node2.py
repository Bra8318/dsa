class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
#Singly circular linked list.
class CLL:
    def __init__(self):
        self.head = None 
        self.end = None
        
    #insert the node.
    def atFirst(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.end = new_node
            self.end.next = self.head
        else:
            new_node.next = self.head
            self.end.next = new_node
            self.head = new_node
         
        
    def atLast(self,data):
         new_node = Node(data)
         if self.head is None:
             self.head = new_node
             self.end = new_node
             self.end.next = self.head
         else:
             self.end.next = new_node
             self.end = new_node
             self.end.next = self.head
             

    def atPosition(self,data,pos):
        new_node = Node(data)
        if self.head is None:
             self.head = new_node
             self.end = new_node
             self.end.next = self.head
        else:
            if pos == 1 or pos == 0:
                self.atFirst(data)
            elif pos == -1:
                self.atLast(data)
            else:
                temp = self.head
                for i in range(1,pos-1):
                    temp = temp.next
                new_node.next = temp.next
                temp.next = new_node
        
           
    #Delete the node.
    def removeAtFirst(self):
        if self.head is None:
            print("Node is not exist")
        elif self.head == self.end:
             self.head = None
             self.end = None
 
        else:
            temp = self.head
            self.head = temp.next
            self.end.next = self.head

    def removeAtEnd(self):
         if self.head is None:
            print("Node is not exist")
         elif self.head == self.end:
             self.head = None
             self.end = None
         else:
            temp = self.head
            while temp.next != self.end:
                temp = temp.next
            temp.next = self.head
            self.end = None
            self.end = temp

    def removeAtPosition(self,pos):
         if self.head is None:
            print("Node is not exist")
         elif self.head == self.end:
             self.head = None
             self.end = None
         else:
            if pos == 1:
                self.removeAtFirst()
            elif pos == -1:
                self.removeAtEnd()
            else:
                temp = self.head
                temp1 = self.head.next
                for i in range(1,pos-1):
                    temp = temp.next
                    temp1 = temp1.next
                temp.next = temp1.next
                if temp1.next == self.end:
                    self.end = temp
                temp1 = None
        
        
        
            

    def display(self):
        if self.head is None:
            print("Circular linked list does not exist")
        else:
            temp = self.head
            print(temp.data,end = "-->")
            while temp.next != self.head:
                temp = temp.next
                print(temp.data,end = "-->")
            print(temp.next.data,end = "-->")
                    

l = CLL()
n1 = Node(10)
l.head = n1
l.end = n1
l.end.next = n1

n2 = Node(20)
l.end.next = n2
l.end = n2
l.end.next = l.head

n3 = Node(30)
l.end.next = n3
l.end = n3
l.end.next = l.head

n4 = Node(40)
l.end.next = n4
l.end = n4
l.end.next = l.head



#l.atFirst(5)
#l.atFirst(2)
#l.atLast(40)
#l.atLast(50)
#l.atPosition(50,-1)
#l.removeAtFirst()
#l.removeAtFirst()
#l.removeAtFirst()
#l.removeAtFirst()
#l.removeAtFirst()
#l.removeAtEnd()
#l.removeAtEnd()
#l.removeAtEnd()
#l.removeAtEnd()
#l.removeAtPosition(1)
l.removeAtPosition(3)
l.display()
