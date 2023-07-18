n, k = map(int, input().split())

how_long = []
how_many = []
all = []
range_total_medicine = 100000000000000000000000


for _ in range(n):
    tmp = list(map(int, input().split()))

    how_long.append(tmp[0])
    how_many.append(tmp[1])

for i in range(n):
    all.append([how_long[i], how_many[i]])

all.sort()

all_copy = all

all_range = all.index(all[n // 2])

while range_total_medicine > k:
    range_total_medicine = 0
    for i in range(all_range):
        range_total_medicine += i[1]

    if range_total_medicine > k:
        all_range


print(all)


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
