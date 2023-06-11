import os.path
import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            print('Длина наименования товара превышает 10 символов.')

    @classmethod
    def instantiate_from_csv(cls):
        """
        класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv_
        """
        with open(os.path.join(os.path.dirname(__file__), 'items.csv'), newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for i in reader:
                name, price, quantity = i['name'], float(i['price']), int(i['quantity'])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(num):
        """
        статический метод, возвращающий число из числа-строки
        """
        number = int(float(num))
        return number
