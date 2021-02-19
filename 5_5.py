with open("5_5.txt", "w+", encoding="utf-8") as f:
    f.write(input("Числа, разделённые пробелом: "))
    f.seek(0)
    s = []
    for line in f:
        a = line.split()
        for n in a:
            if n.isdigit():
                s.append(float(n))
            else:
                pass
    print(f"Сумма чисел: {sum(s)}")
