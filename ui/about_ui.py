
################################################################################
## Form generated from reading UI file 'about.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
)

from qfluentwidgets import (
    BodyLabel,
    CardWidget,
    PrimaryPushButton,
    StrongBodyLabel,
    TitleLabel,
)


class Ui_about:
    def setupUi(self, about):
        if not about.objectName():
            about.setObjectName("about")
        about.resize(660, 460)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(about.sizePolicy().hasHeightForWidth())
        about.setSizePolicy(sizePolicy)
        about.setMinimumSize(QSize(0, 0))
        about.setSizeIncrement(QSize(0, 0))
        about.setBaseSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(about)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TitleLabel = TitleLabel(about)
        self.TitleLabel.setObjectName("TitleLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.TitleLabel.sizePolicy().hasHeightForWidth())
        self.TitleLabel.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.TitleLabel)

        self.StrongBodyLabel = StrongBodyLabel(about)
        self.StrongBodyLabel.setObjectName("StrongBodyLabel")
        sizePolicy1.setHeightForWidth(self.StrongBodyLabel.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.StrongBodyLabel, 0, Qt.AlignHCenter)

        self.CardWidget_2 = CardWidget(about)
        self.CardWidget_2.setObjectName("CardWidget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.CardWidget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.BodyLabel_2 = BodyLabel(self.CardWidget_2)
        self.BodyLabel_2.setObjectName("BodyLabel_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.BodyLabel_2.sizePolicy().hasHeightForWidth())
        self.BodyLabel_2.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.BodyLabel_2)

        self.PrimaryPushButton_2 = PrimaryPushButton(self.CardWidget_2)
        self.PrimaryPushButton_2.setObjectName("PrimaryPushButton_2")
        sizePolicy1.setHeightForWidth(self.PrimaryPushButton_2.sizePolicy().hasHeightForWidth())
        self.PrimaryPushButton_2.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.PrimaryPushButton_2)


        self.verticalLayout.addWidget(self.CardWidget_2)

        self.CardWidget_3 = CardWidget(about)
        self.CardWidget_3.setObjectName("CardWidget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.CardWidget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.BodyLabel_3 = BodyLabel(self.CardWidget_3)
        self.BodyLabel_3.setObjectName("BodyLabel_3")
        sizePolicy2.setHeightForWidth(self.BodyLabel_3.sizePolicy().hasHeightForWidth())
        self.BodyLabel_3.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.BodyLabel_3)

        self.PrimaryPushButton_3 = PrimaryPushButton(self.CardWidget_3)
        self.PrimaryPushButton_3.setObjectName("PrimaryPushButton_3")
        sizePolicy1.setHeightForWidth(self.PrimaryPushButton_3.sizePolicy().hasHeightForWidth())
        self.PrimaryPushButton_3.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.PrimaryPushButton_3)


        self.verticalLayout.addWidget(self.CardWidget_3)

        self.CardWidget = CardWidget(about)
        self.CardWidget.setObjectName("CardWidget")
        sizePolicy2.setHeightForWidth(self.CardWidget.sizePolicy().hasHeightForWidth())
        self.CardWidget.setSizePolicy(sizePolicy2)
        self.horizontalLayout = QHBoxLayout(self.CardWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.BodyLabel = BodyLabel(self.CardWidget)
        self.BodyLabel.setObjectName("BodyLabel")
        sizePolicy2.setHeightForWidth(self.BodyLabel.sizePolicy().hasHeightForWidth())
        self.BodyLabel.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.BodyLabel)

        self.PrimaryPushButton = PrimaryPushButton(self.CardWidget)
        self.PrimaryPushButton.setObjectName("PrimaryPushButton")
        sizePolicy1.setHeightForWidth(self.PrimaryPushButton.sizePolicy().hasHeightForWidth())
        self.PrimaryPushButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.PrimaryPushButton)


        self.verticalLayout.addWidget(self.CardWidget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(about)

        QMetaObject.connectSlotsByName(about)
    # setupUi

    def retranslateUi(self, about):
        about.setWindowTitle(QCoreApplication.translate("about", "Form", None))
        self.TitleLabel.setText(QCoreApplication.translate("about", "\u5173\u4e8e", None))
        self.StrongBodyLabel.setText(QCoreApplication.translate("about", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">\u62bd\u7b7e</span></p><p align=\"center\"><span style=\" font-size:16pt;\">\u4e00\u4e2a\u7b80\u5355\u6613\u7528\u7684\u62bd\u7b7e\u5de5\u5177</span></p><p align=\"right\"><span style=\" font-size:6pt;\">Copyright \u00a9 2023-2024 \u6c89\u9ed8\u306e\u91d1</span></p></body></html>", None))
        self.BodyLabel_2.setText(QCoreApplication.translate("about", "\u7248\u672c\u53f7\uff1a", None))
        self.PrimaryPushButton_2.setText(QCoreApplication.translate("about", "\u68c0\u67e5\u66f4\u65b0", None))
        self.BodyLabel_3.setText(QCoreApplication.translate("about", "\u95ee\u9898\u53cd\u9988", None))
        self.PrimaryPushButton_3.setText(QCoreApplication.translate("about", "GitHub Issues", None))
        self.BodyLabel.setText(QCoreApplication.translate("about", "\u9879\u76ee\u5f00\u6e90\u5730\u5740", None))
        self.PrimaryPushButton.setText(QCoreApplication.translate("about", "GitHub Repo", None))
    # retranslateUi

