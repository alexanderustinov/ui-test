# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import math
import re
import sys


class Window(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Python ")
		self.setGeometry(100, 100, 360, 350)
		self.UiComponents()
		self.show()

	def UiComponents(self):
		self.label = QLabel(self)
		self.label.setGeometry(5, 5, 350, 70)
		self.label.setWordWrap(True)

		# setting style sheet to the label
		self.label.setStyleSheet("QLabel"
								"{"
								"border : 2px solid black;"
								"background : white;"
								"}")
		self.label2 = QLabel(self)
		self.label2.setGeometry(5, 76, 350, 70)
		self.label2.setWordWrap(True)

		# setting style sheet to the label
		self.label2.setStyleSheet("QLabel"
								 "{"
								 "border : 2px solid black;"
								 "background : white;"
								 "}")
		# setting alignment to the label
		self.label.setAlignment(Qt.AlignRight)

		push_equal = QPushButton("Вычислить", self)
		push_equal.setGeometry(250, 300, 100, 40)

		# adding equal button a color effect
		c_effect = QGraphicsColorizeEffect()
		c_effect.setColor(Qt.blue)
		push_equal.setGraphicsEffect(c_effect)


		push_mul = QPushButton("*", self)
		push_mul.setGeometry(105, 150, 100, 40)


		# clear button
		push_clear = QPushButton("Стереть", self)
		push_clear.setGeometry(250, 150, 100, 40)

		# del one character button
		push_tg = QPushButton("tg", self)
		push_tg.setGeometry(5, 150, 100, 40)

		# adding action to each of the button
		push_equal.clicked.connect(self.action_equal)
		push_tg.clicked.connect(self.action_tg)
		push_mul.clicked.connect(self.action_mul)
		push_clear.clicked.connect(self.action_clear)

	def action_equal(self):
		equation = self.label.text()
		ans = 0
		while equation.rfind('(') != -1:
			l = equation.rfind('(')+1
			r = equation.find(')')

			if equation[l:r] == '':
				ans = -1
				break
			else:
				eq = eval(equation[l:r])
			eq = math.tan(eq)
			equation = '{}{}{}'.format(equation[:equation.rfind('t')], eq, equation[r+1:])
		if ans != -1:
			ans = eval(equation)
		self.label2.setText(ans)

	def action_mul(self):
		# appending label text
		text = self.label.text()
		self.label.setText(text + " * ")

	def action_clear(self):
		# clearing the label text
		self.label.setText("")

	def action_tg(self):
		self.label.setText('tg({})'.format(self.label.text()))

	def keyPressEvent(self, event):
		key = event.key()
		text = ''
		if key == Qt.Key_0:
			text = '0'
		elif key == Qt.Key_1:
			text = '1'
		elif key == Qt.Key_2:
			text = '2'
		elif key == Qt.Key_3:
			text = '3'
		elif key == Qt.Key_4:
			text = '4'
		elif key == Qt.Key_5:
			text = '5'
		elif key == Qt.Key_6:
			text = '6'
		elif key == Qt.Key_7:
			text = '7'
		elif key == Qt.Key_8:
			text = '8'
		elif key == Qt.Key_9:
			text = '9'
		if text:
			current_text = self.label.text()
			self.label.setText(current_text + text)

# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
