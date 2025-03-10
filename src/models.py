from typing import List


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация товара.
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str, products: List[Product]):
        """
        Инициализация категории.
        """
        self.name = name
        self.description = description
        self.products = products

        Category.total_categories += 1

        Category.total_products += len(products)
