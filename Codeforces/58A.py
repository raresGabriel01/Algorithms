#https://codeforces.com/problemset/problem/58/A


def ord(ch):
    if ch == "h":
        return 0
    elif ch == "e":
        return 1
    elif ch == "l":
        return 2
    else:
        return 3


text = input()

temp = text

for ch in text:
    if ch not in "hello":
        temp = temp.replace(ch,"")



d = {

}

o = 0

for ch in temp:
    if ch in d:
        d[ch] += 1
    else:
        if ord(ch) <= o:
            d[ch] = 1
            o += 1

list = list(d.keys())
if len(list) != 4:
    print("NO")
else:
    if list[0]=="h" and list[1]=="e" and list[2]=="l" and list[3]=="o" and d["l"] >= 2 :
        print("YES")
    else:
        print("NO")


