import sys

from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton, QMessageBox
import math


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.input_field = None
        self.initUI()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Quit", "Are you sure you want to quit?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()
    def initUI(self):
        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, 300, 200)

        # FIELDS
        self.input_field = QLineEdit(self)
        self.output_field = QLineEdit(self)
        layout = QVBoxLayout()
        layout.addWidget(self.input_field)
        layout.addWidget(self.output_field)

        # BUTTONS ADD !COLOR!
        self.addButton = QPushButton('+', self)
        self.addButton.setStyleSheet("background-color: #add8e6")
        self.logButton = QPushButton('ln', self)
        self.logButton.setStyleSheet("background-color: #add8e6")

        add_and_log_layout = QHBoxLayout()
        add_and_log_layout.addWidget(self.logButton)
        add_and_log_layout.addWidget(self.addButton)

        self.clearButton = QPushButton('Clear', self)
        self.calcButton = QPushButton('Calculate', self)

        clear_and_calc_layout = QHBoxLayout()
        clear_and_calc_layout.addWidget(self.clearButton)
        clear_and_calc_layout.addWidget(self.calcButton)
        clear_and_calc_layout.addStretch()

        layout.addLayout(add_and_log_layout)
        layout.addLayout(clear_and_calc_layout)
        self.setLayout(layout)

        self.addButton.clicked.connect(self.addition)
        self.logButton.clicked.connect(self.calc_log)
        self.clearButton.clicked.connect(self.clearInputField)
        self.calcButton.clicked.connect(self.calculateResult)

        self.show()

    def addition(self):
        try:
            current_text = self.input_field.text()
            self.input_field.setText(current_text + '+')
        except:
            self.output_field.setText("Complete one operation first")

    def calc_log(self):
        try:
            current_number = float(self.input_field.text())
            result = math.log(current_number)
            self.output_field.setText(str(result))
        except:
            self.output_field.setText("Complete one operation first")


    def clearInputField(self):
        self.input_field.clear()
        self.output_field.clear()

    def calculateResult(self):
        expression = self.input_field.text()
        try:
            result = eval(expression)
            self.output_field.setText(str(result))
        except Exception as e:
            self.output_field.setText('Error')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    sys.exit(app.exec())
