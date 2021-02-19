with open("5_3.txt", "r", encoding="utf-8") as f:
    t = []
    n = 0
    for line in f:
        s = line.split()
        n += 1
        if float(s[1]) < 20000:
            print(s[0])
        t.append(float(s[1]))
    print(f"Средняя величина дохода сотрудников {sum(t) / n}")
