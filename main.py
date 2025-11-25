# main.py

from shop import Shop, Discount

# --- Частина 1: один екземпляр store ---
store = Shop("TechZone", "Електроніка")

# Вивід атрибутів окремо
print(store.shop_name)
print(store.store_type)

# Виклик методів
store.describe_shop()
store.open_shop()

# --- Частина 2: три різних магазини ---
store1 = Shop("MegaBooks", "Книги")
store2 = Shop("FashionUA", "Одяг")
store3 = Shop("FreshMarket", "Продукти")

store1.describe_shop()
store2.describe_shop()
store3.describe_shop()

# --- Частина 3: number_of_units ---
print("Початкова кількість товарів:", store.number_of_units)

store.number_of_units = 15
print("Після зміни вручну:", store.number_of_units)

store.set_number_of_units(25)
print("Після set_number_of_units:", store.number_of_units)

store.increment_number_of_units(10)
print("Після increment_number_of_units:", store.number_of_units)

# --- Частина 4: клас Discount ---
store_discount = Discount(
    "SaleShop",
    "Одяг",
    ["Куртки", "Кросівки", "Рюкзаки"]
)

store_discount.get_discounts_products()
store_discount.describe_shop()

# --- Частина 5: перевірка імпорту в іншому файлі ---
all_store = Shop("AllStore", "Універсальний")
all_store.open_shop()
