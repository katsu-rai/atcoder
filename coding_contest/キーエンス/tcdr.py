s = list(input())
ans = ""
i = 0

while i < len(s):
    if s[i] == "a" or s[i] == "i" or s[i] == "u" or s[i] == "e" or s[i] == "o":
        s.remove(s[i])
        i -= 1

    i += 1

for i in s:
    ans = ans + i

print(ans)
