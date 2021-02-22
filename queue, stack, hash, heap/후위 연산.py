temp = input()
stack = []
for x in temp:
    if x.isdecimal():
        stack.append(x)
    else:
        b = int(stack.pop())
        a = int(stack.pop())
        if x == '+':
            stack.append((a + b))
        elif x == '-':
            stack.append((a - b))
        elif x == '/':
            stack.append((a / b))
        elif x == '*':
            stack.append((a * b))
print(stack[0])