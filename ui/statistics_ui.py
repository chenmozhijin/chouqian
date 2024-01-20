# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'statistics.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QSizePolicy, QSpacerItem, QTableWidgetItem, QVBoxLayout,
    QWidget)

from qfluentwidgets import (BodyLabel, CalendarPicker, ComboBox, PushButton,
    TableWidget, TitleLabel)

class Ui_statistics(object):
    def setupUi(self, statistics):
        if not statistics.objectName():
            statistics.setObjectName(u"statistics")
        statistics.resize(660, 460)
        self.verticalLayout_2 = QVBoxLayout(statistics)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.TitleLabel = TitleLabel(statistics)
        self.TitleLabel.setObjectName(u"TitleLabel")

        self.verticalLayout_2.addWidget(self.TitleLabel)

        self.ComboBox = ComboBox(statistics)
        self.ComboBox.setObjectName(u"ComboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ComboBox.sizePolicy().hasHeightForWidth())
        self.ComboBox.setSizePolicy(sizePolicy)
        self.ComboBox.setMinimumSize(QSize(160, 0))

        self.verticalLayout_2.addWidget(self.ComboBox, 0, Qt.AlignLeft)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.BodyLabel = BodyLabel(statistics)
        self.BodyLabel.setObjectName(u"BodyLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.BodyLabel.sizePolicy().hasHeightForWidth())
        self.BodyLabel.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.BodyLabel)

        self.CalendarPicker = CalendarPicker(statistics)
        self.CalendarPicker.setObjectName(u"CalendarPicker")
        sizePolicy1.setHeightForWidth(self.CalendarPicker.sizePolicy().hasHeightForWidth())
        self.CalendarPicker.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.CalendarPicker)

        self.BodyLabel_2 = BodyLabel(statistics)
        self.BodyLabel_2.setObjectName(u"BodyLabel_2")
        sizePolicy1.setHeightForWidth(self.BodyLabel_2.sizePolicy().hasHeightForWidth())
        self.BodyLabel_2.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.BodyLabel_2)

        self.CalendarPicker_2 = CalendarPicker(statistics)
        self.CalendarPicker_2.setObjectName(u"CalendarPicker_2")
        sizePolicy1.setHeightForWidth(self.CalendarPicker_2.sizePolicy().hasHeightForWidth())
        self.CalendarPicker_2.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.CalendarPicker_2)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.PushButton = PushButton(statistics)
        self.PushButton.setObjectName(u"PushButton")

        self.horizontalLayout.addWidget(self.PushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.TableWidget = TableWidget(statistics)
        self.TableWidget.setObjectName(u"TableWidget")
        self.TableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout_2.addWidget(self.TableWidget)


        self.retranslateUi(statistics)

        QMetaObject.connectSlotsByName(statistics)
    # setupUi

    def retranslateUi(self, statistics):
        statistics.setWindowTitle(QCoreApplication.translate("statistics", u"Form", None))
        self.TitleLabel.setText(QCoreApplication.translate("statistics", u"\u7edf\u8ba1", None))
        self.BodyLabel.setText(QCoreApplication.translate("statistics", u"\u4ece", None))
        self.CalendarPicker.setText(QCoreApplication.translate("statistics", u"\u9009\u62e9\u4e00\u4e2a\u65e5\u671f", None))
        self.BodyLabel_2.setText(QCoreApplication.translate("statistics", u"\u5230", None))
        self.CalendarPicker_2.setText(QCoreApplication.translate("statistics", u"\u9009\u62e9\u4e00\u4e2a\u65e5\u671f", None))
        self.PushButton.setText(QCoreApplication.translate("statistics", u"\u91cd\u7f6e", None))
    # retranslateUi

