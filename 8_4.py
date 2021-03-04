class OfficeEquip:
    my_warehouse = []
    i = 1

    def __init__(self, name, color, price, quantity):
        self.name = name
        self.color = color
        self.price = price
        self.quantity = quantity

    @staticmethod
    def my_args():
        while True:
            name = input('Название: ')
            color = input('Цвет: ')
            price = input('Цена: ')
            if price.isdigit():
                pass
            else:
                print('Необходимо указывать цену числом')
                continue
            quantity = input('Количество: ')
            if quantity.isdigit():
                pass
            else:
                print('Необходимо указывать количество числом')
                continue
            return name, color, price, quantity

    def put_in(self):
        b = (self.i, dict(название=self.name, цвет=self.color, цена=self.price, количество=self.quantity))
        self.my_warehouse.append(b)
        OfficeEquip.i += 1
        return self.my_warehouse


class Printer(OfficeEquip):
    printing = True
    scanning = False


class Scanner(OfficeEquip):
    printing = False
    scanning = True


class MFD(OfficeEquip):
    printing = True
    scanning = True


printer = Printer(*OfficeEquip.my_args())
scanner = Scanner(*OfficeEquip.my_args())
mfd = MFD(*OfficeEquip.my_args())

printer.put_in()
scanner.put_in()
mfd.put_in()

print(OfficeEquip.my_warehouse)
Options.check_function()

