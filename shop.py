# shop.py

class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = 0  # значення за замовчуванням

    def describe_shop(self):
        print(f"Назва магазину: {self.shop_name}")
        print(f"Тип магазину: {self.store_type}")

    def open_shop(self):
        print("Магазин відкритий онлайн.")

    def set_number_of_units(self, number):
        """Задати точну кількість видів товарів."""
        self.number_of_units = number

    def increment_number_of_units(self, amount):
        """Збільшити кількість товарів на певне число."""
        self.number_of_units += amount


# Клас-нащадок Discount
class Discount(Shop):
    def __init__(self, shop_name, store_type, discount_products):
        super().__init__(shop_name, store_type)
        self.discount_products = discount_products  # список товарів зі знижкою

    def get_discounts_products(self):
        print("Товари зі знижками:")
        for p in self.discount_products:
            print(f"- {p}")
