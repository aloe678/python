from random import randint

my_list = []
i = 0
while i < 10:
    my_list.append(randint(0, 1000))
    i += 1


print(my_list)

new_list = [my_list[i] for i, j in enumerate(my_list) if my_list[i] > my_list[i-1]]
print(new_list)
