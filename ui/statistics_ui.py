
################################################################################
## Form generated from reading UI file 'statistics.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtWidgets import (
    QAbstractItemView,
    QHBoxLayout,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
)

from qfluentwidgets import (
    BodyLabel,
    CalendarPicker,
    ComboBox,
    PushButton,
    TableWidget,
    TitleLabel,
)


class Ui_statistics:
    def setupUi(self, statistics):
        if not statistics.objectName():
            statistics.setObjectName("statistics")
        statistics.resize(660, 460)
        self.verticalLayout_2 = QVBoxLayout(statistics)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.TitleLabel = TitleLabel(statistics)
        self.TitleLabel.setObjectName("TitleLabel")

        self.verticalLayout_2.addWidget(self.TitleLabel)

        self.ComboBox = ComboBox(statistics)
        self.ComboBox.setObjectName("ComboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ComboBox.sizePolicy().hasHeightForWidth())
        self.ComboBox.setSizePolicy(sizePolicy)
        self.ComboBox.setMinimumSize(QSize(160, 0))

        self.verticalLayout_2.addWidget(self.ComboBox, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.BodyLabel = BodyLabel(statistics)
        self.BodyLabel.setObjectName("BodyLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.BodyLabel.sizePolicy().hasHeightForWidth())
        self.BodyLabel.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.BodyLabel)

        self.CalendarPicker = CalendarPicker(statistics)
        self.CalendarPicker.setObjectName("CalendarPicker")
        sizePolicy1.setHeightForWidth(self.CalendarPicker.sizePolicy().hasHeightForWidth())
        self.CalendarPicker.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.CalendarPicker)

        self.BodyLabel_2 = BodyLabel(statistics)
        self.BodyLabel_2.setObjectName("BodyLabel_2")
        sizePolicy1.setHeightForWidth(self.BodyLabel_2.sizePolicy().hasHeightForWidth())
        self.BodyLabel_2.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.BodyLabel_2)

        self.CalendarPicker_2 = CalendarPicker(statistics)
        self.CalendarPicker_2.setObjectName("CalendarPicker_2")
        sizePolicy1.setHeightForWidth(self.CalendarPicker_2.sizePolicy().hasHeightForWidth())
        self.CalendarPicker_2.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.CalendarPicker_2)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.PushButton = PushButton(statistics)
        self.PushButton.setObjectName("PushButton")

        self.horizontalLayout.addWidget(self.PushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.TableWidget = TableWidget(statistics)
        self.TableWidget.setObjectName("TableWidget")
        self.TableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.TableWidget.setTabKeyNavigation(False)
        self.TableWidget.setProperty("showDropIndicator", False)
        self.TableWidget.setDragDropOverwriteMode(False)
        self.TableWidget.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.TableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.TableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.TableWidget.horizontalHeader().setStretchLastSection(False)

        self.verticalLayout_2.addWidget(self.TableWidget)


        self.retranslateUi(statistics)

        QMetaObject.connectSlotsByName(statistics)
    # setupUi

    def retranslateUi(self, statistics):
        statistics.setWindowTitle(QCoreApplication.translate("statistics", "Form", None))
        self.TitleLabel.setText(QCoreApplication.translate("statistics", "\u7edf\u8ba1", None))
        self.BodyLabel.setText(QCoreApplication.translate("statistics", "\u4ece", None))
        self.CalendarPicker.setText(QCoreApplication.translate("statistics", "\u9009\u62e9\u4e00\u4e2a\u65e5\u671f", None))
        self.BodyLabel_2.setText(QCoreApplication.translate("statistics", "\u5230", None))
        self.CalendarPicker_2.setText(QCoreApplication.translate("statistics", "\u9009\u62e9\u4e00\u4e2a\u65e5\u671f", None))
        self.PushButton.setText(QCoreApplication.translate("statistics", "\u91cd\u7f6e", None))
    # retranslateUi

