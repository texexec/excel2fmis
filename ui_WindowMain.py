# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WindowMainbYKUKm.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTableView,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1305, 719)
        self.action_O = QAction(MainWindow)
        self.action_O.setObjectName(u"action_O")
        self.action_X = QAction(MainWindow)
        self.action_X.setObjectName(u"action_X")
        self.action_C = QAction(MainWindow)
        self.action_C.setObjectName(u"action_C")
        self.action_F = QAction(MainWindow)
        self.action_F.setObjectName(u"action_F")
        self.action_H = QAction(MainWindow)
        self.action_H.setObjectName(u"action_H")
        self.action_F_3 = QAction(MainWindow)
        self.action_F_3.setObjectName(u"action_F_3")
        self.action_A_3 = QAction(MainWindow)
        self.action_A_3.setObjectName(u"action_A_3")
        self.action_W = QAction(MainWindow)
        self.action_W.setObjectName(u"action_W")
        self.action_Excel_O = QAction(MainWindow)
        self.action_Excel_O.setObjectName(u"action_Excel_O")
        self.action_K = QAction(MainWindow)
        self.action_K.setObjectName(u"action_K")
        self.action_C_2 = QAction(MainWindow)
        self.action_C_2.setObjectName(u"action_C_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 2, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout_3.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.horizontalLayout_3.addWidget(self.pushButton_9)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_1 = QPushButton(self.centralwidget)
        self.pushButton_1.setObjectName(u"pushButton_1")

        self.horizontalLayout.addWidget(self.pushButton_1)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.horizontalLayout.addWidget(self.comboBox)

        self.lineEdit_1 = QLineEdit(self.centralwidget)
        self.lineEdit_1.setObjectName(u"lineEdit_1")
        self.lineEdit_1.setStyleSheet(u"")
        self.lineEdit_1.setDragEnabled(True)
        self.lineEdit_1.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.lineEdit_1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"\ub9d1\uc740 \uace0\ub515"])
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout.addWidget(self.pushButton_7)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"background-color: rgb(207, 207, 207);")
        self.tableView.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tableView.setSortingEnabled(True)
        self.tableView.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_2.addWidget(self.tableView, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1305, 22))
        self.menu_F = QMenu(self.menubar)
        self.menu_F.setObjectName(u"menu_F")
        self.menu_H = QMenu(self.menubar)
        self.menu_H.setObjectName(u"menu_H")
        self.menu_C = QMenu(self.menubar)
        self.menu_C.setObjectName(u"menu_C")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu_F.menuAction())
        self.menubar.addAction(self.menu_C.menuAction())
        self.menubar.addAction(self.menu_H.menuAction())
        self.menu_F.addAction(self.action_O)
        self.menu_F.addAction(self.action_W)
        self.menu_F.addSeparator()
        self.menu_F.addAction(self.action_X)
        self.menu_H.addAction(self.action_H)
        self.menu_H.addAction(self.action_F_3)
        self.menu_H.addSeparator()
        self.menu_H.addAction(self.action_A_3)
        self.menu_C.addAction(self.action_Excel_O)
        self.menu_C.addSeparator()
        self.menu_C.addAction(self.action_K)
        self.menu_C.addAction(self.action_C_2)

        self.retranslateUi(MainWindow)
        self.action_X.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FMIS \uc77c\uad04\ub4f1\ub85d", None))
        self.action_O.setText(QCoreApplication.translate("MainWindow", u"\uc5f4\uae30(&O)...", None))
        self.action_X.setText(QCoreApplication.translate("MainWindow", u"\ub05d\ub0b4\uae30(&X)", None))
        self.action_C.setText(QCoreApplication.translate("MainWindow", u"\ubcf5\uc0ac(&C)", None))
        self.action_F.setText(QCoreApplication.translate("MainWindow", u"\ucc3e\uae30(&F)...", None))
        self.action_H.setText(QCoreApplication.translate("MainWindow", u"\ub3c4\uc6c0\ub9d0 \ubcf4\uae30(&H)", None))
        self.action_F_3.setText(QCoreApplication.translate("MainWindow", u"\ud53c\ub4dc\ubc31 \ubcf4\ub0b4\uae30(&F)", None))
        self.action_A_3.setText(QCoreApplication.translate("MainWindow", u"Excel2FMIS \uc815\ubcf4(&A)", None))
        self.action_A_3.setIconText(QCoreApplication.translate("MainWindow", u"Excel2FMIS \uc815\ubcf4(A)", None))
        self.action_W.setText(QCoreApplication.translate("MainWindow", u"\uc0c8 \ucc3d(W)", None))
        self.action_Excel_O.setText(QCoreApplication.translate("MainWindow", u"\ubcf4\uc218\ubaa9\ub85d(Excel) \uc5f4\uae30(O)", None))
        self.action_K.setText(QCoreApplication.translate("MainWindow", u"\ubcf4\uc218\uacf5\uc0ac\uc2b9\ub77d\uc11c \uc0dd\uc131(K)", None))
        self.action_C_2.setText(QCoreApplication.translate("MainWindow", u"\uc900\uacf5\uac80\uc0ac\uc870\uc11c \uc0dd\uc131(C)", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\uc18c\uacf5\uc885\ucf54\ub4dc\uac80\uc0c9", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\uc0d8\ud50c(Excel)\ub2e4\uc6b4\ub85c\ub4dc", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#909090;\">\uc0c1\ud0dc</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.pushButton_1.setStatusTip(QCoreApplication.translate("MainWindow", u"Excel \ud30c\uc77c \uc120\ud0dd", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c\uc5f4\uae30", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\uc18c\uc561\ubcf4\uc218", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\ub2e8\uac00\ubcf4\uc218", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\uc77c\ubc18\uc218\uc120", None))

#if QT_CONFIG(statustip)
        self.comboBox.setStatusTip(QCoreApplication.translate("MainWindow", u"\uc18c\uc561\ubcf4\uc218, \ub2e8\uac00\ubcf4\uc218, \uc77c\ubc18\uc218\uc120 \uc911 \uc120\ud0dd", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(tooltip)
        self.lineEdit_1.setToolTip(QCoreApplication.translate("MainWindow", u"\uc18c\uacf5\uc885\ucf54\ub4dc(\ub2e8\uc77c\uc18c\uacf5\uc885\uc758 \uacbd\uc6b0)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineEdit_1.setStatusTip(QCoreApplication.translate("MainWindow", u"\uc18c\uacf5\uc885\ucf54\ub4dc \uc785\ub825", None))
#endif // QT_CONFIG(statustip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#909090;\">\uc18c\uacf5\uc885</span></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\ub2e8\uc77c\uc18c\uacf5\uc885", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\ubcf5\ud569\uc18c\uacf5\uc885", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\uc77c\uad04\uc0dd\uc131", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\uadf8\ub8f9\uc0dd\uc131", None))
#if QT_CONFIG(tooltip)
        self.pushButton_6.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButton_6.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\uc9c0\uc2dc\ubaa9\ub85d\ubcf4\uae30", None))
#if QT_CONFIG(tooltip)
        self.pushButton_7.setToolTip(QCoreApplication.translate("MainWindow", u"'\uacf5\uc885\ubaa9\ub85d' \uc120\ud0dd", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButton_7.setStatusTip(QCoreApplication.translate("MainWindow", u"\ub2e4\uc6b4\ub85c\ub4dc \ubc1b\uc740 '\uacf5\uc885\ubaa9\ub85d' \uc120\ud0dd \ud6c4 \uae08\uc561 \uc0dd\uc131", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\uacf5\uc885\ubaa9\ub85d", None))
#if QT_CONFIG(tooltip)
        self.tableView.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tableView.setStatusTip(QCoreApplication.translate("MainWindow", u"\ud56d\ubaa9\uc120\ud0dd \u21dd \ub354\ube14\ud074\ub9ad  \u21dd \ubcf5\uc0ac", None))
#endif // QT_CONFIG(statustip)
        self.menu_F.setTitle(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c(&F)", None))
        self.menu_H.setTitle(QCoreApplication.translate("MainWindow", u"\ub3c4\uc6c0\ub9d0(&H)", None))
        self.menu_C.setTitle(QCoreApplication.translate("MainWindow", u"\uc18c\uc561\uc591\uc2dd(C)", None))
    # retranslateUi

