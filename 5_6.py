with open("5_6.txt", "r", encoding="utf-8") as f:
    for line in f:
        a = line.replace('(', ' ')
        b = a.replace(')', ' ')
        b = b.split()
        c = []
        for l in b:
            if l.isdigit():
                c.append(int(l))
            else:
                pass
        print(f"{line[0]} {sum(c)}")