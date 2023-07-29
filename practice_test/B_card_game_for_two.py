n = int(input())
card_list = list(map(int, input().split()))
total = 0

card_list.sort()

for i in range(len(card_list)):
    if i % 2 == 0:
        total += card_list[i]
    else:
        total -= card_list[i]

print(abs(total))
