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
        self.player = 'WHITE'
        self.sad = True

        self.board = [
            [Pieces.CLOSE, Pieces.BLACK, Pieces.CLOSE, Pieces.BLACK, Pieces.CLOSE, Pieces.BLACK, Pieces.CLOSE, Pieces.BLACK],
            [Pieces.BLACK, Pieces.CLOSE, Pieces.BLACK, Pieces.CLOSE, Pieces.BLACK, Pieces.CLOSE, Pieces.BLACK, Pieces.CLOSE],
            [Pieces.CLOSE, Pieces.BLACK, Pieces.CLOSE, Pieces.BLACK, Pieces.CLOSE, Pieces.BLACK, Pieces.CLOSE, Pieces.BLACK],
            [Pieces.EMPTY, Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE],
            [Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE, Pieces.EMPTY, Pieces.CLOSE, Pieces.EMPTY],
            [Pieces.WHITE, Pieces.CLOSE, Pieces.WHITE, Pieces.CLOSE, Pieces.WHITE, Pieces.CLOSE, Pieces.WHITE, Pieces.CLOSE],
            [Pieces.CLOSE, Pieces.WHITE, Pieces.CLOSE, Pieces.WHITE, Pieces.CLOSE, Pieces.WHITE, Pieces.CLOSE, Pieces.WHITE],
            [Pieces.WHITE, Pieces.CLOSE, Pieces.WHITE, Pieces.CLOSE, Pieces.WHITE, Pieces.CLOSE, Pieces.WHITE, Pieces.CLOSE],
        ]

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

        for i in range(8):
            for j in range(8):
                if self.board[i][j] == Pieces.CLOSE:
                    continue
                getattr(self, "tb_%s_%s" % (i, j)).clicked.connect(self.click_pieces_two)

        self.show_board()

    def click_pieces_two(self):
        tb = self.sender()
        pos = tb.objectName().split("_")
        pos[1] = int(pos[1])
        pos[2] = int(pos[2])
        pieces = self.board[pos[1]][pos[2]]
# ----------------------------------------------------------------------------------
        if self.xod:  # Walking the selected stone
            if pos[1] == self.x and pos[2] == self.y:  # If you click again
                tb.setChecked(True)
                return

            if [pos[1], pos[2]] in self.xod:  # If you can walk
                self.move(self.x, self.y, pos[1], pos[2])
                self.show_board()
                self.xod.clear()
                if not self.sad:  # If an opponent eats a stone
                    self.sad = True
                    if 'KING' in str(pieces):
                        self.xod = self.check_king_enemy(pos[1], pos[2])
                    else:
                        self.xod = self.check_enemy(pos[1], pos[2])
                    if self.xod:  # If you eat more stones
                        tb.setChecked(True)
                        self.x = pos[1]
                        self.y = pos[2]
                    else:
                        self.player = 'WHITE' if self.player == 'BLACK' else 'BLACK'
                        self.lb_player.setText(self.player)
                else:
                    tb.setChecked(False)
                    self.player = 'WHITE' if self.player == 'BLACK' else 'BLACK'
                    self.lb_player.setText(self.player)
            else:  # If it is not possible to walk
                tb.setChecked(False)
# ----------------------------------------------------------------------------------
        else:  # The choice of stone
            if pieces == Pieces.EMPTY:  # If an empty cell is selected
                tb.setChecked(False)
                return
            if self.check_all_enemy():  # If the opponent is able to take the stone
                if [pos[1], pos[2]] not in self.check_all_enemy():  # If there is no selected cell
                    tb.setChecked(False)
                    return
            if self.player not in str(pieces):  # Cancel when a competitor is selected
                tb.setChecked(False)
                return

            self.check_xod(pos[1], pos[2], pieces)
            if self.xod:
                self.x = pos[1]
                self.y = pos[2]
            else:   # If there is no walking path
                tb.setChecked(False)
