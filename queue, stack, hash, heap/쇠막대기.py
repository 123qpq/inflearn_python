getpipe = input()
answer = 0
getpipe = getpipe.replace("()", "|")
stack = 0
for pipe in getpipe:
    if pipe == "(":
        stack += 1
    elif pipe == "|":
        answer += stack
    else:
        stack -= 1
        answer += 1
print(answer)
