import sys
import json
from PyQt5.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget, QMessageBox


class JSONViewer(QWidget):
    def __init__(self, data):
        super().__init__()
        self.setWindowTitle('JSON Viewer')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()
        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(['Key', 'Value'])
        self.populate_tree(None, data)
        layout.addWidget(self.tree)
        self.setLayout(layout)

    def populate_tree(self, parent, data):
        if isinstance(data, dict):
            for k, v in data.items():
                item = QTreeWidgetItem([str(k), ''])
                if parent is None:
                    self.tree.addTopLevelItem(item)
                else:
                    parent.addChild(item)
                if isinstance(v, (dict, list)):
                    self.populate_tree(item, v)
                else:
                    item.setText(1, str(v))
        elif isinstance(data, list):
            for i, v in enumerate(data):
                item = QTreeWidgetItem(['', ''])
                if parent is None:
                    self.tree.addTopLevelItem(item)
                else:
                    parent.addChild(item)
                if isinstance(v, (dict, list)):
                    self.populate_tree(item, v)
                else:
                    item.setText(1, str(v))

    def closeEvent(self, event):
        reply = QMessageBox.question(
                    self,
                    "Выйти",
                    "Вы уверены, что хотите выйти?",
                    QMessageBox.Yes | QMessageBox.No,
                    QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            event.accept()
        else:
             event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    with open('smoking.json', 'r') as file:
        data = json.load(file)
    viewer = JSONViewer(data)
    viewer.show()

    sys.exit(app.exec_())