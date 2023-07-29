n, Y = map(int, input().split())
combination = []


for x in range(n + 1):
    for y in range(n + 1 - x):
        z = n - x - y
        if x + y + z == n and x * 10000 + y * 5000 + z * 1000 == Y:
            print(f"{x} {y} {z}")
            exit()

print("-1 -1 -1")
