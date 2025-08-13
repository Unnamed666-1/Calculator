import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit


class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        # Налаштовуємо вікно
        self.setWindowTitle("Калькулятор")
        self.setGeometry(100, 100, 300, 350)

        # Створюємо основний лойаут
        vbox = QVBoxLayout()

        # Поле для вводу виразів
        self.entry = QLineEdit(self)
        self.entry.setReadOnly(True) # Забороняємо вводити текст вручну
        self.entry.setFixedHeight(35) # Фіксуємо висоту поля
        vbox.addWidget(self.entry)

        # Створюємо сітковий лойаут
        grid = QGridLayout()

        # Опис кнопок калькулятора
        buttons = [
            ('n!', 0, 0), ('x^y', 0, 1), ('x^^y', 0, 2), ('x[n]y', 0, 3),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), ('00',5 ,3 ),        
            ]

        # Створюємо кнопки і додаємо їх до сіткового лойауту
        for (text, row, col) in buttons:
            button = QPushButton(text)
            button.setFixedSize(60, 60)
            grid.addWidget(button, row, col)
            button.clicked.connect(self.on_button_click)

        # Додаємо сітковий  лойаут до основного лойауту
        vbox.addLayout(grid)

        # Кнопка очищення
        clear_button = QPushButton('C')
        clear_button.setFixedSize(200, 60)
        clear_button.clicked.connect(self.clear_entry)
        vbox.addWidget(clear_button)

        # Встановлюємо основний лайаут
        self.setLayout(vbox)

    def on_button_click(self):
        button = self.sender()
        text = button.text()

        if text == '=':
            try:
                expression = self.entry.text()
                result = str(eval(expression)) # Використовуємо eval для обчислення виразу
                self.entry.setText(result)
            except:
                self.entry.setText("Помилка")
        else:
            self.entry.setText(self.entry.text() + text)

    def clear_entry(self):
        self.entry.clear()


# Запуск додатку
if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())