a = input("Введите набор слов, разделённых пробелом: ").split()
for n, el in enumerate(a, 1):
    print(n, el[0:10])