# ----------------------------------------------------------------------------------

    def check_all_enemy(self):
        arr_xod = []
        for i in range(0, 8):
            for j in range(0, 8):
                if self.player in str(self.board[i][j]):  # All WHITE or BLACK stones
                    if 'KING' in str(self.board[i][j]):  # If there is a KING
                        if self.check_king_enemy(i, j):
                            arr_xod.append([i, j])
                    else:  # If there is a simple stone
                        if self.check_enemy(i, j):
                            arr_xod.append([i, j])
        return arr_xod

    def check_xod(self, x: int, y: int, pieces: Pieces):

        if 'KING' in str(pieces):
            # If the opponent is able to eat the stone
            self.xod = self.check_king_enemy(x, y)
            if self.xod:
                return

            # For a simple walk
            self.xod = self.check_king_empty(x, y)
            if self.xod:
                return
        else:
            # If the opponent is able to eat the stone
            self.xod = self.check_enemy(x, y)
            if self.xod:
                return

            # For a simple walk
            self.xod = self.check_empty(x, y)
            if self.xod:
                return

    def check_king_empty(self, x: int, y: int):  # Roads that the KING may walk
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

    def check_king_enemy(self, x: int, y: int):  # Roads the KING can eat
        arr_xod = []
        for i in (-1, 1):
            for j in (-1, 1):
                for k in range(1, 8):
                    if 0 <= x + i * k <= 7 and 0 <= y + j * k <= 7:  # Not to get out of the board
                        if self.board[x + i * k][y + j * k] == Pieces.EMPTY:  # Skip empty places
                            continue
                        if self.player not in str(self.board[x + i * k][y + j * k]):  # If there is an enemy stone in the path
                            for m in range(k+1, 8):
                                if 0 <= x + i * m <= 7 and 0 <= y + j * m <= 7:  # Not to get out of the board
                                    if self.board[x + i * m][y + j * m] == Pieces.EMPTY:  # If you can get an opponent’s stone
                                        arr_xod.append([x + i * m, y + j * m])
                                    else:
                                        break
                        else:
                            break
        return arr_xod

    def move(self, x1, y1, x2, y2):
        self.board[x2][y2] = self.board[x1][y1]
        self.board[x1][y1] = Pieces.EMPTY
        if abs(x1 - x2) >= 2:  # If the enemy stone is eaten
            k = (x2 - x1) // (y2 - y1)  # y=kx+b
            b = y1 - k * x1
            for x in range(x1, x2, (x2-x1) // abs(x1 - x2)):
                if self.board[x][k * x + b] != Pieces.EMPTY:
                    self.sad = False
                self.board[x][k * x + b] = Pieces.EMPTY

    def check_empty(self, x: int, y: int):  # Allowed paths
        arr_xod = []
        i = -1 if self.player == 'WHITE' else 1
        for j in (-1, 1):
            if 0 <= x + i <= 7 and 0 <= y + j <= 7:
                if self.board[x + i][y + j] == Pieces.EMPTY:
                    arr_xod.append([x + i, y + j])
        return arr_xod

    def check_enemy(self, x: int, y: int):  # Stones that can be eaten
        arr_xod = []
        for i in (-1, 1):
            for j in (-1, 1):
                if 0 <= x + i <= 7 and 0 <= y + j <= 7:  # Not to get out of the board
                    if self.board[x + i][y + j] != Pieces.EMPTY:  # Skip empty places
                        if self.player not in str(self.board[x + i][y + j]):  # If nearby enemy stones
                            if 0 <= x + 2 * i <= 7 and 0 <= y + 2 * j <= 7:  # Not to get out of the board
                                if self.board[x + 2 * i][y + 2 * j] == Pieces.EMPTY:  # If you can get an opponent’s stone
                                    arr_xod.append([x + 2 * i, y + 2 * j])
        return arr_xod

    def show_board(self):
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == Pieces.CLOSE:
                    continue
                if self.board[i][j] == Pieces.WHITE and i == 0:
                    self.board[i][j] = Pieces.KING_WHITE
                if self.board[i][j] == Pieces.BLACK and i == 7:
                    self.board[i][j] = Pieces.KING_BLACK
                getattr(self, "tb_%s_%s" % (i, j)).setChecked(False)
                getattr(self, "tb_%s_%s" % (i, j)).setIcon(self.images[self.board[i][j].value])
