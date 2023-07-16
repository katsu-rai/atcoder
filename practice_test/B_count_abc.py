n = int(input())
s = input()
count = 0

for i in range(n - 2):
    condition_a = s[i] == "A"
    condition_b = s[i + 1] == "B"
    condition_c = s[i + 2] == "C"

    if condition_a and condition_b and condition_c:
        count += 1

print(count)
