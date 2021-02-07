my_list = [6, 5, 5, 4, 1]
n = 0
print("Для завершения программы введите символ '-' ")
while n != "-" :
    n = input("Натуральное число: ")
    if n.isdigit():
        n = int(n)
        for t in my_list:
            if t == n:
                i = my_list.index(n)
                p = my_list.count(n)
                my_list.insert(i + p, n)
                print(my_list)
                break
            elif t < n:
                my_list.insert(my_list.index(t), n)
                print(my_list)
                break
    elif n == "-":
        break
    else:
        print("Это значение не подходит")
        continue