n, a, b = map(int, input().split())
tmp = 0
elements_list = []
result = 0

for i in range(1, n + 1):
    tmp = 0
    i = str(i)
    for j in i:
        j = int(j)
        tmp += j

    if tmp >= a and tmp <= b:
        i = int(i)
        elements_list.append(i)

# print(elements_list)

for i in elements_list:
    result += i

print(result)
