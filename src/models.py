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
    def products(self) -> List[Product]:
        """
        Геттер для получения списка товаров категории как объектов Product.
        """
        return self.__products

    def products_info(self) -> List[str]:
        """
        Возвращает список товаров категории в формате строк.
        """
        result = []
        for product in self.__products:
            product_str = f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            result.append(product_str)
        return result
