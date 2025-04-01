# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SigninWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_signinwindow(object):
    def setupUi(self, signinwindow):
        if not signinwindow.objectName():
            signinwindow.setObjectName(u"signinwindow")
        signinwindow.resize(400, 100)
        signinwindow.setMinimumSize(QSize(400, 100))
        signinwindow.setMaximumSize(QSize(16777215, 100))
        self.gridLayout = QGridLayout(signinwindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.loginentry = QLineEdit(signinwindow)
        self.loginentry.setObjectName(u"loginentry")

        self.gridLayout.addWidget(self.loginentry, 0, 1, 1, 1)

        self.loginlabel = QLabel(signinwindow)
        self.loginlabel.setObjectName(u"loginlabel")

        self.gridLayout.addWidget(self.loginlabel, 0, 0, 1, 1)

        self.passwordlabel = QLabel(signinwindow)
        self.passwordlabel.setObjectName(u"passwordlabel")

        self.gridLayout.addWidget(self.passwordlabel, 1, 0, 1, 1)

        self.passwordentry = QLineEdit(signinwindow)
        self.passwordentry.setObjectName(u"passwordentry")

        self.gridLayout.addWidget(self.passwordentry, 1, 1, 1, 1)

        self.loginbutton = QPushButton(signinwindow)
        self.loginbutton.setObjectName(u"loginbutton")

        self.gridLayout.addWidget(self.loginbutton, 0, 2, 2, 1)


        self.retranslateUi(signinwindow)

        QMetaObject.connectSlotsByName(signinwindow)
    # setupUi

    def retranslateUi(self, signinwindow):
        signinwindow.setWindowTitle(QCoreApplication.translate("signinwindow", u"\u0412\u0445\u043e\u0434", None))
        self.loginlabel.setText(QCoreApplication.translate("signinwindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.passwordlabel.setText(QCoreApplication.translate("signinwindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.loginbutton.setText(QCoreApplication.translate("signinwindow", u"\u0412\u043e\u0439\u0442\u0438", None))
    # retranslateUi

