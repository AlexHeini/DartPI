from gui import DartApp
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication([])
    window = DartApp()
    window.show()
    app.exec()
