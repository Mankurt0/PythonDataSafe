# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SignupWindow.ui'
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

class Ui_signupwindow(object):
    def setupUi(self, signupwindow):
        if not signupwindow.objectName():
            signupwindow.setObjectName(u"signupwindow")
        signupwindow.resize(400, 100)
        signupwindow.setMinimumSize(QSize(400, 100))
        signupwindow.setMaximumSize(QSize(16777215, 100))
        self.gridLayout = QGridLayout(signupwindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 9, -1, -1)
        self.loginentry = QLineEdit(signupwindow)
        self.loginentry.setObjectName(u"loginentry")

        self.gridLayout.addWidget(self.loginentry, 0, 1, 1, 1)

        self.loginlabel = QLabel(signupwindow)
        self.loginlabel.setObjectName(u"loginlabel")

        self.gridLayout.addWidget(self.loginlabel, 0, 0, 1, 1)

        self.passwordlabel = QLabel(signupwindow)
        self.passwordlabel.setObjectName(u"passwordlabel")

        self.gridLayout.addWidget(self.passwordlabel, 1, 0, 1, 1)

        self.passwordentry = QLineEdit(signupwindow)
        self.passwordentry.setObjectName(u"passwordentry")

        self.gridLayout.addWidget(self.passwordentry, 1, 1, 1, 1)

        self.loginbutton = QPushButton(signupwindow)
        self.loginbutton.setObjectName(u"loginbutton")

        self.gridLayout.addWidget(self.loginbutton, 0, 2, 2, 1)


        self.retranslateUi(signupwindow)

        QMetaObject.connectSlotsByName(signupwindow)
    # setupUi

    def retranslateUi(self, signupwindow):
        signupwindow.setWindowTitle(QCoreApplication.translate("signupwindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.loginlabel.setText(QCoreApplication.translate("signupwindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.passwordlabel.setText(QCoreApplication.translate("signupwindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.loginbutton.setText(QCoreApplication.translate("signupwindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0430\u043a\u043a\u0430\u0443\u043d\u0442", None))
    # retranslateUi

