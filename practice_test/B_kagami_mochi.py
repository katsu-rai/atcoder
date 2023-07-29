n = int(input())
mochi_list = []
count = 0

for _ in range(n):
    tmp = int(input())
    mochi_list.append(tmp)

mochi_list.sort()

for i in range(len(mochi_list))[::-1]:
    while i > -1:
        if mochi_list[i] > mochi_list[i - 1]:
            count += 1

print(count)
