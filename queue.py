queue = []
def enqueue():
    item = eval(input("Enter a item name :"))
    queue.append(item)

def dequeue():
    delete = queue.pop(0)
    print("deleted item is :",delete)

def display():
    if len(queue) == 0:
        print("Queue is not exist:")
    else:
        #print(queue)
        print("Queue is : ",end = "[")
        for items in queue:
            print(items,end=",")
        print(end="]")



        
while True:
    print("\n Enter Your Option:\n 1.Enqueue \n 2.Dequeue \n 3.Display")
    option = input("Enter Your Option:")
    if option == '1':
        print("Enqueue is selected:")
        enqueue()
    elif option == '2':
        print("Dequeue is selected:")
        dequeue()
    elif option == '3':
        print("Display is selected:")
        display()
        
    else:
        break

