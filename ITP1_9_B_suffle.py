decks = []

while True:
    tmp = input()
    try:
        tmp = int(tmp)
        deck.append(deck.pop(deck[: tmp - 1]))
    except:
        if tmp == "-":
            break
        deck = tmp
        decks.append[deck]

# while True:
#     s = input()
#     if s == "-":
#         break
#     m = int(input())
#     for i in range(m):
#         h = int(input())
#         le = s[0:h]
#         ri = s[h:]
#         s = ri + le
#     print(s)
