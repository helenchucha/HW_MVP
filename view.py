'''
View - візуальний інтерфейс користувача для консолі.
Це простий приклад реалізації вигляду у MVP архітектурі, який відповідає лише за
вигляд інформації та отримання даних від користувача.

Цей модуль відповідає за взаємодію з користувачем через консоль:
- display_menu (відображення меню)
- get_user_choice (отримання вибору користувача)
- show_order (виведення поточного замовлення)
- show_message (виведення повідомлень)

Особливості:
- Виводить меню з переліком товарів та їх цінами.
- Запитує користувача ввести ID товару та кількість для додавання до кошика.
- Показує фінальне замовлення з підрахунком суми.
- Виводить будь-які повідомлення або повідомлення про помилки.
'''


class ConsoleView:
    def display_menu(self, menu):
        print("Меню:")
        for id, item in menu.items():
            print(f"{id}. {item['name']} - {item['price']} грн")
        print()

    def get_user_choice(self):
        try:
            item_id = int(input("Введіть ID товару для додавання до кошика: "))
            quantity = int(input("Введіть кількість: "))
            return item_id, quantity
        except ValueError:
            print("Некоректний ввід. Спробуйте ще раз.")
            return self.get_user_choice()

    def show_order(self, order, menu):
        print("\nВаше замовлення:")
        total = 0
        for item in order:
            item_info = menu[item['id']]
            subtotal = item_info['price'] * item['quantity']
            total += subtotal
            print(f"{item_info['name']} x {item['quantity']} = {subtotal} грн")
        print(f"Загальна сума: {total} грн\n")

    def show_message(self, message):
        print(message)