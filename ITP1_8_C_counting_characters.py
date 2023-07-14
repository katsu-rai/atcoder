characters = list(map(chr, range(97, 123)))

count_char_dict = dict(zip(characters, [0] * len(characters)))

while True:
    try:
        string = input().lower()
    except:
        break
    for char in string:
        if char in characters:
            count_char_dict[char] += 1

for i in characters:
    print(f"{i} : {count_char_dict[i]}")
