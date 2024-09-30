import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget

class Class1(QWidget):
    def __init__(self):
        super().__init__()
        ui_path = "_internal/ui/test.ui"
        uic.loadUi(ui_path, self)
        self.screen1()

    def screen1(self):
        self.stackedWidget.setCurrentWidget(self.page)
        self.page2btn.clicked.connect(self.screen2)

    def screen2(self):
        self.stackedWidget.setCurrentWidget(self.page_2)
        self.screen1btn.clicked.connect(self.screen1)
        self.screen3btn.clicked.connect(self.screen3)

    def screen3(self):
        try:
            self.screen_3 = Screen_3(self)
            self.screen_3.show()
        except Exception as e:
            print(f"Error opening Screen_3: {e}")

class Screen_3(QWidget):
    def __init__(self, Class1_instance):
        super(Screen_3, self).__init__()
        try:
            ui_path = "_internal/ui/screen3.ui"
            uic.loadUi(ui_path, self)
            self.Class1_instance = Class1_instance

            self.btn2.clicked.connect(self.taketoscreen2)
        except Exception as e:
            print(f"Error initializing Screen_3: {e}")

    def taketoscreen2(self):
        self.Class1_instance.screen2()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Class1()
    window.show()
    sys.exit(app.exec_())
