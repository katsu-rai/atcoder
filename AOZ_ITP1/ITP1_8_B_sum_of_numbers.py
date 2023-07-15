answer = 0
while True:
    tmp = input()
    if tmp == "0":
        break

    for i in tmp:
        i = int(i)
        answer += i

    print(answer)
    answer = 0
