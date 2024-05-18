s = input("")

stack = []
for char in s:
    if char == '<':
        if stack:
            stack.pop()
    elif char == '-':
        continue
    else:
        stack.append(char)
print(''.join(stack))
