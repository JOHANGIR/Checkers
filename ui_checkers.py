# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chess.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_checkers_board(object):
    def setupUi(self, checkers_board):
        checkers_board.setObjectName("checkers_board")
        checkers_board.setWindowModality(QtCore.Qt.NonModal)
        checkers_board.resize(554, 634)
        checkers_board.setStyleSheet("#centralwidget{\n"
                                     "    background-color: rgb(255, 255, 255);\n"
                                     "}\n"
                                     "QToolButton {\n"
                                     "    background-color: rgb(170, 85, 0);\n"
                                     "    border: none;\n"
                                     "}\n"
                                     "\n"
                                     "QToolButton:checked {\n"
                                     "    background-color: rgb(0, 85, 255);\n"
                                     "}")
        self.centralwidget = QtWidgets.QWidget(checkers_board)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.tb_5_6 = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_5_6.sizePolicy().hasHeightForWidth())
        self.tb_5_6.setSizePolicy(sizePolicy)
        self.tb_5_6.setIconSize(QtCore.QSize(65, 65))
        self.tb_5_6.setCheckable(True)
        self.tb_5_6.setObjectName("tb_5_6")
        self.gridLayout.addWidget(self.tb_5_6, 5, 6, 1, 1)
        self.tb_6_1 = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_6_1.sizePolicy().hasHeightForWidth())
        self.tb_6_1.setSizePolicy(sizePolicy)
        self.tb_6_1.setIconSize(QtCore.QSize(65, 65))
        self.tb_6_1.setCheckable(True)
        self.tb_6_1.setObjectName("tb_6_1")
        self.gridLayout.addWidget(self.tb_6_1, 6, 1, 1, 1)
        self.tb_1_0 = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_1_0.sizePolicy().hasHeightForWidth())
        self.tb_1_0.setSizePolicy(sizePolicy)
        self.tb_1_0.setIconSize(QtCore.QSize(65, 65))
        self.tb_1_0.setCheckable(True)
        self.tb_1_0.setObjectName("tb_1_0")
        self.gridLayout.addWidget(self.tb_1_0, 1, 0, 1, 1)
        self.tb_0_5 = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_0_5.sizePolicy().hasHeightForWidth())
        self.tb_0_5.setSizePolicy(sizePolicy)
        self.tb_0_5.setIconSize(QtCore.QSize(65, 65))
        self.tb_0_5.setCheckable(True)
        self.tb_0_5.setObjectName("tb_0_5")
        self.gridLayout.addWidget(self.tb_0_5, 0, 5, 1, 1)
        self.tb_2_5 = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_2_5.sizePolicy().hasHeightForWidth())
        self.tb_2_5.setSizePolicy(sizePolicy)
        self.tb_2_5.setIconSize(QtCore.QSize(65, 65))
        self.tb_2_5.setCheckable(True)
        self.tb_2_5.setObjectName("tb_2_5")
        self.gridLayout.addWidget(self.tb_2_5, 2, 5, 1, 1)
        self.tb_7_0 = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_7_0.sizePolicy().hasHeightForWidth())
        self.tb_7_0.setSizePolicy(sizePolicy)
        self.tb_7_0.setIconSize(QtCore.QSize(65, 65))
        self.tb_7_0.setCheckable(True)
        self.tb_7_0.setObjectName("tb_7_0")
        self.gridLayout.addWidget(self.tb_7_0, 7, 0, 1, 1)
        self.tb_4_5 = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_4_5.sizePolicy().hasHeightForWidth())
        self.tb_4_5.setSizePolicy(sizePolicy)
        self.tb_4_5.setIconSize(QtCore.QSize(65, 65))
        self.tb_4_5.setCheckable(True)
        self.tb_4_5.setObjectName("tb_4_5")
        self.gridLayout.addWidget(self.tb_4_5, 4, 5, 1, 1)
        self.tb_4_3 = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_4_3.sizePolicy().hasHeightForWidth())
        self.tb_4_3.setSizePolicy(sizePolicy)
        self.tb_4_3.setIconSize(QtCore.QSize(65, 65))
        self.tb_4_3.setCheckable(True)
        self.tb_4_3.setObjectName("tb_4_3")
        self.gridLayout.addWidget(self.tb_4_3, 4, 3, 1, 1)
        self.tb_6_5 = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_6_5.sizePolicy().hasHeightForWidth())
        self.tb_6_5.setSizePolicy(sizePolicy)
        self.tb_6_5.setIconSize(QtCore.QSize(65, 65))
        self.tb_6_5.setCheckable(True)
        self.tb_6_5.setObjectName("tb_6_5")
        self.gridLayout.addWidget(self.tb_6_5, 6, 5, 1, 1)
        self.tb_3_2 = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_3_2.sizePolicy().hasHeightForWidth())
        self.tb_3_2.setSizePolicy(sizePolicy)
        self.tb_3_2.setIconSize(QtCore.QSize(65, 65))
        self.tb_3_2.setCheckable(True)
        self.tb_3_2.setObjectName("tb_3_2")
        self.gridLayout.addWidget(self.tb_3_2, 3, 2, 1, 1)
        self.tb_3_4 = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_3_4.sizePolicy().hasHeightForWidth())
        self.tb_3_4.setSizePolicy(sizePolicy)
        self.tb_3_4.setIconSize(QtCore.QSize(65, 65))
        self.tb_3_4.setCheckable(True)
        self.tb_3_4.setObjectName("tb_3_4")
        self.gridLayout.addWidget(self.tb_3_4, 3, 4, 1, 1)
        self.tb_2_3 = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_2_3.sizePolicy().hasHeightForWidth())
        self.tb_2_3.setSizePolicy(sizePolicy)
        self.tb_2_3.setIconSize(QtCore.QSize(65, 65))
        self.tb_2_3.setCheckable(True)
        self.tb_2_3.setObjectName("tb_2_3")
        self.gridLayout.addWidget(self.tb_2_3, 2, 3, 1, 1)
        self.tb_1_6 = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_1_6.sizePolicy().hasHeightForWidth())
        self.tb_1_6.setSizePolicy(sizePolicy)
        self.tb_1_6.setIconSize(QtCore.QSize(65, 65))
        self.tb_1_6.setCheckable(True)
        self.tb_1_6.setObjectName("tb_1_6")
        self.gridLayout.addWidget(self.tb_1_6, 1, 6, 1, 1)
        self.tb_7_2 = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_7_2.sizePolicy().hasHeightForWidth())
        self.tb_7_2.setSizePolicy(sizePolicy)
        self.tb_7_2.setIconSize(QtCore.QSize(65, 65))
        self.tb_7_2.setCheckable(True)
        self.tb_7_2.setObjectName("tb_7_2")
        self.gridLayout.addWidget(self.tb_7_2, 7, 2, 1, 1)
        self.tb_4_1 = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_4_1.sizePolicy().hasHeightForWidth())
        self.tb_4_1.setSizePolicy(sizePolicy)
        self.tb_4_1.setIconSize(QtCore.QSize(65, 65))
        self.tb_4_1.setCheckable(True)
        self.tb_4_1.setObjectName("tb_4_1")
        self.gridLayout.addWidget(self.tb_4_1, 4, 1, 1, 1)
        self.tb_7_4 = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_7_4.sizePolicy().hasHeightForWidth())
        self.tb_7_4.setSizePolicy(sizePolicy)
        self.tb_7_4.setIconSize(QtCore.QSize(65, 65))
        self.tb_7_4.setCheckable(True)
        self.tb_7_4.setObjectName("tb_7_4")
        self.gridLayout.addWidget(self.tb_7_4, 7, 4, 1, 1)
        self.tb_5_2 = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_5_2.sizePolicy().hasHeightForWidth())
        self.tb_5_2.setSizePolicy(sizePolicy)
        self.tb_5_2.setIconSize(QtCore.QSize(65, 65))
        self.tb_5_2.setCheckable(True)
        self.tb_5_2.setObjectName("tb_5_2")
        self.gridLayout.addWidget(self.tb_5_2, 5, 2, 1, 1)
        self.tb_2_1 = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_2_1.sizePolicy().hasHeightForWidth())
        self.tb_2_1.setSizePolicy(sizePolicy)
        self.tb_2_1.setIconSize(QtCore.QSize(65, 65))
        self.tb_2_1.setCheckable(True)
        self.tb_2_1.setObjectName("tb_2_1")
        self.gridLayout.addWidget(self.tb_2_1, 2, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lb_player = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lb_player.setFont(font)
        self.lb_player.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_player.setObjectName("lb_player")
        self.horizontalLayout.addWidget(self.lb_player)
        self.gridLayout.addLayout(self.horizontalLayout, 8, 0, 1, 8)
        self.tb_4_7 = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_4_7.sizePolicy().hasHeightForWidth())
        self.tb_4_7.setSizePolicy(sizePolicy)
        self.tb_4_7.setIconSize(QtCore.QSize(65, 65))
        self.tb_4_7.setCheckable(True)
        self.tb_4_7.setObjectName("tb_4_7")
        self.gridLayout.addWidget(self.tb_4_7, 4, 7, 1, 1)
        self.tb_3_0 = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_3_0.sizePolicy().hasHeightForWidth())
        self.tb_3_0.setSizePolicy(sizePolicy)
        self.tb_3_0.setIconSize(QtCore.QSize(65, 65))
        self.tb_3_0.setCheckable(True)
        self.tb_3_0.setObjectName("tb_3_0")
        self.gridLayout.addWidget(self.tb_3_0, 3, 0, 1, 1)
        self.tb_0_3 = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_0_3.sizePolicy().hasHeightForWidth())
        self.tb_0_3.setSizePolicy(sizePolicy)
        self.tb_0_3.setIconSize(QtCore.QSize(65, 65))
        self.tb_0_3.setCheckable(True)
        self.tb_0_3.setObjectName("tb_0_3")
        self.gridLayout.addWidget(self.tb_0_3, 0, 3, 1, 1)
        self.tb_1_4 = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_1_4.sizePolicy().hasHeightForWidth())
        self.tb_1_4.setSizePolicy(sizePolicy)
        self.tb_1_4.setIconSize(QtCore.QSize(65, 65))
        self.tb_1_4.setCheckable(True)
        self.tb_1_4.setObjectName("tb_1_4")
        self.gridLayout.addWidget(self.tb_1_4, 1, 4, 1, 1)
        self.tb_1_2 = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_1_2.sizePolicy().hasHeightForWidth())
        self.tb_1_2.setSizePolicy(sizePolicy)
        self.tb_1_2.setIconSize(QtCore.QSize(65, 65))
        self.tb_1_2.setCheckable(True)
        self.tb_1_2.setObjectName("tb_1_2")
        self.gridLayout.addWidget(self.tb_1_2, 1, 2, 1, 1)
        self.tb_3_6 = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_3_6.sizePolicy().hasHeightForWidth())
        self.tb_3_6.setSizePolicy(sizePolicy)
        self.tb_3_6.setIconSize(QtCore.QSize(65, 65))
        self.tb_3_6.setCheckable(True)
        self.tb_3_6.setObjectName("tb_3_6")
        self.gridLayout.addWidget(self.tb_3_6, 3, 6, 1, 1)
        self.tb_2_7 = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_2_7.sizePolicy().hasHeightForWidth())
        self.tb_2_7.setSizePolicy(sizePolicy)
        self.tb_2_7.setIconSize(QtCore.QSize(65, 65))
        self.tb_2_7.setCheckable(True)
        self.tb_2_7.setObjectName("tb_2_7")
        self.gridLayout.addWidget(self.tb_2_7, 2, 7, 1, 1)
        self.tb_0_7 = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_0_7.sizePolicy().hasHeightForWidth())
        self.tb_0_7.setSizePolicy(sizePolicy)
        self.tb_0_7.setIconSize(QtCore.QSize(65, 65))
        self.tb_0_7.setCheckable(True)
        self.tb_0_7.setObjectName("tb_0_7")
        self.gridLayout.addWidget(self.tb_0_7, 0, 7, 1, 1)
        self.tb_5_4 = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_5_4.sizePolicy().hasHeightForWidth())
        self.tb_5_4.setSizePolicy(sizePolicy)
        self.tb_5_4.setIconSize(QtCore.QSize(65, 65))
        self.tb_5_4.setCheckable(True)
        self.tb_5_4.setObjectName("tb_5_4")
        self.gridLayout.addWidget(self.tb_5_4, 5, 4, 1, 1)
        self.tb_0_1 = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_0_1.sizePolicy().hasHeightForWidth())
        self.tb_0_1.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/black.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tb_0_1.setIcon(icon)
        self.tb_0_1.setIconSize(QtCore.QSize(65, 65))
        self.tb_0_1.setCheckable(True)
        self.tb_0_1.setObjectName("tb_0_1")
        self.gridLayout.addWidget(self.tb_0_1, 0, 1, 1, 1)
        self.tb_6_3 = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_6_3.sizePolicy().hasHeightForWidth())
        self.tb_6_3.setSizePolicy(sizePolicy)
        self.tb_6_3.setIconSize(QtCore.QSize(65, 65))
        self.tb_6_3.setCheckable(True)
        self.tb_6_3.setObjectName("tb_6_3")
        self.gridLayout.addWidget(self.tb_6_3, 6, 3, 1, 1)
        self.tb_6_7 = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_6_7.sizePolicy().hasHeightForWidth())
        self.tb_6_7.setSizePolicy(sizePolicy)
        self.tb_6_7.setIconSize(QtCore.QSize(65, 65))
        self.tb_6_7.setCheckable(True)
        self.tb_6_7.setObjectName("tb_6_7")
        self.gridLayout.addWidget(self.tb_6_7, 6, 7, 1, 1)
        self.tb_7_6 = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_7_6.sizePolicy().hasHeightForWidth())
        self.tb_7_6.setSizePolicy(sizePolicy)
        self.tb_7_6.setIconSize(QtCore.QSize(65, 65))
        self.tb_7_6.setCheckable(True)
        self.tb_7_6.setObjectName("tb_7_6")
        self.gridLayout.addWidget(self.tb_7_6, 7, 6, 1, 1)
        self.tb_5_0 = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_5_0.sizePolicy().hasHeightForWidth())
        self.tb_5_0.setSizePolicy(sizePolicy)
        self.tb_5_0.setIconSize(QtCore.QSize(65, 65))
        self.tb_5_0.setCheckable(True)
        self.tb_5_0.setObjectName("tb_5_0")
        self.gridLayout.addWidget(self.tb_5_0, 5, 0, 1, 1)
        checkers_board.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(checkers_board)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 554, 21))
        self.menubar.setObjectName("menubar")
        checkers_board.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(checkers_board)
        self.statusbar.setObjectName("statusbar")
        checkers_board.setStatusBar(self.statusbar)

        self.retranslateUi(checkers_board)
        QtCore.QMetaObject.connectSlotsByName(checkers_board)

    def retranslateUi(self, checkers_board):
        _translate = QtCore.QCoreApplication.translate
        checkers_board.setWindowTitle(_translate("checkers_board", "Shashka"))
        self.lb_player.setText(_translate("checkers_board", "Player"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    checkers_board = QtWidgets.QMainWindow()
    ui = Ui_checkers_board()
    ui.setupUi(checkers_board)
    checkers_board.show()
    sys.exit(app.exec_())
