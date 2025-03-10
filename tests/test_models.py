import pytest

from src.models import Category, Product


@pytest.fixture
def sample_products() -> list[Product]:
    """Создаем список продуктов для тестов"""
    product1 = Product("Ноутбук", "Игровой ноутбук", 150000.0, 5)
    product2 = Product("Смартфон", "Флагманский смартфон", 80000.0, 10)
    return [product1, product2]


@pytest.fixture(autouse=True)
def reset_category_counts() -> None:
    """
    Сброс глобальных счетчиков перед каждым тестом.
    pytest будет автоматически применять фикстуру к каждому тесту.
    """
    Category.total_categories = 0
    Category.total_products = 0


def test_product_initialization() -> None:
    product = Product("Телевизор", "4K Smart TV", 49999.99, 7)

    assert product.name == "Телевизор"
    assert product.description == "4K Smart TV"
    assert product.price == 49999.99
    assert product.quantity == 7


def test_category_initialization(sample_products: list[Product]) -> None:
    category = Category("Электроника", "Устройства и гаджеты", sample_products)

    assert category.name == "Электроника"
    assert category.description == "Устройства и гаджеты"
    assert isinstance(category.products, list)
    assert len(category.products) == 2

    for product in category.products:
        assert isinstance(product, Product)


def test_total_categories_increases(sample_products: list[Product]) -> None:
    assert Category.total_categories == 0

    Category("Электроника", "Гаджеты", sample_products)
    assert Category.total_categories == 1

    Category("Бытовая техника", "Техника для дома", [])
    assert Category.total_categories == 2


def test_total_products_increases(sample_products: list[Product]) -> None:
    assert Category.total_products == 0

    Category("Электроника", "Гаджеты", sample_products)
    assert Category.total_products == 2

    Category("Канцелярия", "Товары для офиса", [])
    assert Category.total_products == 2

    Category("Игрушки", "Для детей", [Product("Кубики", "Деревянные кубики", 500.0, 50)])
    assert Category.total_products == 3
