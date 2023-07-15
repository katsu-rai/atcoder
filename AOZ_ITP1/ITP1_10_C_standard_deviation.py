import math

while True:
    n = int(input())

    if n == 0:
        break

    list_s = list(map(int, input().split()))
    m = 0
    result = 0

    for i in range(n):
        m += list_s[i]
    m = m / n

    for i in range(n):
        result += (list_s[i] - m) * (list_s[i] - m)
    result = math.sqrt(result / n)

    print(result)
