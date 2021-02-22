word = input()
worddic = {}
for w in word:
    worddic[w] = worddic.get(w, 0) + 1

comp = input()
for c in comp:
    worddic[c] = worddic.get(c, 0) - 1

for x in worddic:
    if worddic[x] != 0:
        print("NO")
        break
else:
    print("YES")