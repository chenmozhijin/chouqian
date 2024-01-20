# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, CardWidget, ComboBox, PushButton,
    ScrollArea, SpinBox, SubtitleLabel, SwitchButton,
    TitleLabel)

class Ui_settings(object):
    def setupUi(self, settings):
        if not settings.objectName():
            settings.setObjectName(u"settings")
        settings.resize(660, 460)
        self.verticalLayout_2 = QVBoxLayout(settings)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.TitleLabel = TitleLabel(settings)
        self.TitleLabel.setObjectName(u"TitleLabel")

        self.verticalLayout_2.addWidget(self.TitleLabel)

        self.ScrollArea = ScrollArea(settings)
        self.ScrollArea.setObjectName(u"ScrollArea")
        self.ScrollArea.setFrameShape(QFrame.NoFrame)
        self.ScrollArea.setFrameShadow(QFrame.Plain)
        self.ScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 642, 339))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.SubtitleLabel = SubtitleLabel(self.scrollAreaWidgetContents)
        self.SubtitleLabel.setObjectName(u"SubtitleLabel")

        self.verticalLayout_3.addWidget(self.SubtitleLabel)

        self.CardWidget = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget.setObjectName(u"CardWidget")
        sizePolicy.setHeightForWidth(self.CardWidget.sizePolicy().hasHeightForWidth())
        self.CardWidget.setSizePolicy(sizePolicy)
        self.CardWidget.setBorderRadius(5)
        self.horizontalLayout_2 = QHBoxLayout(self.CardWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.BodyLabel = BodyLabel(self.CardWidget)
        self.BodyLabel.setObjectName(u"BodyLabel")

        self.horizontalLayout_2.addWidget(self.BodyLabel)

        self.SwitchButton = SwitchButton(self.CardWidget)
        self.SwitchButton.setObjectName(u"SwitchButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.SwitchButton.sizePolicy().hasHeightForWidth())
        self.SwitchButton.setSizePolicy(sizePolicy1)
        self.SwitchButton.setLayoutDirection(Qt.RightToLeft)
        self.SwitchButton.setChecked(False)

        self.horizontalLayout_2.addWidget(self.SwitchButton)


        self.verticalLayout_3.addWidget(self.CardWidget)

        self.CardWidget_2 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_2.setObjectName(u"CardWidget_2")
        sizePolicy.setHeightForWidth(self.CardWidget_2.sizePolicy().hasHeightForWidth())
        self.CardWidget_2.setSizePolicy(sizePolicy)
        self.CardWidget_2.setBorderRadius(5)
        self.horizontalLayout_3 = QHBoxLayout(self.CardWidget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.BodyLabel_2 = BodyLabel(self.CardWidget_2)
        self.BodyLabel_2.setObjectName(u"BodyLabel_2")

        self.horizontalLayout_3.addWidget(self.BodyLabel_2)

        self.SwitchButton_2 = SwitchButton(self.CardWidget_2)
        self.SwitchButton_2.setObjectName(u"SwitchButton_2")
        sizePolicy1.setHeightForWidth(self.SwitchButton_2.sizePolicy().hasHeightForWidth())
        self.SwitchButton_2.setSizePolicy(sizePolicy1)
        self.SwitchButton_2.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_3.addWidget(self.SwitchButton_2)


        self.verticalLayout_3.addWidget(self.CardWidget_2)

        self.CardWidget_4 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_4.setObjectName(u"CardWidget_4")
        self.horizontalLayout = QHBoxLayout(self.CardWidget_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.BodyLabel_4 = BodyLabel(self.CardWidget_4)
        self.BodyLabel_4.setObjectName(u"BodyLabel_4")

        self.horizontalLayout.addWidget(self.BodyLabel_4)

        self.SpinBox = SpinBox(self.CardWidget_4)
        self.SpinBox.setObjectName(u"SpinBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.SpinBox.sizePolicy().hasHeightForWidth())
        self.SpinBox.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.SpinBox)


        self.verticalLayout_3.addWidget(self.CardWidget_4)

        self.CardWidget_5 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_5.setObjectName(u"CardWidget_5")
        sizePolicy.setHeightForWidth(self.CardWidget_5.sizePolicy().hasHeightForWidth())
        self.CardWidget_5.setSizePolicy(sizePolicy)
        self.CardWidget_5.setBorderRadius(5)
        self.horizontalLayout_4 = QHBoxLayout(self.CardWidget_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.BodyLabel_5 = BodyLabel(self.CardWidget_5)
        self.BodyLabel_5.setObjectName(u"BodyLabel_5")

        self.horizontalLayout_4.addWidget(self.BodyLabel_5)

        self.ComboBox = ComboBox(self.CardWidget_5)
        self.ComboBox.setObjectName(u"ComboBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.ComboBox.sizePolicy().hasHeightForWidth())
        self.ComboBox.setSizePolicy(sizePolicy3)
        self.ComboBox.setMinimumSize(QSize(160, 0))
        self.ComboBox.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_4.addWidget(self.ComboBox)


        self.verticalLayout_3.addWidget(self.CardWidget_5)

        self.SubtitleLabel_2 = SubtitleLabel(self.scrollAreaWidgetContents)
        self.SubtitleLabel_2.setObjectName(u"SubtitleLabel_2")

        self.verticalLayout_3.addWidget(self.SubtitleLabel_2)

        self.CardWidget_3 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_3.setObjectName(u"CardWidget_3")
        self.horizontalLayout_6 = QHBoxLayout(self.CardWidget_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.BodyLabel_3 = BodyLabel(self.CardWidget_3)
        self.BodyLabel_3.setObjectName(u"BodyLabel_3")

        self.horizontalLayout_6.addWidget(self.BodyLabel_3)

        self.horizontalSpacer = QSpacerItem(40, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.PushButton = PushButton(self.CardWidget_3)
        self.PushButton.setObjectName(u"PushButton")

        self.horizontalLayout_6.addWidget(self.PushButton)


        self.verticalLayout_3.addWidget(self.CardWidget_3)

        self.ScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.ScrollArea)


        self.retranslateUi(settings)

        QMetaObject.connectSlotsByName(settings)
    # setupUi

    def retranslateUi(self, settings):
        settings.setWindowTitle(QCoreApplication.translate("settings", u"Form", None))
        self.TitleLabel.setText(QCoreApplication.translate("settings", u"\u8bbe\u7f6e", None))
        self.SubtitleLabel.setText(QCoreApplication.translate("settings", u"\u62bd\u7b7e", None))
        self.BodyLabel.setText(QCoreApplication.translate("settings", u"\u62bd\u7b7e\u52a8\u753b", None))
        self.SwitchButton.setText(QCoreApplication.translate("settings", u"\u5173", None))
        self.SwitchButton.setOnText(QCoreApplication.translate("settings", u"\u5f00", None))
        self.SwitchButton.setOffText(QCoreApplication.translate("settings", u"\u5173", None))
        self.BodyLabel_2.setText(QCoreApplication.translate("settings", u"\u51cf\u5c11\u91cd\u590d", None))
        self.SwitchButton_2.setText(QCoreApplication.translate("settings", u"\u5173", None))
        self.SwitchButton_2.setOnText(QCoreApplication.translate("settings", u"\u5f00", None))
        self.SwitchButton_2.setOffText(QCoreApplication.translate("settings", u"\u5173", None))
        self.BodyLabel_4.setText(QCoreApplication.translate("settings", u"\u5c0f\u7ec4\u6570\u91cf", None))
        self.BodyLabel_5.setText(QCoreApplication.translate("settings", u"\u9ed8\u8ba4\u5217\u8868", None))
        self.SubtitleLabel_2.setText(QCoreApplication.translate("settings", u"\u914d\u7f6e", None))
        self.BodyLabel_3.setText(QCoreApplication.translate("settings", u"\u5bfc\u5165\u914d\u7f6e", None))
        self.PushButton.setText(QCoreApplication.translate("settings", u"\u9009\u62e9\u914d\u7f6e\u6587\u4ef6", None))
    # retranslateUi

