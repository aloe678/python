# a
from itertools import count
from itertools import cycle

a = int(input("Число начальное: "))
b = int(input("Число конечное: "))
my_list = []
for el in count(a):
    if el > b:
        break
    else:
        my_list.append(el)


print(my_list)

# b
new_list = []
i = 0
for el in cycle(my_list):
    if i > 20:
        break
    else:
        new_list.append(el)
        i += 1
print(new_list)
