"""
Infix to Prefix
using stack

Steps:
1. Reverse expression and then inverse the parentheses
2. Scan
3. Reverse expression

"""
## Stack class
class Stack:
    def __init__(self):
        self.elements = []
        self.top = None
    
    def isEmpty(self):
        if (self.top == None):
            return 1
        else:
            return 0

    def push(self, data):
        self.elements.append(data)
        self.top = data

    def pop(self):
        if (self.isEmpty()):
            return -1
        else:
            top_index = len(self.elements) - 1
            if (top_index == 0):
                self.top = None
            else:
                self.top = self.elements[top_index - 1]
            del top_index
            return self.elements.pop()
    
    def peek(self):
        if (self.isEmpty()):
            return -1
        else:
            return self.top

    def display(self):
        length = len(self.elements)
        print('\n---\nStack\n---')
        while (length != 0):
            print(self.elements[length - 1])
            length = length - 1
        print('---')

## Function to reverse expression and inverse the parentheses
def reverse(exp):
    exp = exp[::-1]
    new_exp = ''
    i = 0

    # Reverse the parentheses
    while (i != len(exp)):
        if (exp[i] == '('):
            new_exp += ')'
        elif (exp[i] == ')'):
            new_exp += '('
        else:
            new_exp += exp[i]
        i += 1
    return new_exp

## Function to check if a character is an operand
def isOperand(char):
    asci = ord(char)
    if ((asci >= 65 and asci <= 90) or (asci >= 97 and asci <= 122)):
        return 1
    return 0

## Function to check operator degree
def operand(char):
    if (char == '-' or char == '+'):
        return 1
    elif (char == '*' or char == '/'):
        return 2
    elif (char == '^'):
        return 3
    elif (char == '(' or char == ')'):
        return 100
    else:
        return -1
    
## Function to scan expression and convert it to reversed prefix
def scan(exp):
    new_exp = ''

    # Scan the expression
    stack = Stack()
    for char in exp:

        # If the char is an operand, append it to the string
        if (isOperand(char)):
            new_exp += char

        # Char is operator
        else:

            # If the stack is empty, push char to the stack
            if (stack.isEmpty()):
                stack.push(char)
            else:       

                # Check if the char is closing parentheses
                if (char == ')'):
                    while (stack.peek() != '('):
                        new_exp += stack.pop()
                    stack.pop()

                # Check whether the top of stack is parentheses or not
                elif (stack.peek() == '('):
                    stack.push(char)

                # Top of stack is operator
                else:

                    # If char has higher or same degree
                    # than the top of stack
                    if (operand(char) >= operand(stack.peek())):
                        stack.push(char)
                    
                    # If char has lower degree than the
                    # top of stack
                    else:
                        new_exp += stack.pop()
                        stack.push(char)

    # Pop all the remaining items in stack                    
    while (stack.isEmpty() == 0):
        new_exp += stack.pop()
    return new_exp

## Function to convert infix to prefix
def convert(exp):
    exp = reverse(exp)
    exp = scan(exp)
    exp = reverse(exp)
    return exp

"""
MAIN FUNCTION
"""
def main():
    expression = "(A-B/C)*(A/K-L)"

    print(convert(expression))

main()
