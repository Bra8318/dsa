#Conversion of Infix to Prefix. 
precedence = {'+':1,'-':1,'*':2,'/':2,'^':3}

def reverse(express):
    expression = express[::-1]
    expression = list(expression)
    for i in range (len(expression)):
        if expression[i] == '(':
            expression[i] = ')'
        elif expression[i] == ')':
            expression[i] = '('   
    return ''.join(expression)



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
        postfix += (stack.pop())
    return ''.join(postfix)


print("Conversion of Infix to Prefix Expression :")
express = input("Enter The Infix Expression :")
expression = reverse(express)
print("Infix Expression :",express)
print("Prefix Expression :",postfix(expression)[::-1])


#conversion of prefix to infix.
'''def infix(expression):
    stack =[]

    for char in expression[::-1]:
        if char.isalnum():
            stack.append(char)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            new = f"({operand1}{char}{operand2})"
            stack.append(new)
    return stack[0]

print("Conversion of Prefix to Infix Expression :")
expression = input("Enter The Prefix Expression :")
print("Prefix Expression :",expression)
print("Infix Expression :",infix(expression))'''


