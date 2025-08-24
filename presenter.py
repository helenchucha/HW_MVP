'''
Presenter - координує взаємодію між моделлю та уявленням.

Цей модуль відповідає за логіку бізнес-процесів:
- отримання меню з моделі та його передача для відображення у View.
- обробка користувацького вводу для додавання товарів до замовлення.
- обробка виключень при неправильному введенні (наприклад, невірний ID товару).
- керування процесом додавання товарів до замовлення до завершення.
- підсумкове відображення замовлення та повідомлення користувачу.

Особливості:
- Модуль не займається безпосередньо відображенням або зчитуванням даних.
- Ініціалізація з моделлю та уявленням.
- run - Запуск циклу взаємодії з користувачем.
'''

class OrderPresenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        menu = self.model.get_menu()
        self.view.display_menu(menu)

        while True:
            item_id, quantity = self.view.get_user_choice()
            try:
                self.model.add_to_order(item_id, quantity)
            except ValueError:
                self.view.show_message("Невірний ID. Спробуйте ще раз.")
                continue
            more = input("Додати ще? (так/ні): ").strip().lower()
            if more != 'так':
                break

        self.view.show_order(self.model.get_order(), menu)
        self.view.show_message("Дякуємо за замовлення!")