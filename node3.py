class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

#doubly circular linked list.
class CLL:
    def __init__(self):
        self.head = None
        self.tail = None


     

    def display(self):
        if self.head is None:
            print("Cicrular linked is not exist")
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
l.tail = n1

          
l.display()
