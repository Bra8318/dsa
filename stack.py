# Stack using list.
stack = []
# push operation is used to insert at top
def push():
    value = eval(input("enter a value: "))
    if len(stack) == 0:
        stack.append(value)
    else:
        stack.insert(0,value)

# pop operation is used to delete at top
def pop():
    if len(stack) == 0:
        print("Stack is Empty ")
    else:
        print("the removed element is",stack[0])
        del stack[0]

def display():
    if len(stack) == 0:
        print("Stack is Empty ")
    else:
        for i in stack:
            print(i)
        print()
    





while(True):
    print("\n Stack operations are: \n 1.Push Operation \n 2.Pop Operation \n 3.Display")
    option = int(input("Enter a option: "))
    if option == 1:
        print("Push Operation is Selected")
        push()
    elif option == 2:
        print("Pop Operation is Selected")
        pop()
    elif option == 3:
        print("Display Operation is Selected")
        display()
    else:
        print("You are Exited")
        break
