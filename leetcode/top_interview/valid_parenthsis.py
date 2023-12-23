s = input()
stack = []

dict = {")": "(", "]": "[", "}": "{"}

for i in s:
    if i == "(" or i == "{" or i == "[":
        stack.append(i)

    elif i == ")" or i == "}" or i == "]":
        if dict[i] not in stack:
            return False

return True
