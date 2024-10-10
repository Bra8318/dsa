# Stack using linked list.
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        
# push operation is used to insert at top 
    def push(self):
        value = eval(input("enter a value: "))
        new  = Node(value)
        if self.top is None:
            self.top = new
            self.top.next = None
        else:
            new.next = self.top
            self.top = new
# pop operation is used to delete at top 
    def pop(self):
        if self.top is None:
            print("Stack is Empty : ")
        elif self.top.next is None:
            print("the removed element is",self.top.data)
            self.top = None
        else:
            temp = self.top
            print("the removed element is",temp.data)
            self.top = temp.next
            temp = None
            
    def display(self):
        if self.top is None:
            print("Stack is Empty : ")
        else:
            temp = self.top
            while temp is not None:
                print(temp.data)
                temp = temp.next


s = Stack()
while(True):
    print("\n Stack operations are: \n 1.Push Operation \n 2.Pop Operation \n 3.Display")
    option = int(input("Enter a option: "))
    if option == 1:
        print("Push Operation is Selected")
        s.push()
    elif option == 2:
        print("Pop Operation is Selected")
        s.pop()
    elif option == 3:
        print("Display Operation is Selected")
        s.display()
    else:
        print("You are Exited")
        break
                 
'''s.push(10)
s.push(20)
s.push(30)    
s.push(40)

s.pop()
s.pop()
s.pop()
s.pop()

s.display()'''
            

        

            

        

            

        
