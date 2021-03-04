class MyError(Exception):
    def __init__(self, text):
        self.text = text


my_list = []
while True:
    my_1 = input('Введите число. Чтобы выйти, введите "Stop": ')
    try:
        if my_1.isdigit():
            my_list.append(my_1)
        elif my_1.lower() == 'stop':
            print(my_list)
            break
        else:
            raise MyError('Это не число')
    except MyError as err:
        print(err)
