from typing import List


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Инициализация товара.
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        """
        Геттер для приватного атрибута __price.
        """
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """
        Сеттер для приватного атрибута __price.
        """
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, data: dict):  # type: ignore
        """
        Класс-метод для создания нового продукта из словаря.
        """
        name = data.get("name")
        description = data.get("description")
        price = data.get("price")
        quantity = data.get("quantity")

        return cls(name, description, price, quantity)  # type: ignore

    def __str__(self) -> str:
        """
        Строковое отображение товара.
        """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """
        Складывает два продукта по формуле: цена * количество + цена * количество,
        но только если оба продукта одного типа.
        """
        if not isinstance(other, Product):
            raise TypeError("Складывать можно только объекты класса Product или его наследников.")

        if type(self) is not type(other):
            raise TypeError(f"Нельзя сложить {type(self).__name__} с {type(other).__name__}")

        return self.price * self.quantity + other.price * other.quantity


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: str,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        """
        Инициализация смартфона.
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self) -> str:
        """
        Строковое отображение смартфона.
        """
        base_str = super().__str__()
        return (
            f"{base_str} | Модель: {self.model}, Память: {self.memory}GB, "
            f"Цвет: {self.color}, Производительность: {self.efficiency}"
        )


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: int,
        color: str,
    ) -> None:
        """
        Инициализация газонной травы.
        """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self) -> str:
        """
        Строковое отображение газонной травы.
        """
        base_str = super().__str__()
        return (
            f"{base_str} | Страна: {self.country}, Период прорастания: {self.germination_period} "
            f"дней, Цвет: {self.color}"
        )


class Category:
    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        """
        Инициализация категории.
        """
        self.name = name
        self.description = description
        self.__products = products

        Category.total_categories += 1
        Category.total_products += len(products)

    def add_product(self, product: Product) -> None:
        """
        Добавляет товар в приватный список товаров.
        Принимает только объекты класса Product и его наследников.
        """
        if not isinstance(product, Product):
            raise TypeError("Можно добавить только объект класса Product или его наследников.")

        self.__products.append(product)
        Category.total_products += 1

    @property
    def products(self) -> List[str]:
        """
        Геттер для получения списка товаров категории в виде строк.
        """
        return [str(product) for product in self.__products]

    def __str__(self) -> str:
        """
        Строковое отображение категории.
        """
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
