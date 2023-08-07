n = int(input())
list = list(map(int, input().split()))

# s1 = list[0]

# list.sort(reverse=True)
# stronggest = list[0]

# if s1 == stronggest and s1 == list[1]:
#     print(1)
# elif s1 == stronggest:
#     print(0)
# else:
#     print(stronggest - s1 + 1)

s1 = list[0]

list.remove(list[0])
ans = 0

for i in list:
    if s1 < i:
        s1 += i - s1 + 1
        ans += i - s1 + 1
    elif s1 == i:
        s1 += 1
        ans += 1

print(ans)
