while True:
    M, F, R = map(int, input().split())
    if M == -1 and F == -1 and R == -1:
        break
    if M == -1 or F == -1:
        print("F")
    elif M + F >= 80:
        print("A")
    elif M + F >= 65:
        print("B")
    elif M + F >= 50:
        print("C")
    elif M + F >= 30:
        if R >= 50:
            print("C")
        else:
            print("D")
    else:
        print("F")
