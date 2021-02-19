import json

with open("5_7.txt", "r", encoding="utf-8") as f:
    d = {}
    x = {}
    v = []
    g = []
    for line in f:
        a = line.split()
        n = a[0]
        p = int(a[2]) - int(a[3])
        if p > 0:
            v.append(p)
        d[n] = p
    x["average_profit"] = sum(v) / len(v)
    g.append(d)
    g.append(x)


with open("5_7.json", "w", encoding="utf-8") as j_f:
    json.dump(g, j_f, ensure_ascii=False)