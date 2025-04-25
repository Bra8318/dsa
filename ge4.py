class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if (len(self.stack) == 0):
            print("stack is empty")

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    def peek(self):
        print(self.stack[-1])

    def size(self):
        print(len(self.stack))

    def display(self):
        print(self.stack)

    #op = operand.and s = symbol
    def postfix(self,exp):
        for s in exp.split():
            if s.isdigit():
                self.push(int(s))
            else:
                op2 = self.pop()
                op1 = self.pop()
                if s == '+':
                    self.push(op1 + op2)
                elif s == '-':
                    self.push(op1-op2)
                elif s == '*':
                    self.push(op1*op2)
                elif s == '/':
                    self.push(op1/op2)
                elif s == '^':
                    self.push(op1**op2)
        return self.pop()

    def prefix(self,exp):
        expression = exp[::-1]
        for s in expression.split():
            if s.isdigit():
                self.push(int(s))
            else:
                op2 = self.pop()
                op1 = self.pop()
                if s == '+':
                    self.push(op2+op1)
                elif s == '-':
                    self.push(op2-op1)
                elif s == '*':
                    self.push(op2*op1)
                elif s == '/':
                    self.push(op2/op1)
                elif s == '^':
                    self.push(op2**op1)
        return self.pop()
                    
         
    
#s = Stack()
#s.push(10)
#s.push(20)
#s.push(30)
#s.push(40)
#s.pop()
#s.peek()
#s.size()
#s.display()



Stack = Stack()
result = input("Enter your expression type \n 1.postfix \n 2. prefix \n")
exp = input("enter your expression ")

if result == 'postfix':
    print(Stack.postfix(exp))
elif result == 'prefix':
    print(Stack.prefix(exp))
else:
    print("None")

