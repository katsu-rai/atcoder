n, m = map(int, input().split())
sellers = []
buyers = []
x = 10000000000


sellers = list(map(int, input().split()))
buyers = list(map(int, input().split()))

for i in sellers:
    for j in buyers:
        if j >= i:
            x = max(x, i)
