from enum import Enum

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QToolButton
from PyQt5 import QtCore, QtGui

from ui_checkers import Ui_checkers_board

Pieces = Enum("Pieces", "CLOSE EMPTY WHITE BLACK KING_WHITE KING_BLACK")


class CheckersMain(QMainWindow, Ui_checkers_board):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = Ui_checkers_board()
        self.show()
        self.lb_player = 'WHITE'

        # self.board = [
        #     [Pieces.CLOSE, Pieces.BLACK, Pieces.CLOSE, Pieces.BLACK, Pieces.CLOSE, Pieces.BLACK, Pieces.CLOSE, Pieces.BLACK],
        #     [Pieces.BLACK, Pieces.CLOSE, Pieces.BLACK, Pieces.CLOSE, Pieces.BLACK, Pieces.CLOSE, Pieces.BLACK, Pieces.CLOSE],
        #     [Pieces.CLOSE, Pieces.BLACK, Pieces.CLOSE, Pieces.BLACK, Pieces.CLOSE, Pieces.BLACK, Pieces.CLOSE, Pieces.BLACK],
        #     [Pieces.EMPTY, Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE],
        #     [Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE, Pieces.EMPTY],
        #     [Pieces.WHITE, Pieces.CLOSE, Pieces.WHITE, Pieces.CLOSE, Pieces.WHITE, Pieces.CLOSE, Pieces.WHITE, Pieces.CLOSE],
        #     [Pieces.CLOSE, Pieces.WHITE, Pieces.CLOSE, Pieces.WHITE, Pieces.CLOSE, Pieces.WHITE, Pieces.CLOSE, Pieces.WHITE],
        #     [Pieces.WHITE, Pieces.CLOSE, Pieces.WHITE, Pieces.CLOSE, Pieces.WHITE, Pieces.CLOSE, Pieces.WHITE, Pieces.CLOSE],
        # ]

        self.images = ['', '', '']
        self.icon_white = QtGui.QIcon()
        self.icon_white.addPixmap(QtGui.QPixmap("images/white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.images.append(self.icon_white)
        self.icon_black = QtGui.QIcon()
        self.icon_black.addPixmap(QtGui.QPixmap("images/black.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.images.append(self.icon_black)
        self.icon_king_white = QtGui.QIcon()
        self.icon_king_white.addPixmap(QtGui.QPixmap("images/king_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.images.append(self.icon_king_white)
        self.icon_king_black = QtGui.QIcon()
        self.icon_king_black.addPixmap(QtGui.QPixmap("images/king_black.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.images.append(self.icon_king_black)

        self.board = [
            [Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE,
             Pieces.KING_BLACK],
            [Pieces.EMPTY, Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE, Pieces.EMPTY,
             Pieces.CLOSE],
            [Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE, Pieces.BLACK, Pieces.CLOSE,
             Pieces.EMPTY],
            [Pieces.EMPTY, Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE, Pieces.EMPTY,
             Pieces.CLOSE],
            [Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE, Pieces.BLACK, Pieces.CLOSE,
             Pieces.BLACK],
            [Pieces.EMPTY, Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE, Pieces.WHITE, Pieces.CLOSE, Pieces.EMPTY,
             Pieces.CLOSE],
            [Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE, Pieces.BLACK, Pieces.CLOSE, Pieces.WHITE, Pieces.CLOSE,
             Pieces.EMPTY],
            [Pieces.EMPTY, Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE, Pieces.EMPTY,
             Pieces.CLOSE],
        ]

        self.show_board()

    def click_pieces(self):
        tb = self.sender()
        # self.tb_5_6.setChecked()
        pos = tb.objectName().split("_")
        pos[1] = int(pos[1])
        pos[2] = int(pos[2])
        pieces = self.board[pos[1]][pos[2]]
        if pieces == Pieces.EMPTY:
            tb.setChecked(False)
            return

        # Agar raqib toshni olish imkoni bo'lsa
        self.xod = self.check_enemy(pos[1], pos[2], Pieces.BLACK if pieces == Pieces.WHITE else Pieces.WHITE)
        if self.xod:
            print(self.xod)
            return

        # Oddiy bir qadan yurish uchun
        self.xod = self.check_empty(pos[1], pos[2], Pieces.BLACK if pieces == Pieces.WHITE else Pieces.WHITE)
        if self.xod:
            print(self.xod)
            return

        print(pos[1], pos[2])

    def move(self, x1, y1, x2, y2):
        self.board[x2][y2] = self.board[x1][y1]
        self.board[x1][y1] = Pieces.EMPTY
        if abs(x1 - x2) == 2:  # Dushman tosh urib olinsa
            self.board[(x1 + x2) // 2][(y1 + y2) // 2] = Pieces.EMPTY

    def check_empty(self, x: int, y: int, enemy: Pieces):  # Yurish mumkin bo'lgan yo'llar
        arr_xod = []
        i = -1 if enemy == Pieces.BLACK else 1
        # for i in (-1, 1):
        for j in (-1, 1):
            if 0 <= x + i <= 7 and 0 <= y + j <= 7:
                if self.board[x + i][y + j] == Pieces.EMPTY:
                    arr_xod.append([x + i, y + j])
        return arr_xod

    def check_enemy(self, x: int, y: int, enemy: Pieces):  # Olish mumkin bo'lgan toshlar
        arr_xod = []
        for i in (-1, 1):
            for j in (-1, 1):
                if 0 <= x + i <= 7 and 0 <= y + j <= 7:  # Doskadan tashqariga chiqib ketmaslik uchun
                    if self.board[x + i][y + j] == enemy:  # Raqib tosh yonida bo'lsa
                        if 0 <= x + 2 * i <= 7 and 0 <= y + 2 * j <= 7:  # Doskadan tashqariga chiqib ketmaslik uchun
                            if self.board[x + 2 * i][y + 2 * j] == Pieces.EMPTY:  # Raqib toshni olish imkoni bo'lsa
                                arr_xod.append([x + 2 * i, y + 2 * j])
        return arr_xod

    def print_board(self):
        for item in self.board:
            for p in item:
                print(p.value, end=' ')
            print()

    def show_board(self):
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == Pieces.CLOSE:
                    continue
                getattr(self, "tb_%s_%s" % (i, j)).clicked.connect(self.click_pieces)
                if self.board[i][j] == Pieces.EMPTY:
                    continue
                getattr(self, "tb_%s_%s" % (i, j)).setIcon(self.images[self.board[i][j].value])
