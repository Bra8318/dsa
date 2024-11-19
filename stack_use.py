'''#infix to postfix algorithym:
precedence = {'+':1,'-':1,'*':2,'/':2,'^':3}

def postfix(expression):
    stack = []
    postfix = ' '

    for char in expression:
        if char.isalnum():
            postfix += char

        elif char == '(':
            stack.append(char)

        elif char == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop() 
            stack.pop()

        else:
            while stack and precedence.get(char,0) <= precedence.get(stack[-1],0):
                postfix += stack.pop()
            stack.append(char)

#delete all the operator.
    while stack:
        postfix += stack.pop()
    return postfix


print("Conversion of Infix to Postfix Expression :")
expression = input("Enter The Infix Expression :")
print("Infix Expression :",expression)
print("Postfix Expression :",postfix(expression))'''



#Postfix To Infix Algorithyn.
def infix(expression):
    stack =[]

    for char in expression:
        if char.isalnum():
            stack.append(char)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            new = f"({operand1}{char}{operand2})"
            stack.append(new)
    return stack.pop()

print("Conversion of Postfix to Infix Expression :")
expression = input("Enter The Postfix Expression :")
print("Postfix Expression :",expression)
print("Infix Expression :",infix(expression))
            


