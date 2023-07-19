n, k = map(int, input().split())

how_long = []
how_many = []
all = []
sum = 0


for _ in range(n):
    tmp = list(map(int, input().split()))

    how_long.append(tmp[0])
    how_many.append(tmp[1])

for i in range(n):
    all.append([how_long[i], how_many[i]])

all.sort()

for i in reversed(range(n)):
    sum += all[i][1]
    if sum > k:
        day = all[i][0]
        # why not all[i][0] + 1?
        print(day + 1)

        exit()

print(1)


# N, K= map(int, input().split())
# AB = [list(map(int, input().split())) for _ in range(N)]

# S = sorted(AB)
# sum = 0
# for i in range(N):
#     sum += S[-i-1][1]
#     if sum > K:
#         print(S[-i-1][0] + 1)

#         exit()
# print(1)
