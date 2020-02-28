from enum import Enum

from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow

from ui_checkers import Ui_checkers_board

Pieces = Enum("Pieces", "CLOSE EMPTY WHITE BLACK KING_WHITE KING_BLACK")


class CheckersMain(QMainWindow, Ui_checkers_board):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = Ui_checkers_board()
        self.show()

        self.xod = []
        self.lb_player = 'WHITE'
        self.click = True

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

        self.images = ['', '']
        self.icon_empty = QtGui.QIcon()
        self.icon_empty.addPixmap(QtGui.QPixmap("images/empty.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.images.append(self.icon_empty)
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
            [Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE, Pieces.KING_BLACK],
            [Pieces.EMPTY, Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE],
            [Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE, Pieces.BLACK, Pieces.CLOSE, Pieces.EMPTY],
            [Pieces.EMPTY, Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE],
            [Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE, Pieces.BLACK, Pieces.CLOSE, Pieces.BLACK],
            [Pieces.EMPTY, Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE, Pieces.WHITE, Pieces.CLOSE, Pieces.WHITE, Pieces.CLOSE],
            [Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE, Pieces.BLACK, Pieces.CLOSE, Pieces.WHITE, Pieces.CLOSE, Pieces.EMPTY],
            [Pieces.EMPTY, Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE],
        ]

        for i in range(8):
            for j in range(8):
                if self.board[i][j] == Pieces.CLOSE:
                    continue
                getattr(self, "tb_%s_%s" % (i, j)).clicked.connect(self.click_pieces)

        self.show_board()

    def click_pieces(self):
        tb = self.sender()
        # self.tb_5_6.setChecked()
        pos = tb.objectName().split("_")
        pos[1] = int(pos[1])
        pos[2] = int(pos[2])
        pieces = self.board[pos[1]][pos[2]]
        if not self.xod and pieces == Pieces.EMPTY:
            tb.setChecked(False)
            return

        if self.xod:  # Walking the selected stone
            if [pos[1], pos[2]] in self.xod:
                print('Makaka')

            self.xod.clear()
            self.lb_player = 'WHITE' if self.lb_player == 'BLACK' else 'BLACK'
            pass
        else:  # The choice of stone
            if self.lb_player not in str(pieces):  # Cancel when a competitor is selected
                tb.setChecked(False)
                return
            self.x = pos[1]
            self.y = pos[2]
            self.check_xod(pos[1], pos[2], pieces)

            # If there is no walking path
            if not self.xod:
                tb.setChecked(False)

        print(pos[1], pos[2])

    def check_xod(self, x: int, y: int, pieces: Pieces):

        if 'KING' in str(pieces):
            # If the opponent is able to eat the stone
            self.xod = self.check_king_enemy(x, y)
            if self.xod:
                print('check_king_enemy', self.xod)
                return

            # For a simple walk
            self.xod = self.check_king_empty(x, y)
            if self.xod:
                print('check_king_empty', self.xod)
                return
        else:
            # If the opponent is able to eat the stone
            self.xod = self.check_enemy(x, y)
            if self.xod:
                print('check_enemy', self.xod)
                return

            # For a simple walk
            self.xod = self.check_empty(x, y)
            if self.xod:
                print('check_empty', self.xod)
                return

    def check_king_empty(self, x: int, y: int):  # Damka yurishi mumkin bo'lgan yo'llar
        arr_xod = []
        for i in (-1, 1):
            for j in (-1, 1):
                for k in range(1, 8):
                    if 0 <= x + i * k <= 7 and 0 <= y + j * k <= 7:
                        if self.board[x + i * k][y + j * k] == Pieces.EMPTY:
                            arr_xod.append([x + i * k, y + j * k])
                        else:
                            break
                    else:
                        break
        return arr_xod

    def check_king_enemy(self, x: int, y: int):  # Olish mumkin bo'lgan yo'llar
        arr_xod = []
        for i in (-1, 1):
            for j in (-1, 1):
                for k in range(1, 8):
                    if 0 <= x + i * k <= 7 and 0 <= y + j * k <= 7:  # Doskadan tashqariga chiqib ketmaslik uchun
                        if self.board[x + i * k][y + j * k] == Pieces.EMPTY:  # Bo'sh joyni tashlab ketish
                            continue
                        if self.lb_player not in str(self.board[x + i * k][y + j * k]):  # Yo'lida raqib tosh bo'lsa
                            for m in range(k+1, 8):
                                if 0 <= x + i * m <= 7 and 0 <= y + j * m <= 7:  # Doskadan tashqariga chiqib ketmaslik uchun
                                    if self.board[x + i * m][y + j * m] == Pieces.EMPTY:  # Raqib toshni olish imkoni bo'lsa
                                        arr_xod.append([x + i * m, y + j * m])
                                    else:
                                        break
                        else:
                            break
        return arr_xod

    def move(self, x1, y1, x2, y2):
        self.board[x2][y2] = self.board[x1][y1]
        self.board[x1][y1] = Pieces.EMPTY
        if abs(x1 - x2) >= 2:  # Dushman tosh urib olinsa
            k = (x2 - x1) // (y2 - y1)  # y=kx+b
            b = y1 - k * x1
            for x in range(x1, x2, (x2-x1) // abs(x1 - x2)):
                self.board[x][k * x + b] = Pieces.EMPTY

    def check_empty(self, x: int, y: int):  # Yurish mumkin bo'lgan yo'llar
        arr_xod = []
        i = -1 if self.lb_player == 'WHITE' else 1
        for j in (-1, 1):
            if 0 <= x + i <= 7 and 0 <= y + j <= 7:
                if self.board[x + i][y + j] == Pieces.EMPTY:
                    arr_xod.append([x + i, y + j])
        return arr_xod

    def check_enemy(self, x: int, y: int):  # Olish mumkin bo'lgan toshlar
        arr_xod = []
        for i in (-1, 1):
            for j in (-1, 1):
                if 0 <= x + i <= 7 and 0 <= y + j <= 7:  # Doskadan tashqariga chiqib ketmaslik uchun
                    if self.board[x + i][y + j] != Pieces.EMPTY:  # Bosh bo'lmasa
                        if self.lb_player not in str(self.board[x + i][y + j]):  # Raqib tosh yonida bo'lsa
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
                getattr(self, "tb_%s_%s" % (i, j)).setChecked(False)
                getattr(self, "tb_%s_%s" % (i, j)).setIcon(self.images[self.board[i][j].value])
