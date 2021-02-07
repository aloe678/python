n = int(input("Количество элементов в списке: "))
my_list = []
while len(my_list) < n:
    my_list.append(input("Элемент списка: "))
i = 0
while i < n / 2:
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    i = i + 2
print(my_list)