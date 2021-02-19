with open("5_2.txt", "r", encoding="utf-8") as f:
    n = 0
    for line in f:
        s = line.split()
        n += 1
        print(f"{n} строка - количество слов {len(s)}")
    print(f"Количество строк: {n}")
