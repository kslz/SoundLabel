# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Mainwindow(object):
    def setupUi(self, Mainwindow):
        if not Mainwindow.objectName():
            Mainwindow.setObjectName(u"Mainwindow")
        Mainwindow.resize(738, 799)
        Mainwindow.setMinimumSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(Mainwindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.groupBox_6 = QGroupBox(Mainwindow)
        self.groupBox_6.setObjectName(u"groupBox_6")
        font = QFont()
        font.setPointSize(16)
        self.groupBox_6.setFont(font)
        self.gridLayout = QGridLayout(self.groupBox_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_2 = QWidget(self.groupBox_6)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_5 = QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.widget_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_3.addWidget(self.lineEdit_2)


        self.verticalLayout_5.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.label_3 = QLabel(self.widget_5)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(self.widget_5)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_4.addWidget(self.lineEdit_3)


        self.verticalLayout_5.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.widget_2)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.widget_6)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setPointSize(10)
        self.label_4.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.pushButton_4 = QPushButton(self.widget_6)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_5.addWidget(self.pushButton_4)

        self.widget_8 = QWidget(self.widget_6)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy)
        self.widget_8.setMinimumSize(QSize(0, 0))
        self.widget_8.setFont(font1)
        self.widget_8.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_6 = QVBoxLayout(self.widget_8)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.widget_8)
        self.checkBox.setObjectName(u"checkBox")
        font2 = QFont()
        font2.setPointSize(12)
        self.checkBox.setFont(font2)

        self.verticalLayout_6.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.widget_8)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setFont(font2)

        self.verticalLayout_6.addWidget(self.checkBox_2)


        self.horizontalLayout_5.addWidget(self.widget_8)


        self.verticalLayout_5.addWidget(self.widget_6)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.pushButton_5 = QPushButton(self.groupBox_6)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(3)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy1)
        self.pushButton_5.setFont(font)

        self.verticalLayout_2.addWidget(self.pushButton_5)

        self.widget = QWidget(self.groupBox_6)
        self.widget.setObjectName(u"widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy2)
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(9, -1, -1, 9)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(2)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy3)
        self.pushButton.setFont(font)

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy1.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy1)
        self.pushButton_3.setFont(font)

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy3.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy3)
        self.pushButton_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.pushButton_2)


        self.verticalLayout_2.addWidget(self.widget)


        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_6)

        self.groupBox = QGroupBox(Mainwindow)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.widget_3 = QWidget(self.groupBox)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_2 = QGroupBox(self.widget_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.radioButton = QRadioButton(self.groupBox_2)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout_3.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.groupBox_2)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout_3.addWidget(self.radioButton_2)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.verticalLayout_3.addWidget(self.label)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_5)

        self.pushButton_6 = QPushButton(self.groupBox_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font2)

        self.verticalLayout_3.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.groupBox_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFont(font2)

        self.verticalLayout_3.addWidget(self.pushButton_7)


        self.horizontalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.widget_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFont(font)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_7 = QWidget(self.groupBox_3)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setFont(font1)
        self.horizontalLayout_6 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.tableWidget = QTableWidget(self.widget_7)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 2):
            self.tableWidget.setRowCount(2)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem8)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFont(font1)
        self.tableWidget.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.tableWidget.setFocusPolicy(Qt.StrongFocus)
        self.tableWidget.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.horizontalLayout_6.addWidget(self.tableWidget)


        self.verticalLayout_4.addWidget(self.widget_7)


        self.horizontalLayout.addWidget(self.groupBox_3)


        self.gridLayout_2.addWidget(self.widget_3, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)


        self.retranslateUi(Mainwindow)
        self.pushButton_4.clicked.connect(Mainwindow.click_refreshBTN)
        self.pushButton_5.clicked.connect(Mainwindow.click_play_soundBTN)
        self.pushButton.clicked.connect(Mainwindow.click_backBTN)
        self.pushButton_2.clicked.connect(Mainwindow.click_nextBTN)
        self.pushButton_3.clicked.connect(Mainwindow.click_checkBTN)
        self.pushButton_6.clicked.connect(Mainwindow.click_output_now)
        self.pushButton_7.clicked.connect(Mainwindow.click_back_to_main)

        QMetaObject.connectSlotsByName(Mainwindow)
    # setupUi

    def retranslateUi(self, Mainwindow):
        Mainwindow.setWindowTitle(QCoreApplication.translate("Mainwindow", u"\u8bed\u97f3\u6807\u8bb0", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Mainwindow", u"\u97f3\u9891\u4fe1\u606f", None))
        self.label_2.setText(QCoreApplication.translate("Mainwindow", u"\u5f00\u59cb\u65f6\u95f4", None))
        self.label_3.setText(QCoreApplication.translate("Mainwindow", u"\u7ed3\u675f\u65f6\u95f4", None))
        self.label_4.setText(QCoreApplication.translate("Mainwindow", u"\u5982\u679c\u4f60\u89c9\u5f97\u65f6\u95f4\u5207\u7684\u4e0d\u597d\uff0c\u8bf7\u4fee\u6539\u8fd9\u91cc\u7684\u8d77\u6b62\u65f6\u95f4\n"
"\uff08\u5355\u4f4d\uff1a\u6beb\u79d2\uff09\u4fee\u6539\u540e\u70b9\u51fb\u64ad\u653e\u97f3\u9891\u53ef\u4ee5\u67e5\u770b\u6548\u679c\n"
"\uff0c\u622a\u53d6\u5408\u9002\u540e\u70b9\u51fb\u786e\u5b9a\u6807\u6ce8\u624d\u80fd\u4fdd\u5b58\u4fee\u6539", None))
        self.pushButton_4.setText(QCoreApplication.translate("Mainwindow", u"\u5237\u65b0\u6570\u636e\u5217\u8868", None))
        self.checkBox.setText(QCoreApplication.translate("Mainwindow", u"\u5207\u6362\u6761\u76ee\u540e\u81ea\u52a8\u64ad\u653e", None))
        self.checkBox_2.setText(QCoreApplication.translate("Mainwindow", u"\u786e\u5b9a\u6807\u6ce8\u540e\u81ea\u52a8\u8df3\u5230\u4e0b\u4e00\u6761", None))
        self.pushButton_5.setText(QCoreApplication.translate("Mainwindow", u"\u64ad\u653e\u97f3\u9891", None))
        self.pushButton.setText(QCoreApplication.translate("Mainwindow", u"\u4e0a\u4e00\u6761", None))
        self.pushButton_3.setText(QCoreApplication.translate("Mainwindow", u"\u786e\u5b9a\u6807\u6ce8", None))
        self.pushButton_2.setText(QCoreApplication.translate("Mainwindow", u"\u4e0b\u4e00\u6761", None))
        self.groupBox.setTitle(QCoreApplication.translate("Mainwindow", u"\u6807\u6ce8\u4fe1\u606f", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Mainwindow", u"\u662f\u5426\u53ef\u7528", None))
        self.radioButton.setText(QCoreApplication.translate("Mainwindow", u"\u4e0d\u53ef\u7528", None))
        self.radioButton_2.setText(QCoreApplication.translate("Mainwindow", u"\u53ef\u7528", None))
        self.label.setText(QCoreApplication.translate("Mainwindow", u"\u5982\u679c\u4f60\u89c9\u5f97\u8fd9\u6761\u6548\u679c\n"
"\u592a\u5dee\u4e86\u8bf7\u9009\u62e9\u4e0d\u53ef\u7528", None))
        self.label_5.setText(QCoreApplication.translate("Mainwindow", u"\u5f53\u524d\u7f16\u53f7\uff1a1024", None))
        self.pushButton_6.setText(QCoreApplication.translate("Mainwindow", u"\u5bfc\u51fa\u5f53\u524d\u97f3\u9891", None))
        self.pushButton_7.setText(QCoreApplication.translate("Mainwindow", u"\u8fd4\u56de\u9996\u9875", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Mainwindow", u"\u6570\u636e\u5217\u8868", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Mainwindow", u"\u6587\u672c", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Mainwindow", u"\u68c0\u67e5\u72b6\u6001", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Mainwindow", u"\u53ef\u7528", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Mainwindow", u"\u64cd\u4f5c", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Mainwindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Mainwindow", u"\u65b0\u5efa\u884c", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Mainwindow", u"\u4f60\u597d", None));
        ___qtablewidgetitem7 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Mainwindow", u"3", None));
        ___qtablewidgetitem8 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Mainwindow", u"4", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

    # retranslateUi

