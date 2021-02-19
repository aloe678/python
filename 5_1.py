
while True:
    with open("5_1.txt", "a", encoding="utf-8") as f:
        s = (input("Строка: ") + "\n")
        f.write(s)
        if s == "\n":
            break
