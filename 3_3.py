def my_func(a_1, a_2, a_3):
    """Возвращает сумму наибольших значений"""
    try:
        a = [float(a_1), float(a_2), float(a_3)]
        n = min(a)
        a.remove(n)
        return sum(a)
    except ValueError:
        return "Введённое значение не подходит"


print(my_func(input("Первое число: "), input("Второе число: "), input("Третье число: ")))
