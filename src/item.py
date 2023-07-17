import csv
import os
import math

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    initialized = False  # Add initialized class variable

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
        self.__class__.all.append(self)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        if len(new_name) > 10:
            self.__name = new_name[:10]
        else:
            self.__name = new_name

    @classmethod
    def instantiate_from_csv(cls):
        cls.all.clear()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, 'items.csv')

        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                price = float(row['price'])
                quantity = int(row['quantity'])
                item = cls(name, price, quantity)

    @staticmethod
    def string_to_number(value: str) -> float:
        """
        Преобразует строковое значение в число с плавающей точкой.

        :param value: Строковое значение.
        :return: Число с плавающей точкой.
        """
        return math.floor(float(value))


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity * self.pay_rate

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
        return self.price

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта .
        """
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта для использования str().
        """
        return self.__name
