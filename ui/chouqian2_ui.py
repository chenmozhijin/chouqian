
################################################################################
## Form generated from reading UI file 'chouqian2.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide6.QtGui import QCursor, QFont
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLayout,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)

from qfluentwidgets import (
    CaptionLabel,
    PillPushButton,
    PushButton,
    ScrollArea,
    Slider,
    TitleLabel,
)
from ui.custom_widgets import TextLineEdit


class Ui_chouqian2:
    def setupUi(self, chouqian2):
        if not chouqian2.objectName():
            chouqian2.setObjectName("chouqian2")
        chouqian2.resize(660, 460)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(chouqian2.sizePolicy().hasHeightForWidth())
        chouqian2.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(chouqian2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TitleLabel = TitleLabel(chouqian2)
        self.TitleLabel.setObjectName("TitleLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.TitleLabel.sizePolicy().hasHeightForWidth())
        self.TitleLabel.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.TitleLabel, 0, Qt.AlignmentFlag.AlignLeft)

        self.ScrollArea = ScrollArea(chouqian2)
        self.ScrollArea.setObjectName("ScrollArea")
        self.ScrollArea.setStyleSheet("background-color: transparent;")
        self.ScrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.ScrollArea.setFrameShadow(QFrame.Shadow.Plain)
        self.ScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.ScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 642, 280))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.chouqian_textEdit = TextLineEdit(self.scrollAreaWidgetContents)
        self.chouqian_textEdit.setObjectName("chouqian_textEdit")
        self.chouqian_textEdit.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.chouqian_textEdit.sizePolicy().hasHeightForWidth())
        self.chouqian_textEdit.setSizePolicy(sizePolicy2)
        self.chouqian_textEdit.setMinimumSize(QSize(0, 0))
        self.chouqian_textEdit.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.chouqian_textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.chouqian_textEdit.setFrameShadow(QFrame.Shadow.Plain)
        self.chouqian_textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.chouqian_textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.chouqian_textEdit.setReadOnly(True)
        self.chouqian_textEdit.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_2.addWidget(self.chouqian_textEdit)

        self.ScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.ScrollArea)

        self.CaptionLabel = CaptionLabel(chouqian2)
        self.CaptionLabel.setObjectName("CaptionLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.CaptionLabel.sizePolicy().hasHeightForWidth())
        self.CaptionLabel.setSizePolicy(sizePolicy3)
        self.CaptionLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.CaptionLabel)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.PillPushButton_reduce = PillPushButton(chouqian2)
        self.PillPushButton_reduce.setObjectName("PillPushButton_reduce")
        sizePolicy1.setHeightForWidth(self.PillPushButton_reduce.sizePolicy().hasHeightForWidth())
        self.PillPushButton_reduce.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.PillPushButton_reduce)

        self.Slider = Slider(chouqian2)
        self.Slider.setObjectName("Slider")
        sizePolicy1.setHeightForWidth(self.Slider.sizePolicy().hasHeightForWidth())
        self.Slider.setSizePolicy(sizePolicy1)
        self.Slider.setMinimumSize(QSize(150, 0))
        self.Slider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_3.addWidget(self.Slider)

        self.PillPushButton_add = PillPushButton(chouqian2)
        self.PillPushButton_add.setObjectName("PillPushButton_add")
        sizePolicy1.setHeightForWidth(self.PillPushButton_add.sizePolicy().hasHeightForWidth())
        self.PillPushButton_add.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.PillPushButton_add)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.PushButton = PushButton(chouqian2)
        self.PushButton.setObjectName("PushButton")
        sizePolicy1.setHeightForWidth(self.PushButton.sizePolicy().hasHeightForWidth())
        self.PushButton.setSizePolicy(sizePolicy1)
        self.PushButton.setMinimumSize(QSize(100, 0))
        font = QFont()
        font.setFamilies(["Segoe UI"])
        font.setPointSize(16)
        font.setBold(False)
        self.PushButton.setFont(font)

        self.verticalLayout.addWidget(self.PushButton, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer = QSpacerItem(0, 38, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(chouqian2)

        QMetaObject.connectSlotsByName(chouqian2)
    # setupUi

    def retranslateUi(self, chouqian2):
        chouqian2.setWindowTitle(QCoreApplication.translate("chouqian2", "Form", None))
        self.TitleLabel.setText(QCoreApplication.translate("chouqian2", "\u968f\u673a\u5c0f\u7ec4", None))
        self.chouqian_textEdit.setHtml(QCoreApplication.translate("chouqian2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:30px;\"><br /></p></body></html>", None))
        self.CaptionLabel.setText(QCoreApplication.translate("chouqian2", "1", None))
        self.PillPushButton_reduce.setText(QCoreApplication.translate("chouqian2", "-", None))
        self.PillPushButton_add.setText(QCoreApplication.translate("chouqian2", "+", None))
        self.PushButton.setText(QCoreApplication.translate("chouqian2", "\u62bd\u7b7e", None))
    # retranslateUi

