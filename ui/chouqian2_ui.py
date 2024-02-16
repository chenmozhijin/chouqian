# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chouqian2.ui'
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
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

from qfluentwidgets import (CaptionLabel, PillPushButton, PushButton, Slider,
    TitleLabel, ToggleButton)

class Ui_chouqian2(object):
    def setupUi(self, chouqian2):
        if not chouqian2.objectName():
            chouqian2.setObjectName(u"chouqian2")
        chouqian2.resize(660, 460)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(chouqian2.sizePolicy().hasHeightForWidth())
        chouqian2.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(chouqian2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.TitleLabel = TitleLabel(chouqian2)
        self.TitleLabel.setObjectName(u"TitleLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.TitleLabel.sizePolicy().hasHeightForWidth())
        self.TitleLabel.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.TitleLabel, 0, Qt.AlignLeft)

        self.chouqian_textEdit = QTextEdit(chouqian2)
        self.chouqian_textEdit.setObjectName(u"chouqian_textEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.chouqian_textEdit.sizePolicy().hasHeightForWidth())
        self.chouqian_textEdit.setSizePolicy(sizePolicy2)
        self.chouqian_textEdit.setMinimumSize(QSize(0, 0))
        self.chouqian_textEdit.setStyleSheet(u"QTextEdit {\n"
"     background-color: transparent;\n"
"     border: none;\n"
"	font-size: 30px;\n"
"	text-align: center;\n"
"}")
        self.chouqian_textEdit.setFrameShape(QFrame.NoFrame)
        self.chouqian_textEdit.setFrameShadow(QFrame.Plain)
        self.chouqian_textEdit.setReadOnly(True)
        self.chouqian_textEdit.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout.addWidget(self.chouqian_textEdit)

        self.CaptionLabel = CaptionLabel(chouqian2)
        self.CaptionLabel.setObjectName(u"CaptionLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.CaptionLabel.sizePolicy().hasHeightForWidth())
        self.CaptionLabel.setSizePolicy(sizePolicy3)
        self.CaptionLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.CaptionLabel)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.PillPushButton = PillPushButton(chouqian2)
        self.PillPushButton.setObjectName(u"PillPushButton")
        sizePolicy1.setHeightForWidth(self.PillPushButton.sizePolicy().hasHeightForWidth())
        self.PillPushButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.PillPushButton)

        self.Slider = Slider(chouqian2)
        self.Slider.setObjectName(u"Slider")
        sizePolicy1.setHeightForWidth(self.Slider.sizePolicy().hasHeightForWidth())
        self.Slider.setSizePolicy(sizePolicy1)
        self.Slider.setMinimumSize(QSize(150, 0))
        self.Slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.Slider)

        self.PillPushButton_2 = PillPushButton(chouqian2)
        self.PillPushButton_2.setObjectName(u"PillPushButton_2")
        sizePolicy1.setHeightForWidth(self.PillPushButton_2.sizePolicy().hasHeightForWidth())
        self.PillPushButton_2.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.PillPushButton_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.PushButton = PushButton(chouqian2)
        self.PushButton.setObjectName(u"PushButton")
        sizePolicy1.setHeightForWidth(self.PushButton.sizePolicy().hasHeightForWidth())
        self.PushButton.setSizePolicy(sizePolicy1)
        self.PushButton.setMinimumSize(QSize(100, 0))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(16)
        font.setBold(False)
        self.PushButton.setFont(font)

        self.verticalLayout.addWidget(self.PushButton, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(0, 38, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(chouqian2)

        QMetaObject.connectSlotsByName(chouqian2)
    # setupUi

    def retranslateUi(self, chouqian2):
        chouqian2.setWindowTitle(QCoreApplication.translate("chouqian2", u"Form", None))
        self.TitleLabel.setText(QCoreApplication.translate("chouqian2", u"\u968f\u673a\u5c0f\u7ec4", None))
        self.chouqian_textEdit.setHtml(QCoreApplication.translate("chouqian2", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:30px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.CaptionLabel.setText(QCoreApplication.translate("chouqian2", u"1", None))
        self.PillPushButton.setText(QCoreApplication.translate("chouqian2", u"-", None))
        self.PillPushButton_2.setText(QCoreApplication.translate("chouqian2", u"+", None))
        self.PushButton.setText(QCoreApplication.translate("chouqian2", u"\u62bd\u7b7e", None))
    # retranslateUi

