keyword = input().upper()
answer = 0
list_of_words = []

while True:
    tmp_line = input().upper().split(" ")
    if tmp_line[0] == "END_OF_TEXT":
        break

    list_of_words += tmp_line

for word in list_of_words:
    if word == keyword:
        answer += 1

print(answer)

# W=input().lower()
# ans=0
# while True:
#     T=input()
#     if T=="END_OF_TEXT":break
#     T=T.lower()
#     t=T.split()
#     for ti in t:
#         if ti==W:ans+=1
# print(ans)
