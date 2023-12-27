class Category:
    total_category = 0
    total_products = 0

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.products = []
        Category.total_category += 1


class Product:
    def __init__(self, name: str, description: str, price: int | float, quantity_in_stock: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock
        Category.total_products += 1
