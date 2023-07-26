n = int(input())
S = input()

a = False
b = False
c = False

ans = 0

while a != True or b != True or c != True:
    s = S[ans]

    if s == "A":
        a = True
    if s == "B":
        b = True
    if s == "C":
        c = True

    ans += 1

print(ans)
