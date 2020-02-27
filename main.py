import sys

from PyQt5.QtWidgets import QApplication

from checkers import CheckersMain

app = QApplication(sys.argv)
main = CheckersMain()
sys.exit(app.exec_())
