from src.items import Category, Product, ProductsFromCategory, LawnGrass, SmartPhone


def main():
    # Объявление объектов класса Category
    cat_1 = Category("Самокаты", "средство передвижения")
    cat_2 = Category("Автомобили", "механическое транспортное средство")

    # Объявление объектов класса Product
    prod_1 = Product("Runner3000", "самокат", 5000, 8)
    prod_2 = Product("Lada Vesta", "автомобиль", 100000, 3)
    prod_3 = Product("KIA Rio", "автомобиль", 150000, 5)

    # Объявление объектов класса LawnGrass
    grass_1 = LawnGrass("Зеленая трава", "газонная трава", 1200, 3,
                        "Россия", "30 дней", "зеленый")

    # Объявление объектов класса SmartPhone
    phone_1 = SmartPhone("Xiaomi Mi 12 T", "смартфон", 4000, 6,
                         "супер мощный", "Mi12T", "8Gb", "black")

    # Вызов __repr__ у созданных объектов через миксин
    print(repr(prod_3))
    print(repr(grass_1))
    print(repr(phone_1))
    print(f"-" * 40)

    # Добавление продукта в список категории
    cat_1.add_products = prod_1
    cat_2.add_products = prod_2
    cat_2.add_products = prod_3
    cat_2.add_products = phone_1
    cat_1.add_products = [1, 2, 3]  # будет ошибка добавления
    print(f"-" * 40)

    # Вывод общего количества категорий и продуктов
    print(Category.total_category)
    print(Category.total_products)
    print(f"-" * 40)

    # Вывод товаров в выбранной категории
    for x in cat_2.add_products:
        print(x)
    print(f"-" * 40)

    # Вывод общего количества товаров в выбранной категории
    print(cat_1)
    print(cat_2)
    print(f"-" * 40)

    # Уменьшение цены на товар
    print(prod_1.price)
    prod_1.price = 4000
    print(prod_1.price)
    print(f"-" * 40)

    # Увеличение цены на товар
    print(prod_3.price)
    prod_3.price = 180000
    print(prod_3.price)
    print(f"-" * 40)

    # Вывод товаров в категории через новый класс
    items = ProductsFromCategory(cat_2)
    for item in items:
        print(item)
    print(f"-" * 40)

    # Получение суммы общего числа двух выбранных продуктов
    print(prod_2 + prod_3)
    print(f"-" * 40)

    # Вывод экземпляров новых классов LawnGrass и SmartPhone
    print(grass_1)
    print(phone_1)
    print(f"-" * 40)

    # Проверка сложения товаров из разных классов
    print(prod_2 + grass_1)
    print(phone_1 + grass_1)
    print(prod_1 + phone_1)
    print(f"-" * 40)


if __name__ == "__main__":
    main()
