class MyError(Exception):
    def __init__(self, text):
        self.text = text


num_1 = input('Делимое: ')
num_2 = input('Делитель: ')

try:
    num_1 = int(num_1)
    num_2 = int(num_2)
    if num_2 == 0:
        raise MyError('На ноль делить нельзя')
    res = num_1 / num_2
except (ValueError, MyError) as err:
    print(err)
else:
    print(res)
finally:
    print('Конец')
