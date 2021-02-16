from sys import argv

my_name, hours, rate, premium = argv


def my_salary():
    s = int(hours) * int(rate) + int(premium)
    return s


print(my_salary())
