import pytest

from src.items import Category, Product


@pytest.fixture
def test_data():
    cat_1 = Category("Самокаты", "средство передвижения")
    cat_2 = Category("Автомобили", "механическое транспортное средство")
    prod_1 = Product("Runner3000", "самокат", 5000, 8)
    prod_2 = Product("Lada Vesta", "автомобиль", 100000, 3)
    prod_3 = Product("KIA Rio", "самолет", 150000, 5)
    return cat_1, cat_2, prod_1, prod_2, prod_3


def test_category_init(test_data):
    assert test_data[0].name == "Самокаты"
    assert test_data[0].description == "средство передвижения"


def test_product_init(test_data):
    assert test_data[3].name == "Lada Vesta"
    assert test_data[3].description == "автомобиль"
    assert test_data[3].price == 100000
    assert test_data[3].quantity_in_stock == 3


def test_counting(test_data):
    assert Category.total_category == 2
    assert Category.total_products == 3
