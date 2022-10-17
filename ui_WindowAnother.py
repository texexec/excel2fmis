# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WindowAnotherKkYbkS.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTableView,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(593, 330)
        Dialog.setWindowTitle(u"\uc18c\uacf5\uc885\ucf54\ub4dc \uac80\uc0c9")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setDragEnabled(True)
        self.lineEdit.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.tableView = QTableView(Dialog)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"background-color: rgb(207, 207, 207);")
        self.tableView.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.tableView.setSortingEnabled(True)

        self.gridLayout.addWidget(self.tableView, 1, 0, 1, 1)

        QWidget.setTabOrder(self.lineEdit, self.tableView)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
#if QT_CONFIG(tooltip)
        Dialog.setToolTip(QCoreApplication.translate("Dialog", u"\uc18c\uacf5\uc885 \uc785\ub825", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\uc18c\uacf5\uc885\ucf54\ub4dc \uac80\uc0c9", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\uc0c1\ud0dc", None))
#if QT_CONFIG(tooltip)
        self.tableView.setToolTip(QCoreApplication.translate("Dialog", u"\ud56d\ubaa9\uc120\ud0dd \u21dd \ub354\ube14\ud074\ub9ad(copy)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tableView.setStatusTip(QCoreApplication.translate("Dialog", u"\ud56d\ubaa9\uc120\ud0dd \u21dd \ub354\ube14\ud074\ub9ad  \u21dd \ubcf5\uc0ac", None))
#endif // QT_CONFIG(statustip)
    # retranslateUi

