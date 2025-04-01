# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QHeaderView, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QTabWidget, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        self.signin = QAction(MainWindow)
        self.signin.setObjectName(u"signin")
        self.signin.setCheckable(False)
        self.signup = QAction(MainWindow)
        self.signup.setObjectName(u"signup")
        self.signout = QAction(MainWindow)
        self.signout.setObjectName(u"signout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.texttab = QWidget()
        self.texttab.setObjectName(u"texttab")
        self.gridLayout_3 = QGridLayout(self.texttab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.texttablet = QTableWidget(self.texttab)
        if (self.texttablet.columnCount() < 2):
            self.texttablet.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.texttablet.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.texttablet.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.texttablet.setObjectName(u"texttablet")
        self.texttablet.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.texttablet.setFrameShape(QFrame.Shape.StyledPanel)
        self.texttablet.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.texttablet.setShowGrid(True)
        self.texttablet.setRowCount(0)
        self.texttablet.setColumnCount(2)
        self.texttablet.horizontalHeader().setCascadingSectionResizes(False)

        self.gridLayout_3.addWidget(self.texttablet, 0, 0, 1, 1)

        self.tabWidget.addTab(self.texttab, "")
        self.imagetab = QWidget()
        self.imagetab.setObjectName(u"imagetab")
        self.gridLayout_2 = QGridLayout(self.imagetab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.imagetablet = QTableWidget(self.imagetab)
        if (self.imagetablet.columnCount() < 2):
            self.imagetablet.setColumnCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.imagetablet.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.imagetablet.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        self.imagetablet.setObjectName(u"imagetablet")
        self.imagetablet.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.imagetablet.setFrameShape(QFrame.Shape.StyledPanel)
        self.imagetablet.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.imagetablet.setShowGrid(True)
        self.imagetablet.setRowCount(0)
        self.imagetablet.setColumnCount(2)
        self.imagetablet.horizontalHeader().setCascadingSectionResizes(False)

        self.gridLayout_2.addWidget(self.imagetablet, 0, 0, 1, 1)

        self.tabWidget.addTab(self.imagetab, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 800, 33))
        self.menu = QMenu(self.menuBar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menu.menuAction())
        self.menu.addAction(self.signin)
        self.menu.addAction(self.signup)
        self.menu.addSeparator()
        self.menu.addAction(self.signout)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Data Safe", None))
        self.signin.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.signup.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0440\u0435\u0433\u0435\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
        self.signout.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
        ___qtablewidgetitem = self.texttablet.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0438\u0441\u044c", None));
        ___qtablewidgetitem1 = self.texttablet.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.texttab), QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0441\u0442", None))
        ___qtablewidgetitem2 = self.imagetablet.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0438\u0441\u044c", None));
        ___qtablewidgetitem3 = self.imagetablet.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.imagetab), QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0410\u0443\u0442\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f", None))
    # retranslateUi

