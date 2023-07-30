n, d = map(int, input().split())
S_list = [[0] * 5 for _ in range(n)]
flag = False
ans = 0

for i in range(n):
    S_list[i] = input()


for j in range(n):
    i = 0
    while True:
        if S_list[i][j] == "x":
            break
        i += 1
        if i >= n:
            ans += 1
            break

        # print(S_list[i][j])
        # j += 1
        # if j >= d:
        #     break

print(ans)
