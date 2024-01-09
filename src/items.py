from typing import Any


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
    def products_list(self) -> list:
        prod_list = []
        for product in self.__products:
            if product:
                prod_list.append(f"{product.name_prod}, {product.price} руб. Остаток: {product.quantity_in_stock}")
        return prod_list

    @products_list.setter
    def products_list(self, product):
        self.__products.append(product)


class Product:
    """
    Класс, представляющий продукты.
    """
    def __init__(self, name_prod: str, description_prod: str, price: int | float, quantity_in_stock: int):
        self.name_prod = name_prod
        self.description_prod = description_prod
        self.__price = price
        self.quantity_in_stock = quantity_in_stock
        Category.total_products += 1

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
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
        return Product(name_prod, description_prod, price, quantity_in_stock)
