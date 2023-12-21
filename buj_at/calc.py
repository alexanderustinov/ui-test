import argparse
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt
import math


class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Калькулятор')
        self.setGeometry(100, 100, 300, 400)
        self.input_field = QLineEdit()
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.input_field = QLineEdit()
        self.layout.addWidget(self.input_field)
        button_layout = [
            'tan', '*',
            'Clear', '='
        ]

        hbox = QHBoxLayout()
        for text in button_layout:
            button = QPushButton(text)
            hbox.addWidget(button)
            button.clicked.connect(self.buttonClicked)
        self.layout.addLayout(hbox)

        self.central_widget.setLayout(self.layout)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Подтверждение',
                                     "Вы уверены, что хотите выйти?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def buttonClicked(self):
        button = self.sender()
        text = button.text()

        if text == '=':
            try:
                result = eval(self.input_field.text())
                self.input_field.setText(str(result))
            except:
                self.input_field.setText('Ошибка')

        elif text == 'Clear':
            self.input_field.clear()

        elif text == 'tan':
            try:
                value = float(self.input_field.text())
                result = math.tan(value)
                self.input_field.setText(str(result))
            except:
                self.input_field.setText('Ошибка')

        else:
            self.input_field.setText(self.input_field.text() + text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--logging")
    app = QApplication(sys.argv)
    ex = CalculatorApp()
    ex.show()
    sys.exit(app.exec_())
