N, P, Q = map(int, input().split())
list_D = list(map(int, input().split()))

for i in range(N):
    if P > Q + list_D[i]:
        P = Q + list_D[i]

print(P)
