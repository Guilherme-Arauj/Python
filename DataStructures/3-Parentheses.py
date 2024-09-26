class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

def check_parentheses(expression):
    stack = Stack()
    for char in expression:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.is_empty() or stack.pop() != '(':
                return "Error"
    return "OK" if stack.is_empty() else "Error"

expression = input("Enter an expression: ")
result = check_parentheses(expression)
print(result)
