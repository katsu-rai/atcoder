import collections

nums = list(map(int, input().split(",")))
counter = collections.Counter(nums)

max = 0
ans = 0

for i in counter:
    if max < counter[i]:
        ans = int(i)
        max = counter[i]

print(ans)
