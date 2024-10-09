#single linked list:

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#creating object of Node.
Node1 = Node(10)
Node2 = Node(20)
Node3 = Node(30)
Node4 = Node(40)
Node5 = Node(50)

#linking of the Node.
Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node5

#adding a new node in begging.
new_Node6 = Node(60)
new_Node6.next = Node1
Pointer = new_Node6

#adding a new node in last.
new_Node7 = Node(70)
Node5.next = new_Node7

"""#adding a new node in the mid of linked list
new_Node8 = Node(80)

Node1.next = Node2
Node2.next = new_Node8
new_Node8.next = Node2 
Node3.next = Node4
Node4.next = Node5"""

#creating a pointer
#Pointer = Node1


#display linked list
while Pointer is not None:
    print(Pointer.data ,end = '->')
    Pointer = Pointer.next 
print("none")





