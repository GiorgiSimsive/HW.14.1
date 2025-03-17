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

    def __add__(self, other):  # type: ignore
        """
        Складывает два продукта по формуле: цена * количество + цена * количество.
        """
        if not isinstance(other, Product):
            raise TypeError("Складывать можно только с другим продуктом")
        return self.price * self.quantity + other.price * other.quantity


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
        """
        if isinstance(product, Product):
            self.__products.append(product)
            Category.total_products += 1
        else:
            raise TypeError("Можно добавить только объект класса Product.")

    @property
    def products(self) -> List[str]:
        """
        Геттер для получения списка товаров категории в виде строк.
        """
        return [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products]

    def __str__(self) -> str:
        """
        Строковое отображение категории.
        """
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
