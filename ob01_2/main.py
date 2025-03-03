class Store():
    def __init__(self, name, address):
        self.name = name  # название магазина
        self.address = address  # адрес магазина
        self.items = {}  # словарь, где ключ - название товара, а значение - его цена. Например: {'яблоки': 100, 'бананы': 250}

    def add_goods(self, product, price):
        """Метод для добавления товара в ассортимент"""
        self.items[product] = price
        print(f"Товар \"{product}\" по цене \"{price}\" добавлен в магазин {self.name}")

    def del_goods(self, product):
        """Метод для удаления товара из ассортимента"""
        del self.items[product]
        print(f"Товар \"{product}\" удален из магазина {self.name}")

    def show_price(self, product):
        """Метод для получения цены товара по его названию.
        Если товар отсутствует, возвращайте None"""
        print(self.items.get(product))

    def update_price(self, product, price):
        """Метод для обновления цены товара"""
        self.items[product] = price
        print(f"Товар: {product}\tНовая цена: {self.items[product]}")

    def show_goods(self):
        """Показать все товары в магазине"""
        print(f"\n{"#" * 10} Ассортимент в магазине {self.name} ({self.address}) {"#" * 10}\n")
        for product in self.items:
            print(f"Товар: {product}\tЦена: {self.items[product]}")


if __name__ == "__main__":
    # Создаем три магазина
    store1 = Store("Магнит", "ул. Ленина, 10")
    store2 = Store("Пятерочка", "ул. Мира, 5")
    store3 = Store("Перекресток", "ул. Гагарина, 15")

    # Добавляем товары в первый магазин
    store1.add_goods("яблоки", 100)
    store1.add_goods("бананы", 250)
    store1.add_goods("молоко", 80)
    store1.add_goods("хлеб", 50)
    store1.add_goods("яйца", 120)

    # Добавляем товары во второй магазин
    store2.add_goods("колбаса", 300)
    store2.add_goods("сыр", 200)
    store2.add_goods("печенье", 90)

    # Добавляем товары в третий магазин
    store3.add_goods("рыба", 400)
    store3.add_goods("мясо", 500)
    store3.add_goods("вода", 60)

    # Тестируем методы магазина store1

    # Показываем все товары в магазине
    store1.show_goods()

    # Добавляем новый товар
    store1.add_goods("йогурт", 70)

    # Обновляем цену товара
    store1.update_price("яблоки", 120)

    # Удаляем товар
    store1.del_goods("хлеб")

    # Показываем цену товара
    store1.show_price("молоко")  # Покажет цену молока
    store1.show_price("кефир")  # Возвращает None, т.к. товар отсутствует

    # Показываем обновленный ассортимент
    store1.show_goods()
