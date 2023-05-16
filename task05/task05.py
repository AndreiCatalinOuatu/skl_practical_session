f = open("input.txt", "r")
txt = f.readline()
f.close()
dic = {}
no_of_chars = 0

for ch in txt:
    if ch.isalpha():
        no_of_chars += 1
        if ch in dic.keys():
            dic[ch] += 1
        else:
            dic[ch] = 1

print(no_of_chars)
print(dic)

for key in dic.keys():
    dic[key] = dic[key] / no_of_chars

print(dic)
print(sum(dic.values()))