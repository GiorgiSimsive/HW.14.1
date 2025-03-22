import pytest

from src.models import Category, LawnGrass, Product, Smartphone


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
        _ = p1 + 5  # type: ignore
    except TypeError as e:
        assert str(e) == "Складывать можно только объекты класса Product или его наследников."
    else:
        assert False, "TypeError не был вызван"


@pytest.fixture
def smartphone():  # type: ignore
    return Smartphone(
        name="iPhone 15 Pro",
        description="Новый флагман Apple",
        price=150000,
        quantity=5,
        efficiency="A17 Pro",
        model="15 Pro",
        memory=256,
        color="Space Black",
    )


@pytest.fixture
def lawn_grass():  # type: ignore
    return LawnGrass(
        name="Трава универсальная",
        description="Газон для дачи",
        price=3000,
        quantity=10,
        country="Голландия",
        germination_period=14,
        color="Зеленый",
    )


def test_smartphone_creation(smartphone):  # type: ignore
    assert smartphone.name == "iPhone 15 Pro"
    assert smartphone.description == "Новый флагман Apple"
    assert smartphone.price == 150000
    assert smartphone.quantity == 5
    assert smartphone.efficiency == "A17 Pro"
    assert smartphone.model == "15 Pro"
    assert smartphone.memory == 256
    assert smartphone.color == "Space Black"

    expected_str = (
        "iPhone 15 Pro, 150000 руб. Остаток: 5 шт. | "
        "Модель: 15 Pro, Память: 256GB, Цвет: Space Black, Производительность: A17 Pro"
    )
    assert str(smartphone) == expected_str


def test_lawn_grass_creation(lawn_grass):  # type: ignore
    assert lawn_grass.name == "Трава универсальная"
    assert lawn_grass.description == "Газон для дачи"
    assert lawn_grass.price == 3000
    assert lawn_grass.quantity == 10
    assert lawn_grass.country == "Голландия"
    assert lawn_grass.germination_period == 14
    assert lawn_grass.color == "Зеленый"

    expected_str = (
        "Трава универсальная, 3000 руб. Остаток: 10 шт. | "
        "Страна: Голландия, Период прорастания: 14 дней, Цвет: Зеленый"
    )
    assert str(lawn_grass) == expected_str


def test_product_addition(smartphone, lawn_grass):  # type: ignore
    with pytest.raises(TypeError) as excinfo:
        _ = smartphone + lawn_grass

    assert str(excinfo.value) == "Нельзя сложить Smartphone с LawnGrass"


def test_add_product_type_error(smartphone):  # type: ignore
    with pytest.raises(TypeError):
        _ = smartphone + "NotAProduct"


def test_price_setter_negative(smartphone, capsys):  # type: ignore
    smartphone.price = -500
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert smartphone.price == 150000


def test_add_different_product_types_error(smartphone, lawn_grass):  # type: ignore
    with pytest.raises(TypeError) as exc_info:
        _ = smartphone + lawn_grass

    assert "Нельзя сложить Smartphone с LawnGrass" in str(exc_info.value)


def test_add_invalid_product_type() -> None:
    category = Category("Смартфоны", "Флагманы", [])

    with pytest.raises(TypeError) as exc_info:
        category.add_product("не продукт")  # type: ignore[arg-type]

    assert "Можно добавить только объект класса Product" in str(exc_info.value)

    with pytest.raises(TypeError) as exc_info:
        category.add_product(123)  # type: ignore[arg-type]

    assert "Можно добавить только объект класса Product" in str(exc_info.value)
