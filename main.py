from model import SushiMenuModel
from view import ConsoleView
from presenter import OrderPresenter

# Запуск програми
if __name__ == "__main__":
    model = SushiMenuModel()
    view = ConsoleView()
    presenter = OrderPresenter(model, view)
    presenter.run()