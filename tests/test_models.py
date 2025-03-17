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
        assert isinstance(product, str)


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


def test_product_price_getter_setter() -> None:

    product = Product("Тестовый продукт", "Описание", 100, 10)

    assert product.price == 100

    product.price = 150
    assert product.price == 150

    product.price = -50
    assert product.price == 150


def test_category_add_product_and_products_getter() -> None:
    p1 = Product("Молоко", "1 литр", 80, 10)
    p2 = Product("Хлеб", "Булка", 40, 20)

    category = Category("Продукты", "Еда", [p1])

    category.add_product(p2)

    products_output = category.products

    assert "Молоко, 80 руб. Остаток: 10 шт." in products_output
    assert "Хлеб, 40 руб. Остаток: 20 шт." in products_output


def test_category_class_variables() -> None:

    initial_categories = Category.total_categories
    initial_products = Category.total_products

    p1 = Product("Товар1", "Описание", 100, 5)
    p2 = Product("Товар2", "Описание", 150, 8)

    Category("Категория1", "Описание", [p1])
    Category("Категория2", "Описание", [p2])

    assert Category.total_categories == initial_categories + 2

    assert Category.total_products >= initial_products + 2


def test_product_str() -> None:
    product = Product("Молоко", "1 литр", 80, 15)
    expected_output = "Молоко, 80 руб. Остаток: 15 шт."
    assert str(product) == expected_output


def test_category_str() -> None:
    p1 = Product("Молоко", "1 литр", 80, 15)
    p2 = Product("Хлеб", "Булка", 40, 20)

    category = Category("Продукты", "Еда", [p1, p2])

    expected_output = "Продукты, количество продуктов: 35 шт."
    assert str(category) == expected_output


def test_category_products_property() -> None:
    p1 = Product("Молоко", "1 литр", 80, 15)
    p2 = Product("Хлеб", "Булка", 40, 20)

    category = Category("Продукты", "Еда", [p1, p2])

    products_output = category.products

    assert products_output == ["Молоко, 80 руб. Остаток: 15 шт.", "Хлеб, 40 руб. Остаток: 20 шт."]


def test_product_add() -> None:
    p1 = Product("Молоко", "1 литр", 80, 10)
    p2 = Product("Хлеб", "Булка", 40, 5)

    assert p1 + p2 == 1000


def test_product_add_with_invalid_type() -> None:
    p1 = Product("Молоко", "1 литр", 80, 10)

    try:
        _ = p1 + 5
    except TypeError as e:
        assert str(e) == "Складывать можно только с другим продуктом"
    else:
        assert False, "TypeError не был вызван"
