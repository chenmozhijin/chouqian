# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chouqian1.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLayout,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (CaptionLabel, ComboBox, PillPushButton, PushButton,
    ScrollArea, Slider, StrongBodyLabel, TitleLabel,
    ToggleButton)

class Ui_chouqian1(object):
    def setupUi(self, chouqian1):
        if not chouqian1.objectName():
            chouqian1.setObjectName(u"chouqian1")
        chouqian1.resize(660, 460)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(chouqian1.sizePolicy().hasHeightForWidth())
        chouqian1.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(chouqian1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.TitleLabel = TitleLabel(chouqian1)
        self.TitleLabel.setObjectName(u"TitleLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.TitleLabel.sizePolicy().hasHeightForWidth())
        self.TitleLabel.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.TitleLabel, 0, Qt.AlignLeft)

        self.ComboBox = ComboBox(chouqian1)
        self.ComboBox.setObjectName(u"ComboBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ComboBox.sizePolicy().hasHeightForWidth())
        self.ComboBox.setSizePolicy(sizePolicy2)
        self.ComboBox.setMinimumSize(QSize(160, 0))
        self.ComboBox.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout.addWidget(self.ComboBox)

        self.ScrollArea = ScrollArea(chouqian1)
        self.ScrollArea.setObjectName(u"ScrollArea")
        self.ScrollArea.setFrameShape(QFrame.NoFrame)
        self.ScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 642, 209))
        self.scrollAreaWidgetContents.setAutoFillBackground(True)
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.StrongBodyLabel = StrongBodyLabel(self.scrollAreaWidgetContents)
        self.StrongBodyLabel.setObjectName(u"StrongBodyLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.StrongBodyLabel.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel.setSizePolicy(sizePolicy3)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(1)
        font.setBold(True)
        self.StrongBodyLabel.setFont(font)
        self.StrongBodyLabel.setTextFormat(Qt.PlainText)
        self.StrongBodyLabel.setAlignment(Qt.AlignCenter)
        self.StrongBodyLabel.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.StrongBodyLabel)

        self.ScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.ScrollArea)

        self.CaptionLabel = CaptionLabel(chouqian1)
        self.CaptionLabel.setObjectName(u"CaptionLabel")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.CaptionLabel.sizePolicy().hasHeightForWidth())
        self.CaptionLabel.setSizePolicy(sizePolicy4)
        self.CaptionLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.CaptionLabel)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.PillPushButton = PillPushButton(chouqian1)
        self.PillPushButton.setObjectName(u"PillPushButton")
        sizePolicy1.setHeightForWidth(self.PillPushButton.sizePolicy().hasHeightForWidth())
        self.PillPushButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.PillPushButton)

        self.Slider = Slider(chouqian1)
        self.Slider.setObjectName(u"Slider")
        sizePolicy1.setHeightForWidth(self.Slider.sizePolicy().hasHeightForWidth())
        self.Slider.setSizePolicy(sizePolicy1)
        self.Slider.setMinimumSize(QSize(150, 0))
        self.Slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.Slider)

        self.PillPushButton_2 = PillPushButton(chouqian1)
        self.PillPushButton_2.setObjectName(u"PillPushButton_2")
        sizePolicy1.setHeightForWidth(self.PillPushButton_2.sizePolicy().hasHeightForWidth())
        self.PillPushButton_2.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.PillPushButton_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.PushButton = PushButton(chouqian1)
        self.PushButton.setObjectName(u"PushButton")
        sizePolicy1.setHeightForWidth(self.PushButton.sizePolicy().hasHeightForWidth())
        self.PushButton.setSizePolicy(sizePolicy1)
        self.PushButton.setMinimumSize(QSize(100, 0))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(16)
        font1.setBold(False)
        self.PushButton.setFont(font1)

        self.verticalLayout.addWidget(self.PushButton, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(0, 38, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(chouqian1)

        QMetaObject.connectSlotsByName(chouqian1)
    # setupUi

    def retranslateUi(self, chouqian1):
        chouqian1.setWindowTitle(QCoreApplication.translate("chouqian1", u"Form", None))
        self.TitleLabel.setText(QCoreApplication.translate("chouqian1", u"\u968f\u673a\u59d3\u540d", None))
        self.CaptionLabel.setText(QCoreApplication.translate("chouqian1", u"1", None))
        self.PillPushButton.setText(QCoreApplication.translate("chouqian1", u"-", None))
        self.PillPushButton_2.setText(QCoreApplication.translate("chouqian1", u"+", None))
        self.PushButton.setText(QCoreApplication.translate("chouqian1", u"\u62bd\u7b7e", None))
    # retranslateUi

