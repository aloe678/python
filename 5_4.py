my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("5_4.txt", "r", encoding="utf-8") as f, open("5_4_2.txt", "w", encoding="utf-8") as f_2:
    for line in f:
        a = line.split()
        print(line.replace(a[0], my_dict.get(a[0])), end='', file=f_2)
