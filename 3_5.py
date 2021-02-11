
def my_func():
    s = 0
    while True:
        a = list(input("Введите числа, разделённые пробелом. Введите 'exit' для выхода: ").split())
        for n in a:
            if n == "exit":
                break
            try:
                n = float(n)
                s = s + n
            except ValueError:
                pass
        else:
            print(s)
            continue
        break
    return s


print(my_func())
