# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inputdata.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.dataTableWidget = QTableWidget(self.widget)
        if (self.dataTableWidget.columnCount() < 3):
            self.dataTableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.dataTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.dataTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.dataTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.dataTableWidget.setObjectName(u"dataTableWidget")
        self.dataTableWidget.setTabletTracking(False)

        self.horizontalLayout.addWidget(self.dataTableWidget)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.textEdit = QTextEdit(self.widget_3)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.textEdit)


        self.verticalLayout.addWidget(self.widget_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.back_to_main)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u6570\u636e", None))
        ___qtablewidgetitem = self.dataTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u540d", None));
        ___qtablewidgetitem1 = self.dataTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u8def\u5f84", None));
        ___qtablewidgetitem2 = self.dataTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u64cd\u4f5c", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u53cc\u51fb\u5de6\u4e0a\u89d2\u7684\u8868\u683c\u6765\u5bfc\u5165\u5bf9\u5e94\u7684\u97f3\u9891\u548c\u5b57\u5e55\n"
"\u6ce8\u610f\uff1a\u97f3\u9891\u53ea\u652f\u6301wav,acc\u548cmp3\u683c\u5f0f\n"
"\u4e14\u97f3\u9891\u548c\u5b57\u5e55\u7684\u6587\u4ef6\u540d\u5fc5\u987b\u76f8\u540c\uff0c\u540e\u7f00\u53ef\u4ee5\u4e0d\u540c", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u8fd4\u56de\u5165\u53e3", None))
    # retranslateUi

