# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(802, 544)
        MainWindow.setMaximumSize(QSize(2000, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.usuario = QLabel(self.centralwidget)
        self.usuario.setObjectName(u"usuario")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(30)
        self.usuario.setFont(font)

        self.verticalLayout.addWidget(self.usuario, 0, Qt.AlignmentFlag.AlignHCenter)

        self.linha_usuari = QLineEdit(self.centralwidget)
        self.linha_usuari.setObjectName(u"linha_usuari")
        self.linha_usuari.setMinimumSize(QSize(500, 100))
        self.linha_usuari.setMaximumSize(QSize(500, 16777215))
        font1 = QFont()
        font1.setPointSize(30)
        self.linha_usuari.setFont(font1)

        self.verticalLayout.addWidget(self.linha_usuari, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.valor = QLabel(self.centralwidget)
        self.valor.setObjectName(u"valor")
        self.valor.setFont(font1)

        self.verticalLayout.addWidget(self.valor, 0, Qt.AlignmentFlag.AlignHCenter)

        self.linha_valor = QLineEdit(self.centralwidget)
        self.linha_valor.setObjectName(u"linha_valor")
        self.linha_valor.setMinimumSize(QSize(500, 100))
        self.linha_valor.setMaximumSize(QSize(1000, 16777215))
        self.linha_valor.setFont(font1)

        self.verticalLayout.addWidget(self.linha_valor, 0, Qt.AlignmentFlag.AlignHCenter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.usuario.setText(QCoreApplication.translate("MainWindow", u"usuario", None))
        self.linha_usuari.setText("")
        self.valor.setText(QCoreApplication.translate("MainWindow", u"valor", None))
        self.linha_valor.setText("")
    # retranslateUi

