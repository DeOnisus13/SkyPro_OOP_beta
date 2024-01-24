from typing import Any
from abc import ABC, abstractmethod


class AbstractProduct(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __str__(self):
        pass


class ReportMixin:
    def __repr__(self, *args, **kwargs):
        return f"Создан объект {self.__class__.__name__} - {self.__dict__}"


class Category:
    """
    Класс, представляющий категорию продуктов.
    """
    total_category = 0
    total_products = 0

    def __init__(self, name_cat: str, description_cat: str, product: Any = None):
        self.name_cat = name_cat
        self.description_cat = description_cat
        self.__products = []
        self.__products.append(product)
        Category.total_category += 1

    @property
    def add_products(self) -> list:
        """
        Метод вывода товаров по шаблону.
        """
        prod_list = []
        for product in self.__products:
            if product:
                prod_list.append(f"{product.name_prod}, {product.price} руб. Остаток: {product.quantity_in_stock}")
        return prod_list

    @add_products.setter
    def add_products(self, product):
        """
        Сеттер для добавления продуктов в список.
        """
        if isinstance(product, Product):
            self.__products.append(product)
        else:
            print("Ошибка добавления")

    def __str__(self):
        """
        Строковый вывод количества продуктов в категории.
        """
        return f"{self.name_cat}, количество продуктов: {self.__len__()} шт."

    def __len__(self):
        """
        Вывод количества продуктов на складе из категории.
        """
        sum_quantity_in_stock = 0
        for product in self.__products:
            if product:
                sum_quantity_in_stock += product.quantity_in_stock
        return sum_quantity_in_stock


class Product(AbstractProduct, ReportMixin):
    """
    Класс, представляющий продукты.
    """

    def __init__(self, name_prod: str, description_prod: str, price: int | float, quantity_in_stock: int):
        self.name_prod = name_prod
        self.description_prod = description_prod
        self.__price = price
        self.quantity_in_stock = quantity_in_stock
        Category.total_products += 1
        # super().__repr__(self)

    @property
    def price(self):
        """
        Геттер для параметра цены.
        """
        return self.__price

    @price.setter
    def price(self, new_price):
        """
        Сеттер для изменения цены на товар.
        """
        if new_price < self.__price:
            confirm = input(f"На товар {self.name_prod} цена будет снижена. Вы уверены?\n(y/n): ")
            if confirm.lower() == "y":
                self.__price = new_price
                print(f"Цена на товар {self.name_prod} снижена")
            else:
                print("Действие отменено")
        else:
            self.__price = new_price
            print(f"На товар {self.name_prod} цена успешно обновлена")

    @staticmethod
    def add_product(name_prod: str, description_prod: str, price: int | float, quantity_in_stock: int):
        """
        Метод для добавления нового товара.
        """
        return Product(name_prod, description_prod, price, quantity_in_stock)

    def __str__(self):
        """
        Строковое отображение для количества продукта.
        """
        return f"{self.name_prod}, {self.__price} руб. Остаток: {self.quantity_in_stock} шт."

    def __add__(self, other):
        """
        Метод для сложения объектов между собой.
        """
        if type(self) is type(other):
            return self.__price * self.quantity_in_stock + other.__price * other.quantity_in_stock
        else:
            return "Товары из разных классов нельзя складывать"


class ProductsFromCategory:
    """
    Класс, принимающий на вход категорию и дающий возможность использовать цикл for для
    прохода по всем товарам данной категории.
    """

    def __init__(self, category: Category):
        self.category = category

    def __iter__(self):
        return iter(self.category.add_products)


class LawnGrass(Product):
    """
    Класс для товара - газонная трава
    """

    def __init__(self, name_prod: str, description_prod: str, price: int | float, quantity_in_stock: int,
                 country_origin: str, germination_period: str, color: str):
        super().__init__(name_prod, description_prod, price, quantity_in_stock)
        self.country_origin = country_origin
        self.germination_period = germination_period
        self.color = color
        # super().__repr__(self)


class SmartPhone(Product):
    """
    Класс для товара - смартфон
    """
    def __init__(self, name_prod: str, description_prod: str, price: int | float, quantity_in_stock: int,
                 performance: str, model: str, memory: str, color: str):
        super().__init__(name_prod, description_prod, price, quantity_in_stock)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color
        # super().__repr__(self)
