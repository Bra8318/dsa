class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self):
        data = int(input("Enter the data: "))
        new = Node(data)
        if self.front is None:
            self.front = new
            self.rear = new
        else:
            self.rear.next = new
            self.rear = new

    def dequeue(self):
        if self.front is None:
            print("Queue is empty. ")
        elif self.front == self.rear:
            front = None
        else:
            temp = self.front
            front = temp.next
            temp = None

    def display(self):
        if self.front is None:
            print("Queue is empty. ")
        else:
            temp = self.front
            while temp is not None:
                print(temp.data,end = ",")
                temp = temp.next

q = Queue()
while True:
    print("\n Enter the Queue's operations : \n 1.Enqueue \n 2.Dequeue \n 3.Display")
    option = int(input("Enter the operations: "))
    if option == 1:
        print("Enqueue is selected")
        q.enqueue()
    elif option == 2:
        print("Dequeue is selected")
        q.dequeue()
    elif option == 3:
        print("Display is selected")
        q.display()
    else:
        break



            
